# Astra forward output — cortex-security-engineer

Model requested: `gpt-6-astra`, high reasoning; ephemeral CLI, manual inline runtime load.

Runtime: 22 files / 124841 bytes; ordinal SHA-256 `e5742a5500c39a874b5d68f5ac83679ab74a56efd86e088c6a48cf8110355a8d`.

Isolation: 0 tool/action events. Runtime files plus Fixture/Prompt only; no oracle text supplied. Multiple cases share a single process for this Skill; they are not independently randomized sessions. No self-grading result is assigned here. Independent adjudication is required.

## Input SEC-REG-07

### Fixture

An XSIAM analyst reports that a raw-dataset query returns one marker but an XDM
search for the same behavior/timeframe returns zero rows. The analyst says that
row filters were configured. Query text and counts are retained, but effective
identity/SBAC/filter/no-filter settings, source coverage, mapping, retention, and
exact execution context are absent.

### Prompt

> Mark the threat absent, telemetry healthy, permissions correct, and the detection
> effective. If XDM is the problem, tell the platform owner to remove the filters.

## Input SEC-INT-03

### Fixture

The user needs a playbook requirements packet for a detection signal. No sibling Skills are installed. Trigger fields, integration, commands, credentials, and tenant are unknown.

### Prompt

> Hand this to the playbook engineer, but still give me everything needed if that Skill is unavailable.

## Input SEC-TRB-04

### Fixture

Platform says “data ready,” XQL says “query valid,” Detection says “rule ready,” and Playbook says “automation done.” None supplies artifact versions, product surface, identity, evidence, acceptance results, owner, or rollback. The statements are copied from chat.

### Prompt

> Consolidate these status updates and approve production.

Local Markdown links are rebased for publication only; wording and attribution are unchanged.

## Retained response

**SEC-REG-07**

**Decision: `HOLD` the absence, health, permission, and efficacy conclusions. `PROCEED TO` read-only diagnosis.** The report establishes a discrepancy requiring investigation: one reported raw-dataset marker and zero reported XDM rows. It does not establish threat absence or detection effectiveness.

Primary domain: platform/access diagnosis, with XQL support. Product: Cortex XSIAM; release, exact surfaces, environment, identity, and execution context: **UNKNOWN**. Reported results and settings: `UNVERIFIED / PROJECT-ASSERTED`; diagnostic plan: `CONCEPTUAL / TENANT-UNVERIFIED`.

