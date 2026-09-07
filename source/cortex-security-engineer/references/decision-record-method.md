# Security Decision-Record Method

## Contents

- [Purpose](#purpose)
- [Record set](#record-set)
- [Requirement record](#requirement-record)
- [Threat and risk record](#threat-and-risk-record)
- [Telemetry record](#telemetry-record)
- [Control record](#control-record)
- [Validation record](#validation-record)
- [Operations record](#operations-record)
- [Decision record](#decision-record)
- [Quality checks](#quality-checks)

## Purpose

Use these records to make a cross-domain decision reviewable without pretending the implementation exists. Keep stable IDs so requirements, risks, evidence, controls, tests, owners, and decisions can be traced.

The record statuses below describe work state. They do not replace the canonical evidence classes in [evidence and product boundaries](evidence-and-product-boundaries.md).

## Record set

| Record | Prefix | Answers |
|---|---|---|
| Requirement | `REQ-` | What must be true, for whom, and under what constraints? |
| Threat/Risk | `RSK-` | What behavior or failure matters and why? |
| Telemetry | `TEL-` | What observable evidence is required and what limits it? |
| Control | `CTL-` | What prevention/detection/investigation/response capability addresses the risk? |
| Validation | `VAL-` | What test establishes each bounded property? |
| Operations | `OPS-` | Who owns health, exceptions, failure, tuning, recovery, and retirement? |
| Evidence | `EV-` | What authoritative observation supports a claim? |
| Decision | `DEC-` | Which option did the accountable owner choose, at which gate? |

Trace:

`REQ -> RSK -> TEL -> CTL -> VAL -> OPS -> DEC`

A control without a risk or requirement is unjustified. A test without an acceptance criterion is inconclusive. A decision without an owner and evidence ceiling is incomplete.

## Requirement record

Write testable requirements:

| Field | Guidance |
|---|---|
| ID | stable `REQ-###` |
| Actor/consumer | analyst, detection owner, incident commander, platform operator, auditor |
| SHALL/MUST | one observable outcome |
| Scope | product/release/surface/assets/identity/data/environment/time |
| Preconditions | entitlement, telemetry, permission, dependency |
| Success | measurable or reviewable condition |
| Unacceptable outcome | false block, missed class, data leakage, excessive delay, unowned failure |
| Priority | business/risk-owner input, not inferred from product |
| Evidence | current support and unknowns |
| Owner/approver | accountable roles |

Bad: “Improve Cortex detections.”

Better: “`REQ-004`: The control owner MUST receive an actionable signal for the defined credential-access behavior within the agreed operational window, with required entity context and a documented path for missing telemetry; the numeric window and volume target remain policy inputs.”

Do not invent thresholds, service levels, or severity.

## Threat and risk record

Record behavior and control failure rather than a product feature:

| Field | Guidance |
|---|---|
| ID | `RSK-###` |
| Protected asset/decision | what can be harmed |
| Actor and preconditions | plausible, not asserted attribution |
| Behavior/path | sequence, trust boundary, privilege and data flow |
| Existing controls | observed or unknown |
| Impact | operational, confidentiality, integrity, availability, regulatory |
| Likelihood assumptions | evidence and uncertainty |
| Benign alternatives | false-positive model |
| Evasion/coverage gaps | false-negative model |
| Abuse case | how the proposed control could be misused |
| Residual risk | risk after the proposed bounded control |
| Risk owner | accepts or rejects, not the assistant |

ATT&CK can organize behaviors. It does not prove the activity occurred, that a data source is present, or that a product control covers the technique.

## Telemetry record

Use one record per observable:

| Field | Guidance |
|---|---|
| ID | `TEL-###` |
| Observable | plain-language event/state |
| Product/source | exact product, collector/integration/agent/source family |
| Dataset/schema | exact observed value or `UNKNOWN` |
| Field semantics/type | exact observed value or `UNKNOWN` |
| Grain | one row/object per what |
| Time | source time, ingestion time, timezone, clock uncertainty |
| Coverage | population, platforms, assets, identities, blind spots |
| Quality | freshness, nulls, parsing/mapping, duplication, sampling |
| Retention | observed duration or `UNKNOWN` |
| Access | identity, RBAC/SBAC, dataset/object scope |
| Privacy | minimization, redaction, storage/export constraints |
| Evidence | class/qualifiers, date, tenant record |
| Failure signal | how loss/degradation becomes visible |

Feature entitlement is not telemetry evidence. A single sample is not population coverage.

## Control record

| Field | Guidance |
|---|---|
| ID/type | `CTL-###`; prevent/detect/investigate/enrich/respond/recover |
| Intent | requirement/risk addressed |
| Trigger/input | semantic contract, not assumed syntax |
| Logic | conceptual or specialist artifact reference |
| Output | signal/case/context/action and grain |
| Target surface | exact product/release/editor/runtime |
| Dependencies | `TEL`, XQL, detection, TIM, playbook, platform packages |
| Failure modes | silence, noise, duplicates, lag, denied permission, partial action |
| FP/FN | scenarios and measurement |
| Safety | scope, human gate, blast radius, idempotency, data handling |
| Recovery | stop/revert/restore/manual path |
| Owner | build, operate, approve, recover |
| Evidence ceiling | current class/qualifiers |

Keep controls distinct:

- a hunt finds evidence and generates hypotheses;
- an interactive query returns scoped records;
- a detection generates a governed signal;
- TIM manages intelligence and indicators;
- a playbook coordinates tasks;
- a response action changes endpoint, cloud, network, identity, case, or external state;
- a platform control provides entitlement, access, data, integration, or runtime foundations.

## Validation record

Each `VAL` names one property:

| Field | Guidance |
|---|---|
| Property | syntax, schema, logic, signal quality, permission, failure handling, recovery, operations |
| Level | `S`, `D`, `C`, or `E` |
| Environment | isolated static, official docs, named non-production context |
| Fixture | known-positive, known-benign, negative, null, boundary, denied, failure, rollback |
| Expected | objective pass/fail observation |
| Prohibited | false claims or unsafe effects |
| Evidence capture | artifact, hash, identity, time, sanitized output |
| Result | `PASS`, `FAIL`, `NOT RUN`, or `N/A`, with a rationale; `N/A` only when the level does not apply |
| Owner/reviewer | independent where required |

Do not merge component and end-to-end results.

## Operations record

Define before promotion:

- control owner, on-call/escalation owner, data/platform owner, approver, recovery owner;
- health inputs: ingestion, freshness, parser/mapping, permission, job/rule/playbook state;
- outcome inputs: volume, triage disposition, false-positive causes, known misses, response completion/failure;
- capacity and cost indicators appropriate to the product;
- exception/allowlist/suppression owner, rationale, scope, evidence, expiry, review;
- release/change process and rollback trigger;
- manual fallback and degraded mode;
- documentation/runbook and evidence retention;
- review cadence and material-change triggers;
- retirement criteria, archive, cleanup, and dependent-control check.

Do not manufacture numeric thresholds; identify them as policy inputs and name the owner.

## Decision record

Use:

| Field | Content |
|---|---|
| ID/date/status | `DEC-###`; `PROPOSED`, `APPROVED`, `REJECTED`, `SUPERSEDED` |
| Decision owner | accountable human/board/team |
| Question | one choice |
| Options | include do-nothing/defer when relevant |
| Criteria | risk, coverage, safety, operations, cost, reversibility, evidence |
| Evidence | linked `EV/VAL` and evidence ceiling |
| Tradeoffs | benefits, drawbacks, residual risk |
| Choice/rationale | owner decision, not assistant authorization |
| Conditions | gates before implementation/promotion |
| Expiry/revisit | date or material-change trigger |
| Non-claims | tenant/deployment/efficacy limits |

When the owner has not approved, use “recommended option” and leave status `PROPOSED`.

## Quality checks

- Every material statement has a source or an explicit evidence class.
- Every requirement has success and unacceptable outcomes.
- Every risk links to a requirement and owner.
- Every telemetry dependency has coverage/access/failure paths.
- Every control has FP, FN, abuse, failure, and recovery analysis.
- Every consequential action has policy and human authorization.
- Every test names a level, fixture, expected observation, and retained evidence.
- Every work package has one accountable owner and objective acceptance.
- Every decision states alternatives, residual risk, and non-claims.
- No status, link, or prose upgrades `S/D` into `C/E`.
