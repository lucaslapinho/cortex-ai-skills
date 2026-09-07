# Example: Connected Collector, No Visible Events

## Symptom

A user reports that an unnamed Cortex collector shows “connected,” but a query returns zero rows.

## Applicable boundary

Product, component type, version, license, dataset, query, timeframe, and identity are all unknown.

Status: `UNVERIFIED / TENANT-UNVERIFIED`. The statement supports only a user-reported component status, not a verified cause.

## Why zero rows are ambiguous

Competing hypotheses include:

1. the source produced no matching event or export filtered it;
2. the collector control channel is connected but its source input is misconfigured;
3. the collector received data but could not send it;
4. transport or ingestion rejected/delayed it;
5. a raw record exists under a different literal dataset;
6. parsing or mapping failed;
7. retention, source time, or query window excludes it;
8. RBAC/SBAC/dataset access hides it;
9. the query field/filter is wrong.

## Read-only discriminating checks

| Order | Check | If present | If absent |
|---:|---|---|---|
| 1 | Controlled source event and source audit | Continue with its marker | Fix source/export before Cortex |
| 2 | Component assignment and input evidence | Check send/queue/errors | Inspect source permissions/config |
| 3 | Component send and transport evidence | Check ingestion | Inspect proxy/TLS/route/backpressure |
| 4 | Tenant ingestion health/metric | Find raw data | Inspect entitlement/rejection/service |
| 5 | Literal raw dataset and marker | Check parsing/mapping | Check name, indexing, identity, retention |
| 6 | Parser/mapping result/error | Check normalized query | Fix/test rule under change control |
| 7 | Same bounded query under intended scope | Interpret result | Inspect RBAC/SBAC/time/filter |

Do not guess a dataset or field. Ask the query owner for the exact bounded query and identity.

If the clarified product is XSIAM and raw records are visible while XDM returns
zero rows, add a specific access hypothesis: current documentation does not support
XDM queries under **Datasets Rows** filters. Inspect the effective scope and
no-filter policy under the same identity/timeframe before attributing the symptom
to a parser or Data Model Rule. This is a documented possibility, not an observed
tenant cause. Keep row filters and SBAC intact; an authorized raw-dataset check is
preferable to broadening access. See the
[XSIAM access boundary](../../references/api-auth-and-access.md#xsiam-raw-dataset-scope-versus-xdm-visibility),
rechecked on 2026-09-06.

## State changes held

Do not restart/reinstall the component, rotate credentials, disable parsing, or replay source data until:

- the exact component and owner are known;
- transient evidence is retained;
- the change is approved;
- duplicate/backlog implications are understood;
- rollback and end-to-end verification are defined.

## Expected outcome

The immediate deliverable is a layer-status matrix and next read-only check, not a fabricated root cause. C/E remain `NOT RUN`.
