"""Offline audit and reproducible packaging; never installs or deploys a Skill."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import stat
import unicodedata
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

SKILLS = (
    "cortex-xql-query-engineer", "cortex-detection-engineer",
    "cortex-playbook-engineer", "cortex-threat-hunter", "cortex-tim-engineer",
    "cortex-platform-engineer", "cortex-security-engineer",
)
RUNTIME_FILES = {"SKILL.md", "VERSION"}
RUNTIME_DIRS = {"agents", "references", "templates", "examples"}
COUNTS = (41, 39, 28, 26, 37, 41, 41)
CATEGORIES = ("basic", "intermediate", "advanced", "troubleshooting",
              "ambiguity", "adversarial", "regression")
CASE = re.compile(r"^##\s+([A-Z][A-Z0-9-]*)(?:\s+[—-]|:)[^\n]*$", re.M)
LINK = re.compile(r"(?<!!)\[[^\]\n]*\]\((<[^>]+>|[^\s)]+)(?:\s+\"[^\"]*\")?\)")
REPARSE = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def checked_files(root: Path) -> list[Path]:
    """Reject links/junctions before descending; don't follow external content."""
    found = []
    def walk(directory):
        for path in directory.iterdir():
            info = path.lstat()
            if path.is_symlink() or getattr(info, "st_file_attributes", 0) & REPARSE:
                raise ValueError(f"Link/reparse dependency: {path.name}")
            if path.name in {".git", "__pycache__"}:
                continue
            if path.is_dir():
                walk(path)
            elif path.is_file():
                found.append(path)
            else:
                raise ValueError(f"Non-regular file: {path.name}")
    if root.is_symlink() or getattr(root.lstat(), "st_file_attributes", 0) & REPARSE:
        raise ValueError("Root cannot be a link/reparse point")
    walk(root)
    return sorted(found, key=lambda p: p.relative_to(root).as_posix())


def runtime(path: Path) -> bool:
    return (len(path.parts) == 1 and path.name in RUNTIME_FILES
            or len(path.parts) > 1 and path.parts[0] in RUNTIME_DIRS)


def identity(root: Path, files: list[Path]) -> dict:
    ordered = sorted(files, key=lambda p: p.relative_to(root).as_posix())
    rows = [{"path": p.relative_to(root).as_posix(), "bytes": p.stat().st_size,
             "sha256": digest(p.read_bytes())} for p in ordered]
    records = "\n".join(f"{r['sha256']}  {r['path']}" for r in rows)
    return {"files": len(rows), "bytes": sum(r["bytes"] for r in rows),
            "sha256": digest(records.encode("utf-8")), "entries": rows}


def manifests(root: Path) -> dict:
    result = {}
    for name in SKILLS:
        skill = root / name
        files = checked_files(skill)
        result[name] = {"version": (skill / "VERSION").read_text().strip(),
                        "runtime": identity(skill, [p for p in files if runtime(p.relative_to(skill))]),
                        "publication": identity(skill, files)}
    return result


def anchors(text: str) -> set[str]:
    result, counts = set(), {}
    fence = False
    for line in text.splitlines():
        if re.match(r"^\s*(```|~~~)", line):
            fence = not fence
        if fence or not re.match(r"^#{1,6} ", line):
            continue
        title = re.sub(r"^#{1,6} +", "", line).strip().lower()
        title = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", title)
        title = "".join(c for c in title if c in " -_" or unicodedata.category(c)[0] in "LN")
        slug = title.replace(" ", "-")
        number = counts.get(slug, 0)
        counts[slug] = number + 1
        result.add(slug if not number else f"{slug}-{number}")
    return result


