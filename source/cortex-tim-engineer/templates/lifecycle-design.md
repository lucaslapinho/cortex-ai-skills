# Indicator lifecycle design

## Objective and scope

- Business/security objective: `{{VALUE}}`
- Indicator populations/types: `{{VALUE}}`
- Sources: `{{VALUE}}`
- Cortex product/version/license: `{{VALUE_OR_UNKNOWN}}`
- Consumers: `{{VALUE}}`
- Evidence label: `{{CANONICAL_CLASS}} / {{PROVENANCE}} / {{TENANT_QUALIFIER}}`

## Definitions

Define each term in this policy without assuming native Cortex states:

| Term | Policy meaning | Native product mapping/evidence |
|---|---|---|
| Observed | `{{VALUE}}` | `{{VALUE_OR_UNVERIFIED}}` |
| Active/current | `{{VALUE}}` | `{{VALUE_OR_UNVERIFIED}}` |
| Expired | `{{VALUE}}` | `{{VALUE_OR_UNVERIFIED}}` |
| Reactivated | `{{VALUE}}` | `{{VALUE_OR_UNVERIFIED}}` |
| Source-withdrawn | `{{VALUE}}` | `{{VALUE_OR_UNVERIFIED}}` |
| Revoked | `{{VALUE}}` | `{{VALUE_OR_UNVERIFIED}}` |
| Excluded | `{{INGESTION_ENRICHMENT_AUTOMATION_OTHER}}` | `{{VALUE_OR_UNVERIFIED}}` |
| Deleted | `{{VALUE}}` | `{{VALUE_OR_UNVERIFIED}}` |
| Quarantine/review | `{{CONCEPTUAL_POLICY_STATE}}` | `{{DO_NOT_ASSUME_NATIVE}}` |

## Transition table

| From | Trigger/evidence | To | Owner | Consumer effect | Approval | Rollback/readback |
|---|---|---|---|---|---|---|
| `{{STATE}}` | `{{SOURCE_OR_POLICY_EVENT}}` | `{{STATE}}` | `{{OWNER}}` | `{{NONE_OR_SEPARATE_ACTION}}` | `{{REFERENCE}}` | `{{METHOD}}` |
| `{{STATE}}` | `{{SOURCE_OR_POLICY_EVENT}}` | `{{STATE}}` | `{{OWNER}}` | `{{NONE_OR_SEPARATE_ACTION}}` | `{{REFERENCE}}` | `{{METHOD}}` |
| `{{STATE}}` | `{{SOURCE_OR_POLICY_EVENT}}` | `{{STATE}}` | `{{OWNER}}` | `{{NONE_OR_SEPARATE_ACTION}}` | `{{REFERENCE}}` | `{{METHOD}}` |

## Expiration policy

| Source/type | Clock and timestamp semantics | Duration/mode | Precedence evidence | Exception owner |
|---|---|---|---|---|
| `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` | `{{OFFICIAL_TENANT_OR_POLICY}}` | `{{OWNER}}` |

- Removal detectable by exact integration: `{{YES_NO_UNKNOWN_WITH_EVIDENCE}}`
- Multi-feed behavior: `{{DOCUMENTED_RULE_OR_UNVERIFIED}}`
- Manual override behavior: `{{DOCUMENTED_RULE_AND_AUDIT}}`
- Stale-but-never-expire review: `{{CADENCE_OWNER}}`

## Conflicts and repeated observations

- Source reliability scale/owner: `{{VALUE}}`
- Equal-reliability handling: `{{VALUE_AND_EVIDENCE}}`
- Source replay behavior: `{{VALUE}}`
- Genuine new observation rule: `{{VALUE}}`
- Conflicting verdict/score handling: `{{SEPARATE_FROM_EXPIRATION}}`
- Source withdrawal versus global revocation: `{{VALUE}}`

## Enrichment, relationships, and tags

- Can enrichment refresh lifecycle state: `{{POLICY_AND_EVIDENCE}}`
- Relationship validity/expiry: `{{POLICY_AND_SCHEMA_EVIDENCE}}`
- Tag governance: `{{VOCABULARY_OWNER_REVIEW}}`
- Sensitive-value exclusion: `{{POLICY}}`

## Distribution and control boundary

- Distribution eligibility: `{{FILTER_POLICY}}`
- Expiry/removal propagation: `{{MECHANISM_AND_SLA}}`
- Consumer readback: `{{METHOD}}`
- Enforcement approval: `{{SEPARATE_REFERENCE}}`
- False-positive/allowlist gate: `{{METHOD}}`

## Audit and validation

- Before/after state retained: `{{LOCATION_AND_RETENTION}}`
- Actor/automation identity: `{{SANITIZED_REFERENCE}}`
- UTC timestamps and source evidence: `{{LOCATION}}`
- Bounded transition cases: `{{CREATE_UPDATE_REPLAY_EXPIRE_REACTIVATE_WITHDRAW}}`
- Cortex readback: `{{NOT_RUN_OR_ARTIFACT}}`
- Consumer/control readback: `{{NOT_RUN_OR_ARTIFACT}}`
- Residual limitations: `{{LIST}}`
