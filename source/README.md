# Cortex AI Skills

Seven modular AI Skills for evidence-scoped work across the Palo Alto Networks Cortex ecosystem. Each Skill can be installed and used independently; the repository adds shared development research and review evidence but is never required at runtime.

## Skills

| Skill | Primary use |
|---|---|
| [`cortex-xql-query-engineer`](cortex-xql-query-engineer/README.md) | Construct, explain, review, optimize, and troubleshoot XQL with explicit product, surface, schema, and tenant boundaries |
| [`cortex-detection-engineer`](cortex-detection-engineer/README.md) | Design and review evidence-scoped detections across their threat model, telemetry, validation, tuning, and lifecycle |
| [`cortex-playbook-engineer`](cortex-playbook-engineer/README.md) | Design safe Cortex automation with approvals, failure handling, recovery, verification, and evidence |
| [`cortex-threat-hunter`](cortex-threat-hunter/README.md) | Build hypothesis-driven hunts with telemetry gaps, pivots, scoping, competing explanations, and detection handoff |
| [`cortex-tim-engineer`](cortex-tim-engineer/README.md) | Engineer governed threat-intelligence collection, scoring, lifecycle, interoperability, and distribution workflows |
| [`cortex-platform-engineer`](cortex-platform-engineer/README.md) | Design and troubleshoot Cortex platform, collection, ingestion, mapping, integration, access, and data-flow architecture |
| [`cortex-security-engineer`](cortex-security-engineer/README.md) | Scope and route cross-domain Cortex security-engineering requests while remaining useful without sibling Skills |

The XQL Skill was implemented and independently approved first. Its structure became the [frozen architecture](ARCHITECTURE.md) for the other domains; its XQL-specific content was not cloned into them.

## Evidence contract

Factual product behavior follows this precedence:

1. current official Palo Alto Networks documentation;
2. official Palo Alto examples, repositories, API references, and product guides;
3. verified project-specific Cortex knowledge actually available in the workspace;
4. secondary sources only when necessary and clearly labeled.

Claims use one status: `VERIFIED`, `VERSION-DEPENDENT`, `INFERRED`, `CONCEPTUAL`, `UNSUPPORTED`, `DEPRECATED`, or `UNVERIFIED`. Provenance and validation depth use separate qualifiers such as `OFFICIAL-CURRENT`, `PROJECT-ASSERTED`, `REFERENCED-ONLY`, `TENANT-UNVERIFIED`, `TENANT-SCHEMA-VERIFIED`, `TENANT-COMPILED`, and `TENANT-EXECUTED`.

Static structure or official documentation never proves tenant schema, compilation, import, execution, deployment, returned results, detection efficacy, or performance. Every Skill's `VALIDATION.md` records those levels separately.

## Install one Skill

Treat each top-level Skill directory as a publication/source package, not as the installable runtime tree. Create a target directory named for the selected Skill and copy only `SKILL.md`, `VERSION`, `agents/`, `references/`, `templates/`, and `examples/`. Do not install `README.md`, `CHANGELOG.md`, `VALIDATION.md`, `tests/`, root `research/` or `reviews/`, prior outputs, or scorer material into model runtime context.

For current Codex local discovery, place each Skill under one of the documented locations:

```text
# User scope
$HOME/.agents/skills/<skill-name>/

# Repository scope
$REPO_ROOT/.agents/skills/<skill-name>/
```

Codex also searches `.agents/skills` from the current working directory upward through the repository root. This source checkout intentionally keeps publication packages at its root and is not itself a Codex or Claude automatic-discovery tree, because the publication packages contain scorer-only tests. Build the runtime-only target directory first. Recheck the [official Build skills documentation](https://developers.openai.com/codex/skills) before installation because discovery locations can evolve.

Invoke it using the host-supported selector or by naming the Skill naturally. This repository's OpenAI adapter prompts use `$skill-name`; other ChatGPT or Claude-style hosts may expose a different selector. See each Skill README for its capability-based platform status. Static compatibility is not a runtime claim.

## Host-surface boundaries

| Surface | Required packaging/loading | Repository evidence |
|---|---|---|
| ChatGPT desktop | Runtime-only standalone Skill through the supported workspace mechanism | Static package compatibility reviewed; manual load and behavioral runtime `NOT RUN` |
| ChatGPT web/mobile | Plugin packaging | Plugin package not included; runtime `NOT RUN` |
| Codex CLI/IDE | Runtime-only directory in a documented `.agents/skills` location | Static package compatibility reviewed; automatic discovery `NOT RUN`; only XQL has a separately recorded tests-free manual-load smoke result |
| Claude Code | Runtime-only directory under `.claude/skills/<skill-name>/` | Static package compatibility reviewed; discovery and runtime `NOT RUN` |
| claude.ai | Runtime-only ZIP custom Skill with code execution | Upload and runtime `NOT RUN` |
| Claude API | Uploaded custom Skill referenced by `skill_id` with code execution | Upload and runtime `NOT RUN`; do not assume network or runtime package installation |

Review the current [OpenAI Skill guidance](https://learn.chatgpt.com/docs/build-skills), [Claude Code Skills guidance](https://code.claude.com/docs/en/skills), and [Anthropic Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) before distribution because host mechanisms can change.

## Package boundaries

Each Skill separates:

- a complete publication package;
- an oracle-free runtime package containing only the operating files; and
- a scorer package containing authored tests and evaluation artifacts.

Tests, expected observations, prohibited behaviors, authored results, review reports, prior outputs, root research, and sibling Skills must not be exposed to the model during a controlled forward test.

## Development and review

### Reproduce the audit and build runtime ZIPs

With Python 3.10+ and no third-party packages, run from this repository:

```text
python -B tools/release.py audit --release
python -B -m unittest discover -s tools -p test_release.py -v
python -B tools/release.py manifest
python -B tools/release.py package --output ../cortex-ai-skills-release-new
```

The output directory must not exist and must be outside this source tree. Packaging creates seven individually rooted runtime-only ZIPs, one complete source ZIP, a per-file identity manifest, and `SHA256SUMS`. It refuses unresolved release markers, escaping runtime links, reparse dependencies, and overwrites. ZIP timestamps/order/permissions are fixed; CRC and source stability are checked. Nothing is installed globally or deployed to Cortex. The source ZIP contains tests and review evidence and must not be used as a runtime Skill.

The tool checks static structure; it does not replace official-document review, independent behavioral evaluation, host discovery, or tenant tests. See the [Astra review](reviews/astra-review.md) for the final improvement pass and its exact evidence boundaries.

Optional model evaluation uses `tools/evaluate.py` with an explicitly selected model and case IDs; `--individual` creates a fresh ephemeral process per case. `tools/evaluate_astra_cases.py` reproduces the 23-case completion sample, not the full catalog, and consumes model quota. Both refuse overwriting evidence. Only runtime content plus Fixture/Prompt is supplied; a separate reviewer must score the outputs. Offline source summaries do not establish a new live-document or tenant check.

### Review records

- [Architecture specification](ARCHITECTURE.md)
- [Contribution guide](CONTRIBUTING.md)
- [Repository changelog](CHANGELOG.md)
- [Phase 1 research](research/phase-1-checkpoint.md)
- [Golden Reference approval](reviews/xql-golden-reference-review.md)
- [Cross-Skill review](reviews/cross-skill-review.md)
- [Adversarial review](reviews/adversarial-review.md)
- [Compatibility review](reviews/compatibility-review.md)
- [Known limitations](reviews/known-limitations.md)
- [Final QA and release matrix](reviews/final-qa.md)

Some review links are release artifacts and become authoritative only when final QA is complete. Follow [CONTRIBUTING.md](CONTRIBUTING.md) for source, testing, safety, and change-control requirements.

## Project knowledge boundary

The build consumed Cortex artifacts that were actually readable in the execution environment and reconciled them with current official documentation. The [project knowledge inventory](research/project-knowledge-inventory.md) records what was accessible and which Skills consume it; [project-versus-official differences](research/project-vs-official-differences.md) records meaningful discrepancies. Inaccessible ChatGPT Project/File Library items and named-but-missing originals were recorded as unavailable; they were not reconstructed or represented as ingested knowledge.

Project-specific material can influence workflow and conventions, but it cannot override current official product behavior silently. Meaningful differences are retained and classified as legacy, customized, version-specific, incorrect, or unresolved.

## Safety and non-certifications

Read-only analysis is the default. State-changing guidance requires explicit authorization, least privilege, scope, blast-radius control, partial-failure handling, recovery, verification, and evidence retention as applicable.

This `0.1.0` repository does not by itself certify a specific Cortex tenant, schema, license, role, compiler, import format, execution result, deployment, production efficacy, or measured performance. Check the per-Skill validation ledgers and the final QA report before relying on a capability claim.

## License

Released under the [MIT License](LICENSE).
