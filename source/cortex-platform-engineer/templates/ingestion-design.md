# Ingestion Design

Use for a new or changed inbound data source. Keep literal tenant values and credentials out of the document.

## Intake

- Product/deployment/version:
- License/add-on:
- Environment/tenant alias:
- Source system and owner:
- Expected log/event:
- Consumer:
- Design only or authorized change:

## Evidence ledger

| Claim | Status | Qualifier | Source/date | Tenant gap |
|---|---|---|---|---|
| Collection route supported |  |  |  |  |
| Source permissions |  |  |  |  |
| Dataset/object |  |  |  |  |
| Parsing/mapping |  |  |  |  |
| Capacity/retention |  |  |  |  |

## Path

`data → source → collector / agent / integration → transport → ingestion → parsing / mapping → dataset / object → query visibility`

| Layer | Selected design | Owner | Input evidence | Output evidence | Failure/check |
|---|---|---|---|---|---|
| Data/source |  |  |  |  |  |
| Export/fetch |  |  |  |  |  |
| Collector/integration |  |  |  |  |  |
| Transport |  |  |  |  |  |
| Ingestion |  |  |  |  |  |
| Parsing |  |  |  |  |  |
| Mapping |  |  |  |  |  |
| Dataset/query |  |  |  |  |  |

## Source fixture

- Sanitized payload location/hash:
- Unique marker:
- Event time/timezone:
- Vendor/product/resource identity:
- Expected raw fields:
- Expected normalized fields:
- Sensitive-data handling:

## Collection component

- Current catalog/source page:
- Component and version:
- Profile/policy/integration version:
- Execution location:
- Supported format:
- Credential custodian:
- Network boundary:
- Source-side least privilege:
- Cortex-side least privilege:

Do not invent configuration keys. Link the current official procedure or target UI export.

## Transport and failure handling

- DNS/proxy/firewall owners:
- TLS/certificate requirements:
- Timeouts:
- Retry/backoff:
- Idempotency/duplicate behavior:
- Buffer/backpressure:
- Partial failure/dead-letter/replay:
- Audit/correlation ID:

## Parsing and mapping

- Raw dataset evidence:
- Parser/content version:
- Parser owner:
- Malformed/null/multiline behavior:
- Data Model Rule/version:
- Normalized target:
- Conflict/default-rule ownership:
- Error surface:
- Rollback/export:

## Dataset, access, and retention

- Literal dataset/preset/model:
- Schema/type evidence:
- RBAC/dataset permission:
- SBAC row scope:
- Source time versus insert time:
- Retention/storage tier:
- Minimal bounded query owner:

## Capacity

- Observed average/peak:
- Size distribution:
- Burst window:
- Source-side queue:
- Published limit source/version:
- Safety factor rationale:
- Load-test plan:
- Loss/delay acceptance:

Do not claim capacity from a published maximum alone.

## Test matrix

| Fixture | Expected source | Expected raw | Expected mapped | Expected query | Result |
|---|---|---|---|---|---|
| Positive |  |  |  |  | `NOT RUN` |
| Benign |  |  |  |  | `NOT RUN` |
| Malformed |  |  |  |  | `NOT RUN` |
| Duplicate/replay |  |  |  |  | `NOT RUN` |
| Delayed/out-of-order |  |  |  |  | `NOT RUN` |
| Null/optional |  |  |  |  | `NOT RUN` |
| Credential denied |  |  |  |  | `NOT RUN` |
| Recovery |  |  |  |  | `NOT RUN` |

## Change, rollback, and audit

- Approval:
- Current configuration/hash:
- Non-production/canary:
- Exact change:
- Blast radius:
- Rollback trigger/steps:
- Recovery owner:
- Post-change checks:
- Evidence location/retention:

