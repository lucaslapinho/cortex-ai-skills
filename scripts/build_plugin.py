"""Build and validate the skill-only ChatGPT plugin from canonical source.

No host installation, tenant access or network calls are performed.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import stat
import sys
import tempfile
import unicodedata
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ".codex-plugin/plugin.json"
NAME = "cortex-ai-skills"
NUMBER = r"(?:0|[1-9][0-9]*)"
PRERELEASE_ID = r"(?:0|[1-9][0-9]*|[0-9A-Za-z-]*[A-Za-z-][0-9A-Za-z-]*)"
SEMVER = re.compile(NUMBER + r"\." + NUMBER + r"\." + NUMBER
                    + r"(?:-" + PRERELEASE_ID + r"(?:\." + PRERELEASE_ID + r")*)?"
                    + r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?")
MAX_COMPRESSED = 100_000_000
MAX_EXPANDED = 512 * 1024 * 1024
MAX_MEMBER = 100 * 1024 * 1024
REPARSE = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)


def release_module(root: Path):
    spec = importlib.util.spec_from_file_location("reviewed_release", root / "source/tools/release.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate JSON key")
        result[key] = value
    return result


def parse_json(data: bytes) -> dict:
    value = json.loads(data.decode("utf-8"), object_pairs_hook=json_object)
    if not isinstance(value, dict):
        raise ValueError("Expected JSON object")
    return value


class UniqueLoader(yaml.SafeLoader):
    """Safe YAML parsing with duplicate mapping keys rejected."""


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str) or key in result:
            raise ValueError("YAML mapping keys must be unique strings")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def parse_yaml(data: str) -> dict:
    value = yaml.load(data, Loader=UniqueLoader)
    if not isinstance(value, dict):
        raise ValueError("Expected YAML mapping")
    return value


def safe_name(name: str) -> str:
    if (not name or name.strip() != name or "\\" in name or ":" in name
            or name.startswith("/") or any(not p or p in {".", ".."} for p in name.split("/"))
            or len(name.split("/")) > 20 or len(name) > 240
            or any(ord(c) < 32 for c in name)):
        raise ValueError("Unsafe archive/resource path")
    if PurePosixPath(name).as_posix() != name:
        raise ValueError("Noncanonical archive/resource path")
    return name


def text(value, label: str, limit: int, single_line=False):
    if (not isinstance(value, str) or not value.strip() or len(value) > limit
            or any(unicodedata.category(c) in {"Cc", "Cf", "Zl", "Zp"}
                   and c not in "\n\r\t" for c in value)
            or (single_line and any(c in value for c in "\r\n\t"))):
        raise ValueError(f"Invalid {label}")


def manifest_path(value) -> str:
    if not isinstance(value, str) or not value.startswith("./"):
        raise ValueError("Manifest paths must start with ./")
    return safe_name(value[2:])


def validate_manifest(data: bytes, files: dict[str, bytes]) -> dict:
    manifest = parse_json(data)
    allowed = {"name", "version", "description", "author", "homepage", "repository",
               "license", "skills", "interface", "keywords"}
    if set(manifest) - allowed:
        raise ValueError("Unsupported fields in this skills-only compatibility manifest")
    if manifest.get("name") != NAME:
        raise ValueError("Unexpected plugin name")
    version = manifest.get("version")
    if not isinstance(version, str) or len(version) > 64 or not SEMVER.fullmatch(version):
        raise ValueError("Invalid plugin version")
    text(manifest.get("description"), "plugin description", 1024)
    author = manifest.get("author")
    if not isinstance(author, dict):
        raise ValueError("Missing author")
    text(author.get("name"), "author name", 120)
    if manifest.get("skills") != "./skills/":
        raise ValueError("skills must be the string ./skills/")
    interface = manifest.get("interface")
    if not isinstance(interface, dict):
        raise ValueError("Missing interface")
    for field, limit in (("displayName", 30), ("shortDescription", 30), ("developerName", 80)):
        text(interface.get(field), field, limit, single_line=True)
    text(interface.get("longDescription"), "longDescription", 4000)
    if interface.get("category") != "Security":
        raise ValueError("Expected Security category")
    capabilities = interface.get("capabilities")
    if not isinstance(capabilities, list) or not 1 <= len(capabilities) <= 20:
        raise ValueError("Invalid capabilities")
    for capability in capabilities:
        text(capability, "capability", 120, single_line=True)
    prompts = interface.get("defaultPrompt", [])
    if not isinstance(prompts, list) or len(prompts) > 3:
        raise ValueError("Invalid defaultPrompt")
    normalized_prompts = set()
    for prompt in prompts:
        text(prompt, "starter prompt", 128, single_line=True)
        normalized = " ".join(unicodedata.normalize("NFKC", prompt).casefold().split())
        if normalized in normalized_prompts or "@" in prompt:
            raise ValueError("Duplicate or MCP-mention starter prompt")
        normalized_prompts.add(normalized)
    for field in ("logo", "composerIcon"):
        asset = manifest_path(interface.get(field))
        if asset not in files or not asset.startswith("assets/") or not asset.endswith(".svg"):
            raise ValueError(f"Missing supported presentation asset: {field}")
        if len(files[asset]) > 5 * 1024 * 1024:
            raise ValueError("Icon exceeds local limit")
        svg = ET.fromstring(files[asset])
        if svg.tag != "{http://www.w3.org/2000/svg}svg":
            raise ValueError("Expected SVG icon")
        width, height = svg.get("width", ""), svg.get("height", "")
        if not width.isdigit() or not height.isdigit() or width != height or not 48 <= int(width) <= 4096:
            raise ValueError("Icon must be a square with numeric dimensions >=48")
        for element in svg.iter():
            if element.tag.rsplit("}", 1)[-1] not in {"svg", "rect", "path", "g", "circle", "title"}:
                raise ValueError("Unsupported SVG element")
            if any(key.startswith("on") or "href" in key for key in element.attrib):
                raise ValueError("External or active SVG content")
    return manifest


def validate_payload(files: dict[str, bytes], root: Path) -> dict:
    release = release_module(root)
    for name in files:
        safe_name(name)
    if MANIFEST not in files:
        raise ValueError("Plugin manifest missing")
    if any(p in files for p in ("plugin.json", ".claude-plugin/plugin.json", ".agent-plugin/plugin.json")):
        raise ValueError("Competing plugin manifests")
    manifest = validate_manifest(files[MANIFEST], files)
    names = sorted({p.split("/")[1] for p in files if p.startswith("skills/") and len(p.split("/")) > 2})
    if names != sorted(release.SKILLS):
        raise ValueError("Expected exactly seven named skill directories")
    expected_allowed = {MANIFEST, "LICENSE", manifest_path(manifest["interface"]["logo"]),
                        manifest_path(manifest["interface"]["composerIcon"])}
    markdown = {}
    for name, data in files.items():
        if name in expected_allowed:
            continue
        parts = PurePosixPath(name).parts
        if len(parts) < 3 or parts[0] != "skills" or parts[1] not in release.SKILLS:
            raise ValueError("Unexpected plugin file")
        relative = Path(*parts[2:])
        if not release.runtime(relative) or data is None:
            raise ValueError("Development/scorer content found in runtime")
        if name.endswith(".zip"):
            raise ValueError("Nested ZIP forbidden")
        decoded = data.decode("utf-8")
        if "\x00" in decoded:
            raise ValueError("Binary/NUL runtime resource")
        if name.endswith(".md"):
            markdown[name] = decoded
    for skill in names:
        entry = f"skills/{skill}/SKILL.md"
        if entry not in files:
            raise ValueError("Skill entrypoint missing")
        match = re.fullmatch(r"---\r?\n(.*?)\r?\n---(?:\r?\n|$)(.*)", files[entry].decode("utf-8"), re.S)
        if not match or not match[2].strip():
            raise ValueError("Invalid frontmatter or empty instructions")
        frontmatter = parse_yaml(match[1])
        if frontmatter.get("name") != skill or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill):
            raise ValueError("Invalid skill identity")
        if len(skill) > 64 or len(NAME + ":" + skill) > 64:
            raise ValueError("Qualified skill identity exceeds limit")
        text(frontmatter.get("description"), "skill description", 1024)
        version_path = f"skills/{skill}/VERSION"
        if version_path not in files or not SEMVER.fullmatch(files[version_path].decode().strip()):
            raise ValueError("Missing/invalid Skill VERSION")
        adapter_path = f"skills/{skill}/agents/openai.yaml"
        if adapter_path in files:
            adapter = parse_yaml(files[adapter_path].decode("utf-8"))
            interface = adapter.get("interface")
            if not isinstance(interface, dict):
                raise ValueError("Invalid adapter interface")
            text(interface.get("display_name"), "adapter display_name", 80)
            text(interface.get("short_description"), "adapter short_description", 64)
            if len(interface["short_description"]) < 25:
                raise ValueError("Adapter short_description too short")
            if "default_prompt" in interface:
                text(interface["default_prompt"], "adapter default_prompt", 4096)
    if files.get("LICENSE") != (root / "LICENSE").read_bytes():
        raise ValueError("Missing or changed project license")
    references = 0
    for name, body in markdown.items():
        for match in release.LINK.finditer(body):
            href = match[1].strip("<>")
            parsed = urlsplit(href)
            if parsed.scheme in {"https", "http", "mailto"}:
                continue
            if parsed.scheme or href.startswith(("/", "\\")):
                raise ValueError(f"Unsupported local reference in {name}")
            target = PurePosixPath(name).parent
            for part in unquote(parsed.path).split("/") if parsed.path else []:
                if part == "..":
                    target = target.parent
                elif part and part != ".":
                    target = target / part
            resolved = target.as_posix() if parsed.path else name
            if (not resolved.startswith("/".join(name.split("/")[:2]) + "/")
                    or resolved not in files):
                raise ValueError(f"Missing or escaping resource: {name}: {href}")
            if parsed.fragment and resolved in markdown:
                if unquote(parsed.fragment) not in release.anchors(markdown[resolved]):
                    raise ValueError(f"Missing resource anchor: {name}: {href}")
            references += 1
    return {"plugin_version": manifest["version"], "skills": names, "files": len(files),
            "relative_references": references}


def payload(root: Path) -> dict[str, bytes]:
    release = release_module(root)
    metadata_files = release.checked_files(root / "plugin")
    license_info = (root / "LICENSE").lstat()
    if ((root / "LICENSE").is_symlink()
            or getattr(license_info, "st_file_attributes", 0) & REPARSE):
        raise ValueError("License cannot be a link/reparse dependency")
    source = root / "source"
    report = release.audit(source)
    if report["errors"]:
        raise ValueError("Canonical source audit failed: " + "; ".join(report["errors"]))
    result = {MANIFEST: (root / "plugin" / MANIFEST).read_bytes(),
              "LICENSE": (root / "LICENSE").read_bytes()}
    manifest = parse_json(result[MANIFEST])
    for field in ("logo", "composerIcon"):
        path = manifest_path(manifest["interface"][field])
        result[path] = (root / "plugin" / path).read_bytes()
    if {p.relative_to(root / "plugin").as_posix() for p in metadata_files} != set(result) - {"LICENSE"}:
        raise ValueError("Unexpected plugin metadata/asset file")
    for skill in sorted(release.SKILLS):
        directory = source / skill
        for path in release.checked_files(directory):
            relative = path.relative_to(directory)
            if release.runtime(relative):
                result[f"skills/{skill}/{relative.as_posix()}"] = path.read_bytes()
    return result


def zip_bytes(files: dict[str, bytes]) -> bytes:
    import io
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo(name, (2026, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    return stream.getvalue()


def read_zip(path: Path) -> dict[str, bytes]:
    if path.stat().st_size > MAX_COMPRESSED:
        raise ValueError("ZIP exceeds compressed size limit")
    with zipfile.ZipFile(path) as archive:
        infos = archive.infolist()
        if not infos or len(infos) > 5000 or sum(i.file_size for i in infos) > MAX_EXPANDED:
            raise ValueError("Empty or oversized ZIP")
        names, normalized = set(), set()
        for info in infos:
            # ZipInfo normalizes backslashes on Windows and truncates NULs.
            # Validate original spelling before relying on the normalized name.
            name = safe_name(info.orig_filename)
            if name != info.filename:
                raise ValueError("Archive path was altered during ZIP parsing")
            key = unicodedata.normalize("NFKC", name).casefold()
            if name in names or key in normalized:
                raise ValueError("Duplicate or normalization-colliding archive paths")
            if (info.is_dir() or info.flag_bits & 1 or info.file_size > MAX_MEMBER
                    or stat.S_IFMT(info.external_attr >> 16) not in {0, stat.S_IFREG}
                    or info.compress_type not in {zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED}):
                raise ValueError("Unsupported archive member type/size/compression")
            names.add(name)
            normalized.add(key)
        for name in names:
            if any(parent.as_posix() in names for parent in PurePosixPath(name).parents
                   if parent.as_posix() != "."):
                raise ValueError("Archive file/directory conflict")
        return {info.filename: archive.read(info) for info in infos}


def validate_zip(path: Path, root: Path) -> dict:
    files = read_zip(path)
    report = validate_payload(files, root)
    current = payload(root)
    if files != current:
        raise ValueError("ZIP differs from canonical runtime, metadata, or assets")
    return {**report, "sha256": sha(path.read_bytes()), "canonical_files_identical": True}


def inventory(files: dict[str, bytes]) -> list[dict]:
    return [{"path": path, "bytes": len(data), "sha256": sha(data)}
            for path, data in sorted(files.items())]


def build(root: Path, output: Path) -> dict:
    root, output = root.resolve(), output.resolve()
    if output.exists() or any(output.is_relative_to(root / p) for p in ("source", "plugin", "scripts", ".git")):
        raise ValueError("Output must be a new directory outside source, plugin and tooling")
    files = payload(root)
    report = validate_payload(files, root)
    version = report["plugin_version"]
    # Validate the staged directory separately; retain no manually maintained skill copy.
    with tempfile.TemporaryDirectory(prefix="cortex-plugin-stage-") as staging:
        stage = Path(staging)
        for name, data in files.items():
            target = stage / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        staged = {p.relative_to(stage).as_posix(): p.read_bytes() for p in stage.rglob("*") if p.is_file()}
        if staged != files:
            raise ValueError("Staged files differ from planned runtime")
        validate_payload(staged, root)
        archive = zip_bytes(staged)
        if archive != zip_bytes(staged):
            raise ValueError("Build is not reproducible")
    if len(archive) > MAX_COMPRESSED:
        raise ValueError("Built archive exceeds size limit")
    output.mkdir(parents=True)
    plugin_name = f"{NAME}-plugin-{version}.zip"
    plugin_path = output / plugin_name
    plugin_path.write_bytes(archive)
    zip_report = validate_zip(plugin_path, root)
    archives = [{"file": plugin_name, "bytes": len(archive), "sha256": sha(archive)}]
    release = release_module(root)
    for skill in report["skills"]:
        relative_files = {path.removeprefix(f"skills/{skill}/"): data for path, data in files.items()
                          if path.startswith(f"skills/{skill}/")}
        skill_version = relative_files["VERSION"].decode().strip()
        runtime_name = f"{skill}-{skill_version}-runtime.zip"
        runtime_data = zip_bytes({f"{skill}/{path}": data for path, data in relative_files.items()})
        runtime_path = output / runtime_name
        runtime_path.write_bytes(runtime_data)
        reopened = read_zip(runtime_path)
        if reopened != {f"{skill}/{path}": data for path, data in relative_files.items()}:
            raise ValueError("Standalone runtime differs after ZIP serialization")
        archives.append({"file": runtime_name, "bytes": len(runtime_data), "sha256": sha(runtime_data)})
    baseline = json.loads((root / "packages/0.1.0/release-manifest.json").read_text(encoding="utf-8"))
    old_entries = {f"skills/{skill}/{entry['path']}": entry["sha256"]
                   for skill, record in baseline["skills"].items()
                   for entry in record["runtime"]["entries"]}
    differences = []
    for path, data in sorted(files.items()):
        if not path.startswith("skills/"):
            continue
        if old_entries.get(path) != sha(data):
            differences.append({"path": path, "baseline_sha256": old_entries.get(path),
                                "current_sha256": sha(data),
                                "reason": "Reviewed 0.1.1 source refresh; see per-Skill CHANGELOG and refresh reference."})
    removed = set(old_entries) - set(files)
    if removed:
        raise ValueError("Historical runtime resources unexpectedly removed")
    result = {"format": "codex-compatibility", "plugin": NAME, "plugin_version": version,
              "source_revision_boundary": "Canonical source/ at build time; history in packages/0.1.0",
              "skill_versions": {skill: files[f"skills/{skill}/VERSION"].decode().strip() for skill in report["skills"]},
              "files": inventory(files), "archives": archives,
              "changes_since_0.1.0": differences, "exceptions_to_canonical_copy": [],
              "validation": {**zip_report, "deterministic_rebuild": True,
                             "chatgpt_import": "NOT RUN", "discovery_and_behavior": "NOT RUN",
                             "tenant_compilation_execution": "NOT RUN"}}
    (output / "release-manifest.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    (output / "SHA256SUMS").write_text("".join(f"{a['sha256']}  {a['file']}\n" for a in archives), encoding="utf-8", newline="\n")
    if files != payload(root):
        raise ValueError("Canonical source changed during build")
    return {"result": "PASS", "archives": archives, "validation": result["validation"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("build", "validate"))
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--zip", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "build":
            if args.output is None:
                parser.error("build requires --output")
            result = build(args.root, args.output)
        else:
            if args.zip is None:
                parser.error("validate requires --zip")
            result = {"result": "PASS", **validate_zip(args.zip, args.root.resolve())}
    except (ValueError, OSError, KeyError, yaml.YAMLError, ET.ParseError, zipfile.BadZipFile) as exc:
        result = {"result": "FAIL", "error": str(exc)}
    print(json.dumps(result, indent=2))
    return int(result["result"] != "PASS")


if __name__ == "__main__":
    raise SystemExit(main())
