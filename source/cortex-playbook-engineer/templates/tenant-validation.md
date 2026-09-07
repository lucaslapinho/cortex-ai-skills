# Playbook Tenant Validation Record

**Artifact classification under evaluation:** `{{CONCEPTUAL | CONFIGURATION GUIDANCE | VERIFIED IMPORTABLE ARTIFACT}}`  
**Initial rule:** begin below `VERIFIED IMPORTABLE ARTIFACT`; promote only after every required result is retained.  
**Safety:** importing or executing content requires separate authorization and an isolated target.

## 1. Validation identity

- Record ID/reviewer/date UTC: `{{VALUES}}`
- Product/deployment/release/build: `{{VALUES}}`
- Sanitized tenant/environment alias: `{{VALUE}}`
- Artifact name/version/path/hash: `{{VALUES}}`
- Source/export schema and provenance: `{{VALUES}}`
- Change/test authorization: `{{REFERENCE}}`
- Identity role, object/data scope, and integration-command permissions: `{{VALUES}}`

## 2. Dependency inventory

| Dependency | Name/version/revision | Required/optional | Installed/readback | Permission | Test status |
|---|---|---|---|---|---|
| Pack | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` |
| Script/command | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` |
| Integration/instance | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` |
| Sub-playbook | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` |
| Credential/engine/network | `{{REFERENCE ONLY}}` | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` |

No secret values belong in this record.

## 3. Gate S — static and behavioral review

- Required lifecycle stages and safe omissions: `{{RESULT}}`
- Input/output/context type and cardinality: `{{RESULT}}`
- Command/argument/output evidence: `{{RESULT}}`
- Unreachable paths, loops, collisions, and concurrency: `{{RESULT}}`
- Error, retry, timeout, idempotency, and partial failure: `{{RESULT}}`
- Approval/action/recovery/readback: `{{RESULT}}`
- Secrets, hostile content, data minimization: `{{RESULT}}`
- Authored/independent behavioral cases: `{{RESULT}}`

**S result:** `{{PASS/FAIL/NOT RUN/N/A - RATIONALE}}`  
**Evidence references:** `{{VALUES}}`

## 4. Gate D — official documentation

| Material claim | Exact official source | Product/release match | Current/deprecated | Result/limitation |
|---|---|---|---|---|
| `{{CLAIM}}` | `{{URL}}` | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` |

**D result:** `{{PASS/FAIL/NOT RUN/N/A - RATIONALE}}`  
**Documentation review date:** `{{DATE}}`

## 5. Gate C1 — validator or SDK

- Tool/version/OS/runtime: `{{VALUES}}`
- Exact command and configuration: `{{VALUES}}`
- Exit/result and sanitized output location/hash: `{{VALUES}}`
- Warnings/deprecations/dependency graph: `{{VALUES}}`
- Corrections and artifact hash after correction: `{{VALUES}}`

**C1 result:** `{{PASS/FAIL/NOT RUN/N/A - RATIONALE}}`

## 6. Gate C2 — controlled import

- Exact target/import method and identity: `{{VALUES}}`
- Pre-import backup/recovery: `{{VALUES}}`
- Name/ID collision handling: `{{VALUES}}`
- Import result and object readback: `{{VALUES}}`
- Inputs/outputs/tasks/edges/dependencies/settings preserved: `{{VALUES}}`
- Protected actions remain disabled/stubbed: `{{VALUES}}`
- Import log/evidence hash: `{{VALUES}}`

**C2 result:** `{{PASS/FAIL/NOT RUN/N/A - RATIONALE}}`

`C = PASS` requires the declared C scope to be explicit. Import acceptance does not prove execution.

## 7. Gate E1 — debugger or controlled simulation

- Fixture: `{{MOCK OR SANITIZED TEST OBJECT}}`
- Identity/permissions: `{{VALUES}}`
- Protected tasks skipped/stubbed and parallel safety verified: `{{VALUES}}`
- Breakpoints/overrides and known debugger limits: `{{VALUES}}`
- Context/output/decision/error observations: `{{VALUES}}`
- Any real platform/external effects and readback: `{{VALUES}}`
- Evidence location/hash: `{{VALUES}}`

**E1 result:** `{{PASS/FAIL/NOT RUN/N/A - RATIONALE}}`

## 8. Gate E2 — bounded reversible execution

Execute only under separate authorization.

| Case | Expected | Observed | Side effect/readback | Recovery | Result |
|---|---|---|---|---|---|
| Valid | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |
| Empty/null/wrong type | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |
| Error/timeout/retry | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |
| Duplicate/replay | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |
| Loop bound/partial | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |
| Approval reject/expire | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |
| Negative permission | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |
| Notification failure | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |
| Authorized canary action | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |

**E2 result:** `{{PASS/FAIL/NOT RUN/N/A - RATIONALE}}`

## 9. Evidence and claim decision

- S result: `{{PASS/FAIL/NOT RUN/N/A - RATIONALE}}`
- D result: `{{PASS/FAIL/NOT RUN/N/A - RATIONALE}}`
- C result: `{{PASS/FAIL/NOT RUN/N/A - RATIONALE}}`
- E result: `{{PASS/FAIL/NOT RUN/N/A - RATIONALE}}`
- Exact behavior established: `{{CLAIM}}`
- Behavior not established: `{{LIMITATIONS}}`
- Artifact classification now supported: `{{CLASS}}`
- Unresolved severity counts: `{{COUNTS}}`
- Independent reviewer decision: `{{REFERENCE}}`
- Production rollout decision: `{{OUT OF SCOPE / BLOCKED / SEPARATELY AUTHORIZED}}`

Never reuse a target-specific result as universal support for another product, release, tenant, identity, or dependency set.
