# Baselines, thresholds, and tuning

## Contents

- [Baseline design](#baseline-design)
- [Threshold design](#threshold-design)
- [Suppression and grouping](#suppression-and-grouping)
- [False-positive analysis](#false-positive-analysis)
- [False-negative analysis](#false-negative-analysis)
- [Exception governance](#exception-governance)
- [Tuning experiment](#tuning-experiment)
- [Stop conditions](#stop-conditions)

## Baseline design

A baseline must identify:

- population and segmentation keys;
- start/end, timezone, retention, and source versions;
- working days, maintenance, business cycles, and seasonality;
- known incidents or tests excluded from the baseline and why;
- missing telemetry, nulls, late arrivals, and access scope;
- metric and denominator;
- expected drift and review date.

Do not call a few hours of traffic a baseline for a weekly or monthly process. Do not pool service accounts, administrators, workstations, servers, and ephemeral infrastructure without testing whether their distributions differ.

Platform Analytics/ABIOC baselines are product-managed behavior. Do not claim their learned window or features unless current official documentation explicitly provides them. A user-defined correlation threshold is not the same construct.

## Threshold design

Choose a method appropriate to the behavior:

| Method | Use when | Risk |
|---|---|---|
| Absolute count | Denominator and population are stable | Breaks under scale/seasonality |
| Rate or ratio | Exposure/opportunity varies | Bad denominator creates false confidence |
| Peer-group deviation | Comparable peers exist | Peer contamination or sparse groups |
| Per-entity historical deviation | Entity history is representative | Cold start and role change |
| Sequence condition | Order/timing is discriminative | Late/out-of-order telemetry |
| Rare combination | Joint behavior is unusual | Cardinality and novelty noise |

Every candidate threshold records:

- mathematical definition and boundary inclusivity;
- window and evaluation cadence;
- grouping key and null behavior;
- baseline evidence and sample size;
- expected match/Issue volume;
- analyst capacity and maximum acceptable volume;
- sensitivity target and known missed variants;
- review/expiry date and owner.

Without representative data, label it `CONCEPTUAL` and supply a measurement plan. Never present “5 failures in 10 minutes” or any other familiar value as universally valid.

## Suppression and grouping

Suppression is not tuning the behavioral predicate. It changes Issue visibility after matches. Define:

- purpose: duplicate control, not hiding a weak rule;
- suppression duration and field/key semantics;
- null behavior;
- expected distinct entities during the period;
- what evidence remains queryable;
- analyst and Case-grouping impact;
- rollback trigger.

Current correlation documentation exposes suppression configuration, but exact duration/options are version-sensitive. Verify them in the target product and editor.

Case grouping is broader platform logic. Correct field mapping can influence grouping, but cannot guarantee a Case. Measure both fragmentation and over-grouping.

## False-positive analysis

Use a table:

| Benign mechanism | Distinguishing evidence | Frequency/scope | Proposed change | Introduced false-negative risk | Owner/expiry |
|---|---|---|---|---|---|

Questions:

- Is the match truly benign or merely authorized but risky?
- Is the allow condition stable and resistant to attacker mimicry?
- Can scope be narrowed by signer, path, parent, user role, device class, or approved change window using verified fields?
- Will an exclusion remove causality/triage context?
- Can the behavior be retained in shadow/low-severity review rather than discarded?

Avoid actor-controlled allow keys such as filename alone. Avoid broad path, username, domain, or parent-process exclusions without provenance and expiry.

## False-negative analysis

Model:

- alternative tools/interpreters or living-off-the-land paths;
- case/encoding/path variations;
- renamed binaries and remote execution;
- missing or null arguments;
- alternate event subtypes;
- source/parser/retention/permission gaps;
- below-threshold distribution across entities or time windows;
- delayed/out-of-order events;
- suppressed signals and generated exceptions;
- attacker mimicry of allowlisted properties.

For each, add a fixture or explicitly accept residual risk. Precision improvement without recall review is incomplete.

## Exception governance

Every manual or product-generated exception needs:

- stable ID and rule revision;
- exact predicate/scope;
- reason and evidence;
- requester, approver, and owner;
- creation/review/expiry dates;
- affected populations and estimated volume;
- security risk and compensating coverage;
- validation fixtures;
- removal and verification steps.

Current BIOC documentation describes an automatic PROCESS-SHA256 exception above 100 endpoints over 72 hours. Monitor it as a behavior-changing rule event. Verify whether the exception masks malicious propagation or simply a common binary before retaining it.

## Tuning experiment

1. Freeze the prior revision and representative fixture set.
2. State the observed defect and desired quality change.
3. Change one meaningful variable where possible.
4. Replay positive, benign, negative, boundary, null, delayed, duplicate, and high-volume fixtures.
5. Compare row grain, match count, Issue count, distinct entities, FP themes, known-recall fixtures, and analyst effort.
6. Check rule-surface compatibility again.
7. Run shadow/canary with a bounded population and window.
8. Record result, decision, owner, rollback, and next review.

Do not overwrite evidence from the prior revision. A failed experiment remains traceable.

## Stop conditions

Reject or roll back tuning when:

- a known high-impact positive no longer matches;
- a required field/source is absent or materially degraded;
- rule volume approaches product safeguards or exceeds capacity;
- suppression/exception scope is broader than intended;
- Case over-grouping or fragmentation materially worsens;
- the exact rule surface no longer accepts the logic;
- ownership, approval, or rollback is missing;
- the change depends on an invented field, function, setting, or tenant claim.
