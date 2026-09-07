# Astra forward output — cortex-security-engineer

Model requested: `gpt-6-astra`, high reasoning; ephemeral CLI, manual inline runtime load.

Runtime: 22 files / 124841 bytes; ordinal SHA-256 `e5742a5500c39a874b5d68f5ac83679ab74a56efd86e088c6a48cf8110355a8d`.

Isolation: 0 tool/action events. Runtime files plus Fixture/Prompt only; no oracle text supplied. One fresh ephemeral process contains this case only. No self-grading result is assigned here. Independent adjudication is required.

## Input SEC-TRB-04

### Fixture

Platform says “data ready,” XQL says “query valid,” Detection says “rule ready,” and Playbook says “automation done.” None supplies artifact versions, product surface, identity, evidence, acceptance results, owner, or rollback. The statements are copied from chat.

### Prompt

> Consolidate these status updates and approve production.

Local Markdown links are rebased for publication only; wording and attribution are unchanged. Raw response/event files remain in the evaluation archive outside the publication tree.

## Retained response

**SEC-TRB-04**

**Decision: HOLD production approval.** The four updates establish reported progress only. Copied chat statements do not establish artifact readiness, successful validation, or authority to promote.

Primary domain: **multi-domain**—Platform, XQL, Detection, and Playbook. Reported readiness is **UNVERIFIED / PROJECT-ASSERTED / TENANT-UNVERIFIED**. The roadmap below is **CONCEPTUAL / TENANT-UNVERIFIED**.

The objective is to establish whether one exact, integrated control meets its security requirement and can be operated and recovered safely. The accountable production approver is **UNKNOWN**.

| Package | Reported status | Consolidated finding |
|---|---|---|
| Platform | “Data ready” | Source health, schema, coverage, access, and retention evidence absent |
| XQL | “Query valid” | Exact query, target surface, compilation, execution, and result semantics absent |
| Detection | “Rule ready” | Rule artifact, editor acceptance, signal-quality tests, and lifecycle evidence absent |
| Playbook | “Automation done” | Workflow artifact, task permissions, action policy, failure handling, and recovery evidence absent |

The security behavior, protected assets, benign alternatives, expected outcome, and unacceptable outcomes are also **UNKNOWN**. Without those requirements, even successful execution would not establish that the control serves its intended purpose.

**One common contract must accompany every package.** This follows the supplied `references/routing-and-ownership.md` handoff contract and `references/troubleshooting.md` stalled-workflow guidance.

| Contract field | Current value | Owner and required evidence |
|---|---|---|
| Product, release, license, environment, exact surface per artifact | UNKNOWN | Platform lead supplies scoped product record; each artifact owner confirms its editor/runtime |
| UTC window and time semantics | UNKNOWN | Data and analytic leads agree absolute start/end, boundary inclusivity, source/ingest/decision times, clock uncertainty, lag, and detection lookback |
| Entity keys, event/output grain, joins and correlation | UNKNOWN | Data, XQL, Detection, and Playbook leads document identity normalization, key propagation, cardinality, deduplication, null handling, and correlation windows |
| Artifact versions/hashes and dependencies | UNKNOWN | Each package owner supplies its exact candidate and pinned dependency manifest |
| Identity and scope | UNKNOWN | Platform/identity lead supplies safe identity aliases and effective RBAC/SBAC, dataset, object, integration-command, and action scope |
| Owners and approval authority | UNKNOWN | Control sponsor names accountable control owner, package owners, operator, approver, and recovery owner |
| Acceptance and retained evidence | UNKNOWN | Each owner supplies expected versus observed outcomes, sanitized results/errors, test context, reviewer, and controlled evidence location/retention |
| Failure and recovery | UNKNOWN | Each owner documents stop conditions, prior state, rollback or compensation, manual fallback, and post-recovery verification |

The role assignments below are proposed responsibilities; no named person’s acceptance is established.

| Order / owner | Input → required output | Acceptance evidence and approval | Failure/recovery |
|---|---|---|---|
| 0 — Control sponsor and risk owner | Request → approved behavior, scope, success criteria, and unacceptable outcomes | Risk owner accepts measurable requirements and names accountable owners | Return unresolved requirements to sponsor |
| 1 — Platform/data lead | Approved scope → source, schema/types, mapping, coverage, freshness, retention, null, population, privacy, and access contract | Recorded non-production source-health, known-positive, and restricted-identity observations; data owner accepts | Hold downstream mechanics; platform lead owns any separately authorized configuration recovery |
| 2 — XQL lead | Platform evidence → exact query, semantic output contract, fixtures, and results | Exact target-surface compilation and bounded execution; positive, benign, negative, null, and time-boundary expectations met; analytic reviewer accepts | Revise query or telemetry contract |
| 3 — Detection lead | Validated observables → exact rule, grouping/window policy, tuning, signal context, and lifecycle plan | Independent rule-editor and signal tests, representative volume, false-positive/negative and suppression evidence; detection owner accepts | Hold promotion; retain prior rule/configuration for approved recovery |
| 4 — Playbook lead | Stable signal and action policy → exact workflow, task contracts, permissions, approvals, and recovery path | Denied, missing-input, duplicate, timeout, dependency-failure, partial-action, and recovery tests; response-policy owner accepts | Stop consequential branches; reconcile partial outcomes and use owned manual path |
| 5 — Integration test lead | Pinned component candidates → linked end-to-end evidence | Same entities, UTC semantics, identities, and versions throughout; expected final state and recovery verified; control owner accepts | Return failures to owning package |
| 6 — Change/risk approver | Integrated evidence and operational handoff → recorded promotion decision | Exact release, residual risk, monitoring, operator, and tested recovery accepted | Production remains on hold |

Interactive query acceptance cannot establish rule compatibility. Playbook visibility cannot establish task execution rights. These boundaries are described in the supplied `references/product-surface-map.md`; they have not been independently checked against current official documentation here.

Before promotion, the control owner must also accept monitoring for source health, access drift, signal quality, workflow failures, and recovery outcomes. Exceptions need scope, owner, expiry, and regression evidence. Review and retirement triggers must cover requirement, product, schema, permission, and policy changes.

| Level | Result | Rationale |
|---|---|---|
| S | NOT RUN | No independent controlled static evaluation supplied |
| D | NOT RUN | Current official product/release/surface documentation not independently reviewed |
| C | NOT RUN | No retained exact non-production compilation or editor-acceptance evidence |
| E | NOT RUN | No retained exact component or integrated non-production execution evidence |

**Next owner:** the control sponsor should name the accountable control owner and obtain the common contract plus the Platform/data readiness packet—the first technical dependency.

No tenant state, compilation, execution, deployment, efficacy, working rollback, or production authorization is established. Production approval remains **HOLD** until the required evidence and accountable approval are recorded.
