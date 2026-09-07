# API and Access Review

## Target contract

- Product/API family:
- Deployment/version:
- Operation:
- Read/write/command/job:
- Current official API page:
- Tenant FQDN evidence:
- Endpoint/schema evidence:
- Environment:

## Identity and authentication

- Identity alias/owner:
- API key/service identity type:
- Credential custodian/store:
- Rotation/revocation:
- Secret redaction:
- TLS/proxy boundary:

Never include the actual key, token, certificate private key, password, or client secret.

## Authorization

| Layer | Required | Observed | Evidence | Gap |
|---|---|---|---|---|
| Product/license |  |  |  |  |
| Component RBAC |  |  |  |  |
| Dataset access |  |  |  |  |
| SBAC scope |  |  |  |  |
| Object sharing |  |  |  |  |
| Integration command |  |  |  |  |
| External system |  |  |  |  |

## Data contract

- Query model: raw dataset / XDM / other / not applicable:
- Dataset-access management enabled and effective dataset access:
- SBAC enabled, effective Datasets Rows filters, and no-filter policy:
- XSIAM XDM compatibility with that scope and current official evidence:
- Request schema/version:
- Response schema/version:
- Required fields:
- Sensitive fields:
- Result bound:
- Pagination/stream behavior:
- Retention/logging:

Use `UNVERIFIED` for every literal not supported by the current API reference.

For XSIAM XDM under row-level filtering, use the
[documented access branch](../references/api-auth-and-access.md#xsiam-raw-dataset-scope-versus-xdm-visibility).
An empty result does not authorize removing filters or broadening the identity.

## Client safety

- Timeout:
- Retry/backoff:
- Server-directed delay:
- Cancellation/terminal states:
- Concurrency:
- Idempotency/duplicate risk:
- Partial failure:
- Schema validation:
- Audit/correlation ID:
- Output minimization:

## Change gate

- State change:
- Exact target:
- Approval:
- Scope/exclusions:
- Before-state evidence:
- Blast radius:
- Rollback/recovery:
- Post-write readback:

## Test matrix

| Test | Expected | Status |
|---|---|---|
| Valid least-privilege identity |  | `NOT RUN` |
| Invalid credential |  | `NOT RUN` |
| Authenticated but forbidden identity |  | `NOT RUN` |
| Out-of-scope row/object |  | `NOT RUN` |
| Timeout |  | `NOT RUN` |
| Retryable response |  | `NOT RUN` |
| Ambiguous write response |  | `NOT RUN` |
| Partial result/failure |  | `NOT RUN` |
| Revoked credential |  | `NOT RUN` |

## Verdict

- Canonical evidence status:
- S result: `{{PASS | FAIL | NOT RUN | N/A}}` — `{{INDEPENDENT RESPONSE-EVALUATION RATIONALE AND RECORD}}`
- D result: `{{PASS | FAIL | NOT RUN | N/A}}` — `{{DATED OFFICIAL-DOCUMENT RATIONALE AND SOURCES, OR REASON NOT APPLICABLE/RUN}}`
- C result: `{{PASS | FAIL | NOT RUN | N/A}}` — `{{NAMED TENANT/API-SCHEMA VALIDATION RATIONALE AND RECORD, OR REASON NOT RUN}}`
- E result: `{{PASS | FAIL | NOT RUN | N/A}}` — `{{OBSERVED API EXECUTION/RESULT RATIONALE AND RECORD, OR REASON NOT RUN}}`
- Approved for design / non-production test / production:
- Conditions:
- Unresolved risks:
