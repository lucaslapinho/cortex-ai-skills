# Lateral-Movement Hunt with Schema Gates

This example shows how to design a cross-source lateral-movement hunt when the tenant datasets and join keys are unknown. It intentionally stops before emitting executable XQL.

## Context and evidence

| Item | Value |
|---|---|
| Hypothesis | A user or source endpoint authenticated to a different endpoint and was followed by unusual process or remote-session activity within a bounded time window. |
| Product | Cortex XSIAM 3.x |
| Surface | Interactive Query Center hunt design |
| Canonical class | `CONCEPTUAL` |
| Qualifier | `TENANT-UNVERIFIED` |
| Executability | `CONCEPTUAL — NOT EXECUTABLE` |
| Reason for gating | No tenant dataset list, mapped schema, authentication source, endpoint/network source, key types, retention, identity scope, or representative rows are available. |

The behavior may require more than one telemetry source, but no universal Cortex dataset or field names are assumed. `xdr_data` process fields alone do not prove that the required authentication or remote-session event is present.

## Observable contract

| Observable | Required semantic value | Tenant evidence required |
|---|---|---|
| Authentication event | Source entity, destination entity, account, outcome, event time, logon/session mechanism | Exact dataset, fields, types, parser/mapping, population, success semantics |
| Endpoint/process or network follow-on | Destination endpoint, process/connection, user context, event time | Exact dataset/fields, collection scope, null behavior |
| Entity normalization | Stable host/user identifiers and alias rules | Observed examples showing both sources represent the same identity |
| Temporal relation | Maximum acceptable delay and clock uncertainty | Source clock quality, ingestion delay, `_time` semantics, retained window |
| Baseline/context | Known management systems, jump hosts, scanners, service accounts, maintenance windows | Governed lists and provenance, not hard-coded guesses |

## Schema-discovery sequence

1. Select the exact product, release, Query Center identity, license, timeframe, and business scope.
2. Inventory visible datasets/presets and identify the authoritative authentication and endpoint/network sources.
3. Inspect bounded representative records; verify field names, types, null population, time semantics, and success/failure values.
4. Establish canonical entity mappings. Do not join a display hostname to an identifier merely because values look similar.
5. Measure key uniqueness on each side and estimate one-to-one, one-to-many, or many-to-many fan-out.
6. Quantify clock skew and select a temporal window that represents the hypothesis.
7. Build and validate each side independently before joining.
8. If reliable keys cannot be established, keep the two result sets separate and correlate manually or through a documented tenant-supported method.

## Conceptual plan

**CONCEPTUAL — NOT XQL; placeholders must not be executed**

```text
LEFT:
  read {{TENANT-VERIFIED AUTHENTICATION DATASET}}
  within {{BOUNDED TIMEFRAME}}
  retain successful remote authentication events using {{VERIFIED SUCCESS SEMANTICS}}
  project {{EVENT TIME, SOURCE ENTITY, DESTINATION ENTITY, ACCOUNT, SESSION TYPE}}

RIGHT:
  read {{TENANT-VERIFIED ENDPOINT OR NETWORK DATASET}}
  within the same coverage-aware timeframe
  retain {{FOLLOW-ON ACTIVITY RELEVANT TO THE HYPOTHESIS}}
  project {{EVENT TIME, DESTINATION ENTITY, ACCOUNT, PROCESS/CONNECTION CONTEXT}}

CORRELATE ONLY AFTER VALIDATION:
  match on {{SEMANTICALLY IDENTICAL, TYPE-COMPATIBLE TENANT KEYS}}
  require right.event_time within {{VALIDATED TEMPORAL TOLERANCE}} after left.event_time
  use {{DELIBERATE JOIN TYPE AND CONFLICT STRATEGY}}
  preserve source evidence IDs and both timestamps
  cap analyst output only after preserving the intended population and order
```

## Join-readiness gate

| Check | Pass condition | Current result |
|---|---|---|
| Both datasets exist and are visible | Direct tenant observation under the test identity | `NOT RUN` |
| Required fields exist and are populated | Tenant schema plus bounded samples | `NOT RUN` |
| Keys have the same meaning and compatible types | Data dictionary plus representative comparison | `NOT RUN` |
| Key uniqueness/fan-out is measured | Cardinality statistics from both sides | `NOT RUN` |
| Time semantics and skew are understood | Source and ingestion timing evidence | `NOT RUN` |
| Each side independently returns known fixtures | Positive and negative tenant tests | `NOT RUN` |
| Join output preserves expected grain | Representative joined fixtures and duplicate analysis | `NOT RUN` |

No executable join is permitted until these checks pass. A documented `join` stage does not validate the chosen datasets, keys, or hunt logic.

## Expected result contract

The intended output grain is one correlated authentication-to-follow-on sequence, preserving both source record identifiers/timestamps, normalized user and endpoint identities, session mechanism, follow-on activity, and correlation delay. A match supports a sequence for investigation; it does not prove lateral movement or compromise.

## False positives and false negatives

Likely benign alternatives include authorized administration, remote support, patching, software deployment, jump hosts, service accounts, vulnerability scanning, orchestration, and failover. Validate governance and change windows rather than inserting an unverified allowlist.

Missed paths can result from alternate protocols, local accounts, credential reuse without a visible authentication event, NAT/proxy/VDI ambiguity, hostname reuse, renamed tools, cloud control-plane activity, field nulls, parser changes, collection gaps, short retention, permissions, clock skew, or a time window that is too narrow.

## Optimization notes

- Bound both inputs to the smallest window that still covers the sequence and timing uncertainty.
- Apply high-selectivity, type-correct filters and project only necessary correlation/evidence fields on each side before the join.
- Measure fan-out before and after the join. A lower row count does not establish correct correlation.
- Choose join type and conflict strategy explicitly. Preserve both original timestamps and source IDs.
- Avoid a join if a documented set filter or separate pivot answers the question with less ambiguity.
- Any performance claim requires a tenant comparison with equivalent semantics; none was performed here.

## Troubleshooting

- **No data on one side:** check collection, ingestion health, parser/mapping, retention, timeframe, identity scope, field population, and known fixtures.
- **Type mismatch:** validate field types and normalize only with documented functions whose return types are appropriate for the target surface.
- **Row explosion:** inspect duplicate keys and many-to-many relationships; aggregate only if the new grain still answers the hypothesis.
- **False temporal correlations:** measure source clocks and ingestion delay; compare event time rather than assuming arrival order.
- **Unresolvable identity:** stop the join and report the coverage gap; do not substitute a look-alike key.

## Rule-conversion boundary

This hunt has no executable query and is therefore ineligible for BIOC, scheduled correlation, real-time correlation, or XQLp conversion. Even after a tenant query is built, the exact target restrictions, detection semantics, false-positive model, volume, grouping, action, and rule-editor validation must be handled separately.

## Official references

- [Datasets and presets](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Datasets-and-presets)
- [XSIAM Data Model schema](https://cortex-docs.paloaltonetworks.com/xsiam-data-model-schema/readme.md)
- [`join` stage](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/stages/join.md)
- [Query Center permissions](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Query-Center-permissions)
- [Data retention](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Data-retention)

Use [the investigation template](../../templates/investigation-query.md) once the observables are known, then record execution in [the tenant validation record](../../templates/tenant-validation.md).
