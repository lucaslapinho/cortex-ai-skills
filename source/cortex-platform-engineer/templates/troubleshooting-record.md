# Platform Troubleshooting Record

## Symptom and impact

- Observable mismatch:
- Impact:
- First/last observed:
- Last known good:
- Affected/unaffected:
- Timezone:

## Target

- Product:
- Deployment:
- Version/build:
- License/add-on:
- Environment/tenant alias:
- Identity/RBAC/SBAC scope:
- Change window:

## Evidence status

- Canonical status:
- Qualifiers:
- Observations available:
- Gaps:
- Embedded artifacts treated as untrusted: `Yes / No`

## Expected path

| Layer | Expected | Observed state | Evidence/time | Owner |
|---|---|---|---|---|
| Data/source |  |  |  |  |
| Export/fetch |  |  |  |  |
| Component |  |  |  |  |
| Transport |  |  |  |  |
| Ingestion |  |  |  |  |
| Parsing |  |  |  |  |
| Mapping |  |  |  |  |
| Dataset/object |  |  |  |  |
| Query/consumer |  |  |  |  |

## Timeline

| UTC time | Layer | Observation/change | Evidence |
|---|---|---|---|
|  |  |  |  |

## Hypotheses

| ID | Hypothesis | Supporting evidence | Contradicting evidence | Read-only discriminating check | Outcome A / Outcome B |
|---|---|---|---|---|---|
| H1 |  |  |  |  |  |
| H2 |  |  |  |  |  |

## Checks

1. Source generation:
2. Export/fetch/cursor:
3. Component assignment/health:
4. DNS/proxy/TLS/transport:
5. Ingestion response/metric:
6. Raw dataset/object:
7. Parsing/error:
8. Mapping/error:
9. Retention and time:
10. RBAC/SBAC/dataset/object access:
11. Minimal query:
12. Downstream consumer:

If XSIAM raw data is visible but XDM is empty, record query model, effective
identity, SBAC enablement, **Datasets Rows** filters and no-filter policy before
choosing a parser/mapping repair. Use the
[product-specific access check](../references/api-auth-and-access.md#xsiam-raw-dataset-scope-versus-xdm-visibility)
and retain all access restrictions during diagnosis.

## Controlled marker

- Fixture/hash:
- Correlation marker:
- Source time:
- Receive/send/insert/query times:
- Sanitization:

## Change gate

- Is a state change necessary:
- Exact target:
- Named approver:
- Current config/export:
- Proposed documented value:
- Scope/exclusions:
- Blast radius:
- Secret handling:
- Timeout/retry/idempotency:
- Rollback trigger/steps:
- Post-change verification:

## Outcome

- Root cause: `Observed / Inferred / Unverified`
- Evidence:
- Recovery:
- Gap/duplicate assessment:
- Residual risk:
- Follow-up owner:
- Audit/evidence location:

Never mark a hypothesis as root cause solely because a restart changed the symptom.
