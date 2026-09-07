# Ingestion, Parsing, Mapping, and Datasets

Use this reference for inbound data design, schema provenance, normalization, retention, and query-visibility troubleshooting.

## Contents

- Ingestion contract
- Supported route before configuration
- Raw dataset naming
- Parsing and mapping boundary
- Dataset and schema evidence
- Metrics and freshness
- Retention and availability
- Error and health evidence
- Safe validation sequence

## Ingestion contract

Define:

| Item | Required evidence |
|---|---|
| Expected event | Sanitized sample, generation condition, source owner, source time |
| Collection route | Current product-specific official source and tenant entitlement |
| Authentication | Credential type/custodian and least privilege; no secret value |
| Transport | Documented protocol/security model for the target route |
| Source identity | Vendor, product, device/resource, and stable correlation marker |
| Volume | Observed average/peak, size distribution, burst, loss tolerance |
| Ingestion | Receipt response, metric, or health surface |
| Parsing | Rule/content version, expected fields, malformed behavior |
| Mapping | Data Model Rule/content version and normalized target |
| Dataset/object | Literal tenant-observed or officially documented name |
| Visibility | Identity, RBAC/SBAC, retention, timeframe, exact bounded query |

## Supported route before configuration

Choose from the target product’s current catalog. A route may be:

- Cortex XDR agent telemetry;
- vendor-specific data source or connector;
- Broker VM applet;
- XDR Collector;
- custom HTTP Log Collector;
- cloud-provider integration;
- XSIAM system event-collection integration;
- legacy alert-ingestion compatibility surface;
- XSOAR integration fetch into an XSOAR object flow.

These routes have different payloads, parsing, licenses, destinations, and failure modes. Do not invent a generic ingestion endpoint.

Source: [Vendor-specific data sources and connectors](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/cortex-xsiam-data-sources/vendor-specific-data-sources-and-connectors.md).

## Raw dataset naming

Current XSIAM documentation describes `<vendor>_<product>_raw` naming for several generic ingestion routes and documents route-specific defaults in some cases. This is a documented pattern, not proof of a literal tenant dataset.

Rules:

- do not derive the name from a filename or integration display label;
- preserve the exact vendor/product identity used by the selected route;
- check tenant dataset inventory/autocomplete after data arrives;
- record indexing/creation delay rather than assuming immediate visibility;
- distinguish dataset from preset/view;
- distinguish raw dataset from normalized data-model fields.

The HTTP Log Collector page documents Raw, JSON, CEF, and LEEF input and automatic raw-dataset creation for that XSIAM surface: [Set up an HTTP Log Collector](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Set-up-an-HTTP-log-collector-to-receive-logs?contentId=XAfILj87fu6SWS8m7EbtYw).

XDR Collector dataset behavior is separately documented: [XDR Collector datasets](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/XDR-Collector-datasets).

## Parsing and mapping boundary

| Stage | Purpose | Required proof |
|---|---|---|
| Raw ingestion | Store/represent accepted source data | Sanitized raw row and source marker |
| Parsing Rule | Extract/transform source representation under XQLp-specific grammar | Rule version, fixture result, error evidence |
| Data Model Rule | Map eligible data to XDM fields/model | Rule version, raw input, normalized result |
| Enrichment | Add supported contextual data | Enrichment source, join/key semantics, freshness |
| Query | Retrieve raw or normalized data under identity scope | Exact dataset/model, fields, timeframe, result |

Parsing Rules and Data Model Rules have separate editors, syntax, permissions, and error paths. Ordinary Query Center XQL is not an importable parsing or mapping rule.

Current XSIAM guidance says editing a default Data Model Rule stops Marketplace updates for that rule. Treat this as a configuration-ownership decision with an export, change record, and rollback plan.

Sources: [Parsing rules](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/data-management/parsing-rules.md), [Parsing Rules file structure and syntax](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Parsing-Rules-file-structure-and-syntax), and [Create Data Model Rules](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Create-Data-Model-Rules).

Never invent a parsing stage, rule section, field, or mapping constant. Use a conceptual placeholder if the current editor/reference was not reviewed.

## Dataset and schema evidence

| Evidence | Permitted claim |
|---|---|
| Name in user prompt/file | Candidate name only; `UNVERIFIED` |
| Current official route page | Naming behavior documented; tenant existence unknown |
| Tenant inventory/autocomplete | Dataset observed under recorded identity/time |
| Sanitized sample and schema | Fields/types/population observed for that sample |
| Bounded query result | Record visible within identity/timeframe |

Record:

- literal dataset/preset/model name;
- product, version, integration/collector/parser;
- field names, types, null behavior, and source;
- first/last observed timestamps and insert/source time;
- access identity and dataset-row scope;
- retention tier and query window;
- record count only for the bounded evidence;
- schema and query hashes.

Do not infer a field from semantic similarity or normalize an unknown name into a plausible one.

Raw visibility and XDM visibility can also differ because of the target identity's
**Datasets Rows** scope. Before interpreting empty XDM results as missing
normalization, apply the documented XSIAM
[raw-dataset versus XDM access check](api-auth-and-access.md#xsiam-raw-dataset-scope-versus-xdm-visibility).
Do not broaden access to prove mapping correctness.

## Metrics and freshness

Current XSIAM documentation identifies `metrics_source` and `metrics_view` for ingestion-health metrics. It explains that the dataset and preset do not represent zero-volume intervals identically, and recommends the preset for disruption investigation because it simulates completion of zero values at query time. Analytics prerequisites apply.

Source: [Overview of data ingestion metrics](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Overview-of-data-ingestion-metrics).

Use the documented metric schema only after rechecking the page and target tenant. Do not invent metric fields. A zero or missing metric can reflect prerequisite, scope, source identity, query, or collection state; inspect the full context.

Freshness analysis requires source event time, insert/ingestion time, clock quality, timezone, fallback semantics, aggregation, and the target percentile/metric. Source: [Measuring data freshness](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Measuring-data-freshness).

Do not attribute all delay to network transport.

## Retention and availability

Retention can vary by product, data class, license, storage tier, and tenant configuration. Record:

- data class and dataset;
- hot/archived/cold tier where applicable;
- entitlement and configured retention;
- event time and insertion time;
- requested query window;
- late-arrival behavior;
- deletion/legal/privacy requirements.

No universal Cortex retention period is safe. A record outside the visible window can be expired, delayed, in another tier, or inaccessible.

Source: [Data retention — XSIAM 3.x](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Data-retention).

## Error and health evidence

Current XSIAM documentation describes `parsing_rules_errors` as containing Parsing Rules and Data Model Rules errors. Some fields are rule-type-specific. Use the current page and tenant schema rather than memorizing fields.

Source: [Troubleshooting Data Model Rules](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Troubleshooting-Data-Model-Rules).

Other evidence can include:

- source export errors;
- HTTP collector response codes from the current collector page;
- collector/integration audit logs;
- tenant ingestion-health issues;
- parser/mapping editor diagnostics;
- minimal raw and normalized queries;
- access-denied responses.

Sanitize payloads and identifiers.

## Safe validation sequence

1. Select a non-production tenant or authorized canary source.
2. Save current configuration/export and record owners.
3. Create one sanitized positive fixture with a unique marker and source time.
4. Prove source generation.
5. Prove collector/integration input and send behavior.
6. Prove tenant ingestion receipt or health evidence.
7. Find the literal raw dataset/object.
8. Validate parsing with positive, malformed, duplicate, null, delayed, and negative fixtures.
9. Validate mapping separately.
10. Query raw and normalized views under the intended identity and timeframe.
11. Measure bounded delay and loss using correlated markers.
12. Verify rollback/cleanup and audit evidence.

Do not call the path end-to-end verified unless all material layers have correlated evidence.
