# Initial Architecture Decisions

## Document status

Completion note (2026-09-06): this Phase 1 decision history is preserved. The Golden Reference was subsequently approved and the resulting [frozen architecture](../ARCHITECTURE.md) governs the completed seven-Skill release. Provisional labels below describe their original decision stage, not unfinished publication work.

This is the Phase 1 architecture decision record for the Cortex Skills repository. Decisions marked **Accepted** are explicit project constraints. Decisions marked **Provisional** must be exercised by `cortex-xql-query-engineer`, reviewed, corrected, and frozen in `../ARCHITECTURE.md` only after the Golden Reference review ends with `GOLDEN REFERENCE APPROVED: YES`.

Technical behavior is governed by the current official source register in `documentation-sources.md`. Operational project context is summarized in `project-findings.md`; conflicts must remain visible rather than being silently normalized.

## Decision summary

| ID | Decision | Status |
|---|---|---|
| ADR-001 | Implement and approve XQL as the Golden Reference before the other six Skills | Accepted |
| ADR-002 | Share conventions, never mandatory runtime files | Accepted |
| ADR-003 | Use progressive disclosure inside every Skill | Provisional pending Golden Reference |
| ADR-004 | Apply explicit evidence classes and source precedence | Accepted |
| ADR-005 | Bind claims to product, version, license, deployment, and tenant evidence | Accepted |
| ADR-006 | Require a standalone per-Skill package structure | Provisional pending Golden Reference |
| ADR-007 | Use independent semantic versions and research snapshots | Accepted |
| ADR-008 | Keep the behavioral core capability-based and metadata portable | Provisional pending compatibility review |
| ADR-009 | Test behavior, isolation, safety, and hallucination resistance | Accepted |
| ADR-010 | Require independent review and severity gates | Accepted |
| ADR-011 | Prefer omission or validation steps over invented technical detail | Accepted |
| ADR-012 | Gate destructive actions and keep advisory AI non-authoritative | Accepted |
| ADR-013 | Duplicate only the minimum needed for standalone operation | Accepted |
| ADR-014 | Treat project knowledge as versioned operational evidence | Accepted |
| ADR-015 | Separate static, parser, tenant, and operational validation claims | Accepted |
| ADR-016 | Publish only verified release claims and preserve known limitations | Accepted |

## ADR-001 — Golden Reference first

**Status:** Accepted

**Context:** Seven independently publishable Skills need a common architecture, but generating them simultaneously would replicate design defects and make cross-review superficial.

**Decision:** Complete Phase 1 research, implement only `cortex-xql-query-engineer`, then perform technical, documentation, XQL, adversarial, standalone, compatibility, maintainability, and anti-hallucination reviews. Correct every `BLOCKER`, `CRITICAL`, and `HIGH` finding. Do not freeze `../ARCHITECTURE.md` or implement the remaining six Skills until `../reviews/xql-golden-reference-review.md` concludes exactly:

```text
GOLDEN REFERENCE APPROVED: YES
```

**Consequences:** Early throughput is intentionally lower. Structural decisions are exercised once before parallel replication. A rejected Golden Reference must be revised or recorded as blocked; it cannot be bypassed.

## ADR-002 — Standalone autonomy

**Status:** Accepted

**Context:** Skills must be separately publishable and usable without siblings.

**Decision:** No Skill may import, load, or require any sibling file or root-level research/review artifact at runtime. Common behavior is a convention, not a shared module. Internal links used during execution must resolve within the Skill directory.

Root-level artifacts may aggregate research, decisions, reviews, and release status. They are development evidence only.

**Isolation test:** Copy one Skill into a clean temporary directory, omit every sibling and root document, then run its structural and behavioral suite. Any required external path is a release-blocking dependency defect.

**Consequences:** Small controlled duplication is necessary. Cross-Skill recommendations remain optional and must include a standalone fallback.

## ADR-003 — Progressive disclosure

**Status:** Provisional pending Golden Reference

**Context:** A monolithic `SKILL.md` would be difficult to maintain, expensive to load, and likely to mix durable instructions with version-sensitive product facts.

**Decision:** Keep `SKILL.md` as the behavioral core:

