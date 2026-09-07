# Tenant Validation Record

Use only for evidence actually collected from an authorized environment.

## Context

- Product/deployment/version/build:
- License/add-on:
- Tenant/environment alias:
- UTC date/time:
- Reviewer/operator:
- Change approval:
- Identity role:
- SBAC/dataset/object scope:

## Artifact integrity

- Architecture/configuration/parser/mapping/query/API artifact:
- Version:
- Cryptographic hash:
- Sanitized storage location:
- Secret scan:

## Expected path

`data → source → collector / agent / integration → transport → ingestion → parsing / mapping → dataset / object → query visibility`

## Controlled fixture

- Sanitized fixture/hash:
- Unique correlation marker:
- Source generation condition:
- Source time/timezone:
- Expected raw and normalized values:
- Cleanup:

## Evidence by layer

| Layer | Observation | Identity/time | Evidence hash/location | Status |
|---|---|---|---|---|
| Source |  |  |  | `NOT RUN` |
| Export/fetch |  |  |  | `NOT RUN` |
| Component |  |  |  | `NOT RUN` |
| Transport |  |  |  | `NOT RUN` |
| Ingestion |  |  |  | `NOT RUN` |
| Parsing |  |  |  | `NOT RUN` |
| Mapping |  |  |  | `NOT RUN` |
| Dataset/object |  |  |  | `NOT RUN` |
| Query/consumer |  |  |  | `NOT RUN` |

## C — Product validation or compilation

- Named editor/API/import surface:
- Exact artifact hash:
- Result:
- Sanitized error:
- Status: `PASS / FAIL / NOT RUN / N/A` — rationale required

## E — End-to-end execution

- Bounded start/end:
- Identity/scope:
- Result/correlation marker:
- Source-to-observe delay:
- Count/truncation:
- Duplicates/gaps:
- Resource/capacity observation:
- Status: `PASS / FAIL / NOT RUN / N/A` — rationale required

## Negative and recovery checks

| Fixture | Observation | Status |
|---|---|---|
| Malformed |  | `NOT RUN` |
| Duplicate/replay |  | `NOT RUN` |
| Delayed |  | `NOT RUN` |
| Null/optional |  | `NOT RUN` |
| Unauthorized identity |  | `NOT RUN` |
| Component outage/recovery |  | `NOT RUN` |

## Change and rollback

- Before state:
- Authorized change:
- Post-change state:
- Rollback trigger:
- Rollback performed/result:
- Audit evidence:

## Classification

- Canonical status:
- Qualifiers:
- Operational level:
- Scope of claim:
- Limitations:
- Reviewer sign-off:

Do not promote a documentation or configuration observation to C/E.
