# Data Flow and Trust Boundaries

Use this reference to map ingestion or object delivery and to prevent a partial health signal from being mistaken for end-to-end evidence.

## Contents

- Canonical chain
- Layer contract
- Trust-boundary inventory
- Timestamp and identity continuity
- Raw, parsed, mapped, and visible
- Failure ownership
- Positive and negative tests
- End-to-end evidence packet

## Canonical chain

`data → source → collector / agent / integration → transport → ingestion → parsing / mapping → dataset / object → query visibility`

Some paths legitimately omit or split a layer. Do not erase it; mark it `Not applicable` with evidence. If parsing and mapping are separate, show both. If the consumer is a Case/Issue, automation, or forwarding destination rather than a query, extend the chain after the object.

## Layer contract

| Layer | Required evidence | Common failure | Next discriminating check |
|---|---|---|---|
| Data expectation | Event/object definition, success criteria, correlation marker | Expected behavior was never precisely defined | Define one controlled fixture and its source timestamp |
| Source | Source-side audit/log/record and owner | Event not generated, filtered, delayed, or malformed | Inspect source evidence under a fixed interval |
| Export/fetch | Enabled export, fetch window/cursor, source permissions | Wrong scope, cursor gap, filter, credential, or schedule | Compare source count/marker with exporter/fetch record |
| Collector/agent/integration | Assigned configuration and component health | Wrong policy, inactive process, stale instance, local read failure | Inspect assignment and input-side counter/error |
| Transport | DNS, route, proxy, TLS/certificate, clock, endpoint reachability | Name resolution, certificate, proxy, firewall, or timeout | Use a documented, bounded connectivity check |
| Ingestion | Product receipt/metric/response and timestamp | Rejection, throttling, entitlement, format, size, or backpressure | Inspect current product response and ingestion-health evidence |
| Parsing | Raw sample, rule/version, parser result/error | Format mismatch, rule error, encoding, multiline, unexpected field | Test sanitized fixture in the named editor or inspect parser errors |
| Mapping | Parsed input, mapping rule/version, normalized fields | Rule conflict/disablement, type mismatch, missing source identity | Compare raw and mapped views; inspect mapping error evidence |
| Dataset/object | Literal name, schema, record, retention | Wrong name, delayed creation, expired data, missing entitlement | Inspect tenant inventory/schema under named identity |
| Query visibility | Identity/scope, exact query, timeframe, result metadata | RBAC/SBAC, dataset access, time/filter/null/limit issue | Minimal bounded query or object lookup under same identity |

Do not fabricate counters or field names. Use whatever current product surface documents and retain a sanitized capture.

## Trust-boundary inventory

For each hop record:

- sending and receiving security principals;
- credential type and custodian;
- source and destination trust zones;
- data classification and minimum necessary fields;
- transport confidentiality and authenticity;
- certificate/key lifecycle;
- source allowlist and destination restriction;
- proxy, firewall, DNS, and egress ownership;
- queueing, buffering, replay, and duplicate behavior;
- audit evidence on both sides.

Example conceptual boundaries:

```text
[Source account]
  -- authenticated export -->
[Customer collector host]
  -- protected outbound transport -->
[Cortex tenant ingestion]
  -- tenant data management -->
[Raw dataset]
  -- parsing/mapping -->
[Normalized dataset or object]
  -- RBAC/SBAC -->
[Querying identity]
```

Status: `CONCEPTUAL / TENANT-UNVERIFIED`. It contains no port, endpoint, or credential promise.

## Timestamp and identity continuity

Preserve, where available:

- controlled event correlation marker;
- source event time and timezone;
- exporter/fetch time and cursor/window;
- collector receipt/send times;
- ingestion or insertion time;
- parser/mapping processing time;
- query observation time;
- source identity, device/resource identity, and tenant dataset/object identity.

Do not calculate “freshness” from two clocks without checking clock source, timezone, precision, fallback behavior, and which timestamp each field represents. Current XSIAM ingestion metrics include documented freshness measures, but their existence and population in a tenant remain license/configuration dependent.

Source: [Overview of data ingestion metrics](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Overview-of-data-ingestion-metrics).

## Raw, parsed, mapped, and visible

Treat these as four separate propositions:

1. **Raw received:** the tenant stored an event representation from the source.
2. **Parsed:** the parser extracted expected fields or structure.
3. **Mapped:** eligible data was normalized into the intended data-model fields.
4. **Visible:** the querying identity can retrieve it within retention and timeframe.

Possible states:

| Raw | Parsed | Mapped | Visible | Interpretation |
|---|---|---|---|---|
| No evidence | Unknown | Unknown | No | Start at source/export/transport/ingestion. |
| Yes | No | No | Raw only | Ingestion works for the fixture; inspect parser rule/error. |
| Yes | Yes | No | Raw parsed fields only | Inspect mapping eligibility/rule/error. |
| Yes | Yes | Yes | No | Inspect dataset/object selection, access, retention, and query. |
| Yes | Yes | Yes | Yes | Path observed for the controlled fixture only; coverage remains bounded. |

Never state that one row proves completeness or sustainable capacity.

## Failure ownership

| Failure class | Primary owner | Required handoff |
|---|---|---|
| Source generation/export | Source owner | Marker, source time, export policy, source errors |
| Network/TLS/proxy | Network owner | Source/destination, timestamp, sanitized error, certificate chain metadata |
| Agent/collector/Broker/Engine | Platform owner | Component/version, assignment, health, input/output evidence |
| Ingestion/license | Platform/vendor owner | Product/version/license, response/metric, affected source |
| Parsing/mapping | Data owner | Sanitized raw fixture, rule/version, error, expected schema |
| Dataset/access/query | Data/identity/query owner | Literal dataset/object, identity/scope, retention, exact query |
| Downstream consumer | Detection/automation/integration owner | Input evidence, object ID, consumer status, retry/audit record |

Ownership does not prove cause. Use evidence to route, not to assign blame.

## Positive and negative tests

For each path define:

- positive valid event;
- benign event that should still ingest;
- malformed payload;
- missing required source identity;
- duplicate/replayed marker;
- delayed/out-of-order event;
- null/optional fields;
- oversized or high-volume condition using a safe bound;
- credential failure;
- denied scope;
- parser/mapping failure;
- recovery after a bounded outage.

Do not send synthetic events into production without authorization and a safe namespace. Prefer non-production or an agreed canary source.

## End-to-end evidence packet

Retain:

| Evidence | Required context |
|---|---|
| Architecture version/hash | Product, environment, owners, date |
| Controlled fixture | Sanitized payload and unique marker |
| Source proof | Source record/time and generating identity |
| Component proof | Assignment, version, health, input/output observations |
| Transport proof | Documented check and timestamp; no secrets |
| Ingestion proof | Response/metric/health record |
| Parser/mapping proof | Rule versions, result/error, raw-to-normalized comparison |
| Dataset/object proof | Literal name, schema, retention, record ID/time |
| Query proof | Exact query/hash, identity scope, timeframe, result metadata |
| Safety proof | Approval, scope, rollback, audit, cleanup |

Create an end-to-end test record only for the recorded fixture, tenant, identity,
timeframe, and version. Classify each resulting claim with the canonical evidence
status and qualifiers; use `TENANT-EXECUTED` only when the exact bounded test and its
retained result support it.
