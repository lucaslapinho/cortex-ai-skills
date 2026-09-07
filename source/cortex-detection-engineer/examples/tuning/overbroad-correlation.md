# Tuning an overbroad correlation

## Symptom

A scheduled Cortex XSIAM correlation reportedly generates thousands of matches during software rollout. The operator asks to suppress all Issues for one day and permanently allowlist the parent process.

## Product and evidence

- Product/surface: claimed Cortex XSIAM scheduled correlation
- Rule export, query, tenant logs, and audit rows: not supplied
- Status: `UNVERIFIED / TENANT-UNVERIFIED`
- `S: NOT RUN` — no independent evaluation of this example revision.
- `D: PASS` — cited safeguards and monitoring behavior were documented at the stated source snapshot; the reported cause is not verified.
- `C: NOT RUN` — no exact tenant schema or rule-editor acceptance.
- `E: NOT RUN` — no tenant execution or measured tuning outcome.

The request contains proposed remedies, not evidence of cause. A one-day suppression changes Issue visibility but does not necessarily reduce rule hits or fix selectivity. A broad parent allowlist may be attacker-mimickable.

## Preserve and diagnose

Request:

- rule ID/revision/export and exact XQL;
- `correlations_auditing` records around the spike;
- sampled contributing events and Issue outcomes;
- rollout population/change window;
- grouping key, null rate, duplicates, and window overlap;
- current suppression and exceptions;
- known positive and benign fixtures.

Test hypotheses in this order:

1. missing behavioral/subtype clause;
2. duplicated/replayed telemetry or overlapping schedule windows;
3. null or overbroad grouping key;
4. many-to-many join/cardinality error;
5. legitimate rollout behavior;
6. parser/schema change;
7. actual widespread attack.

## Controlled tuning experiment

- Freeze the original revision.
- Segment rollout endpoints and ordinary populations.
- Add a discriminating verified behavior clause before considering an exception.
- If an exception is necessary, scope it to stable verified properties, owner, rollout window, and expiry.
- Replay positive, rollout-benign, negative, null, duplicate, delayed, and volume fixtures.
- Compare known-positive recall, match/Issue volume, distinct entities, analyst effort, and Case behavior.
- Shadow/canary the candidate with stop and rollback triggers.

## Decision

Do not apply the requested global allowlist or suppression yet. The smallest next step is to inspect the rule/audit/sample evidence and determine whether volume is duplicate/cardinality, missing selectivity, or known rollout behavior.

If volume approaches the current documented 5,000-in-24-hours auto-disable safeguard, treat it as urgent operational risk rather than a tuning target. The threshold is version-sensitive and must be rechecked.

## Expected output

A review should produce the root cause, before/after logic, fixture results, FP/FN impact, exception scope/expiry if any, expected volume, owner, rollback, and monitoring. No tenant result is claimed here.

## Official references

- Local tuning guidance: [baselines, thresholds, and tuning](../../references/baselines-thresholds-and-tuning.md).
- [Create a correlation rule](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/threat-management/detection-rules/what-are-detection-rules/whats-a-correlation-rule/create-a-correlation-rule.md)
- [Monitor correlation rules](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/threat-management/detection-rules/what-are-detection-rules/whats-a-correlation-rule/monitor-correlation-rules.md)
