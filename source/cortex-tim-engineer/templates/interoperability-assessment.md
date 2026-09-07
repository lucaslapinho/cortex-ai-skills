# Interoperability assessment

## Objective

`{{INBOUND_OR_OUTBOUND_USE_CASE}}`

## Exact boundary

| Item | Value/evidence |
|---|---|
| Cortex product/version/deployment | `{{VALUE_OR_UNKNOWN}}` |
| License/add-on | `{{VALUE_OR_UNKNOWN}}` |
| Named integration/version | `{{EXACT_NAME_AND_INSTALLED_VERSION}}` |
| Direction | `{{INBOUND_OUTBOUND_EXPORT_SERVING}}` |
| Protocol/version | `{{TAXII1_TAXII20_21_STIX_VERSION_MISP_EDL_OTHER}}` |
| Source/destination product/version | `{{VALUE}}` |
| Engine/hosting | `{{VALUE_OR_UNKNOWN}}` |
| Official reference reviewed | `{{LINK_AND_DATE}}` |
| Evidence label | `{{CANONICAL_CLASS_PROVENANCE_TENANT}}` |

## Capability comparison

| Requirement | Protocol/source capability | Named Cortex integration behavior | Tenant evidence | Gap/decision |
|---|---|---|---|---|
| Object/indicator types | `{{VALUE}}` | `{{DOCUMENTED_OR_UNVERIFIED}}` | `{{VALUE}}` | `{{VALUE}}` |
| Patterns/values | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` |
| Timestamps/revisions | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` |
| Confidence/scores | `{{VALUE}}` | `{{NO_INVENTED_MAPPING}}` | `{{VALUE}}` | `{{VALUE}}` |
| Tags/labels/markings | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` |
| Relationships | `{{VALUE}}` | `{{SUPPORTED_LIMITED_IGNORED_UNVERIFIED}}` | `{{VALUE}}` | `{{VALUE}}` |
| Revocation/removal | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` |
| Pagination/checkpoint | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` |
| Authentication/TLS | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` |

## Data-loss and transform register

| Source element | Transform/mapping | Preserved/lost/unknown | Impact | Mitigation/acceptance |
|---|---|---|---|---|
| `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` |

No row in this table is a native Cortex schema claim unless backed by exact product or tenant evidence.

## Security and deployment

- Credentials and least privilege: `{{NO_SECRET_DETAILS}}`
- Network exposure and engine route: `{{VALUE}}`
- Certificate/hostname validation: `{{VALUE}}`
- Marking/privacy propagation: `{{VALUE}}`
- Untrusted-content handling: `{{VALUE}}`
- Rate/size/denial-of-service controls: `{{VALUE}}`
- Logs and audit without secrets: `{{VALUE}}`

## Bounded validation

1. `{{VERIFY_APPLICABILITY_AND_INSTALLED_VERSION}}`
2. `{{VALIDATE_CONNECTION_WITHOUT_BROAD_IMPORT_OR_PUBLICATION}}`
3. `{{TEST_SMALL_SANITIZED_REPRESENTATIVE_SET}}`
4. `{{COMPARE_OBJECT_COUNTS_HASHES_MAPPINGS_REJECTIONS}}`
5. `{{TEST_UPDATE_REPLAY_RELATIONSHIP_REVOCATION_MARKING}}`
6. `{{TEST_PAGINATION_FAILURE_RECOVERY}}`
7. `{{READ_BACK_BOTH_SIDES}}`

## Decision

- Status: `{{FIT_FIT_WITH_GAPS_NOT_FIT_NOT_VERIFIED}}`
- Required approvals: `{{LIST}}`
- Accepted losses: `{{LIST_AND_OWNER}}`
- Rollback/offboarding: `{{VALUE}}`
- Tenant execution: `{{NOT_RUN_OR_EVIDENCE}}`
- Production capacity/performance: `{{NOT_MEASURED_OR_EVIDENCE}}`
