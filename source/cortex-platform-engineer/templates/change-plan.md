# Cortex Platform Change Plan

Use for configuration, credential, deployment, collector, parser, mapping, integration, forwarding, or access changes.

## Change identity

- Change title/ID:
- Product/deployment/version:
- Tenant/environment alias:
- Exact component/object:
- Owner:
- Approver:
- Window:
- Production: `No / Yes`

## Objective and non-goals

- Observable desired outcome:
- Non-goals:
- Reason:
- Dependencies:

## Evidence

- Current official source:
- Current configuration/export/hash:
- Current health/data baseline:
- Tenant gaps:
- Proposed literal values verified from:

## Scope and blast radius

- Included sources/components/users/datasets:
- Excluded:
- Data/privacy impact:
- Detection/automation/downstream impact:
- Capacity/retention impact:
- Credential impact:
- Failure domains:

## Preconditions

- [ ] License/version compatibility confirmed
- [ ] Least-privilege identity confirmed
- [ ] Secrets available through approved store
- [ ] Supported backup/export retained
- [ ] Non-production/canary prepared
- [ ] Monitoring and evidence capture ready
- [ ] Rollback owner available
- [ ] Stakeholders notified

## Procedure

List exact product-documented steps only after current verification.

1. Pre-change evidence:
2. Canary or bounded first step:
3. Checkpoint:
4. Remaining bounded change:
5. Post-change check:

Do not place secret values in the procedure.

## Runtime controls

- Idempotency/duplicate behavior:
- Connect/read/overall timeout:
- Retry/backoff and retryable conditions:
- Cancellation:
- Concurrency:
- Partial failure:
- Audit/correlation ID:

## Rollback and recovery

- Rollback trigger:
- Maximum decision time:
- Supported rollback procedure:
- Backup/export:
- Data replay/duplicate implications:
- Credential recovery:
- Recovery owner:
- Verification after rollback:

If rollback is undocumented, say so and define a vendor-supported recovery escalation instead.

## Validation

| Layer | Before | Expected after | Evidence | Result |
|---|---|---|---|---|
| Source |  |  |  | `NOT RUN` |
| Component |  |  |  | `NOT RUN` |
| Transport |  |  |  | `NOT RUN` |
| Ingestion |  |  |  | `NOT RUN` |
| Parsing/mapping |  |  |  | `NOT RUN` |
| Dataset/object |  |  |  | `NOT RUN` |
| Query/consumer |  |  |  | `NOT RUN` |
| Security/access |  |  |  | `NOT RUN` |

## Closeout

- Actual start/end:
- Operator/reviewer:
- Deviations:
- Partial failures:
- Gaps/duplicates:
- Audit/evidence location:
- Residual risk:
- Follow-up:

