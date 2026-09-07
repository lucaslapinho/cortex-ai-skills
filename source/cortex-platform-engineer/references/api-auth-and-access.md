# API Authentication and Access

Use this reference for Cortex API designs, authorization reviews, and access-related troubleshooting. It does not provide a generic executable client.

## Contents

- API target contract
- Authentication boundary
- Authorization layers
- RBAC and SBAC
- Integration-command permissions
- Safe client behavior
- Migration and legacy APIs
- Access troubleshooting
- Review record

## API target contract

Before code or commands, record:

| Attribute | Required value |
|---|---|
| Product/API family | Exact XSIAM, XDR, XSOAR, or other documented family |
| Deployment/version | SaaS/On-prem and API documentation version/review date |
| Tenant endpoint | Tenant API FQDN and current endpoint path from authoritative evidence |
| Operation | Read, create, update, delete, execute command, or long-running job |
| Identity | Human/service/API identity and owner |
| Authorization | Role, component permission, dataset/object access, SBAC scope |
| Data | Minimum input/output, classification, retention, and redaction |
| Runtime controls | Timeout, retry/backoff, cancellation, concurrency, idempotency |
| Safety | Environment, approval, blast radius, rollback/recovery, audit |

If the endpoint or schema is not current and product-specific, stop at a design and verification checklist.

## Authentication boundary

Current XSIAM Platform API guidance requires:

- a tenant API FQDN;
- an API key;
- an API key ID;
- the documented authentication headers.

Status: `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED`. This does not establish a tenant value, key type, assigned role, scope, endpoint, or successful request.

