# Cortex Detection Engineer

Standalone AI Skill for designing, reviewing, validating, tuning, monitoring, and retiring evidence-scoped detections for Cortex XSIAM and Cortex XDR.

## What it provides

The Skill follows this lifecycle:

```text
Threat behavior
  -> threat model
  -> ATT&CK interpretation
  -> telemetry contract
  -> query/logic handoff
  -> expected signal
  -> baseline/threshold
  -> validation
  -> FP/FN analysis
  -> tuning
  -> rule-surface decision
  -> monitoring, rollback, retirement
```

It distinguishes IOC/indicator logic, BIOC, BIOC-derived custom prevention, scheduled correlation, real-time correlation, and Analytics/ABIOC behavior. It also keeps Query Center validity separate from rule compatibility, rule creation separate from deployment, an Issue separate from a Case, and field mapping separate from a grouping guarantee.

It does not provide tenant access, author an entire XQL language solution, configure ingestion, build playbooks, approve prevention/containment, or certify an importable rule file.

## Maturity

Current version: `0.1.0`

This release is pre-1.0 because no live tenant, schema export, rule editor/compiler, representative tenant telemetry, controlled deployment, generated Issue/Case, or production outcome was available during authoring. Product behavior documented in current official sources remains distinct from tenant validation.

See [VALIDATION.md](VALIDATION.md) for the exact ledger and [CHANGELOG.md](CHANGELOG.md) for release history.

## Package layout

```text
cortex-detection-engineer/
├── SKILL.md
├── README.md
├── VERSION
├── CHANGELOG.md
├── VALIDATION.md
├── agents/openai.yaml
├── references/
├── templates/
├── examples/
└── tests/
```

The behavioral core is [SKILL.md](SKILL.md). Detailed facts are progressively disclosed through `references/`; response scaffolds live in `templates/`; demonstrations live in `examples/`; oracle-bearing maintainer cases live in `tests/`.

The Skill has no runtime dependency on repository-root files, sibling Skills, private project memory, a fixed local path, or live network access.

## Example requests

- “Design a Cortex XSIAM correlation rule for suspicious PowerShell behavior, but keep unverified fields as placeholders.”
- “Review whether this Query Center hunt is ready for a BIOC or scheduled correlation rule.”
- “Tune this high-volume detection without hiding likely true positives.”
- “Compare scheduled and real-time correlation for this use case.”
- “Explain why this rule is generating Issues but not useful Cases.”
- “Create a validation and retirement plan for this mature detection.”

Useful inputs include product/version, rule type, objective, telemetry/schema evidence, existing query/export, baseline window, known positives and benign cases, volume, response capacity, permissions, and deployment constraints.

## Evidence model

Every material claim uses one canonical status:

`VERIFIED`, `VERSION-DEPENDENT`, `INFERRED`, `CONCEPTUAL`, `UNSUPPORTED`, `DEPRECATED`, or `UNVERIFIED`.

Qualifiers such as `OFFICIAL-CURRENT`, `OFFICIAL-EXAMPLE`, `TENANT-UNVERIFIED`, `TENANT-SCHEMA-VERIFIED`, `TENANT-COMPILED`, and `TENANT-EXECUTED` describe provenance or depth; they do not replace the status.

Validation levels are independent:

| Level | Establishes | Does not establish |
|---|---|---|
| `S` | Controlled response behavior | Current product facts or tenant behavior |
| `D` | Current official-document support | Tenant availability or acceptance |
| `C` | Named tenant/editor/compiler acceptance | Representative results or quality |
| `E` | Bounded execution/deployment observation | Universal behavior across releases/tenants |

## Installation and invocation

Create a target directory named `cortex-detection-engineer` in the Skills location supported by the host and copy only the oracle-free runtime manifest: `SKILL.md`, `VERSION`, `agents/`, `references/`, `templates/`, and `examples/`. Preserve relative paths. Do not install `README.md`, `CHANGELOG.md`, `VALIDATION.md`, or `tests/` into model context. `agents/openai.yaml` provides optional OpenAI UI, invocation-policy, and dependency metadata; Skill discovery and implicit matching use the `SKILL.md` name and description.

| Surface | Runtime packaging/loading | Invocation/discovery | Current validation |
|---|---|---|---|
| ChatGPT desktop | Runtime-only standalone Skill through the supported workspace mechanism | Select or name the Skill | Independent static package `PASS`; manual load and behavioral runtime `NOT RUN` |
| ChatGPT web/mobile | Requires plugin packaging not included here | Plugin-defined | Plugin packaging and runtime `NOT RUN` |
| Codex CLI/IDE | Runtime-only directory in a documented `.agents/skills` location | `$cortex-detection-engineer`; automatic discovery after installation | Independent static package `PASS`; manual load, automatic discovery, and behavioral runtime `NOT RUN` |
| Claude Code | Runtime-only directory under `.claude/skills/cortex-detection-engineer/` | Host selector or natural name | Independent static package `PASS`; discovery and behavioral runtime `NOT RUN` |
| claude.ai | Runtime-only ZIP uploaded as a custom Skill; code execution required | Workspace Skill selection | Upload and behavioral runtime `NOT RUN` |
| Claude API | Uploaded custom Skill referenced by `skill_id`; code execution required | API request configuration | Upload and behavioral runtime `NOT RUN`; no network or runtime package installation assumed |

Do not interpret a compatible directory shape as a runtime pass.

## Manifests

- **Publication manifest:** the complete Skill directory, including README, changelog, validation ledger, and tests.
- **Runtime manifest:** `SKILL.md`, `VERSION`, `agents/`, `references/`, `templates/`, and `examples/` only.
- **Scorer manifest:** the publication package plus isolated outputs and result records; it must never be exposed to the model under test.

Runtime excludes `README.md`, `CHANGELOG.md`, `VALIDATION.md`, `tests/`, review records, scorers, and prior outputs. A clean runtime copy must remain useful when every sibling and root artifact is absent.

## Safety boundary

Design and read-only review are defaults. Rule create/import/edit/enable/disable/delete, exception changes, suppression changes, lookup/dataset writes, and BIOC-derived prevention are state-changing. They require explicit target, owner, authorization, least privilege, bounded scope, representative tests, blast-radius analysis, recovery/rollback, post-change verification, and audit retention.

A detection signal, ATT&CK mapping, confidence label, or advisory model result never authorizes containment.

## Maintenance

For each product release or relevant content change:

```text
Review official release documentation
  -> refresh affected source records
  -> identify changed rule contracts and limits
  -> revalidate examples and tests
  -> rerun hallucination and compatibility audits
  -> obtain independent review
  -> update VERSION and CHANGELOG
```

Recheck numerical limits, license statements, stages/functions, actions, terminology, grouping behavior, permissions, and safeguard thresholds before production use.

## Contributing

Preserve standalone operation. Cite a specific current official page for every new product behavior. Add a behavioral regression for every corrected failure mode. Never convert author checks into independent approval or tenant execution claims.