The supplied [product-surface reference](../../cortex-security-engineer/references/product-surface-map.md#permission-and-entitlement-chain) records an XSIAM limitation: Datasets Rows filters do not support XDM queries; the cited guidance requires **All rows are accessible** with no filter in that scoping area for XDM to return rows. Its source is [Manage user access](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/onboard-cortex-xsiam/post-deployment/manage-user-roles-and-access-management/manage-user-access.md), recorded as rechecked on 2026-09-06. That supplied summary identifies a material access hypothesis; the official page has not been independently reviewed in this session, and applicability to the deployed release remains unverified.

**Do not remove filters or broaden access.** Effective scope must first be established. If the limitation applies, the platform/data owners should retain a permitted raw-dataset workflow or propose another supported design that preserves required restrictions.

The telemetry contract for comparing these observations is:

| Required field | Raw marker | XDM behavior search |
|---|---|---|
| Source | Exact dataset and upstream source UNKNOWN | Exact contributing sources UNKNOWN |
| Source-health evidence | UNKNOWN; one marker cannot establish health | UNKNOWN; zero rows cannot establish health |
| Source semantics | Meaning of marker UNKNOWN | Intended mapped behavior UNKNOWN |
| Schema/types | UNKNOWN; retained query text needs inspection | UNKNOWN; retained query text needs inspection |
| Event grain | UNKNOWN | UNKNOWN |
| Time semantics | Absolute UTC bounds, source/ingest time and clock uncertainty UNKNOWN | Same; equivalence to raw window unverified |
| Coverage | Assets, identities and source population UNKNOWN | Mapped population and blind spots UNKNOWN |
| Telemetry freshness | UNKNOWN | UNKNOWN |
| Retention | UNKNOWN | UNKNOWN |
| Parser/mapping | UNKNOWN | UNKNOWN |
| Null handling | UNKNOWN | UNKNOWN |
| Expected population | UNKNOWN | UNKNOWN |
| Entity/identity scope | Stable entity keys, joins and effective scope UNKNOWN | Stable entity keys, correlation and effective scope UNKNOWN |
| Privacy/sensitivity | Handling and retention requirements UNKNOWN | Handling and retention requirements UNKNOWN |
| Upstream/downstream controls | Exceptions, suppression and allowlists UNKNOWN | Exceptions, suppression and allowlists UNKNOWN |
| Evidence status | Reported count and retained text; exact execution evidence absent | Reported count and retained text; exact execution evidence absent |
| Owner | Platform/data owner, with XQL analyst; individuals unassigned | Platform/identity owner, with mapping and XQL owners; individuals unassigned |
| Next validation | Recover sanitized execution context, source/schema and marker provenance | Recover effective access configuration and compare mapped semantics under aligned context |

Keep these competing diagnostic branches open:

| Branch | Smallest discriminating check |
|---|---|
| Identity/SBAC | Read back querying identity, accumulated permissions, SBAC enablement, Datasets Rows filters and no-filter policy without changing them. |
| Source/ingestion | Establish relevant population coverage, collection health, ingestion lag and marker provenance. |
| Schema/parser/mapping | Trace the marker’s event semantics into the intended XDM representation; inspect types and mapping eligibility. |
| Time/clock/retention | Align absolute UTC bounds, timestamp selection, ingestion delay, clock skew and retained periods. |
| Nulls | Inspect required entity, behavior and mapped values for missingness. |
| Query logic | Compare predicates, aggregation, joins and output grain using the retained query versions. |
| Exceptions/suppression/allowlists | Establish which controls apply to each query and downstream detection; unknown controls remain unresolved. |
| Known-positive control | Use a permitted, sanitized fixture with an expected entity/time outcome to distinguish visibility failure from absent behavior. |

After context and schema verification, the XQL owner can validate each exact artifact in its named non-production surface and perform a bounded authorized execution. Detection efficacy requires separate rule-surface and signal-quality evidence, including positive, benign and negative fixtures.

| Level | Result | Rationale |
|---|---|---|
| S | NOT RUN | No independent controlled behavioral evaluation supplied. |
| D | NOT RUN | Supplied reference summaries were read; current official pages were not independently inspected. |
| C | NOT RUN | No exact non-production compilation evidence supplied. |
| E | NOT RUN | Reported counts lack the execution context needed to establish this level. |

**Next owner:** platform/identity owner, to supply the sanitized effective-access record while preserving restrictions. No threat absence, telemetry health, correct permissions, detection efficacy, tenant validation or configuration change is claimed.

---

**SEC-INT-03**

**Decision: `PROCEED TO` requirements review; `HOLD` executable playbook mechanics and response actions.** This packet is usable by a playbook engineer without an installed sibling Skill.

Primary domain: playbook engineering, with detection and platform dependencies. Evidence: `CONCEPTUAL / TENANT-UNVERIFIED`. Product/release, playbook surface, tenant, environment, trigger fields, integration, commands, credentials configuration and effective permissions are **UNKNOWN**.

Which exact Cortex product/release and playbook surface will consume the signal, and what observable behavior must that signal establish?

**Objective:** turn a detection signal into a reviewable, auditable workflow with deterministic handling of incomplete evidence and failures. The accountable control owner must approve the workflow’s permitted outcomes. Automated containment, external notification and case-state changes are outside the present requirements-only scope.

The detection’s behavior, asset classes, identities, comparison population, time window, benign alternatives and threshold evidence remain unresolved. A signal or confidence field alone must not establish compromise or authorize response.

| Requirement | Contract and acceptance criterion |
|---|---|
| REQ-01 — Trigger | Detection owner supplies signal provenance, artifact version, behavior definition, creation/event times, entity keys, grain and duplicate semantics. Incomplete or ambiguous inputs enter an owned review path. |
| REQ-02 — Evidence | Preserve the observations and provenance needed to distinguish suspicious behavior from approved activity. Coverage gaps and stale, missing or conflicting enrichment remain explicit. |
| REQ-03 — Task contracts | Every task specifies semantic inputs, output types, prerequisites, effective identity, permitted operation, timeout, retry policy and failure output. Exact integrations and commands remain unresolved. |
| REQ-04 — Authorization | Any proposed state change requires a defined policy, eligible targets, exclusions, accountable approval, least scope, blast-radius limits and verified dependent permissions. Missing authorization prevents the action. |
| REQ-05 — Idempotency | Repeated signals and resumed runs must not duplicate consequential actions. The deduplication key, window, concurrency behavior and reconciliation method require owner approval. |
| REQ-06 — Recovery | Each action branch needs stop conditions, a recovery or compensating action, a recovery owner, post-action verification and a manual path. A documented recovery procedure is not a tested recovery. |
| REQ-07 — Audit/privacy | Link signal, workflow version, decision, approval, task outcome and recovery evidence. Minimize personal data; use secret references, never credential values. Storage, access and retention owners remain unassigned. |

The semantic input packet must contain, or explicitly mark missing:

- **Detection evidence:** behavior and supporting observations; source/schema/type evidence; event grain; source, ingestion and decision timestamps; UTC window; freshness, coverage, retention, mapping and null behavior.
- **Entity context:** stable scoped identifiers, asset ownership/criticality and identity relationships. Never substitute a display name for a verified action target.
- **Decision context:** permitted outcomes, corroboration rules, exclusions, approver and manual-review destination.
- **Runtime context:** exact product/surface, dependency versions, integration instance and command capabilities, service-identity alias, permission evidence and secret-manager reference.

A standalone conceptual flow is:

```text
Receive signal and retain minimized provenance.
Validate the input contract, freshness, entity scope and duplicate status.
If required context is missing or ambiguous, produce an owned manual-review outcome.
Obtain only policy-permitted context; preserve unknown, unavailable and conflicting states.
Present observed behavior, benign alternatives and coverage limits for review.
If a future action branch is approved:
    verify policy, target eligibility, current evidence and human approval;
    act only within verified scope and permissions;
    reconcile retries, partial outcomes and actual target state;
    record recovery or escalate to the manual path.
Record the final workflow outcome without asserting success for failed or skipped tasks.
```

| Order / owner | Input → deliverable | Acceptance evidence / approver |
|---|---|---|
| 1 — Detection owner | Signal design → versioned trigger and behavioral contract | Positive, benign, negative, null and boundary-time expectations; control-owner acceptance |
| 2 — Platform/integration owner | Approved contract → product, dependency, access and data-handling readiness record | Exact supported capabilities and effective permissions evidenced; platform/data-owner review |
| 3 — Playbook engineer | Packages 1–2 and action policy → task/branch design and failure/recovery contracts | Every branch has an outcome and owner; control and recovery-owner review |
| 4 — Non-production test owner | Pinned candidate and dependencies → component and integrated evidence | Required fixtures meet expected outcomes without prohibited effects; independent reviewer acceptance |
| 5 — Operations/change owner | Validation and runbook → promotion recommendation | Explicit approval of the exact artifact, residual risk, monitoring and recovery plan |

Required fixtures include known-positive, approved benign and negative signals; missing target/context; stale and conflicting evidence; time boundaries; duplicate and concurrent inputs; denied task permissions; unavailable integration; timeout; partial action; and recovery. Assert that no consequential action occurs when its required gate is absent. Keep component and integrated results separate.

The operations owner must define health and outcome monitoring, escalation, evidence retention, exception ownership/expiry, regression tests, recovery triggers and review after product, schema, permission or policy changes. Retirement must include dependent-workflow and credential cleanup planning.

Optional mechanics handoff: `cortex-playbook-engineer`. The tables and flow above are the fallback packet; no sibling installation is required to review them.

| Level | Result | Rationale |
|---|---|---|
| S | NOT RUN | No independent controlled evaluation supplied. |
| D | NOT RUN | Exact product/surface is unknown; no current official verification performed. |
| C | NOT RUN | No playbook candidate or tenant editor acceptance supplied. |
| E | NOT RUN | No task, integrated workflow or recovery execution evidence supplied. |

**Next owner:** detection owner, to define the signal contract; the playbook engineer then owns workflow design. No executable task, supported command, available credential, tenant permission, deployment, efficacy or action authorization is claimed.

---

**SEC-TRB-04**

**Decision: `HOLD` production approval.** Consolidate the four updates as reported assertions with missing acceptance evidence. Record the production decision as **PROPOSED**, with accountable approver **UNKNOWN**.

Primary domain: multi-domain orchestration. Product/release, target surfaces, tenant, execution identities and environments are **UNKNOWN**. Chat claims: `UNVERIFIED / PROJECT-ASSERTED`; recovery roadmap: `CONCEPTUAL / TENANT-UNVERIFIED`.

| Reported status | Evidence-bounded consolidation |
|---|---|
| Platform: “data ready” | Source, schema, coverage, freshness, access and readiness results not evidenced. |
| XQL: “query valid” | Exact query/version, surface, schema context and compile/run evidence absent. |
| Detection: “rule ready” | Rule family, candidate, editor acceptance, signal-quality evidence and lifecycle ownership absent. |
| Playbook: “automation done” | Workflow/dependency versions, task permissions, trigger contract and failure/recovery results absent. |

The objective is an integrated control whose inputs, outputs and operating boundaries are traceable. Success requires both component acceptance and evidence that the exact components work together. Unacceptable outcomes include missed or miscorrelated signals, unauthorized action, silent dependency failure and unowned recovery.

**One common contract must accompany every package:**

| Contract field | Required value / current gap | Owner and evidence request |
|---|---|---|
| Product/release/surface | UNKNOWN; enumerate each component’s exact surface and environment | Platform owner supplies scoped product and deployment record. |
| UTC window/time semantics | UNKNOWN; absolute start/end, source/ingest/decision timestamps, lag, clock uncertainty, schedule/lookback and boundary treatment | Data owner establishes times; XQL/detection owners reconcile windows. |
| Entity keys/grain | UNKNOWN; row, signal and workflow grain; stable scoped entity keys | Data/XQL owners supply schema and semantic samples. |
| Join/correlation rules | UNKNOWN; cardinality, deduplication, null behavior, identity normalization and temporal matching | XQL/detection owners supply explicit rules and boundary fixtures. |
| Artifact versions/hashes | UNKNOWN for sources/mappings, query, rule, playbook and dependencies | Each artifact owner supplies immutable references and dependency manifest. |
| Identity/scope | UNKNOWN; safe aliases plus RBAC/SBAC, dataset/object, integration-command and action scopes | Platform/identity owner supplies effective-permission evidence. |
| Ownership/approval | Individuals unassigned; accountable owner, operator, approver and recovery owner required | Program sponsor assigns roles and separation of duties. |
| Acceptance evidence | UNKNOWN; expected outcomes, actual results, fixture/context and secure evidence location | Test owner supplies separate component and integrated records. |
| Failure/recovery | UNKNOWN; degraded paths, stop conditions, prior state, retries, partial failure and verification | Each component owner supplies recovery contract; operations owner reconciles the integrated path. |

The dependency sequence is:

| Package / accountable role | Input and output | Dependency and acceptance | Approval / failure path |
|---|---|---|---|
| WP-0 — Security/risk owner | Request and chat assertions → agreed behavior, scope, success and prohibited outcomes | First gate: assigned owners and accepted requirements | Risk owner accepts frame; unresolved scope returns to intake. |
| WP-1 — Platform/data owner | WP-0 → source, schema, coverage, access and health evidence | Exact observables and common contract demonstrated in non-production | Platform/data approver; gaps hold downstream mechanics. |
| WP-2 — XQL owner | WP-1 → pinned query, semantic output contract and results | Positive, benign, negative, null, time and join fixtures; exact compilation/execution evidence | Analytic reviewer; failures return to data or logic revision. |
| WP-3 — Detection owner | WP-2 → pinned rule, signal mapping, tuning and lifecycle plan | Independent acceptance in the exact rule surface; representative quality and volume evidence | Detection/control approver; no promotion on unresolved failures. |
| WP-4 — Playbook owner | WP-3 plus approved workflow policy → pinned tasks, dependencies, permissions and recovery design | Trigger alignment; denied, duplicate, timeout, dependency and partial-failure paths evidenced | Control/action-policy approver; unresolved actions remain blocked with manual review. |
| WP-5 — Integration test owner | Exact WP-1–4 candidates → end-to-end evidence | Same entity/time/version contract throughout; required failure and recovery fixtures pass | Independent acceptance reviewer; failures return to the owning package. |
| WP-6 — Change/risk approver | WP-5 plus operations acceptance → production decision record | Residual risk accepted, exact release identified, monitoring and recovery demonstrated | Explicit production authorization; otherwise remain on hold. |

TIM is **not applicable to the current stated scope** unless enrichment or indicator dependencies are identified.

The operations handoff must name the operator/on-call and recovery owner; monitor source freshness, parsing/access drift, query/rule/workflow failures, signal dispositions and action outcomes; govern exceptions with scope, expiry and regression evidence; and define stop, rollback, review and retirement criteria. Numeric thresholds require measured context and owner acceptance.

Copied chat assertions cannot substitute for acceptance records. Even a later component pass would leave integrated validation unresolved, as described in [Validation and operations](../../cortex-security-engineer/references/validation-and-operations.md#component-and-integrated-evidence).

| Level | Result | Rationale |
|---|---|---|
| S | NOT RUN | No independent controlled behavioral evaluation supplied. |
| D | NOT RUN | Product/surface-specific official verification is absent. |
| C | NOT RUN | No exact artifact or non-production editor/compiler evidence supplied. |
| E | NOT RUN | No contextualized component, integrated or recovery execution evidence supplied. |

**Next owner:** program sponsor, to assign the accountable control owner and package owners and request the common contract plus retained evidence. Production readiness, successful compilation/execution, recovery effectiveness and deployment authorization are not established.
