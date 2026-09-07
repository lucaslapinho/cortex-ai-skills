# Validation, monitoring, and governance

## Contents

- [Validation ladder](#validation-ladder)
- [Fixture catalog](#fixture-catalog)
- [Deployment gates](#deployment-gates)
- [Monitoring contract](#monitoring-contract)
- [Correlation audit evidence](#correlation-audit-evidence)
- [Change control](#change-control)
- [Rollback and retirement](#rollback-and-retirement)
- [Evidence record](#evidence-record)

## Validation ladder

| Stage | Environment | Evidence | Permitted claim |
|---|---|---|---|
| Design review | Offline | Threat model, source citations, pseudologic | `CONCEPTUAL` |
| Static compatibility | Offline | Current rule contract and query review | Document-supported candidate; no tenant claim |
| Editor/compiler | Non-production tenant | Exact artifact accepted | `C: PASS`; not executed |
| Historical fixture/replay | Isolated or tenant test | Controlled results and known labels | `E: PASS` only for recorded scope |
| Shadow | Tenant, no operational action | Match/volume/quality observations | Bounded tenant behavior |
| Canary | Limited population | Issues, analyst outcomes, rollback evidence | Bounded enablement result |
| Production | Approved scope | Monitoring and outcome evidence | Only the recorded deployment/window |

Do not skip from documentation to broad enablement. Product safeguards are not substitutes for canary limits.

## Fixture catalog

Each fixture records ID, expected behavior, source, integrity hash where applicable, privacy classification, and expected observation.

Required families:

- canonical positive;
- realistic benign lookalike;
- explicit negative;
- just below/at/above thresholds;
- null, empty, malformed, and type-conflict fields;
- non-target event subtype with similar fields;
- duplicate/replayed event;
- delayed and out-of-order sequence;
- clock/timezone boundary;
- high-cardinality and many-to-many correlation;
- high-volume overload;
- missing source/parser/mapping/permission;
- stale/disabled rule and generated exception;
- mapping that fragments or over-groups Cases;
- prompt-injected or poisoned attached artifact.

Do not use customer events in a published Skill. Sanitize and minimize retained tenant fixtures.

## Deployment gates

Before limited enablement:

- [ ] product/version/license and rule surface verified
- [ ] owner, approver, change window, and affected population named
- [ ] exact artifact hash and rollback/export retained
- [ ] required telemetry/schema/types/coverage verified
- [ ] query accepted by the exact rule editor/compiler
- [ ] all material fixtures pass
- [ ] expected volume fits analyst and platform capacity
- [ ] FP/FN/evasion review complete
- [ ] Issue fields and grouping expectations validated
- [ ] permissions and audit access verified
- [ ] safeguards, exceptions, stop conditions, and partial failure defined
- [ ] any prevention/response has a separate approval boundary

## Monitoring contract

Define an objective, query/source, owner, cadence, alert threshold, and response for each metric:

| Dimension | Example evidence |
|---|---|
| Execution health | initiated/completed/error, retry, lag, duration |
| Rule state | enabled/disabled, revision, source, exception count |
| Volume | matches, Issues, distinct entities, rate, safeguard proximity |
| Quality | analyst disposition, duplicate rate, benign themes, known positive recall |
| Coverage | source health, null rate, parser/schema drift, retention/access |
| Investigation | triage time, required fields, drill-down success |
| Case behavior | grouped/ungrouped, fragmentation, over-grouping |
| Safety | prevention/response attempts, failures, rollback, partial state |
| Governance | owner acknowledgement, stale review, expiring exceptions |

Avoid a single “precision” percentage without label quality and denominator. Record unknowns and sampling bias.

## Correlation audit evidence

Current XSIAM documentation identifies the `correlations_auditing` dataset for rule execution monitoring. It documents statuses such as Initiated, Initiated Manually, Completed, and Error, plus query timeframes, execution timestamps, retries, failure reason, schedule, severity, suppression, source, XQL, and rule identity.

Use the page for the documented model and tenant rows for operational evidence. Do not fabricate field names beyond the current page or assume this dataset exists identically in Cortex XDR. See [S10](official-sources.md#s10--monitor-correlation-rules).

For scheduled server errors, distinguish:

- query/resource failure: scope, fields, timeframe, aggregation, and decomposition;
- Issue-generation/output failure: output size, long arrays/strings, descriptions, mappings, suppression fields, and severity configuration.

Use the official troubleshooting page and verify every proposed XQL function before showing syntax. See [S11](official-sources.md#s11--troubleshoot-scheduled-correlation-errors).

## Change control

Every revision records:

- rule ID/name/source and prior/new hash;
- threat behavior and reason for change;
- product/version/source refresh;
- logic, fields, schedule/window, threshold, suppression, mapping, severity, and exception delta;
- affected fixtures and results;
- FP/FN and capacity impact;
- approver, owner, deployment scope/time;
- rollback and monitoring window;
- Issue/Case and downstream dependency impact.

Do not edit a global/vendor rule as if it were user-owned. Use documented copy/exception mechanisms and retain source provenance.

## Rollback and retirement

Rollback triggers include:

- runaway volume or approach to documented safeguard;
- false-positive harm or false-negative regression;
- invalid/missing schema or source degradation;
- unexpected prevention/response;
- Case over-grouping/fragmentation;
- permissions or audit loss;
- rule errors, retries, or lag above tolerance;
- no accountable owner.

Rollback plan identifies exact prior artifact/export, disable/revert procedure, dependent rules/playbooks, data/lookup recovery, expected verification, partial-failure owner, and audit record.

Retirement requires:

- evidence the threat/control need ended or a successor covers it;
- dependency and response-workflow review;
- historical evidence retention;
- exception/suppression cleanup;
- owner and risk approval;
- verification that no stale duplicate remains.

## Evidence record

```text
Detection ID/revision:
Product/version/license:
Rule surface:
Tenant alias:
Identity/role/scope:
Artifact hash:
Official-source snapshot:
Schema evidence:
Fixture IDs:
S result: <PASS | FAIL | NOT RUN | N/A> — <independent response-evaluation rationale and retained record>
D result: <PASS | FAIL | NOT RUN | N/A> — <dated official-document rationale and source record, or reason not applicable/run>
C result: <PASS | FAIL | NOT RUN | N/A> — <named tenant/editor/schema/import rationale and retained record, or reason not run>
E result: <PASS | FAIL | NOT RUN | N/A> — <observed execution/result rationale and retained record, or reason not run>
Observed match/Issue/Case behavior:
FP/FN and coverage notes:
Owner/approver:
Rollback evidence:
Monitoring window:
Sanitized artifacts and retention:
```