Source: [Get started with Cortex XSIAM APIs](https://cortex-docs.paloaltonetworks.com/xsiam-api/get-started-with-cortex-apis.md).

Use placeholders:

```text
<CORTEX_API_FQDN>
<CORTEX_API_KEY>
<CORTEX_API_KEY_ID>
```

Do not:

- derive the API FQDN from a console URL by guesswork;
- place a key in a URL, source file, example, test, or console output;
- echo headers or full responses containing sensitive data;
- use a personal administrator identity when a bounded service identity is appropriate;
- assert that key creation proves access to an operation or dataset.

## Authorization layers

Evaluate separately:

1. authentication succeeded;
2. API family/endpoint is enabled for the product/license;
3. component-level RBAC permits the operation;
4. dataset access permits the selected dataset;
5. SBAC permits the relevant asset, endpoint, Case/Issue, or dataset rows;
6. object-level sharing permits the saved object where applicable;
7. integration-instance command permissions permit the command;
8. external system credentials permit the source-side operation.

A successful unrelated read endpoint does not prove authorization for a write, dataset, integration command, or another product API.

## RBAC and SBAC

Current XSIAM documentation states that RBAC manages component and dataset access, while SBAC refines access to relevant data/content, including documented scoping areas. Current tenant configuration determines whether SBAC is enabled and which scopes apply.

Sources: [Set up users and roles](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Set-up-users-and-roles) and [Manage user access](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Manage-user-access).

Record effective accumulated permission, not only the nominal role name. Predefined role behavior and management location can differ by product/deployment/version. Never invent a role or assume a similarly named role across products is equivalent.

### XSIAM raw-dataset scope versus XDM visibility

Current XSIAM guidance, rechecked on **2026-09-06**, documents a specific boundary:
row-level filters in **Datasets Rows** apply to raw datasets, and XDM queries are
not supported under that filtered scope. The page states that XDM returns rows
only when **All rows are accessible** is selected and no filter is defined in that
scoping area. This is `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED`,
not a claim that any particular tenant has that configuration.

When a permitted raw query returns records but an XDM query is empty, inspect the
query model, effective identity, SBAC enablement, configured row filters, and the
no-filter policy before blaming parsing or mapping. Preserve the same bounded
source marker and timeframe for comparison. Also verify dataset-access management:
the documented **No dataset has been selected** display means access to all XQL
datasets when that management feature is disabled; it is not, by itself, denial.

Do not remove filters, select **All rows are accessible**, disable SBAC, or grant a
broader role to make a query work. Keep the authorized raw-dataset path where
suitable, or have the data and identity owners design and approve a supported
least-privilege alternative. Require negative-scope tests for any proposed change.

Source: [Manage user access — XSIAM](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/onboard-cortex-xsiam/post-deployment/manage-user-roles-and-access-management/manage-user-access.md).

Use negative tests:

- authorized identity can access only the intended component/data;
- identity outside the scope cannot see or act on it;
- write/command permission is denied for read-only identities;
- API key scope matches its owner-approved purpose;
- audit logs distinguish permitted and denied attempts without exposing secrets.

## Integration-command permissions

Current XSIAM guidance documents per-integration-instance command restrictions by role, layered on broader integration access. A user without command permission is restricted across documented invocation/editing surfaces.

Source: [Configure integration permissions](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Configure-integration-permissions).

Verify:

- exact integration and instance;
- exact command;
- permitted roles;
- actual execution identity;
- playbook/work-plan behavior;
- external-system privilege;
- audit evidence.

A content pack’s command definition does not prove that the tenant identity can execute it.

## Safe client behavior

Any client design must include:

- secret retrieval from an approved store;
- request correlation ID without secret material;
- TLS verification;
- explicit connect/read/overall timeout;
- bounded retry with backoff only for documented retryable conditions;
- handling of rate limits and server-directed delay where documented;
- cancellation/terminal-state rules for asynchronous operations;
- concurrency bound;
- idempotency or duplicate-risk analysis for writes;
- response schema/version validation;
- pagination/streaming only when documented for that endpoint;
- minimized output and structured redaction;
- audit and partial-failure record;
- environment guard and approval for writes.

Do not invent response fields, error codes, rate limits, page tokens, or idempotency headers. A pseudocode client must label every unverified literal as a placeholder.

## Migration and legacy APIs

Current XSIAM API release notes document terminology/API migrations and identify legacy APIs without identified successors. They also identify old XSIAM 2.x documentation as deprecated and unmaintained.

Sources: [Notable API migrations](https://cortex-docs.paloaltonetworks.com/xsiam-api/api-release-notes.md#notable-api-migrations) and [Legacy APIs without identified successors](https://cortex-docs.paloaltonetworks.com/xsiam-api/api-release-notes#legacy-apis-without-identified-successor-apis).

Required behavior:

- preserve literal legacy identifiers where an existing contract requires them;
- use current Case/Issue terminology in new prose;
- do not assume a Case/Issue endpoint is a semantic replacement for every old Incident/Alert endpoint;
- obtain an exact current migration mapping or mark it unresolved;
- test response/request compatibility in non-production;
- keep fallback, dual-write, and replay plans safety-gated.

## Access troubleshooting

| Symptom | Plausible causes | Discriminating checks |
|---|---|---|
| Authentication failure | Wrong API FQDN, key/ID mismatch, revoked credential, clock/proxy/TLS | Verify tenant-generated values and sanitized transport/auth error |
| Forbidden | Component RBAC, dataset access, SBAC, object sharing, command restriction | Compare effective accumulated permissions and a known allowed operation |
| Empty result | Valid empty scope, wrong dataset/timeframe, SBAC rows, retention, ingestion gap | Same bounded query under approved comparison identity; inspect ingestion/raw data |
| Not found | Wrong product/API family, legacy endpoint, feature/license unavailable | Re-open current product API index and tenant UI |
| Intermittent error | rate/concurrency, service state, proxy, retry storm | Correlation IDs, bounded timeline, response class, client retry log |
| Write duplicated | retry after ambiguous response, missing idempotency, cursor replay | Request IDs, before/after object state, audit log |

Never “solve” a forbidden response by assigning broad administrator access. Identify the smallest missing permission or scope and obtain owner approval.

## Review record

Return:

- operation and data classification;
- product/deployment/version/API page;
- endpoint and schema evidence status;
- identity owner and secret custody;
- RBAC/SBAC/dataset/object/command permissions;
- request/response minimization;
- retry/timeout/cancel/concurrency/idempotency behavior;
- failure and audit handling;
- non-production test plan;
- write authorization, blast radius, rollback/recovery;
- unresolved assumptions.

Use [templates/api-access-review.md](../templates/api-access-review.md).
