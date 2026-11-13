"""Offline publication checks. No model, network, installation or tenant access."""
from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import stat
import sys
import zipfile
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MAX_FILE_BYTES = 6_000_000
MAX_ARCHIVE_BYTES = 12_000_000
ROOT_FILES = {"README.md", "LICENSE", "CONTRIBUTING.md", ".gitignore", ".gitattributes"}
ROOT_FILES |= {"CHANGELOG.md", "requirements-dev.txt"}
ROOT_DIRS = {"source", "packages", "docs", "scripts", ".github", "plugin"}
BASELINE_MANIFEST_SHA256 = "66d7a34594fac43d2291ecccfef93c6b8d52296f9d7709041b355ed299f07742"
PLUGIN_011_MANIFEST_SHA256 = "f6e3c3fb306f40b34c2fcc972dbd86a67dbb9c977795ebcc589e36d06dea1208"
SKIP = {".git", "__pycache__", ".pytest_cache"}
TEXT_EXTENSIONS = {".md", ".py", ".yaml", ".yml", ".json"}
PATTERNS = (
    re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(rb"\b(?:gh[pousr]_[A-Za-z0-9]{36,255}|github_pat_[A-Za-z0-9_]{50,255})\b"),
    re.compile(rb"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
    re.compile(rb"[A-Za-z]:[\\/]Users[\\/]|/(?:Users|home)/[A-Za-z0-9_. -]+/"),
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_release(root: Path):
    spec = importlib.util.spec_from_file_location("cortex_release", root / "source/tools/release.py")
    if spec is None or spec.loader is None:
        raise ValueError("Cannot load reviewed source audit")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def safe_relative(name: str) -> PurePosixPath:
    path = PurePosixPath(name)
    if (not name or path.is_absolute() or ".." in path.parts or "\\" in name
            or ":" in name or path.as_posix() != name):
        raise ValueError("Unsafe or noncanonical relative path")
    return path


def sensitive(data: bytes) -> bool:
    return any(pattern.search(data) for pattern in PATTERNS)


def validate_archive(path: Path, prefix: str, entries: list[dict]) -> int:
    expected = {}
    for entry in entries:
        relative = safe_relative(entry["path"])
        member = f"{prefix}/{relative.as_posix()}"
        if member in expected:
            raise ValueError("Duplicate manifest entry")
        expected[member] = entry
    with zipfile.ZipFile(path) as archive:
        infos = archive.infolist()
        names = [item.filename for item in infos]
        if len(names) != len(set(names)) or set(names) != set(expected):
            raise ValueError("Archive member set differs from manifest")
        if sum(item.file_size for item in infos) > MAX_ARCHIVE_BYTES:
            raise ValueError("Archive exceeds uncompressed byte limit")
        for info in infos:
            safe_relative(info.filename)
            if (info.is_dir() or info.file_size > MAX_FILE_BYTES
                    or stat.S_ISLNK(info.external_attr >> 16)):
                raise ValueError("Invalid archive member type or size")
            data = archive.read(info)
            entry = expected[info.filename]
            if len(data) != entry["bytes"] or sha256(data) != entry["sha256"]:
                raise ValueError("Archive member identity mismatch")
    return len(expected)


def validate_plugin_release(directory: Path, plugin, canonical=None, pinned_manifest=None) -> int:
    """Validate a release against its own snapshot; only current bytes use source/."""
    data = (directory / "release-manifest.json").read_bytes()
    if pinned_manifest and sha256(data) != pinned_manifest:
        raise ValueError("Historical plugin manifest changed")
    manifest = json.loads(data)
    version = manifest["plugin_version"]
    if directory.name != version:
        raise ValueError("Release version/directory mismatch")
    records = manifest["archives"]
    names = [r["file"] for r in records]
    checksum_rows = [line.split("  ", 1) for line in (directory / "SHA256SUMS").read_text().splitlines()]
    checksums = {name: digest for digest, name in checksum_rows}
    if any(not re.fullmatch(r"[0-9a-f]{64}", digest) for digest in checksums.values()):
        raise ValueError("Invalid release checksum format")
    if (len(names) != len(set(names)) or len(checksums) != len(checksum_rows)
            or set(names) != set(checksums) or set(names) != {p.name for p in directory.glob("*.zip")}):
        raise ValueError("Release ZIPs differ from manifest/checksums")
    opened = {}
    for record in records:
        name = safe_relative(record["file"])
        if len(name.parts) != 1:
            raise ValueError("Archive filename must be a basename")
        path = directory / name.name
        raw = path.read_bytes()
        if (sha256(raw) != record["sha256"] or len(raw) != record["bytes"]
                or checksums[name.name] != record["sha256"]):
            raise ValueError("Release checksum mismatch: " + name.name)
        opened[name.name] = plugin.read_zip(path)
    plugin_name = f"cortex-ai-skills-plugin-{version}.zip"
    payload = opened.get(plugin_name)
    if payload is None or plugin.inventory(payload) != manifest["files"]:
        raise ValueError("Plugin inventory differs from release manifest")
    if json.loads(payload[plugin.MANIFEST])["version"] != version:
        raise ValueError("Plugin version differs from release manifest")
    payload_skills = {key.split("/")[1] for key in payload if key.startswith("skills/")}
    if payload_skills != set(manifest["skill_versions"]):
        raise ValueError("Skill set differs from release manifest")
    if canonical is not None and payload != canonical:
        raise ValueError("Current plugin differs from canonical source")
    expected_names = {plugin_name}
    for skill, skill_version in manifest["skill_versions"].items():
        if payload.get(f"skills/{skill}/VERSION", b"").decode().strip() != skill_version:
            raise ValueError("Skill version differs from release manifest")
        filename = f"{skill}-{skill_version}-runtime.zip"
        expected_names.add(filename)
        expected = {f"{skill}/{key.removeprefix(f'skills/{skill}/')}": value
                    for key, value in payload.items() if key.startswith(f"skills/{skill}/")}
        if not expected or opened.get(filename) != expected:
            raise ValueError("Standalone runtime differs from release snapshot")
    if set(opened) != expected_names:
        raise ValueError("Unexpected release archive")
    return len(opened)


def validate(root: Path = ROOT) -> dict:
    errors = []
    release = load_release(root)
    source = root / "source"
    packages = root / "packages/0.1.0"
    # Ignore only generated build output, not the published packages or source.
    files = [p for p in release.checked_files(root) if p.relative_to(root).parts[0] != "dist"]
    texts = {}
    for path in files:
        rel = path.relative_to(root)
        if rel.parts[0] in SKIP:
            continue
        if ((len(rel.parts) == 1 and rel.name not in ROOT_FILES)
                or (len(rel.parts) > 1 and rel.parts[0] not in ROOT_DIRS)):
            errors.append(f"Unexpected publication path: {rel.as_posix()}")
        if path.stat().st_size > MAX_FILE_BYTES:
            errors.append(f"File too large: {rel.as_posix()}")
            continue
        if path.suffix == ".zip" and path.parent.parent == root / "packages":
            continue
        if path.suffix == ".svg" and path.parent == root / "plugin/assets":
            continue  # Parsed and constrained by build_plugin.validate_manifest.
        if path.suffix not in TEXT_EXTENSIONS and path.name not in (
                ROOT_FILES | {"VERSION", "SHA256SUMS", "LICENSE"}):
            errors.append(f"Unexpected file type: {rel.as_posix()}")
            continue
        data = path.read_bytes()
        if sensitive(data):
            errors.append(f"Sensitive-pattern finding: {rel.as_posix()}")
        try:
            body = data.decode("utf-8")
        except UnicodeDecodeError:
            errors.append(f"Non-UTF-8 text: {rel.as_posix()}")
            continue
        if "\x00" in body:
            errors.append(f"NUL in text: {rel.as_posix()}")
        if path.suffix == ".md":
            texts[path] = body

    local_links = 0
    for path, body in texts.items():
        for match in release.LINK.finditer(body):
            href = match[1].strip("<>")
            parsed = urlsplit(href)
            if parsed.scheme in {"https", "http", "mailto"}:
                continue
            local_links += 1
            if parsed.scheme or href.startswith(("/", "\\")):
                errors.append(f"Absolute/unsupported link: {path.relative_to(root)}")
                continue
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not target.is_relative_to(root) or not target.exists():
                errors.append(f"Missing/escaping local link: {path.relative_to(root)}: {href}")
            elif parsed.fragment and target in texts:
                if unquote(parsed.fragment) not in release.anchors(texts[target]):
                    errors.append(f"Missing anchor: {path.relative_to(root)}: {href}")

    baseline_bytes = (packages / "release-manifest.json").read_bytes()
    if sha256(baseline_bytes) != BASELINE_MANIFEST_SHA256:
        errors.append("Historical 0.1.0 manifest changed")
    manifest = json.loads(baseline_bytes.decode("utf-8"))
    source_files = release.checked_files(source)
    # The archived 0.1.0 source is verified member-by-member below. Current
    # source is allowed to evolve and is matched to the new runtime build.

    checksums = {}
    for line in (packages / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        digest, filename = line.split("  ", 1)
        safe_relative(filename)
        if filename in checksums or not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise ValueError("Invalid checksum record")
        checksums[filename] = digest
    archive_records = manifest["archives"]
    expected_names = {record["file"] for record in archive_records}
    if (len(archive_records) != 8 or len(expected_names) != 8
            or expected_names != set(checksums)
            or expected_names != {p.name for p in packages.glob("*.zip")}):
        errors.append("Expected exactly eight matching archive/checksum records")

    members = 0
    for record in archive_records:
        relative = safe_relative(record["file"])
        if len(relative.parts) != 1:
            raise ValueError("Archive filename must be a basename")
        path = packages / relative.name
        data = path.read_bytes()
        if (len(data) != record["bytes"] or sha256(data) != record["sha256"]
                or checksums.get(path.name) != record["sha256"]):
            errors.append(f"Archive checksum mismatch: {path.name}")
            continue
        if path.name == "cortex-ai-skills-0.1.0-source.zip":
            prefix, entries = "cortex-ai-skills", manifest["source"]["entries"]
        else:
            skill = path.name.removesuffix("-0.1.0-runtime.zip")
            if skill not in manifest["skills"]:
                raise ValueError("Unknown runtime archive")
            prefix, entries = skill, manifest["skills"][skill]["runtime"]["entries"]
        try:
            members += validate_archive(path, prefix, entries)
        except (ValueError, zipfile.BadZipFile, RuntimeError) as exc:
            errors.append(f"Invalid archive {path.name}: {exc}")
    source_audit = release.audit(source)
    errors.extend(source_audit["errors"])
    plugin_spec = importlib.util.spec_from_file_location("current_plugin_builder", root / "scripts/build_plugin.py")
    plugin = importlib.util.module_from_spec(plugin_spec)
    plugin_spec.loader.exec_module(plugin)
    current_payload = plugin.payload(root)
    current_report = plugin.validate_payload(current_payload, root)
    plugin_archives = validate_plugin_release(root / "packages/0.1.1", plugin,
                                             pinned_manifest=PLUGIN_011_MANIFEST_SHA256)
    current_packages = root / "packages" / current_report["plugin_version"]
    if current_packages.name != "0.1.1":
        plugin_archives += validate_plugin_release(current_packages, plugin, canonical=current_payload)
    return {
        "result": "FAIL" if errors else "PASS",
        "files": len(files),
        "source_files": len(source_files),
        "archives": len(archive_records) + plugin_archives,
        "archive_members": members,
        "local_links": local_links,
        "errors": errors,
    }


if __name__ == "__main__":
    sys.dont_write_bytecode = True
    try:
        report = validate()
    except (ValueError, OSError, KeyError, zipfile.BadZipFile) as exc:
        report = {"result": "FAIL", "errors": [str(exc)]}
    print(json.dumps(report, indent=2, ensure_ascii=False))
    raise SystemExit(report["result"] != "PASS")
