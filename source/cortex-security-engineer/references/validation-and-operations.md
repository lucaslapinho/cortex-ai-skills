# Validation and Operations

## Contents

- [Validation levels](#validation-levels)
- [Test dimensions](#test-dimensions)
- [Component and integrated evidence](#component-and-integrated-evidence)
- [Promotion gates](#promotion-gates)
- [Operational model](#operational-model)
- [Exceptions and tuning](#exceptions-and-tuning)
- [Change, recovery, and retirement](#change-recovery-and-retirement)
- [Evidence record](#evidence-record)

## Validation levels

Record each independently:

| Code | Level | May establish | Cannot establish |
|---|---|---|---|
| `S` | isolated static behavioral evaluation | adherence to the Skill contract on hidden fixtures | current docs, tenant state, syntax, execution, efficacy |
| `D` | official-document verification | current named product/release/surface behavior on review date | entitlement, tenant configuration, compile/run |
| `C` | non-production compile/editor acceptance | exact artifact accepted in exact context | correct results, coverage, performance, production safety |
| `E` | non-production execution | exact artifact completed under recorded context | universal behavior, production readiness, ongoing efficacy |

Use exactly `PASS`, `FAIL`, `NOT RUN`, or `N/A`, with a rationale. Use `N/A` only when the level is genuinely inapplicable; use `NOT RUN` when it was applicable but unperformed or blocked. Workflow words and evidence statuses must not replace the validation result.

## Test dimensions

Every control needs tests proportionate to risk:

| Dimension | Representative fixture | Why |
|---|---|---|
| known positive | controlled behavior expected to match/advance | sensitivity and context |
| known benign | approved admin/tool/business workflow | false-positive handling |
| negative | similar behavior that must not match/act | specificity |
| null/missing | absent field, entity, enrichment, or input | deterministic fail behavior |
| boundary time | start/end, lag, clock skew, retention edge | window semantics |
| duplicate/retry | repeated event, pagination, resumed job | idempotency |
| denied permission | restricted role/object/data/command | fail closed and useful errors |
| dependency unavailable | ingestion/integration/enrichment/action down | timeout, fallback, escalation |
| partial action | some targets succeed and some fail | reconciliation and recovery |
| rollback/recovery | controlled reversal or compensating action | recoverability |
| volume/capacity | representative peak/cardinality | safety and operations |
| privacy/export | sensitive fields and destination restrictions | minimization and governance |

Never create live malicious activity or destructive fixtures without a separately approved test plan.

## Component and integrated evidence

Maintain separate records for:

- source/collector health and schema;
- query or hunt observable logic;
- detection editor and signal behavior;
- case/issue mapping;
- TIM enrichment/indicator lifecycle;
- playbook branch/task/integration behavior;
- response authorization/action/recovery;
- monitoring and audit evidence.

Then test the integrated path with the exact versions and identities. A pass at one node does not fill the other rows.

Model negative space:

- signal absent because behavior absent;
- signal absent because collection, parsing, retention, clock, permission, or logic failed;
- signal present but benign;
- signal present but case mapping/enrichment failed;
- action requested but policy denied;
- action accepted but partially failed;
- control healthy but operator did not receive or act on output.

## Promotion gates

| Gate | Required evidence |
|---|---|
| Design | approved requirement/threat/risk/telemetry/control records |
| Documentation | current exact product/release/surface sources |
| Non-production | exact schema/editor/execution fixtures and denied/failure/recovery paths |
| Signal quality | representative volume, FP causes, known FN paths, useful context |
| Safety | authorization, least scope, blast radius, idempotency, rollback/recovery |
| Operations | owner, health/outcome measures, alerts/escalation, evidence retention, runbook |
| Approval | change/risk owner accepts residual risk and exact release artifact |

“Production ready” is not supportable while a required gate is `NOT RUN`.

## Operational model

Define two families of measures.

### Health measures

- entitlement and feature availability;
- data-source/collector/integration state;
- freshness, lag, parsing/mapping errors, null/volume drift;
- identity, role, SBAC, object, dataset, and command access;
- rule/job/playbook/feed/action state and error rate;
- capacity, backlog, timeout, retry, or quota behavior;
- owner and evidence pipeline availability.

### Outcome measures

- signals/cases by entity and time;
- triage disposition and time;
- confirmed benign causes and suppression/exception impact;
- controlled positive and negative fixture performance;
- missed detections found through hunts/incidents;
- enrichment/action completion, partial failure, and recovery;
- analyst context quality and manual effort;
- residual risk and policy exceptions.

Do not invent acceptable numbers. Capture baseline evidence, propose candidate objectives, and have the accountable owner approve them.

## Exceptions and tuning

Every allowlist, exception, suppression, reputation override, or threshold change records:

- owner and approver;
- specific scope and rationale;
- evidence and linked false-positive case;
- creation and expiry/review date;
- expected coverage loss;
- before/after representative test;
- known false-negative regression fixture;
- rollback/removal;
- dependent controls and communications.

“Rule not disabled” does not prove coverage unchanged. Automatic product behavior or generated exceptions also require inspection and regression evidence.

## Change, recovery, and retirement

For each release:

1. pin the artifact/version/hash and dependency versions;
2. record prior state and configuration/export needed for recovery;
3. define a bounded non-production and canary path where supported;
4. define objective stop/rollback triggers;
5. require explicit promotion approval;
6. verify intended state and observe health/outcomes;
7. reconcile partial failures;
8. schedule review after product, schema, license, role, source, threat, or policy change.

Retire when the requirement ends, telemetry/control is superseded, cost/risk exceeds benefit, or evidence cannot be maintained. Archive rationale and evidence, remove or disable through an approved change, clean up schedules/credentials/exceptions/datasets/integrations, and check dependent controls.

## Evidence record

| Field | Required |
|---|---|
| Validation ID/level | `VAL-###`; `S/D/C/E` |
| Date/reviewer | independent role when required |
| Product/release/surface | exact values |
| Environment/identity | safe alias plus RBAC/SBAC/object/data scope |
| Artifact/version/hash | exact candidate |
| Fixture/timeframe | sanitized, bounded, timezone |
| Expected/prohibited | objective assertions |
| Observation | raw result/error reference |
| Result | `PASS/FAIL/NOT RUN/N/A` plus rationale |
| Coverage/limitations | ingestion, parser, retention, clock, permissions, sample limits |
| Follow-up/owner | smallest next action |

Preserve evidence securely and avoid embedding secrets or unnecessary operational data.
