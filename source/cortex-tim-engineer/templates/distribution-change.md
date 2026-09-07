# Indicator distribution and control change

## Change summary

- Objective: `{{VALUE}}`
- Cortex source/product/version: `{{VALUE}}`
- Export/service/integration version: `{{VALUE}}`
- Consumer and environment: `{{VALUE}}`
- Requested action: `{{DISTRIBUTE_ONLY_OR_SECURITY_CONTROL_CHANGE}}`
- Evidence label: `{{CANONICAL_CLASS_PROVENANCE_TENANT}}`

## Scope

| Boundary | Exact value |
|---|---|
| Indicator selection/query | `{{SANITIZED_EXPRESSION_OR_REFERENCE}}` |
| Types/tags/source/age | `{{VALUE}}` |
| Marking/privacy constraints | `{{VALUE}}` |
| Expected count and maximum | `{{ESTIMATE_AND_STOP_LIMIT}}` |
| Refresh cadence | `{{VALUE}}` |
| Consumer/device/policy scope | `{{VALUE}}` |
| Time window | `{{START_END_UTC}}` |

## Risk gates

- Protected/internal/allowlisted values checked: `{{METHOD_RESULT}}`
- False-positive/collateral-impact review: `{{ARTIFACT}}`
- Data-disclosure review: `{{ARTIFACT}}`
- Authentication/TLS/exposure review: `{{ARTIFACT}}`
- Consumer confinement, request overrides, and exported-field minimization: `{{NEGATIVE_ACCESS_TEST_AND_SERIALIZED_OUTPUT_REVIEW}}`
- Availability and stale-output behavior: `{{VALUE}}`
- Consumer capacity and invalid-entry behavior: `{{VALUE_OR_UNVERIFIED}}`

## Approval separation

| Gate | Approver/reference | Status |
|---|---|---|
| Cortex selection/export/service change | `{{VALUE}}` | `{{PENDING_APPROVED_REJECTED}}` |
| Consumer retrieval/configuration | `{{VALUE}}` | `{{PENDING_APPROVED_REJECTED}}` |
| Security policy attachment/commit/enforcement | `{{VALUE}}` | `{{PENDING_APPROVED_REJECTED_NOT_REQUESTED}}` |

Do not proceed past a gate marked `PENDING`, and do not infer that an upstream approval authorizes a downstream control.

## Before state and rollback

- Before-state artifact/hash: `{{VALUE}}`
- Known-good selection/configuration: `{{VALUE}}`
- Rollback owner and trigger: `{{VALUE}}`
- Rollback steps reviewed by operator: `{{YES_NO}}`
- Recovery if service unavailable: `{{VALUE}}`
- Removal/deactivation propagation plan: `{{VALUE}}`

## Staged plan

1. Generate or review a narrow sanitized preview.
2. Validate serialization and exclude invalid/protected values.
3. Serve/export to an isolated or non-enforcing consumer where possible.
4. Confirm authorized consumer fetch and freshness.
5. Stop and obtain separate control approval if enforcement is requested.
6. Apply a bounded canary policy with stop criteria.
7. Read back Cortex, consumer, policy, and observed behavior separately.
8. Record result and retain rollback readiness.

## Verification ledger

| Stage | Expected | Observed evidence | Status |
|---|---|---|---|
| Cortex selection | `{{VALUE}}` | `{{NOT_RUN_OR_ARTIFACT}}` | `{{STATUS}}` |
| Served/exported output | `{{VALUE}}` | `{{NOT_RUN_OR_ARTIFACT}}` | `{{STATUS}}` |
| Consumer fetch/parse | `{{VALUE}}` | `{{NOT_RUN_OR_ARTIFACT}}` | `{{STATUS}}` |
| Policy attachment/commit | `{{VALUE}}` | `{{NOT_RUN_OR_ARTIFACT}}` | `{{STATUS}}` |
| Observed control behavior | `{{VALUE}}` | `{{NOT_RUN_OR_ARTIFACT}}` | `{{STATUS}}` |
| Rollback/readback | `{{VALUE}}` | `{{NOT_RUN_OR_ARTIFACT}}` | `{{STATUS}}` |

## Final status and limitations

| Level | Result | Rationale |
|---|---|---|
| S | `{{PASS/FAIL/NOT RUN/N/A}}` | `{{INDEPENDENT_RESPONSE_EVIDENCE_OR_REASON_NOT_RUN}}` |
| D | `{{PASS/FAIL/NOT RUN/N/A}}` | `{{EXACT_OFFICIAL_SOURCES_AND_REVIEW_DATE_OR_REASON_NOT_RUN}}` |
| C | `{{PASS/FAIL/NOT RUN/N/A}}` | `{{NAMED_CONFIGURATION_ACCEPTANCE_OR_REASON_NOT_RUN}}` |
| E | `{{PASS/FAIL/NOT RUN/N/A}}` | `{{OBSERVED_STAGE_READBACK_OR_REASON_NOT_RUN}}` |

- Decision: `{{PLAN_ONLY_APPROVED_COMPLETED_ROLLED_BACK_FAILED}}`
- Tenant execution: `{{NOT_RUN_OR_EXACT_SCOPE}}`
- Downstream enforcement: `{{NOT_RUN_OR_EXACT_SCOPE}}`
- Performance/capacity: `{{NOT_MEASURED_OR_EVIDENCE}}`
- Residual risks and owners: `{{LIST}}`
