# Cortex Security Engineering Intake

Replace every `{{PLACEHOLDER}}`. Use `UNKNOWN` when evidence is absent. This intake is a read-only design record and authorizes no tenant action.

## Request

| Field | Value |
|---|---|
| Intake ID/date | `{{ID}}` / `{{YYYY-MM-DD}}` |
| Requester/consumer | `{{SAFE ROLE OR TEAM}}` |
| Security objective | `{{OUTCOME}}` |
| Decision required | `{{CHOICE AND DECISION OWNER}}` |
| Success | `{{OBSERVABLE CONDITION}}` |
| Unacceptable outcomes | `{{FALSE BLOCK / MISS / DATA EXPOSURE / OUTAGE / OTHER}}` |
| Priority/deadline source | `{{OWNER/POLICY / UNKNOWN}}` |
| Non-goals | `{{EXCLUSIONS}}` |

## Product and surface

| Field | Value |
|---|---|
| Product | `{{CORTEX XSIAM / XDR / XSOAR / CORTEX CLOUD / OTHER / UNKNOWN}}` |
| Release/build | `{{VALUE / UNKNOWN}}` |
| License/edition/rollout | `{{OBSERVED / REQUIRES VALIDATION}}` |
| Surface/object type | `{{QUERY CENTER / RULE TYPE / CASES-ISSUES / GRAPH SEARCH / PLAYBOOK / TIM / DATA SOURCES / API / RESPONSE / OTHER}}` |
| Environment | `{{DESIGN / DEVELOPMENT / NON-PRODUCTION / PRODUCTION}}` |
| Intended operation | `{{READ / DESIGN / VALIDATE / WRITE / RESPOND}}` |
| Identity | `{{SAFE ALIAS / UNKNOWN}}` |
| RBAC/SBAC/object/data scope | `{{OBSERVED / UNKNOWN}}` |
| Documentation review date | `{{YYYY-MM-DD / NOT REVIEWED}}` |

If the product or surface changes mechanics or safety and remains unknown, ask one concise question or keep all outputs conceptual.

## Domain classification

- Primary domain: `{{XQL / DETECTION / HUNTING / PLAYBOOK / TIM / PLATFORM / MULTI-DOMAIN}}`
- Secondary domains: `{{LIST / NONE}}`
- Optional sibling handoffs: `{{SKILL NAMES / NONE}}`
- Standalone fallback required: `YES`

## Requirement and scope

- Protected assets/data/process: `{{DESCRIPTION}}`
- Entities and trust boundaries: `{{DESCRIPTION}}`
- Timeframe/timezone: `{{VALUE / UNKNOWN}}`
- Geographic/regulatory/privacy constraints: `{{DESCRIPTION / UNKNOWN}}`
- Operational SLO/volume/capacity inputs: `{{OWNER-APPROVED VALUES / UNKNOWN}}`
- Existing controls and evidence: `{{LIST WITH CLASS}}`

## Threat and risk frame

| Item | Value |
|---|---|
| Behavior/preconditions | `{{DESCRIPTION}}` |
| Plausible actor paths | `{{DESCRIPTION; DO NOT ASSERT ATTRIBUTION}}` |
| Impact | `{{CONFIDENTIALITY / INTEGRITY / AVAILABILITY / OPERATIONS / OTHER}}` |
| Benign alternatives | `{{FALSE-POSITIVE SCENARIOS}}` |
| Evasion/coverage gaps | `{{FALSE-NEGATIVE SCENARIOS}}` |
| Control abuse risk | `{{MISUSE / OVERREACH / DATA RISK}}` |
| Risk owner | `{{ROLE / UNKNOWN}}` |

## Telemetry readiness

| Observable | Source/product | Schema/grain | Coverage/freshness/retention | Identity visibility | Evidence class | Gap owner |
|---|---|---|---|---|---|---|
| `{{OBSERVABLE}}` | `{{SOURCE / UNKNOWN}}` | `{{VALUE / UNKNOWN}}` | `{{VALUE / UNKNOWN}}` | `{{VALUE / UNKNOWN}}` | `{{CLASS / QUALIFIERS}}` | `{{ROLE}}` |

Do not infer datasets, fields, parser mappings, population, or visibility from a feature name.

For XSIAM data-access work, record raw-dataset versus XDM query model, effective
SBAC/Datasets Rows filters, and no-filter policy. Preserve the
[documented XDM scope boundary](../references/product-surface-map.md#permission-and-entitlement-chain)
before routing an empty result to parser/mapping repair; no access expansion is
authorized by the intake.

## Authorization and data handling

- Explicitly requested state change: `{{NONE / EXACT OPERATION}}`
- Organizational approval/policy: `{{REFERENCE / NOT PROVIDED}}`
- Least-scope target and blast radius: `{{VALUE / NOT DEFINED}}`
- Secrets/credentials: `{{SECRET REFERENCE ONLY / NONE}}`
- Sensitive-data minimization: `{{FIELDS/SAMPLES/REDACTION}}`
- External transfer/retention: `{{DESTINATION, OWNER, RETENTION / NONE}}`
- Rollback/recovery/manual path: `{{PLAN / NOT DEFINED}}`
- Post-action verification/audit: `{{PLAN / NOT DEFINED}}`

If any required action gate is absent, keep the work read-only and record `HOLD`.

## Evidence ledger

| ID | Claim | Source/observation | Class/qualifiers | Scope limit | Next check |
|---|---|---|---|---|---|
| `EV-001` | `{{CLAIM}}` | `{{LINK OR RECORD}}` | `{{CLASS / QUALIFIERS}}` | `{{LIMIT}}` | `{{CHECK}}` |

## Initial route and decision

- Decision: `{{PROCEED TO GATE / REVISE / HOLD / OUT OF SCOPE}}`
- Rationale: `{{RATIONALE}}`
- First work package/owner: `{{ID / ROLE}}`
- Material unknowns: `{{LIST}}`
- Explicit non-claims: `{{NO TENANT STATE / COMPILE / EXECUTION / DEPLOYMENT / EFFICACY / AUTHORIZATION, AS APPLICABLE}}`