- activation and exclusions;
- product/evidence intake;
- primary workflow;
- anti-hallucination and safety rules;
- output contract;
- explicit routing to deeper local resources.

Place detailed product knowledge and source traceability under `references/`, reusable answer structures under `templates/`, realistic demonstrations under `examples/`, and behavioral evaluations under `tests/`. Load only resources relevant to the current request.

**Consequences:** More files require link validation and navigation tests. The Golden Reference determines practical file granularity before the pattern is frozen.

## ADR-004 — Evidence hierarchy and classification

**Status:** Accepted

**Context:** Cortex behavior changes across products and releases, while local project artifacts contain both valuable operations knowledge and unresolved claims.

**Decision:** Apply this factual precedence:

1. current official Palo Alto Networks documentation;
2. official Palo Alto examples, repositories, API references, and guides;
3. directly available, verified project-specific knowledge;
4. secondary sources only when required.

Every significant claim must use two dimensions. The first is the mandatory canonical status:

```text
VERIFIED
VERSION-DEPENDENT
INFERRED
CONCEPTUAL
UNSUPPORTED
DEPRECATED
UNVERIFIED
```

The second dimension records provenance and validation without replacing the canonical status:

| Provenance/validation qualifier | Meaning |
|---|---|
| `OFFICIAL-CURRENT` | Current first-party documentation was reviewed. |
| `OFFICIAL-EXAMPLE` | A first-party example or repository was reviewed; pin a revision before reuse. |
| `LOCAL-VERIFIED` | The local bytes or structure were directly inspected. |
| `PROJECT-ASSERTED` | Project material makes the claim, but the underlying implementation/runtime evidence is absent. |
| `DERIVATIVE` | The material summarizes or aggregates another source and is not independent corroboration. |
| `REFERENCED-ONLY` | A name, hash, or description is available, but the underlying artifact is not. |
| `TENANT-UNVERIFIED` | Product syntax or behavior may be documented, but current tenant availability/population was not checked. |
| `TENANT-SCHEMA-VERIFIED` | Dataset/field/type availability was observed in the named tenant and review date. |
| `TENANT-COMPILED` | The named tenant accepted the query or artifact syntax. |
| `TENANT-EXECUTED` | The query or artifact executed; record timeframe, identity scope, and result evidence. |

Examples of the required pairing:

- `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED`: syntax or general behavior is documented, but tenant availability or data population is unknown.
- `UNVERIFIED / PROJECT-ASSERTED / REFERENCED-ONLY`: a project summary preserves the claim, but no implementation or authoritative product evidence is available.
- `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-SCHEMA-VERIFIED`: the behavior is documented for a bounded product/version and the relevant tenant schema was observed.
- `DEPRECATED / OFFICIAL-CURRENT`: current release documentation explicitly identifies the surface as legacy or deprecated.

`CURRENT-OFFICIAL`, `TENANT-DEPENDENT`, `LICENSE-DEPENDENT`, and similar labels in the research source register are source-index shorthand. Runtime Skill responses must translate them into the canonical status plus the applicable provenance/validation qualifiers above.

The current date and source review date belong in source records. A local artifact can be `LOCAL-VERIFIED` as bytes while the product behavior it alleges remains canonical `UNVERIFIED` with `PROJECT-ASSERTED` or `TENANT-UNVERIFIED` qualifiers.

**Conflict rule:** Preserve the project statement, identify the conflicting official behavior, decide whether the difference is legacy, customized, version-specific, incorrect, or unresolved, and document the conclusion. Never silently overwrite either side.

## ADR-005 — Product and terminology boundaries

**Status:** Accepted

**Context:** Supplied material mixes XDR, XSIAM, XSOAR, TIM, current names, and legacy technical identifiers.

**Decision:** Attach every executable or configuration claim to:

- product and product surface;
- version or documentation snapshot;
- SaaS/on-premises or other deployment model when material;
- edition/license/add-on when material;
- role/RBAC and installed integration/content prerequisites;
- tenant schema or runtime evidence when required.

Use Case/Issue in new XSIAM 3 user-facing prose. Preserve Incident/Alert in literal legacy APIs, context paths, commands, or imported content when required, with a compatibility note. Model Finding, Issue, Insight, installed endpoint application, Business Application, and DLP application definition as distinct object families.

