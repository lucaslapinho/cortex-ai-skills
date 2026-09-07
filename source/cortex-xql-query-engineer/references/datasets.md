# Datasets, Presets, and Source Validation

Use this reference when selecting a query source, diagnosing a missing dataset, or reviewing a query whose dataset was copied from another tenant, product, or project artifact.

**Documentation review cut:** 2026-09-04  
**Tenant status for this Skill release:** tenant datasets, integrations, defaults, retention, licenses, and population were not observed.

## Contents

- Current general dataset syntax
- Source families are not interchangeable
- Dataset evidence ladder
- Discovery and validation workflow
- Required dataset record
- Restricted execution contexts
- Project-data guardrails
- Missing-data escalation

## Current general dataset syntax

The current XQL command reference documents:

```xql
dataset = <dataset_name>
```

```xql
dataset in (<dataset_name_1>, <dataset_name_2>)
```

```xql
cold_dataset = <dataset_name>
```

These blocks are `CONCEPTUAL` until each placeholder is replaced with a source verified for the target product and tenant. The `dataset` stage must be first unless a `config` stage precedes it. Dataset names are treated case-insensitively according to the current command reference.

If a query omits source selection, current XSIAM guidance and the general command reference document `xdr_data` as the default. That statement does not prove the tenant's default was not changed. Prefer an explicit source when reproducibility matters.

Source: [dataset stage](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/stages/dataset.md) and [How to build XQL queries](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/How-to-build-XQL-queries).

## Source families are not interchangeable

| Source family | Verified interpretation | Required checks |
|---|---|---|
| `xdr_data` | Current general documentation identifies it as the built-in/default dataset for ordinary dataset queries unless the tenant default changed. The current XDR schema reference documents many endpoint/event fields. | Product/version, permission scope, retention, endpoint coverage, field population, and target execution surface. |
| Tenant datasets | Availability reflects configured integrations, ingestion, parsing, and product configuration. | Exact tenant name, source/integration, schema, sample record, data freshness, retention, and RBAC/SBAC. |
| Presets | Product-provided query sources or views documented alongside datasets. | Product/version, current preset inventory, rule-context support, and populated fields. |
| XDM / data model | Normalized fields and aliases documented by the XSIAM Data Model schema; mapped data is required. | Fieldset, source mapping, target product, type, population, and query-context support. |
| Cold storage | Queried with the separately documented `cold_dataset` form. | Entitlement, retention tier, source availability, and performance expectations. |
| Forensic data | Current join guidance says forensic datasets are not included by default and require explicit enabling/selection. | License, permissions, collection state, retention, and exact source syntax. |
| Case and Issue query sources | Cortex XDR 5 has product-specific documentation and limitations. | Do not infer identical XSIAM names or coverage; verify the target product, license, tenant, and field set. |
| Parsing Rules/XQLp input | The system supplies raw input to the rule; ordinary statements do not start with a dataset or preset. | Parsing section, rule-file grammar, lookup constraints, and Data Management permissions. |

An administrator's ability to save a correlation query with an unknown dataset does not establish that the dataset exists or that ordinary users can access it. Treat existence and population as separate claims.

## Dataset evidence ladder

Use the strongest level actually demonstrated:

| Level | Evidence | Permitted statement |
|---|---|---|
| `UNVERIFIED / TENANT-UNVERIFIED` | Name appears in a request, filename, prior query, export, or derivative note. | Candidate source name only; no executable use. |
| `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Current official product documentation defines the source. | Officially documented source, but tenant availability/population unknown. |
| `TENANT-SCHEMA-VERIFIED` | Current tenant lists the source and its schema under a recorded identity/date. | Source and observed fields/types exist in that tenant context. |
| `TENANT-COMPILED` | The target query surface accepts a bounded query. | Syntax and source accepted there; data need not be present. |
| `TENANT-EXECUTED` | The query completes with scope/timeframe and raw result evidence recorded. | Observed result or zero-result state within those constraints. |

A query returning zero rows does not reduce uncertainty about ingestion, coverage, or field population unless those dependencies were independently checked.

## Discovery and validation workflow

1. Record target product, version, execution surface, tenant, identity, and intended time range.
2. Find the source in current product-specific documentation. If it is only in a sample or old version, classify it accordingly.
3. Inspect the target tenant's dataset/preset inventory and Query Builder/Search autocomplete. Allow for documented indexing or autocomplete delay.
4. Capture the source's integration/collector/parser, schema, types, source timestamp, insert timestamp when relevant, retention, and access scopes.
5. Run the smallest safe probe only after the dataset name is tenant-verified. Start with a narrow timeframe and explicit limit.
6. Add one field or filter at a time, preserving compiler text and result metadata.
7. Recheck compatibility if the destination is BIOC, correlation, API, saved/scheduled query, widget, or XQLp.

Conceptual probe shape:

```xql
config timeframe = 15m
| dataset = <tenant_verified_dataset>
| limit 5
```

Status: `CONCEPTUAL / TENANT-UNVERIFIED` until the placeholder is replaced and verified. Do not call a successful probe an ingestion-health test unless the expected event generation, transport, parser, timing, and permission path are also known.

## Required dataset record

For every reusable query, preserve:

| Field | Required content |
|---|---|
| Product and version | Exact product/release or `Unknown`. |
| Query surface | Interactive, saved/scheduled, API, BIOC, correlation type, or XQLp. |
| Dataset or preset | Literal name and whether explicit or tenant-default. |
| Evidence status | Canonical class plus qualifiers. |
| Source path | Agent, integration, collector, API, parser, or `Unknown`. |
| Schema evidence | Source, capture date, fields, and types. |
| Population evidence | Sample timestamp/count or `Not provided`. |
| Retention/timeframe | Applicable retention and requested range. |
| Access | Identity, Query Center privilege, RBAC/SBAC scope, and saved-query access if relevant. |
| Limitations | License, latency, indexing delay, null fields, forensic/cold-storage boundary, and open questions. |

## Restricted execution contexts

| Destination | Dataset constraint to enforce |
|---|---|
| BIOC in Cortex XSIAM | Current documentation allows `xdr_data`, `cloud_audit_log`, and their presets; customized datasets are not supported. A valid BIOC must at minimum filter on `event_type`. |
| Real-time correlation in Cortex XSIAM | Current documentation allows issues, cloud audit logs, third-party datasets, and data models while imposing a limited stage/function set. Dataset views are not supported. |
| Scheduled correlation in Cortex XSIAM | Dataset wildcards are not supported in correlation rules. Query window and schedule are separately bounded. |
| XQLp | Ordinary parsing statements do not begin with dataset/preset selection. `join inner` has lookup-only and section-specific constraints. |

Always re-open the current target page before a production conversion; these restrictions are version-dependent.

## Project-data guardrails

Do not derive a Cortex dataset from:

- a `.csv` or `.tsv` filename;
- an endpoint or application export header;
- project namespaces such as `SOCFramework.*`, `SOCN1.*`, or `Assessment.*`;
- an unavailable playbook/script described in a summary;
- a first-party GitHub sample without a target-tenant schema check;
- a dataset name that merely follows a plausible vendor/product naming convention.

The available project exports have incomplete generating-view, filter, application-family, tenant, and timeframe provenance. They may motivate a discovery question, not an executable dataset assertion.

## Missing-data escalation

When an expected dataset is absent, hand off this evidence rather than inventing a replacement:

- expected telemetry and generating system;
- documented supported ingestion route;
- agent/collector/integration and health state;
- authentication/transport observations;
- parser/mapping and dataset-creation evidence;
- product/version/license;
- tenant identity and RBAC/SBAC scope;
- source event time versus insert time;
- retention and the last known good event;
- exact query, compiler message, and timeframe.

See [fields-and-schema.md](fields-and-schema.md) for field proof, [troubleshooting.md](troubleshooting.md) for zero-result diagnosis, and [official-sources.md](official-sources.md) for source traceability.
