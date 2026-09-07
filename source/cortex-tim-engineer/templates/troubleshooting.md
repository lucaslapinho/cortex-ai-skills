# TIM troubleshooting worksheet

## Symptom and expected behavior

- Symptom: `{{ONE_OBSERVABLE_STATEMENT}}`
- Expected behavior: `{{VALUE_AND_SOURCE}}`
- First observed / last known good UTC: `{{VALUE}}`
- Scope: `{{SOURCE_RUN_INDICATOR_SAMPLE_DESTINATION}}`
- Operational impact: `{{VALUE}}`

## Environment and evidence status

| Item | Value/evidence |
|---|---|
| Product/deployment/version/license | `{{VALUE_OR_UNKNOWN}}` |
| Integration/content version | `{{VALUE_OR_UNKNOWN}}` |
| Engine/hosting | `{{VALUE_OR_UNKNOWN}}` |
| Effective permissions | `{{VALUE_OR_UNKNOWN}}` |
| Recent changes | `{{VALUE_OR_NONE_KNOWN}}` |
| Evidence label | `{{CANONICAL_CLASS_PROVENANCE_TENANT}}` |
| Tenant operation status | `{{NOT_RUN_OR_RETAINED_EVIDENCE}}` |

## Chain localization

For each stage, describe whether an observation is present, failure evidence is
present, or evidence is unavailable. These are checklist outcomes, not evidence
statuses. Classify every material conclusion separately with one canonical status
and applicable qualifiers.

| Stage | Checklist outcome | Sanitized evidence and canonical classification |
|---|---|---|
| Source contains expected object | `{{STATUS}}` | `{{ARTIFACT}}` |
| Transport/authentication succeeds | `{{STATUS}}` | `{{ARTIFACT}}` |
| Page/checkpoint includes object | `{{STATUS}}` | `{{ARTIFACT}}` |
| Mapping/type validation accepts object | `{{STATUS}}` | `{{ARTIFACT}}` |
| Managed indicator readback | `{{STATUS}}` | `{{ARTIFACT}}` |
| Enrichment/relationship processing | `{{STATUS}}` | `{{ARTIFACT}}` |
| Lifecycle state/expiration | `{{STATUS}}` | `{{ARTIFACT}}` |
| Export/service output | `{{STATUS}}` | `{{ARTIFACT}}` |
| Consumer fetch/parse | `{{STATUS}}` | `{{ARTIFACT}}` |
| Downstream policy/control | `{{STATUS}}` | `{{ARTIFACT}}` |

## Competing hypotheses

| ID | Hypothesis | Supporting observation | Refuting observation | Least-invasive next check | Status |
|---|---|---|---|---|---|
| H1 | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` | `{{READ_ONLY_CHECK}}` | `{{OPEN_SUPPORTED_REFUTED}}` |
| H2 | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` | `{{READ_ONLY_CHECK}}` | `{{OPEN_SUPPORTED_REFUTED}}` |
| H3 | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` | `{{READ_ONLY_CHECK}}` | `{{OPEN_SUPPORTED_REFUTED}}` |

## Timeline

| UTC time | Source or stage | Observed event | Evidence/limitations |
|---|---|---|---|
| `{{UTC}}` | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` |

Keep source-reported time, fetch time, processing time, and observation time separate.

## Proposed mutation, if required

- Exact change and target: `{{VALUE_OR_NONE}}`
- Why read-only evidence is insufficient: `{{VALUE}}`
- Approval/reference: `{{REQUIRED}}`
- Bounded scope/volume/time: `{{VALUE}}`
- Before state: `{{ARTIFACT_HASH}}`
- Risk/stop criteria: `{{VALUE}}`
- Rollback: `{{VALUE}}`
- Cortex and consumer readback: `{{VALUE}}`

Do not reset a checkpoint, delete indicators, weaken TLS, bypass exclusions, widen an export, or alter a control without this section completed.

## Conclusion

- Most supported cause: `{{CANONICAL_CLASS_AND_EXPLANATION}}`
- Ruled-out hypotheses: `{{LIST_WITH_EVIDENCE}}`
- Remaining unknowns: `{{LIST}}`
- Safest next action: `{{VALUE}}`
- Tenant/configuration/execution status: `{{EXPLICIT_NOT_RUN_OR_EVIDENCE}}`