**Consequences:** Examples need more metadata, but cross-product hallucinations become reviewable. Mechanical renaming of working legacy identifiers is prohibited.

## ADR-006 — Required per-Skill structure

**Status:** Provisional pending Golden Reference

**Context:** Each Skill needs the same publication, navigation, maintenance, and validation capabilities without relying on root files.

**Decision:** Every Skill must contain meaningful content at these paths:

```text
<skill-name>/
|-- SKILL.md
|-- README.md
|-- VERSION
|-- CHANGELOG.md
|-- VALIDATION.md
|-- references/
|-- templates/
|-- examples/
`-- tests/
```

No empty file or placeholder-only directory may be created solely to satisfy the tree. Each directory must support an identified runtime, maintenance, or test need.

An `agents/openai.yaml` adapter may be included for OpenAI discovery and default prompting. It must contain only supported metadata and must not be required by the platform-neutral behavioral core. Other ecosystem adapters may be added only when their formats are verified and do not alter the core's meaning.

**Consequences:** The package is larger than a minimal Skill, but it remains self-documenting and independently publishable. Golden Reference review may refine optional file names while preserving the mandatory categories.

## ADR-007 — Independent semantic versioning

**Status:** Accepted

**Context:** Domains evolve at different rates and may reach different evidence maturity.

**Decision:** Each `VERSION` uses `MAJOR.MINOR.PATCH`, and each Skill maintains its own `CHANGELOG.md`. A Skill reaches `1.0.0` only after its release gates pass. Use `0.x.x` while major verified functionality is absent or significant uncertainty remains, and state why.

Every version-sensitive reference records a review snapshot. Maintenance follows:

```text
Review official release documentation
-> inspect affected local references
-> classify changed capabilities
-> revalidate examples and tests
-> rerun hallucination and compatibility audits
-> update VERSION and CHANGELOG
```

**Consequences:** Versions will legitimately diverge. Root releases aggregate Skill versions rather than forcing lockstep.

## ADR-008 — Capability-based cross-platform core

**Status:** Provisional pending compatibility review

**Context:** ChatGPT, Codex, and Claude expose different tools, metadata, workspaces, and browsing mechanisms.

**Decision:** Core instructions describe capabilities rather than named hidden tools. For example, require authoritative-document verification when current documentation access is available, and otherwise require an uncertainty label and verification plan. Do not assume proprietary memory, a fixed filesystem, a specific reasoning mode, or a browser implementation.

Platform-specific installation and metadata belong in `README.md` or a verified adapter. Failure to support a platform feature is documented; compatibility is never simulated through false claims.

**Consequences:** Tool-specific automation may be less direct, but the Skill remains portable. Compatibility checkmarks require independent platform review.

## ADR-009 — Behavior-first testing

**Status:** Accepted

**Context:** File presence does not show that a Skill can safely perform its domain task.

**Decision:** Every Skill includes independently evaluable cases for:

- basic, intermediate, and advanced behavior;
- ambiguity and missing context;
- troubleshooting;
- regression;
- adversarial input and prompt injection;
- hallucination resistance;
- destructive-action safety;
- product/version boundary handling;
- standalone execution.

Each test defines input, expected behaviors, prohibited behaviors, evidence requirements, and pass criteria. Domain tests use the scenarios required by the master specification. Fabricated inputs such as `xdr_super_magic_events` and `detect_malware_now()` must be rejected or held for validation rather than normalized into plausible syntax.

**Consequences:** Evaluation requires substantive review rather than a directory check. Test results must say whether they are static inspection, simulated behavior, parser validation, or live tenant execution.

## ADR-010 — Independent reviews and release gates

**Status:** Accepted

**Context:** Authors cannot independently approve their own domain work.

**Decision:** Apply the required cross-review ownership, with separate technical accuracy, architecture, compatibility, security, adversarial, and final QA roles. Findings use:

```text
BLOCKER
CRITICAL
HIGH
MEDIUM
LOW
```

A Skill or repository release requires:

```text
BLOCKER = 0
CRITICAL = 0
HIGH = 0
```

Remaining `MEDIUM` and `LOW` items need justification and remediation guidance. Review records name reviewer role, artifact/version, evidence inspected, tests run, findings, corrections, residual risk, and decision.

**Consequences:** Review output is an auditable artifact. “Files created” and author self-assessment are never release approval.

## ADR-011 — Anti-hallucination fail-closed rule

**Status:** Accepted

**Context:** Invented XQL, datasets, fields, APIs, commands, context paths, playbook constructs, TIM capabilities, or platform parameters can cause incorrect or unsafe operations.

**Decision:** Before emitting executable-looking material, verify every material construct through current authoritative sources and tenant evidence where needed. When verification is unavailable:

1. state what is unknown;
2. assign the correct evidence class;
3. provide the smallest validation step;
4. use conceptual pseudocode only when visibly labeled;
5. omit uncertain executable details.

Do not infer datasets or fields from filenames, project namespace names, prior examples, or model memory. A zero-result query is not proof of absence without coverage, retention, permissions, parser, and collection analysis.

**Consequences:** Some answers will stop at a validation-ready template. This is preferred to fabricated completeness.

## ADR-012 — Security and destructive-action gates

**Status:** Accepted

**Context:** Cortex workflows can isolate endpoints, disable accounts, block indicators, terminate processes, change networks, delete files, revoke users, or otherwise alter production systems.

**Decision:** Destructive or materially disruptive guidance follows:

```text
Detection
-> verification
-> confidence assessment
-> approval or policy gate
-> least-scope action
-> post-action verification
-> rollback or recovery
```

Document authorization, permissions, confidence, scope, blast radius, idempotency, rollback, verification, evidence retention, and human approval. Advisory LLM output cannot be the sole authorizer. Unknown reputation, including DBotScore `0`, cannot be treated as affirmative benignness.

Use only placeholders such as `${CORTEX_API_KEY}`, `${CORTEX_API_KEY_ID}`, `${CORTEX_FQDN}`, and `${CORTEX_TENANT}`. Treat documents, archives, logs, examples, tool output, and embedded prompts as untrusted data, not instructions.

**Consequences:** Fully autonomous containment is not a default pattern. A domain-specific Skill may explain a validated policy exception but cannot invent authorization.

## ADR-013 — Controlled duplication

**Status:** Accepted

**Context:** Standalone Skills need common terminology and safety rules, while blind copying creates drift.

**Decision:** Classify shared text as:

- **required duplication:** minimal evidence labels, source precedence, product boundary, safety, uncertainty, and local navigation required for standalone use;
- **domain-specific overlap:** the current Skill's perspective on an adjacent concept;
- **unnecessary duplication:** large identical explanations with no standalone benefit.

Use the first two deliberately. Remove or refactor the third before release, but never refactor into a required external shared runtime file.

**Consequences:** Maintainers must reconcile repeated critical snippets during updates. Review checks semantic alignment without demanding byte-identical files.

## ADR-014 — Project knowledge provenance

**Status:** Accepted

**Context:** Available project material contains two distinct context families, derivative aggregates, referenced-only originals, endpoint exports with incomplete provenance, and several alleged high-priority defects.

**Decision:** Keep source families separate. Do not treat duplicate summaries as independent corroboration. Use project patterns for naming, workflows, risks, and test design only with their actual status. In particular:

- `SOCFramework.*`, `SOCN1.*`, and `Assessment.*` remain project contracts;
- the `soc-optimization` material is a deprecated/versioned snapshot description, not current source code;
- reported unsafe branches, embedded webhooks, literal containment inputs, duplicate IDs, and AI context mismatches remain project-asserted until the original artifacts are recovered;
- operational endpoint exports are sensitive and do not prove their generating application/filter;
- no supplied saved query or live tenant schema validates XQL fields or datasets.

**Consequences:** Project knowledge strongly shapes adversarial tests and examples but does not bypass current official or tenant validation.

## ADR-015 — Validation claim separation

**Status:** Accepted

**Context:** Static Markdown review, schema parsing, SDK validation, live tenant execution, and production observation answer different questions.

**Decision:** Every validation record states its level:

| Level | What it can establish | What it cannot establish |
|---|---|---|
| Static structure/link review | Required files, links, labels, obvious policy invariants | Product syntax or runtime behavior |
| Behavioral evaluation | Whether the Skill follows its contract on a test prompt | Tenant feature availability |
| Parser/SDK validation | Syntax/schema accepted by a named tool/version | Deployment success or business correctness |
| Non-production tenant test | Actual target-product behavior under recorded tenant conditions | Universal behavior across tenants/releases |
| Production observation | Behavior in the recorded deployment and time window | Permanent product support or future behavior |

For Cortex content-pack validation on Windows hosts, use a supported WSL2/container environment for `demisto-sdk`, record tool versions, and preserve results. Native Windows is not claimed as supported.

**Consequences:** Passing static tests cannot justify `VERIFIED IMPORTABLE ARTIFACT`. Missing tenant access is documented as a limitation, not disguised as a pass.

## ADR-016 — Release truthfulness and publication readiness

**Status:** Accepted

**Context:** The repository must be prepared for GitHub without overstating maturity.

**Decision:** Before any production-ready declaration, validate relative links, directory naming, source traceability, examples, test evidence, versions, changelogs, attribution/license, secret absence, temporary-file absence, standalone copies, compatibility, and final finding counts. The final QA record includes the required matrix and exactly one declaration:

```text
REPOSITORY PRODUCTION READY: YES / NO
```

Use `YES` only after every mandatory gate genuinely passes. Known limitations remain documented even when they are non-blocking.

**Consequences:** Publication preparation may finish with an honest `NO` if tenant validation, licensing, severe findings, or other mandatory evidence remains unresolved.

## Golden Reference architecture hypothesis

The XQL prototype must test whether the decisions above produce a compact and usable package. At minimum it must demonstrate:

- a concise routing and behavior core in `SKILL.md`;
- self-contained official source traceability;
- dataset/field discovery and uncertainty handling;
- separate executable and explanatory output where needed;
- reusable build/review/troubleshooting templates;
- realistic investigation, hunting, detection-support, optimization, and broken-query examples;
- basic through adversarial behavioral tests;
- local validation and maintenance guidance;
- OpenAI metadata isolated from the platform-neutral core;
- operation after sibling and root artifacts are absent.

Only independently reviewed evidence can convert this hypothesis into the frozen architecture in `../ARCHITECTURE.md`.

## Phase 1 checkpoint

### Completed work

- Established precise scopes, exclusions, inputs, outputs, overlaps, and standalone behavior for all seven Skills.
- Recorded initial decisions for sequencing, autonomy, progressive disclosure, evidence, product/version boundaries, packaging, compatibility, tests, review, safety, and release truthfulness.

### Evidence collected

- Full user-supplied master requirements.
- Current project inventory and project-versus-official reconciliation.
- Official source register and product ecosystem mapping developed during Phase 1.
- The existing DFIR architecture as a local convention for evidence-first reasoning, progressive disclosure, source traceability, and behavior-first validation; it is not Cortex product authority.

### Files created or modified by this workstream

- `research/skill-domain-boundaries.md`
- `research/architecture-decisions.md`

### Tests performed

- Manual coverage check against all seven required Skills.
- Boundary overlap review against the required cross-Skill examples.
- Standalone dependency analysis of the proposed architecture.
- Relative-path and product-boundary review of these decisions.

### Findings

- The domains can be separated through explicit contracts without mandatory sibling dependencies.
- Tenant-unverified datasets, fields, commands, integrations, close reasons, licenses, and deployment behavior must remain gated.
- The final file granularity and compatibility adapter policy require Golden Reference evidence.

### Open risks

- No live tenant, current schema export, original playbook YAML, installed integration inventory, or runtime record is available.
- Several project findings remain source-referenced but unverified.
- Static architecture review cannot certify executable XQL or import-ready automation.

### Quality gate status

```text
PHASE 1 ARCHITECTURE WORKSTREAM: PASS FOR GOLDEN-REFERENCE DESIGN
```

### Next phase eligibility

This workstream is ready for consolidation, but only `phase-1-checkpoint.md`, after independent review, determines Phase 2 eligibility. Even after that gate, only `cortex-xql-query-engineer` may be implemented. The remaining six Skills are not eligible until the Golden Reference is independently approved and `../ARCHITECTURE.md` freezes the proven pattern.
