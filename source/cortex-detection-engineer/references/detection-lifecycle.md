# Detection lifecycle

## Contents

- [Lifecycle contract](#lifecycle-contract)
- [1. Threat behavior](#1-threat-behavior)
- [2. Threat model](#2-threat-model)
- [3. ATT&CK interpretation](#3-attck-interpretation)
- [4. Telemetry contract](#4-telemetry-contract)
- [5. Query and logic contract](#5-query-and-logic-contract)
- [6. Expected signal](#6-expected-signal)
- [7. Baseline and threshold](#7-baseline-and-threshold)
- [8. Validation](#8-validation)
- [9. False positives and false negatives](#9-false-positives-and-false-negatives)
- [10. Tuning](#10-tuning)
- [11. Rule-surface decision](#11-rule-surface-decision)
- [12. Monitoring, rollback, and retirement](#12-monitoring-rollback-and-retirement)
- [Promotion gates](#promotion-gates)

## Lifecycle contract

A detection is a maintained decision system, not merely a query. Preserve a stable ID and revision across:

```text
Threat behavior
  -> threat model
  -> ATT&CK interpretation
  -> telemetry
  -> query/logic
  -> expected signal
  -> baseline/threshold
  -> validation
  -> FP/FN analysis
  -> tuning
  -> rule surface
  -> monitoring/rollback/retirement
```

At each transition, record evidence, assumptions, owner, decision, and the condition that would invalidate it.

## 1. Threat behavior

Write the behavior as observable events and relationships:

- actor/entity and target;
- action and sequence;
- relevant time relationship;
- environmental preconditions;
- expected benign alternatives;
- protected asset or decision at risk.

Avoid circular definitions such as “malicious PowerShell is PowerShell that triggers the rule.” A useful behavior statement is falsifiable and independent of a product label.

## 2. Threat model

Document:

| Element | Question |
|---|---|
| Adversary opportunity | What capability or access makes the behavior possible? |
| Preconditions | What must already be true? |
| Protected asset | What can be harmed or abused? |
| Adverse outcome | What security property fails? |
| Detection point | Which observable transition is most discriminative? |
| Alternatives | Which legitimate workflows look similar? |
| Evasions | How can an adversary avoid or mutate the observable? |
| Response consequence | What decision will analysts or automation make? |

Do not select severity from technique name alone. Tie severity to affected asset, confidence, impact, and response policy.

## 3. ATT&CK interpretation

Map after the observable behavior is defined. Record:

- tactic and technique/sub-technique;
- ATT&CK version or access date;
- which observed clause supports the mapping;
- alternatives and uncertainty;
- whether the mapping is for description, coverage reporting, or a rule field.

Palo Alto's current XSIAM coverage dashboard can show rules and contributing source types by ATT&CK mapping, but active source status does not imply every associated rule is active or applicable. Treat dashboard coverage as inventory evidence, not outcome evidence. See [S17](official-sources.md#s17--mitre-attck-framework-coverage).

## 4. Telemetry contract

For every required observation, specify:

- source system and collection mechanism;
- product dataset/preset only when supported;
- event category and exact subtype semantics;
- required fields, types, nullability, and normalization;
- source event time, ingestion time, timezone, clock quality, latency, and retention;
- identity/host/network correlation keys and their stability;
- parser/mapping/version and RBAC/SBAC scope;
- expected positive and negative/control events;
- known blind spots and a missing-telemetry escalation.

Do not infer schema from a filename, dashboard label, project namespace, or example. A Process category does not establish process start or execution; verify subtype and test a non-start Process event.

## 5. Query and logic contract

Define the logic independently of syntax:

1. admission criteria;
2. ordering or time relationship;
3. entity correlation keys;
4. aggregation and row grain;
5. threshold/window semantics;
6. duplicate, null, delayed, and out-of-order handling;
7. excluded behavior and why;
8. output fields for triage, provenance, and grouping;
9. result-volume expectation; and
10. target rule surface.

Only show executable XQL when its stages/functions/operators and every concrete dataset/field are adequately supported for the target product and rule context. Otherwise use clearly marked pseudologic and placeholders.

Query Center success is a discovery result. It is not evidence of BIOC, scheduled-correlation, or real-time-correlation compatibility.

## 6. Expected signal

Define one match:

- What event/entity set does it represent?
- Which risk hypothesis does it support?
- Which facts remain unknown?
- Which fields allow an analyst to verify it?
- Which rule/source IDs preserve provenance?
- What should an analyst do next?
- What must never happen automatically from this signal alone?

Separate:

```text
telemetry row -> query match -> detection signal -> Issue -> possible Case -> investigation conclusion
```

None of these arrows is automatic proof of compromise.

## 7. Baseline and threshold

Do not invent a production threshold. Record:

- measured population and segmentation;
- baseline start/end, timezone, and excluded incidents;
- seasonality, maintenance, business cycles, and source changes;
- chosen statistic or rate denominator;
- candidate threshold and expected volume;
- capacity and service-level constraints;
- minimum sensitivity requirement;
- uncertainty and expiry/review date.

If no representative data exists, provide `CONCEPTUAL` candidates and a collection plan. Thresholds copied from threat reports or another tenant are hypotheses, not validation.

## 8. Validation

Minimum fixture families:

- confirmed or synthetically controlled positive;
- common benign lookalike;
- explicit negative control;
- value just below, at, and above each boundary;
- null/missing/ill-typed fields;
- duplicated, delayed, out-of-order, and replayed events;
- high-cardinality and high-volume cases;
- permission/retention/ingestion gaps;
- rule-editor incompatibility; and
- downgrade/rollback behavior.

Separate historical replay, shadow operation, non-production enablement, and production observation. Retain exact revision hashes and result evidence.

## 9. False positives and false negatives

For each likely false positive, state:

- benign mechanism;
- distinguishing evidence;
- prevalence and affected populations;
- safest refinement;
- risk introduced by the refinement;
- owner and expiry of any exception.

For each false negative/evasion, state:

- missed variation or collection gap;
- why the logic misses it;
- compensating detection or collection;
- test fixture;
- residual risk.

Tuning that lowers volume while increasing high-impact false negatives is not an improvement.

## 10. Tuning

Prefer, in order:

1. correct source/schema/time semantics;
2. strengthen discriminative behavior;
3. segment by environment or entity class;
4. adjust window/threshold with measured evidence;
5. add narrow, owned, expiring exclusions;
6. configure suppression only after preserving analyst visibility and grouping intent.

Never add an indefinite global allowlist merely because a single benign event matched. Monitor any platform-generated BIOC exception as a rule change, not harmless noise.

## 11. Rule-surface decision

Choose the smallest documented surface that represents the behavior and needed time/source relationship. Use the matrix in [rule surfaces](rule-surfaces.md). Verify:

- product/version/license;
- supported source and syntax;
- schedule/real-time semantics;
- action and output fields;
- suppression/grouping behavior;
- safeguards and permissions;
- editor/compiler acceptance;
- audit/monitoring path.

If these are incomplete, keep the candidate in research/shadow state.

## 12. Monitoring, rollback, and retirement

Monitor at least:

- executions, errors, retries, lag, and disabled state;
- matches and Issues by population/time;
- analyst dispositions and time-to-triage;
- precision proxy, known recall fixtures, and FP/FN themes;
- null/field/schema drift and missing telemetry;
- suppression and exception growth;
- Case grouping/fragmentation where relevant;
- source/content/product-version change;
- proximity to documented safeguards;
- owner acknowledgment and review cadence.

Rollback/disable conditions must be explicit: unsafe behavior, runaway volume, invalid schema, missing critical telemetry, excessive analyst burden, material false negatives, or unowned exceptions. Retirement requires a successor or documented residual-risk acceptance, dependency review, evidence retention, and removal verification.

## Promotion gates

| Gate | Minimum evidence | Failure result |
|---|---|---|
| Research -> candidate | Falsifiable behavior and telemetry plan | Return to threat model |
| Candidate -> editor test | Supported product/surface and schema evidence | Keep conceptual |
| Editor test -> shadow | Exact artifact accepted; fixture plan approved | Correct contract |
| Shadow -> limited enablement | Representative FP/FN/volume evidence; owner and rollback | Continue shadow or reject |
| Limited -> production | Safety/permission review, monitoring, response capacity, independent approval | Do not enable broadly |
| Production -> maintained | Review cadence, evidence, tests, exception governance | Disable or assign owner |
| Maintained -> retired | Successor/risk decision, dependency and rollback plan | Keep controlled until resolved |
