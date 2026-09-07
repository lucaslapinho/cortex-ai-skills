# Detection troubleshooting

## Contents

- [Triage order](#triage-order)
- [Symptom matrix](#symptom-matrix)
- [Zero matches](#zero-matches)
- [Too many matches](#too-many-matches)
- [Rule editor rejection](#rule-editor-rejection)
- [Execution or Issue-generation errors](#execution-or-issue-generation-errors)
- [Unexpected Case behavior](#unexpected-case-behavior)
- [Auto-disable or generated exceptions](#auto-disable-or-generated-exceptions)
- [Unsafe response linkage](#unsafe-response-linkage)

## Triage order

1. Preserve rule/export/query, revision, error, timestamps, product/version, and identity scope.
2. Confirm security objective and expected signal grain.
3. Confirm product, license, rule surface, and current documentation.
4. Validate XQL restrictions for the exact surface.
5. Validate tenant dataset, fields, types, nulls, parser, and access.
6. Validate source collection, retention, clocks, latency, and rule window.
7. Validate threshold, aggregation, duplicates, suppression, mapping, and output size.
8. Inspect rule state, audit status, retries, errors, and generated exceptions.
9. Compare analyst outcomes, FP/FN, Case behavior, and downstream dependencies.
10. Make the smallest reversible change; retest all material fixtures.

## Symptom matrix

| Symptom | Likely layers | First discriminating evidence |
|---|---|---|
| Query works, BIOC fails | Rule-context restrictions | Current BIOC page and exact editor error |
| Query works, real-time fails | Unsupported stage/function/source | Current real-time contract and compiler result |
| Zero matches | Coverage, subtype, nulls, window, access, rule state | Known-positive fixture plus source/schema evidence |
| Huge volume | Broad admission, duplicates, null key, threshold/window | Match distribution by entity/source and raw samples |
| Issues missing | Action/configuration, output failure, permissions, auto-disable | Audit/error/state and Issue provenance |
| Cases fragmented | Missing/invalid mapping or platform grouping | Actual Issue fields and Case outcomes |
| Cases over-grouped | Overbroad/stable-looking mapping key | Distinct activity sharing the mapped artifact |
| Rule disabled | Product safeguard, admin change, content update | Audit/change log and hit history |
| Detection quiet after exception | Exception scope too broad | Exception delta and known-positive replay |

## Zero matches

Do not conclude “behavior absent.” Check:

- rule enabled and current revision deployed;
- exact product/rule surface and license;
- source collection and parser/mapping health;
- dataset and field presence under the execution identity;
- event category and target subtype;
- non-null values and type normalization;
- event/insert time, timezone, window, schedule, delay, and retention;
- case sensitivity and rule-context semantics;
- known-positive fixture visibility in Query Center and rule editor;
- suppression/exception behavior and downstream Issue filters.

If the fixture is absent from the source, escalate the telemetry gap. Do not relax the detection until it matches unrelated data.

## Too many matches

First preserve samples and distributions. Then check:

- missing subtype or behavior clause;
- many-to-many join or wrong aggregation grain;
- null/empty grouping key;
- duplicate/replayed events and overlapping windows;
- population scale and unsegmented baseline;
- maintenance/administrative activity;
- broad allow/exclusion assumptions;
- suppression hiding but not reducing rule hits;
- proximity to documented auto-disable safeguards.

Do not set the threshold just below a product safeguard. Define a quality and capacity target well below it.

## Rule editor rejection

Classify:

1. syntax error;
2. stage/function/operator unsupported for this surface;
3. dataset/preset unsupported;
4. custom dataset prohibited for BIOC;
5. missing required `event_type` filter for BIOC;
6. aggregation prohibited for BIOC;
7. mandatory real-time `filter` missing;
8. real-time dataset view or function unsupported;
9. license/permission/object access failure;
10. stale imported artifact or product mismatch.

Return the exact official restriction and compiler message. Do not guess a near-synonym or remove logic without assessing semantics.

## Execution or Issue-generation errors

Current XSIAM troubleshooting separates query/resource errors from Issue-generation errors.

For query/resource errors, test bounded time, early field reduction, aggregation/cardinality, source volume, and decomposition. For Issue-generation errors, inspect output field size, arrays/strings, Issue name/description, drill-down substitutions, field mappings, suppression fields, and severity.

Preserve the failed artifact and exact error. Verify any function used to trim output against the current XQL reference and the target rule context.

## Unexpected Case behavior

Field mapping does not guarantee grouping. Inspect:

- whether the Issue was generated;
- mapped value presence, type, format, normalization, and stability;
- overly broad or missing entity artifacts;
- severity/domain and current qualification behavior;
- related Issue timing and platform grouping context;
- fragmentation and over-grouping samples;
- current Case/Issue documentation.

Do not hard-code a Case outcome from design documentation.

## Auto-disable or generated exceptions

At the current snapshot, BIOC and correlation pages document auto-disable at 5,000 or more hits in 24 hours; BIOC pages also document a PROCESS-SHA256 exception above 100 endpoints in 72 hours. Recheck the page and tenant.

When observed:

1. preserve rule state, audit/change record, volume timeline, and generated exception;
2. identify whether behavior is benign prevalence, duplication, schema drift, attack spread, or logic defect;
3. replay known positive/benign fixtures with the exception;
4. narrow or remove the exception only through authorized change control;
5. retest and monitor below capacity targets.

Never re-enable repeatedly without correcting the cause.

## Unsafe response linkage

If a detection directly isolates endpoints, disables users, deletes files, blocks network traffic, or changes prevention:

- separate detection from response authorization;
- identify actual policy/approval and execution identity;
- require deterministic verification and least scope;
- add idempotency, timeout, cancellation, rollback/recovery, and post-action evidence;
- test partial failure;
- recommend suspension of unsafe linkage to its authorized owner; disable or revert it only within an existing explicit change authorization and approved recovery plan. If authorization or rollback is absent, stop at the evidence-backed handoff rather than making a tenant change.

High confidence or an ATT&CK mapping is not authorization.