def audit(root: Path, release: bool = False) -> dict:
    errors, texts = [], {}
    files = checked_files(root)
    for path in files:
        if path.suffix.lower() not in {".md", ".yaml", ".yml", ".py"} and path.name not in {"VERSION", "LICENSE"}:
            errors.append(f"Unexpected publication file: {path.relative_to(root)}")
            continue
        try:
            body = path.read_bytes().decode("utf-8", errors="strict")
        except UnicodeDecodeError:
            errors.append(f"Invalid UTF-8: {path.relative_to(root)}")
            continue
        if path.suffix != ".md":
            continue
        texts[path] = body
        if any(c in body for c in ("\ufeff", "\u200b", "\u202e")):
            errors.append(f"Invisible/BOM/bidi marker: {path.relative_to(root)}")
        opened = None
        for line in body.splitlines():
            match = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
            if match:
                marker = match[1]
                if opened is None:
                    opened = marker
                elif marker[0] == opened[0] and len(marker) >= len(opened):
                    opened = None
        if opened:
            errors.append(f"Unclosed fence: {path.relative_to(root)}")
        if re.search(r"[A-Za-z]:[\\/]Users[\\/]|/Users/[^\s/]+/|/home/[^\s/]+/|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----", body):
            errors.append(f"Local user path/private key marker: {path.relative_to(root)}")
    links = runtime_links = path_links = runtime_path_links = 0
    for path, body in texts.items():
        skill_root = next((root / name for name in SKILLS if path.is_relative_to(root / name)), None)
        is_runtime = skill_root is not None and runtime(path.relative_to(skill_root))
        for match in LINK.finditer(body):
            href = match[1].strip("<>")
            parsed = urlsplit(href)
            if parsed.scheme in {"https", "http", "mailto"}:
                continue
            if parsed.scheme or href.startswith(("/", "\\")):
                errors.append(f"Absolute/unsupported local link: {path.name}: {href}")
                continue
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            links += 1
            if parsed.path:
                path_links += 1
            if is_runtime:
                runtime_links += 1
                if parsed.path:
                    runtime_path_links += 1
            if not target.is_relative_to(root) or not target.exists():
                errors.append(f"Missing/escaping link: {path.relative_to(root)}: {href}")
                continue
            if is_runtime and (not target.is_relative_to(skill_root) or not runtime(target.relative_to(skill_root))):
                errors.append(f"Runtime/scorer escape: {path.relative_to(root)}: {href}")
            if parsed.fragment and target in texts and unquote(parsed.fragment) not in anchors(texts[target]):
                errors.append(f"Missing anchor: {path.relative_to(root)}: {href}")
    total_cases = 0
    for name, expected in zip(SKILLS, COUNTS):
        skill = root / name
        required = ["SKILL.md", "README.md", "VERSION", "CHANGELOG.md", "VALIDATION.md", "agents/openai.yaml"]
        required += [f"tests/{c}.md" for c in CATEGORIES]
        for rel in required:
            if not (skill / rel).is_file() or not (skill / rel).stat().st_size:
                errors.append(f"Required file absent/empty: {name}/{rel}")
        if not all((skill / d).is_dir() and any((skill / d).iterdir()) for d in RUNTIME_DIRS):
            errors.append(f"Missing/empty runtime directory: {name}")
        entry = texts.get(skill / "SKILL.md", "")
        if not re.match(r"\A---\r?\nname: " + re.escape(name) + r"\r?\ndescription: .+?\r?\n---", entry, re.S):
            errors.append(f"Frontmatter name/description: {name}")
        version = (skill / "VERSION").read_text()
        if not re.fullmatch(r"\d+\.\d+\.\d+\n", version):
            errors.append(f"Invalid VERSION: {name}")
        if len(re.findall(r"^- \[x\]", texts.get(skill / "VALIDATION.md", ""), re.M)) != 18:
            errors.append(f"Expected 18 checklist items: {name}")
        ids = []
        for category in CATEGORIES:
            body = texts.get(skill / f"tests/{category}.md", "")
            matches = list(CASE.finditer(body))
            for i, match in enumerate(matches):
                ids.append(match[1])
                block = body[match.end():matches[i + 1].start() if i + 1 < len(matches) else len(body)]
                for heading in ("Fixture", "Prompt", "Expected observations", "Prohibited behaviors", "Evidence expected", "Authored result"):
                    if not re.search(r"(?:### +|\*\*)" + re.escape(heading) + r"(?::?\*\*|\s*\r?$)", block, re.M):
                        errors.append(f"Missing {heading}: {name}/{match[1]}")
        if len(ids) != expected or len(ids) != len(set(ids)):
            errors.append(f"Case count/uniqueness: {name}: {len(ids)}, expected {expected}")
        total_cases += len(ids)
    if release:
        for rel, terminal in {
            "reviews/xql-golden-reference-review.md": "GOLDEN REFERENCE APPROVED: YES",
            "reviews/cross-skill-review.md": "CROSS-SKILL REVIEW: PASS",
            "reviews/adversarial-review.md": "ADVERSARIAL REVIEW: PASS",
            "reviews/compatibility-review.md": "COMPATIBILITY REVIEW: PASS",
            "reviews/final-qa.md": "REPOSITORY PRODUCTION READY: YES",
        }.items():
            report_text = texts.get(root / rel, "")
            if not report_text.rstrip().endswith(terminal) or report_text.splitlines().count(terminal) != 1:
                errors.append(f"Release gate not approved: {rel}")
        current = manifests(root)
        for name, record in current.items():
            for rel in ("reviews/final-qa.md", "reviews/cross-skill-review.md", "reviews/adversarial-review.md", f"{name}/VALIDATION.md"):
                if record["runtime"]["sha256"] not in texts.get(root / rel, ""):
                    errors.append(f"Current runtime identity absent: {name} in {rel}")
            if record["publication"]["sha256"] not in texts.get(root / "reviews/final-qa.md", ""):
                errors.append(f"Current publication identity absent: {name}")
    return {"result": "FAIL" if errors else "PASS", "publication_files": len(files),
            "markdown_files": len(texts), "local_links_including_anchors": links,
            "runtime_links_including_anchors": runtime_links,
            "local_path_links": path_links, "runtime_path_links": runtime_path_links,
            "authored_cases": total_cases, "errors": errors}


