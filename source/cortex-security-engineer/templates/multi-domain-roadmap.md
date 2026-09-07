# Multi-Domain Cortex Roadmap

Use this template when two or more domains must deliver one security outcome. Sequence by evidence dependencies and preserve owner/approval gates.

## Outcome frame

- Roadmap ID/date: `{{ID}}` / `{{YYYY-MM-DD}}`
- Objective: `{{SECURITY OUTCOME}}`
- Decision owner: `{{ROLE}}`
- Product/release/surfaces: `{{VALUES / UNKNOWN}}`
- Environment: `{{DESIGN / DEVELOPMENT / NON-PRODUCTION / PRODUCTION}}`
- Success: `{{OBSERVABLE END-TO-END CONDITION}}`
- Unacceptable outcomes: `{{LIST}}`
- Non-goals: `{{LIST}}`

## Domain map

| Domain | Why needed | Owner | Deliverable | Optional sibling Skill | Standalone fallback |
|---|---|---|---|---|---|
| Platform | `{{DEPENDENCY}}` | `{{ROLE}}` | `{{READINESS RECORD}}` | `cortex-platform-engineer` | entitlement/data/access checks |
| XQL/Hunt | `{{DEPENDENCY}}` | `{{ROLE}}` | `{{OBSERVABLE/HYPOTHESIS}}` | `{{SKILL}}` | semantic pseudologic and fixtures |
| Detection | `{{DEPENDENCY}}` | `{{ROLE}}` | `{{SIGNAL/LIFECYCLE}}` | `cortex-detection-engineer` | target-selection criteria and tests |
| TIM | `{{DEPENDENCY / NOT APPLICABLE}}` | `{{ROLE}}` | `{{INTELLIGENCE CONTRACT}}` | `cortex-tim-engineer` | source/confidence/lifecycle record |
| Playbook | `{{DEPENDENCY / NOT APPLICABLE}}` | `{{ROLE}}` | `{{WORKFLOW/SAFETY CONTRACT}}` | `cortex-playbook-engineer` | branches, approvals, recovery |

Remove a row only by recording `NOT APPLICABLE` and the reason.

## Dependency graph

| Order | Gate/work package | Requires | Produces | Objective acceptance | Responsible | Accountable/approver | Failure/recovery |
|---:|---|---|---|---|---|---|---|
| 0 | Decision frame | request | approved scope/requirements | owner accepts scope and non-goals | `{{ROLE}}` | `{{ROLE}}` | return to intake |
| 1 | Platform/data readiness | approved frame | entitlement, source, schema, access and health evidence | named non-production checks pass | `{{ROLE}}` | `{{ROLE}}` | hold downstream mechanics |
| 2 | Observable/hunt logic | readiness evidence | semantic query/hypothesis and fixtures | positive/benign/negative expectations are reviewable | `{{ROLE}}` | `{{ROLE}}` | revise telemetry/behavior |
| 3 | Detection design | stable observable | target-specific signal/lifecycle | target editor and quality gates defined | `{{ROLE}}` | `{{ROLE}}` | no rule promotion |
| 4 | TIM/workflow | stable signal and policy | governed enrichment/response flow | action denied safely when gates absent | `{{ROLE}}` | `{{ROLE}}` | manual/degraded path |
| 5 | Integrated validation | exact component candidates | end-to-end evidence | all required tests pass; no prohibited effect | `{{ROLE}}` | `{{ROLE}}` | rollback/revise |
| 6 | Promotion | complete evidence and operations | authorized release record | accountable approval retained | `{{ROLE}}` | `{{ROLE}}` | no production change |
| 7 | Operations/retirement | promoted control | health, outcome, tuning, recovery and retirement evidence | review criteria sustained | `{{ROLE}}` | `{{ROLE}}` | degrade, rollback, retire |

Mark rows not required for this scope rather than claiming implicit completion.

## Evidence gates

| Gate | Required class/qualifier | Current evidence | Status | Gap owner |
|---|---|---|---|---|
| Product/surface | `VERIFIED / OFFICIAL-CURRENT` | `{{EV ID}}` | `PASS/FAIL/NOT RUN/N/A` plus rationale | `{{ROLE}}` |
| Tenant schema/access | `TENANT-SCHEMA-VERIFIED` where needed | `{{EV ID / NONE}}` | `{{RESULT}}` | `{{ROLE}}` |
| Compiler/editor | `TENANT-COMPILED` where applicable | `{{EV ID / NONE}}` | `{{RESULT}}` | `{{ROLE}}` |
| Execution | `TENANT-EXECUTED` where applicable | `{{EV ID / NONE}}` | `{{RESULT}}` | `{{ROLE}}` |
| Integrated acceptance | exact non-production path | `{{EV ID / NONE}}` | `{{RESULT}}` | `{{ROLE}}` |
| Promotion | accountable approval | `{{RECORD / NONE}}` | `{{RESULT}}` | `{{ROLE}}` |

## Cross-domain invariants

- All artifacts use the same product/release/surface and versioned requirement.
- Entity keys, time semantics, signal/output grain, and confidence meaning remain consistent.
- Missing telemetry, nulls, denied permissions, duplicate/retry, timeout, and partial failure have explicit paths.
- Query results, detection matches, indicators, model scores, and ATT&CK labels do not authorize response.
- Secrets and sensitive evidence stay out of artifacts.
- No component pass is presented as integrated efficacy.

## Current decision

- Decision: `{{PROCEED TO GATE / REVISE / HOLD / OUT OF SCOPE}}`
- Blocking dependencies: `{{LIST / NONE}}`
- Parallel work allowed: `{{INDEPENDENT PACKAGES AND WHY}}`
- Residual limitations: `{{LIST}}`
- Explicit non-claims: `{{LIST}}`
- Next owner and artifact: `{{ROLE / DELIVERABLE}}`
