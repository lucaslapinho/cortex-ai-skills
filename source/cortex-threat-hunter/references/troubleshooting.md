# Troubleshooting hunts

## Contents

1. Empty results
2. Too many results
3. Inconsistent counts
4. Missing pivots
5. Timeline conflicts
6. Query uncertainty
7. Access and product mismatches

## 1. Empty results

Do not conclude “no activity.” Check in order:

1. target product and query surface;
2. dataset existence and tenant schema;
3. time field, timezone, and window;
4. retention;
5. collection health with a known-good expected event;
6. permissions and data scope;
7. field value shape, nulls, case, and normalization;
8. parser changes;
9. filters and exclusions;
10. compile and execution outcome;
11. sampling, limits, and cancellation.

Record which checks were actually performed.

## 2. Too many results

Check:

- population/denominator;
- benign administrative/service activity;
- aggregation unit;
- duplicate or fan-out joins;
- shared infrastructure;
- overly broad time or entity predicates;
- baseline segmentation;
- expected-event prevalence.

Reduce ambiguity with discriminators, not undocumented arbitrary exclusions.

## 3. Inconsistent counts

Check:

- raw rows versus unique entities;
- deduplication keys;
- event versus ingestion-time windows;
- late arrival and retention;
- role scope and permissions;
- null/grouping behavior;
- one-to-many joins;
- evolving case/issue/finding state.

Preserve each query-plan revision so two different questions are not compared as identical.

## 4. Missing pivots

A missing pivot may reflect:

- source not collected;
- entity key absent or redacted;
- identity/asset resolution delay;
- license/module not enabled;
- product surface difference;
- time window mismatch;
- data scope restrictions.

Record GAP-nnn. Do not fabricate an identifier or silently substitute a different entity.

## 5. Timeline conflicts

Preserve raw times and identify the clock owner. Compare source, ingestion, detection, and update times. Consider skew, delayed upload, cloud control-plane latency, and analyst-edited objects. Do not choose a preferred timestamp merely because it supports the hypothesis.

## 6. Query uncertainty

If exact XQL cannot be verified:

- stop before presenting executable syntax;
- write a semantic query plan;
- list unresolved dataset/field/type tokens;
- request tenant schema evidence;
- specify compile and bounded-execution acceptance tests;
- route to XQL engineering.

Official examples are patterns, not proof that the same dataset/field is present.

## 7. Access and product mismatches

An apparently missing feature may be caused by product, release, license, permission, scope, or navigation changes. Identify the documentation target and tenant facts separately. Query Center or Graph Search documentation for XSIAM does not establish availability in XDR or in a particular tenant.
