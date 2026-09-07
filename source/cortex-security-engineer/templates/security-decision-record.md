# Cortex Security Decision Record

Use this for a cross-domain architecture or control choice. This document may recommend an option; only the named accountable owner can approve it.

## Record identity

| Field | Value |
|---|---|
| Decision ID | `{{DEC-###}}` |
| Title | `{{ONE DECISION}}` |
| Date/status | `{{YYYY-MM-DD}}` / `{{PROPOSED / APPROVED / REJECTED / SUPERSEDED}}` |
| Decision owner | `{{ACCOUNTABLE ROLE}}` |
| Authors/reviewers | `{{ROLES}}` |
| Product/release/surface | `{{EXACT VALUES / UNKNOWN}}` |
| Environment | `{{DESIGN / DEVELOPMENT / NON-PRODUCTION / PRODUCTION}}` |
| Related records | `{{REQ / RSK / TEL / CTL / VAL / OPS IDS}}` |

Do not mark `APPROVED` without retained owner evidence.

## Decision question

`{{WHAT MUST THE OWNER CHOOSE?}}`

### Scope

- In scope: `{{PRODUCTS, SURFACES, ASSETS, IDENTITIES, DATA, TIME}}`
- Out of scope: `{{EXCLUSIONS}}`
- Deadline and source: `{{VALUE / UNKNOWN}}`
- Revisit triggers: `{{PRODUCT/SCHEMA/LICENSE/THREAT/POLICY/OWNER CHANGE}}`

## Requirements

| ID | MUST/SHOULD/MUST NOT | Acceptance condition | Owner |
|---|---|---|---|
| `REQ-001` | `{{TESTABLE REQUIREMENT}}` | `{{OBSERVATION}}` | `{{ROLE}}` |

## Threat and risk

| ID | Behavior/failure | Asset/impact | Existing control/evidence | FP/FN or abuse risk | Risk owner |
|---|---|---|---|---|---|
| `RSK-001` | `{{DESCRIPTION}}` | `{{DESCRIPTION}}` | `{{CLASS / SOURCE}}` | `{{DESCRIPTION}}` | `{{ROLE}}` |

ATT&CK mapping, if used: `{{INTERPRETIVE MAPPING / NONE}}`. It is not occurrence, attribution, or coverage proof.

## Telemetry contract

| ID | Observable/source | Grain/time | Coverage/access/quality | Evidence | Blocking gap |
|---|---|---|---|---|---|
| `TEL-001` | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` | `{{CLASS / QUALIFIERS}}` | `{{GAP / NONE}}` |

Unknown schema identifiers remain prose placeholders; do not include them in an executable block.

## Options

Include defer/do-nothing when relevant.

| Option | Description | Benefits | Risks/drawbacks | Dependencies | Reversibility | Evidence ceiling |
|---|---|---|---|---|---|---|
| A | `{{DESCRIPTION}}` | `{{LIST}}` | `{{LIST}}` | `{{LIST}}` | `{{VALUE}}` | `{{CLASS}}` |
| B | `{{DESCRIPTION}}` | `{{LIST}}` | `{{LIST}}` | `{{LIST}}` | `{{VALUE}}` | `{{CLASS}}` |

## Recommended control architecture

| ID | Control intent | Domain owner | Input/output | Failure/recovery | Approval gate |
|---|---|---|---|---|---|
| `CTL-001` | `{{DESCRIPTION}}` | `{{XQL/DETECTION/HUNT/PLAYBOOK/TIM/PLATFORM}}` | `{{CONTRACT}}` | `{{PATH}}` | `{{GATE}}` |

### Dependency sequence

| Order | Work package | Predecessor/evidence | Deliverable | Acceptance | Owner | Approver |
|---:|---|---|---|---|---|---|
| 1 | `{{WP-01}}` | `{{INPUT}}` | `{{OUTPUT}}` | `{{PASS CONDITION}}` | `{{ROLE}}` | `{{ROLE}}` |

Optional sibling Skills: `{{LIST / NONE}}`. The record remains usable without them because the contracts and acceptance criteria are complete.

## Validation

| ID | Property | Level | Fixture | Expected/prohibited | Result | Evidence |
|---|---|---|---|---|---|---|
| `VAL-001` | `{{PROPERTY}}` | `{{S/D/C/E}}` | `{{FIXTURE}}` | `{{OBSERVATION / PROHIBITION}}` | `{{PASS/FAIL/NOT RUN/N/A + RATIONALE}}` | `{{RECORD}}` |

Keep current official documentation, tenant compilation, tenant execution, integrated efficacy, and production observation separate.

## Safety and operations

- Requested state change: `{{NONE / EXACT OPERATION}}`
- Authorization/policy: `{{EVIDENCE / NOT PROVIDED}}`
- Execution identity and scopes: `{{SAFE ALIAS / UNKNOWN}}`
- Least scope/blast radius/idempotency: `{{PLAN}}`
- Human approval/denial path: `{{PLAN}}`
- Rollback/recovery/manual path: `{{PLAN}}`
- Monitoring and evidence: `{{HEALTH + OUTCOME + AUDIT}}`
- Exception/tuning governance: `{{OWNER, SCOPE, EXPIRY, REGRESSION}}`
- Retirement: `{{TRIGGER, CLEANUP, DEPENDENCY CHECK}}`

## Decision

- Selected/recommended option: `{{OPTION}}`
- Rationale: `{{TRACE TO REQUIREMENTS, RISKS, EVIDENCE}}`
- Residual risk: `{{DESCRIPTION}}`
- Conditions before next gate: `{{LIST}}`
- Owner acceptance: `{{EVIDENCE / PENDING}}`
- Expiry/review: `{{DATE OR TRIGGER}}`
- Explicit non-claims: `{{TENANT STATE / SYNTAX / EXECUTION / DEPLOYMENT / EFFICACY / AUTHORIZATION LIMITS}}`
