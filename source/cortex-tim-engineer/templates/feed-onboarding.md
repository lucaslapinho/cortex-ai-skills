# Feed onboarding assessment

## Objective

`{{WHY_THIS_SOURCE_IS_NEEDED_AND_WHO_CONSUMES_IT}}`

## Applicable product, version, license, and surface

| Item | Value | Evidence |
|---|---|---|
| Cortex product/deployment | `{{XSIAM_XSOAR_SAAS_XSOAR_ONPREM}}` | `{{ARTIFACT_OR_UNVERIFIED}}` |
| Version/build | `{{VALUE_OR_UNKNOWN}}` | `{{ARTIFACT}}` |
| License/add-on | `{{VALUE_OR_UNKNOWN}}` | `{{ARTIFACT}}` |
| Integration/content pack | `{{EXACT_NAME_AND_VERSION}}` | `{{INVENTORY_OR_UNVERIFIED}}` |
| Direction | `{{INBOUND_FEED_OR_OTHER}}` | `{{OFFICIAL_SOURCE}}` |
| Engine/hosting | `{{VALUE_OR_UNKNOWN}}` | `{{ARTIFACT}}` |
| Effective permissions | `{{VALUE_OR_UNKNOWN}}` | `{{READBACK}}` |

## Evidence status

- Overall: `{{CANONICAL_CLASS}} / {{PROVENANCE}} / {{TENANT_QUALIFIER}}`
- Official sources reviewed: `{{LINKS_AND_DATES}}`
- Tenant operations: `{{NOT_RUN_OR_RETAINED_EVIDENCE}}`
- Material unknowns: `{{LIST}}`

## Source and trust

| Dimension | Decision/evidence |
|---|---|
| Source owner and contact | `{{VALUE}}` |
| Purpose and permitted use | `{{VALUE}}` |
| Transport/protocol/version | `{{VALUE}}` |
| Authentication and rotation owner | `{{NO_SECRETS}}` |
| TLS/proxy/engine route | `{{VALUE}}` |
| Source reliability model | `{{SCALE_OWNER_REVIEW_DATE_OR_UNKNOWN}}` |
| Markings/privacy restrictions | `{{VALUE}}` |
| Expected cadence/volume/burst | `{{ESTIMATE_AND_BASIS}}` |
| Rate/cost constraints | `{{VALUE_OR_UNKNOWN}}` |
| Outage and offboarding owner | `{{VALUE}}` |

## Data contract

| Element | Source semantics | Proposed Cortex handling | Evidence/status |
|---|---|---|---|
| Native ID/revision | `{{VALUE}}` | `{{NO_INVENTED_FIELD}}` | `{{STATUS}}` |
| Indicator pattern/value | `{{VALUE}}` | `{{TYPE_CANDIDATE}}` | `{{STATUS}}` |
| Timestamps | `{{MEANING_TIMEZONE}}` | `{{HANDLING}}` | `{{STATUS}}` |
| Confidence/reputation/score | `{{SCALE_AND_OWNER}}` | `{{MAPPING_OR_UNVERIFIED}}` | `{{STATUS}}` |
| Tags/labels | `{{VALUE}}` | `{{CONTROLLED_MAPPING_OR_NONE}}` | `{{STATUS}}` |
| Markings/TLP | `{{VALUE}}` | `{{PRESERVATION_POLICY}}` | `{{STATUS}}` |
| Relationships | `{{VALUE}}` | `{{SUPPORTED_IGNORED_UNVERIFIED}}` | `{{STATUS}}` |
| Revocation/removal | `{{VALUE}}` | `{{POLICY_OR_UNVERIFIED}}` | `{{STATUS}}` |
| Pagination/checkpoint | `{{VALUE}}` | `{{RECOVERY_POLICY}}` | `{{STATUS}}` |

Representative sample artifact/hash: `{{SANITIZED_ARTIFACT_AND_HASH}}`

## Normalization, identity, and duplicate handling

- Original values retained: `{{YES_NO_PLAN}}`
- Transformations and versions: `{{LIST_WITH_FAILURE_BEHAVIOR}}`
- Identity rule: `{{CONCEPTUAL_OR_VERIFIED_RULE}}`
- Invalid/ambiguous object handling: `{{REJECT_REVIEW_RETAIN_WITH_WARNING}}`
- Multi-source conflict policy: `{{DOCUMENTED_RULE_OR_APPROVED_POLICY}}`
- Replay/idempotency policy: `{{VALUE}}`

## Lifecycle and enrichment

- Expiration owner and policy: `{{VALUE}}`
- Can source removals be observed: `{{VERIFIED_YES_NO_UNKNOWN}}`
- Reactivation trigger: `{{VALUE}}`
- Enrichment integrations/types: `{{VALUE_OR_OUT_OF_SCOPE}}`
- Cache/exclusion/privacy policy: `{{VALUE}}`
- Manual override audit: `{{VALUE}}`

## Bounded validation plan

1. `{{VERIFY_LICENSE_VERSION_PACK_PERMISSIONS}}`
2. `{{CONNECTION_TEST_WITHOUT_IMPORT_IF_SUPPORTED}}`
3. `{{SMALL_SANITIZED_SAMPLE_AND_EXPECTED_COUNTS}}`
4. `{{MAPPING_REJECTION_DUPLICATE_AND_TIMESTAMP_READBACK}}`
5. `{{UPDATE_REPLAY_REMOVAL_REVOCATION_EXPIRATION_CASES}}`
6. `{{RATE_PAGINATION_AND_CHECKPOINT_RECOVERY_WITH_LIMITS}}`
7. `{{ROLLBACK_AND_OFFBOARDING_READBACK}}`

Approval reference: `{{REQUIRED_BEFORE_STATE_CHANGE}}`

## Monitoring and acceptance

| Signal | Expected/bound | Alert/stop criterion | Owner |
|---|---|---|---|
| Fetch health | `{{VALUE}}` | `{{VALUE}}` | `{{OWNER}}` |
| Objects received/rejected | `{{VALUE}}` | `{{VALUE}}` | `{{OWNER}}` |
| Duplicate/conflict rate | `{{VALUE}}` | `{{VALUE}}` | `{{OWNER}}` |
| Freshness/checkpoint age | `{{VALUE}}` | `{{VALUE}}` | `{{OWNER}}` |
| Enrichment errors/cost | `{{VALUE}}` | `{{VALUE}}` | `{{OWNER}}` |
| Distribution effect | `{{OUT_OF_SCOPE_OR_SEPARATE_PLAN}}` | `{{VALUE}}` | `{{OWNER}}` |

## Decision and limitations

- Decision: `{{APPROVE_PILOT_REVISE_REJECT_NOT_AUTHORIZED}}`
- Conditions: `{{LIST}}`
- Rollback/offboarding: `{{METHOD_AND_OWNER}}`
- Unverified tenant behavior: `{{LIST}}`
- Production capacity/performance: `{{NOT_MEASURED_OR_EVIDENCE}}`
