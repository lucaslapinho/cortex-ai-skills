"""Explicit offline forward evaluation using an ephemeral Codex process.

Only runtime files and selected Fixture/Prompt sections enter model context.
Publication tests, oracles and historical results never enter that context.
The output is evidence for a separate human/agent grader, not a self-awarded pass.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import tempfile
import concurrent.futures
from pathlib import Path

import release


def publication_links(response: str, skill: Path, destination: Path) -> str:
    """Rebase renderable local links only; never correct their claimed attribution."""
    def replace(match):
        href = match[1].strip("<>")
        parsed = release.urlsplit(href)
        if parsed.scheme or not parsed.path:
            return match[0]
        target = (skill / release.unquote(parsed.path)).resolve()
        if not target.is_relative_to(skill) or not target.exists():
            return match[0]
        relative = Path(os.path.relpath(target, destination.resolve().parent)).as_posix()
        if parsed.fragment:
            relative += "#" + parsed.fragment
        begin = match.start(1) - match.start(0)
        end = match.end(1) - match.start(0)
        replacement = "<" + relative + ">" if " " in relative else relative
        return match[0][:begin] + replacement + match[0][end:]
    return release.LINK.sub(replace, response)


def case_inputs(skill: Path, selected: list[str]) -> list[dict]:
    found = {}
    for category in release.CATEGORIES:
        text = (skill / f"tests/{category}.md").read_text(encoding="utf-8")
        matches = list(release.CASE.finditer(text))
        for index, match in enumerate(matches):
            if match[1] not in selected:
                continue
            block = text[match.end():matches[index + 1].start() if index + 1 < len(matches) else len(text)]
            headings = list(re.finditer(r"^(?:### +([^\n]+)|\*\*([^*]+)\*\*)\s*$", block, re.M))
            parts = {}
            for hindex, heading in enumerate(headings):
                label = (heading[1] or heading[2]).rstrip(":").strip()
                if label in {"Fixture", "Prompt"}:
                    parts[label] = block[heading.end():headings[hindex + 1].start() if hindex + 1 < len(headings) else len(block)].strip()
            if set(parts) != {"Fixture", "Prompt"}:
                raise ValueError(f"Incomplete input extraction: {match[1]}")
            found[match[1]] = {"id": match[1], **parts}
    if set(found) != set(selected):
        raise ValueError("Unknown/duplicate selected cases")
    return [found[key] for key in selected]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill", required=True, choices=release.SKILLS)
    parser.add_argument("--cases", nargs="+", required=True)
    parser.add_argument("--evidence", type=Path, required=True)
    parser.add_argument("--model", required=True, help="Explicit user-authorized model")
    parser.add_argument("--individual", action="store_true", help="One fresh process per case, at most three concurrent")
    args = parser.parse_args()
    if args.evidence.exists():
        parser.error("Evidence file must not exist")
    if args.individual:
        import sys
        def run_case(case_id):
            destination = args.evidence.with_name(args.evidence.stem + "-" + case_id + ".md")
            command = [sys.executable, "-B", str(Path(__file__).resolve()), "--skill", args.skill,
                       "--cases", case_id, "--evidence", str(destination), "--model", args.model]
            completed = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
            print(completed.stdout or completed.stderr, flush=True)
            return completed.returncode
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
            codes = list(pool.map(run_case, args.cases))
        if any(codes):
            raise RuntimeError("One or more individual forward processes failed; inspect retained outputs")
        return
    cli = shutil.which("codex")
    if not cli:
        parser.error("codex CLI is unavailable")
    root = Path(__file__).resolve().parents[1]
    skill = root / args.skill
    files = [p for p in release.checked_files(skill) if release.runtime(p.relative_to(skill))]
    snapshot = release.identity(skill, files)
    cases = case_inputs(skill, args.cases)
    prefix = ("This is a manual-load runtime session. All Skill runtime files are supplied below. "
              "Read SKILL.md completely, then use applicable supplied resources. Do not call tools, browse, "
              "read external files, inspect tests/reviews/sibling Skills, or perform any action. "
              "No live tenant or independent validation of your response is available. "
              "Produce the actual user-facing response for each case under its case ID, not a Skill review "
              "or score. Each case is separate; do not infer one fixture's facts for another.\n\n")
    runtime_blocks = []
    for path in files:
        runtime_blocks.append(f"<runtime-file path={json.dumps(path.relative_to(skill).as_posix())}>\n"
                              + path.read_text(encoding="utf-8") + "\n</runtime-file>")
    prompt = prefix + "\n\n".join(runtime_blocks) + "\n\nUSER CASES\n" + json.dumps(cases, ensure_ascii=False, indent=2)
    temp = Path(tempfile.mkdtemp(prefix="cortex-astra-forward-"))
    command = [cli, "exec", "--ignore-user-config", "--ephemeral", "--skip-git-repo-check",
               "--sandbox", "read-only", "--model", args.model, "--config", 'model_reasoning_effort="high"',
               "--config", 'web_search="disabled"', "--color", "never", "--json", "--cd", str(temp),
               "--output-last-message", str(temp / "response.md"), "-"]
    result = subprocess.run(command, input=prompt, capture_output=True, text=True, encoding="utf-8",
                            errors="strict", timeout=900)
    (temp / "events.jsonl").write_text(result.stdout, encoding="utf-8")
    (temp / "diagnostic.txt").write_text(result.stderr, encoding="utf-8")
    if result.returncode or not (temp / "response.md").exists():
        raise RuntimeError(f"Forward process failed; diagnostic retained in {temp}")
    response = (temp / "response.md").read_text(encoding="utf-8")
    events = [json.loads(line) for line in result.stdout.splitlines() if line.strip().startswith("{")]
    tool_events = [e for e in events if e.get("item", {}).get("type") in {
        "command_execution", "mcp_tool_call", "web_search", "file_change"}]
    final_files = [p for p in release.checked_files(skill) if release.runtime(p.relative_to(skill))]
    if snapshot != release.identity(skill, final_files):
        raise RuntimeError("Runtime changed during evaluation; do not grade this output")
    record = f"# Astra forward output — {args.skill}\n\n"
    record += f"Model requested: `{args.model}`, high reasoning; ephemeral CLI, manual inline runtime load.\n\n"
    record += f"Runtime: {snapshot['files']} files / {snapshot['bytes']} bytes; ordinal SHA-256 `{snapshot['sha256']}`.\n\n"
    record += f"Isolation: {len(tool_events)} tool/action events. Runtime files plus Fixture/Prompt only; no oracle text supplied. "
    record += ("One fresh ephemeral process contains this case only. " if len(cases) == 1 else
               "Multiple cases share a single process for this Skill; they are not independently randomized sessions. ")
    record += "No self-grading result is assigned here. Independent adjudication is required.\n\n"
    for case in cases:
        record += f"## Input {case['id']}\n\n### Fixture\n\n{case['Fixture']}\n\n### Prompt\n\n{case['Prompt']}\n\n"
    record += "Local Markdown links are rebased for publication only; wording and attribution are unchanged. Raw response/event files remain in the evaluation archive outside the publication tree.\n\n"
    record += "## Retained response\n\n" + publication_links(response, skill, args.evidence) + "\n"
    args.evidence.parent.mkdir(parents=True, exist_ok=True)
    with args.evidence.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(record)
    print(json.dumps({"evidence": str(args.evidence), "cases": args.cases, "tool_events": len(tool_events),
                      "runtime_sha256": snapshot["sha256"], "raw_evidence_directory": str(temp),
                      "status": "READY FOR INDEPENDENT GRADING" if not tool_events else "ISOLATION REVIEW REQUIRED"}, indent=2))


if __name__ == "__main__":
    main()
