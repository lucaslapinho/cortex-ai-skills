# Cortex Control Validation Plan

This plan separates static, documentation, compiler/editor, execution, component, integrated, safety, and operations evidence. It authorizes no live testing.

## Identity and scope

| Field | Value |
|---|---|
| Plan ID/date | `{{VAL-###}}` / `{{YYYY-MM-DD}}` |
| Control/artifact/hash | `{{CTL ID / VERSION / SHA-256}}` |
| Requirement/risk | `{{REQ/RSK IDS}}` |
| Product/release/surface | `{{EXACT VALUES}}` |
| Environment | `{{ISOLATED / DOCUMENTATION / NON-PRODUCTION / PRODUCTION}}` |
| Tester/reviewer | `{{ROLE}}` |
| Identity/scope | `{{SAFE ALIAS, RBAC/SBAC/OBJECT/DATA/COMMAND SCOPE}}` |
| Authorization | `{{TEST APPROVAL RECORD / NOT PROVIDED}}` |
| Data handling | `{{MINIMIZATION, REDACTION, RETENTION, LOCATION}}` |

No production or consequential fixture is permitted without a separate approved plan.

## Claims under test

| Claim | Evidence ceiling before test | Required level | Pass observation | Failure meaning |
|---|---|---|---|---|
| `{{CLAIM}}` | `{{CLASS/QUALIFIERS}}` | `{{S/D/C/E}}` | `{{OBJECTIVE OBSERVATION}}` | `{{BOUNDED INTERPRETATION}}` |

## Component matrix

| Component | Exact candidate | Preconditions | Tests | Evidence capture | Owner |
|---|---|---|---|---|---|
| Platform/data | `{{SOURCE/SCHEMA/ACCESS}}` | `{{LIST}}` | freshness, schema, coverage, denied scope, failure | `{{RECORD}}` | `{{ROLE}}` |
| Query/hunt | `{{ARTIFACT}}` | `{{LIST}}` | positive, benign, negative, null, boundary | `{{RECORD}}` | `{{ROLE}}` |
| Detection | `{{ARTIFACT}}` | `{{LIST}}` | target editor, signal, volume, FP/FN, exception | `{{RECORD}}` | `{{ROLE}}` |
| TIM | `{{ARTIFACT / N/A}}` | `{{LIST}}` | provenance, score/conflict, stale/expiry, consumer | `{{RECORD}}` | `{{ROLE}}` |
| Playbook/action | `{{ARTIFACT / N/A}}` | `{{LIST}}` | branch, denied, timeout, retry, partial failure, recovery | `{{RECORD}}` | `{{ROLE}}` |

## Fixture set

| ID | Type | Input/state | Expected | Prohibited effect | Cleanup/recovery |
|---|---|---|---|---|---|
| F01 | known positive | `{{CONTROLLED FIXTURE}}` | `{{OBSERVATION}}` | `{{UNSAFE EFFECT}}` | `{{PLAN}}` |
| F02 | known benign | `{{FIXTURE}}` | `{{OBSERVATION}}` | `{{EFFECT}}` | `{{PLAN}}` |
| F03 | negative | `{{FIXTURE}}` | `{{OBSERVATION}}` | `{{EFFECT}}` | `{{PLAN}}` |
| F04 | null/missing | `{{FIXTURE}}` | `{{FAIL-CLOSED/DEGRADED PATH}}` | `{{EFFECT}}` | `{{PLAN}}` |
| F05 | time boundary | `{{FIXTURE}}` | `{{OBSERVATION}}` | `{{EFFECT}}` | `{{PLAN}}` |
| F06 | denied identity | `{{FIXTURE}}` | `{{DENIAL/SAFE ERROR}}` | `{{PRIVILEGE BYPASS}}` | `{{PLAN}}` |
| F07 | duplicate/retry | `{{FIXTURE}}` | `{{IDEMPOTENT OUTCOME}}` | `{{DUPLICATE ACTION}}` | `{{PLAN}}` |
| F08 | dependency failure | `{{FIXTURE}}` | `{{TIMEOUT/FALLBACK/ESCALATION}}` | `{{SILENT SUCCESS}}` | `{{PLAN}}` |
| F09 | partial action | `{{FIXTURE}}` | `{{RECONCILIATION}}` | `{{FALSE COMPLETE}}` | `{{PLAN}}` |
| F10 | rollback/recovery | `{{FIXTURE}}` | `{{RESTORED/COMPENSATED STATE}}` | `{{UNBOUNDED CHANGE}}` | `{{PLAN}}` |

## Static and documentation status

| Level | Scope | Result | Evidence | Limit |
|---|---|---|---|---|
| `S` | `{{ISOLATED BEHAVIORAL CASES}}` | `{{PASS/FAIL/NOT RUN/N/A + RATIONALE}}` | `{{RECORD}}` | no current-doc or tenant proof |
| `D` | `{{OFFICIAL PAGES + REVIEW DATE}}` | `{{PASS/FAIL/NOT RUN/N/A + RATIONALE}}` | `{{RECORD}}` | no tenant proof |
| `C` | `{{EXACT NON-PRODUCTION EDITOR}}` | `{{PASS/FAIL/NOT RUN/N/A + RATIONALE}}` | `{{RECORD}}` | no execution/efficacy proof |
| `E` | `{{EXACT NON-PRODUCTION RUN}}` | `{{PASS/FAIL/NOT RUN/N/A + RATIONALE}}` | `{{RECORD}}` | scoped result only |

## Integrated path

- Start condition: `{{FIXTURE/STATE}}`
- Expected sequence: `{{ORDERED OBSERVATIONS}}`
- Correlation/entity/time invariants: `{{LIST}}`
- Human approval/denial point: `{{POINT AND ROLE}}`
- Expected final state: `{{STATE}}`
- Partial/failure state: `{{STATE + ESCALATION}}`
- Evidence linkage: `{{QUERY/RULE/CASE/INDICATOR/PLAYBOOK/ACTION IDS}}`
- Result: `{{PASS/FAIL/NOT RUN/N/A + RATIONALE}}`

## Readiness decision

- Required tests passed: `{{YES/NO}}`
- Blocking failures/not-run items: `{{LIST}}`
- FP/FN and residual risk: `{{SUMMARY}}`
- Operations/rollback evidence: `{{SUMMARY}}`
- Decision: `{{PROCEED TO NEXT GATE / REVISE / HOLD}}`
- Approver: `{{ROLE / PENDING}}`
- Explicit non-claims: `{{NO PRODUCTION / UNIVERSAL / EFFICACY CLAIMS}}`
