# Cortex Security Engineer

`cortex-security-engineer` is the cross-domain intake and orchestration Skill for Cortex security engineering. It converts an ambiguous or multi-domain request into an evidence-bounded decision record, routes specialist mechanics, sequences dependencies, and preserves ownership, approval, validation, and operations gates.

It is useful without any sibling Skill installed. It does not contain a second full XQL, detection, hunting, playbook, TIM, or platform manual.

## What it covers

- product and surface disambiguation across Cortex XSIAM, Cortex XDR, Cortex XSOAR, Cortex Cloud, and licensed capabilities;
- routing among XQL, detection, hunting, playbook, threat-intelligence, and platform work;
- security requirements, threat/risk models, telemetry contracts, control architecture, validation plans, operating models, and decision records;
- multi-domain dependency sequencing and handoff packets;
- evidence, authorization, least-privilege, rollback/recovery, and production-promotion boundaries.

## What it does not claim

The package contains no tenant state, schema, credentials, API responses, configuration exports, compiler output, execution results, deployments, or efficacy measurements. Examples and tests are authored fixtures, not tenant evidence. Version `0.1.0` has independent static, documentation, domain, adversarial, and selected behavioral review for source publication only; it is not a tenant or deployment certification.

## Package navigation

| Need | File |
|---|---|
| Runtime contract | [SKILL.md](SKILL.md) |
| Evidence and Cortex product boundaries | [references/evidence-and-product-boundaries.md](references/evidence-and-product-boundaries.md) |
| Product/surface routing | [references/product-surface-map.md](references/product-surface-map.md) |
| Domain ownership and handoffs | [references/routing-and-ownership.md](references/routing-and-ownership.md) |
| Decision-record method | [references/decision-record-method.md](references/decision-record-method.md) |
| Safety and authorization | [references/safety-and-authorization.md](references/safety-and-authorization.md) |
| Validation and lifecycle | [references/validation-and-operations.md](references/validation-and-operations.md) |
| Current official source register | [references/official-sources.md](references/official-sources.md) |
| Diagnostic branches | [references/troubleshooting.md](references/troubleshooting.md) |
| Reusable records | [request-intake template and adjacent records](templates/request-intake.md) |
| Conceptual worked examples | [example index](examples/README.md) |
| Isolated behavioral suite | [tests/README.md](tests/README.md) |
| Author validation state | [VALIDATION.md](VALIDATION.md) |

For host installation, create a target directory named `cortex-security-engineer` and copy only the 22-file isolated runtime manifest below. The complete 33-file tree is the publication/source package and must not be exposed as runtime context because it includes scorer oracles.

## Manifests

### Publication/source manifest — 33 files

The publication tree is the complete `cortex-security-engineer/` directory:

- `SKILL.md`, `README.md`, `VERSION`, `CHANGELOG.md`, `VALIDATION.md`;
- `agents/openai.yaml`;
- all 9 files under `references/`;
- all 5 files under `templates/`;
- all 5 files under `examples/`;
- all 8 files under `tests/`.

### Isolated runtime manifest — 22 files

Expose only:

- `SKILL.md` and `VERSION`;
- `agents/openai.yaml`;
- all files under `references/`, `templates/`, and `examples/`.

Exclude `README.md`, `CHANGELOG.md`, `VALIDATION.md`, all of `tests/`, repository-root research/reviews, sibling Skills, prior responses, and scorer rubrics.

### Scorer manifest

The evaluator may read the complete publication tree. The runtime must not read these scorer-only files:

- `tests/README.md`;
- `tests/basic.md`;
- `tests/intermediate.md`;
- `tests/advanced.md`;
- `tests/troubleshooting.md`;
- `tests/ambiguity.md`;
- `tests/adversarial.md`;
- `tests/regression.md`.

Responses, evaluator ledgers, and approval records live outside the publication/runtime package. An independent forward run must record the exact publication and runtime hashes.

## Platform compatibility matrix

This is a packaging assessment, not runtime evidence.

| Surface | Runtime packaging/loading | Invocation/discovery | Current validation |
|---|---|---|---|
| ChatGPT desktop | Runtime-only standalone Skill through the supported workspace mechanism | Select or name the Skill | Independent static package `PASS`; manual load and behavioral runtime `NOT RUN` |
| ChatGPT web/mobile | Requires plugin packaging not included here | Plugin-defined | Plugin packaging and runtime `NOT RUN` |
| Codex CLI/IDE | Runtime-only directory in a documented `.agents/skills` location | `$cortex-security-engineer`; automatic discovery after installation | Independent static package `PASS`; manual load, automatic discovery, and behavioral runtime `NOT RUN` |
| Claude Code | Runtime-only directory under `.claude/skills/cortex-security-engineer/` | Host selector or natural name | Independent static package `PASS`; discovery and behavioral runtime `NOT RUN` |
| claude.ai | Runtime-only ZIP uploaded as a custom Skill; code execution required | Workspace Skill selection | Upload and behavioral runtime `NOT RUN` |
| Claude API | Uploaded custom Skill referenced by `skill_id`; code execution required | API request configuration | Upload and behavioral runtime `NOT RUN`; no network or runtime package installation assumed |

Cross-platform text portability does not establish identical discovery, tool access, safety enforcement, or response quality.

`agents/openai.yaml` provides optional OpenAI UI, invocation-policy, and dependency metadata. Skill discovery and implicit matching use the `SKILL.md` name and description.

## Versioning and release

The current version is [VERSION](VERSION). Changes are listed in [CHANGELOG.md](CHANGELOG.md). A release is eligible for approval only when independent reviewers resolve all BLOCKER, CRITICAL, and HIGH findings and record `S` and `D` explicitly. `C` and `E` remain `NOT RUN` unless a named non-production tenant exercise is separately authorized and evidenced.