def write_zip(destination: Path, base: Path, files: list[Path], prefix: str):
    """Fixed timestamps, POSIX members, stable ordering, exclusive creation."""
    with zipfile.ZipFile(destination, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(files, key=lambda p: p.relative_to(base).as_posix()):
            name = f"{prefix}/{path.relative_to(base).as_posix()}"
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def package(root: Path, output: Path) -> dict:
    if output.exists() or output.is_relative_to(root) or root.is_relative_to(output):
        raise ValueError("Output must be a new directory outside the source tree, not an ancestor")
    report = audit(root, release=True)
    if report["errors"]:
        raise ValueError(json.dumps(report))
    before = manifests(root)
    source_files = checked_files(root)
    source_identity = identity(root, source_files)
    output.mkdir(parents=False)
    archives = []
    for name in SKILLS:
        skill = root / name
        files = [p for p in checked_files(skill) if runtime(p.relative_to(skill))]
        destination = output / f"{name}-{before[name]['version']}-runtime.zip"
        write_zip(destination, skill, files, name)
        archives.append(destination)
    destination = output / "cortex-ai-skills-0.1.0-source.zip"
    write_zip(destination, root, source_files, "cortex-ai-skills")
    archives.append(destination)
    if before != manifests(root) or source_identity != identity(root, checked_files(root)):
        raise ValueError("Source changed while packaging; artifacts are incomplete, do not distribute")
    for archive_path in archives:
        with zipfile.ZipFile(archive_path) as archive:
            if archive.testzip() is not None:
                raise ValueError(f"CRC verification failed: {archive_path.name}")
    result = {"recipe": "ordinal POSIX paths; SHA256(file) + two spaces + path; LF joined; no final LF; UTF-8",
              "skills": before, "source": source_identity,
              "archives": [{"file": p.name, "bytes": p.stat().st_size, "sha256": digest(p.read_bytes())} for p in archives]}
    with (output / "release-manifest.json").open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(result, indent=2) + "\n")
    with (output / "SHA256SUMS").open("x", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(f"{r['sha256']}  {r['file']}" for r in result["archives"]) + "\n")
    return {"output": str(output), "archives": result["archives"], "result": "PASS"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("audit", "manifest", "package"))
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--release", action="store_true", help="Require all independent release markers")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    if args.command == "manifest":
        result = manifests(root)
    elif args.command == "audit":
        result = audit(root, args.release)
    else:
        if args.output is None:
            parser.error("package requires --output")
        result = package(root, args.output.resolve())
    print(json.dumps(result, indent=2))
    return 1 if result.get("result") == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())
