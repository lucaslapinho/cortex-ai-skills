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
    plugin.validate_payload(plugin.payload(root), root)
    current_packages = root / "packages/0.1.1"
    if current_packages.exists():
        current_manifest = json.loads((current_packages / "release-manifest.json").read_text(encoding="utf-8"))
        current_checksums = dict(line.split("  ", 1)[::-1] for line in
                                 (current_packages / "SHA256SUMS").read_text(encoding="utf-8").splitlines())
        current_records = current_manifest["archives"]
        if ({record["file"] for record in current_records} != set(current_checksums)
                or set(current_checksums) != {p.name for p in current_packages.glob("*.zip")}):
            errors.append("Current release ZIPs differ from manifest/checksums")
        for record in current_records:
            safe_relative(record["file"])
            archive_path = current_packages / record["file"]
            data = archive_path.read_bytes()
            if (sha256(data) != record["sha256"] or len(data) != record["bytes"]
                    or current_checksums.get(record["file"]) != record["sha256"]):
                errors.append("Current release checksum mismatch: " + record["file"])
                continue
            reopened = plugin.read_zip(archive_path)
            if "-plugin-" in archive_path.name:
                plugin.validate_zip(archive_path, root)
                if plugin.inventory(reopened) != current_manifest["files"]:
                    errors.append("Plugin file inventory differs from release manifest")
            else:
                skill = archive_path.name.removesuffix("-0.1.1-runtime.zip")
                expected = {f"{skill}/{path.removeprefix(f'skills/{skill}/')}": contents
                            for path, contents in plugin.payload(root).items()
                            if path.startswith(f"skills/{skill}/")}
                if skill not in release.SKILLS or reopened != expected:
                    errors.append("Standalone runtime differs from canonical source")
    return {
        "result": "FAIL" if errors else "PASS",
        "files": len(files),
        "source_files": len(source_files),
        "archives": len(archive_records),
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
