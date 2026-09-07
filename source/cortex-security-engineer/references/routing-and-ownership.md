# Routing and Ownership

## Contents

- [Orchestrator responsibility](#orchestrator-responsibility)
- [Domain ownership matrix](#domain-ownership-matrix)
- [Single-domain routing](#single-domain-routing)
- [Multi-domain sequencing](#multi-domain-sequencing)
- [Handoff contract](#handoff-contract)
- [RACI-style minimum](#raci-style-minimum)
- [Stopping conditions](#stopping-conditions)

## Orchestrator responsibility

The Security Engineer owns:

- intake and product/surface disambiguation;
- requirement, threat/risk, telemetry, control, validation, and operations decision records;
- cross-domain dependency ordering;
- owner, approver, evidence, acceptance, rollback/recovery, and lifecycle gates;
- explicit non-claims and unresolved conditions.

The Security Engineer does not silently author specialist syntax, declare a tenant state, or absorb approval authority.

## Domain ownership matrix

| Domain | Owns | Inputs required | Returns to orchestrator | Must not be inferred |
|---|---|---|---|---|
| XQL | language mechanics, dataset/field semantics, query construction/review, performance reasoning, query-context compatibility | objective, product/release/surface, timeframe, schema evidence, output grain | evidenced query/pseudologic, assumptions, expected output, validation status | tenant schema, compile/run, rule compatibility |
| Detection | behavioral signal, rule surface, tuning, FP/FN model, issue mapping, tests, rollout/monitoring/rollback/retirement | threat behavior, telemetry contract, candidate logic, operational SLO | detection design and lifecycle evidence | efficacy from query matches |
| Threat hunting | hypothesis, observables, pivots, analytic plan, evidence interpretation, escalation | threat/risk frame, coverage, timeframe, authorized data | hunt plan/findings with bounded conclusions and control candidates | absence from zero results |
| Playbook | trigger/input/output contracts, tasks, branches, integrations, human gates, error handling, idempotency, recovery | authorized action policy, identities, integration/command permissions, data minimization | conceptual or validated workflow plus failure/recovery evidence | action permission from object visibility |
| TIM | source provenance, indicator types, confidence/scoring, dedup/enrichment, sharing/distribution, expiry/revocation | intelligence requirement, consumers, policy, licenses/permissions | governed indicator lifecycle and consumer evidence | maliciousness or blocking authority |
| Platform | product architecture, licensing, ingestion, collectors/Broker, data sources, RBAC/SBAC, API/integration foundations | product/release, topology, data/control requirement, environment | readiness facts, configuration plan, validation/rollback record | installed state or health without tenant evidence |
| Security Engineer | cross-domain decision and operating model | all above at appropriate depth | consolidated decision, sequence, gates, risks, owners, non-claims | specialist implementation success |

## Single-domain routing

Recommend a sibling Skill only when it materially helps:

- `cortex-xql-query-engineer`
- `cortex-detection-engineer`
- `cortex-threat-hunter`
- `cortex-playbook-engineer`
- `cortex-tim-engineer`
- `cortex-platform-engineer`

Phrase recommendations as optional: “For exact XQL mechanics, optionally continue
with …”. Use the neutral Skill name; platform-specific selectors belong in that
host's adapter or installation guidance. Do not stop with a handoff. Supply the
bounded intake, requirements, unknowns, evidence ceiling, validation steps, and
acceptance criteria the specialist needs.

If no sibling exists:

- provide plain-language logic or `text`-fenced pseudologic;
- identify the exact official reference and tenant checks needed;
- avoid executable-looking syntax, field names, endpoints, task names, or settings not evidenced;
- keep deployment and efficacy claims absent.

## Multi-domain sequencing

Build a dependency graph from evidence, not a generic project plan.

### Common sequence

| Gate | Primary owner | Required output | Approval/evidence to advance |
|---|---|---|---|
| G0 — Decision frame | Security Engineer + risk owner | objective, scope, non-goals, success, unacceptable outcomes | accountable owner accepts frame |
| G1 — Platform/data readiness | Platform + data owner | entitlement, source, schema, coverage, identity/scope, health plan | observed non-production readiness |
| G2 — Analytic readiness | XQL/Hunt | observable logic, output grain, known-positive/benign/negative fixtures | schema and bounded static/tenant evidence |
| G3 — Detection readiness | Detection | target-specific signal, FP/FN, grouping, tuning, mapping, lifecycle | representative non-production tests and owner |
| G4 — Enrichment/response readiness | TIM/Playbook | governed intel and/or workflow with approval/error/recovery paths | exact permission/dependency/action tests |
| G5 — Integrated validation | Cross-domain owners | end-to-end evidence, denied/failure/rollback tests, audit trail | independent acceptance against criteria |
| G6 — Promotion | change/risk approver | approved release/change record, rollback, monitoring | explicit authorization |
| G7 — Operations | control owner | SLOs, telemetry health, drift/tuning, exceptions, incidents, retirement | periodic evidence and reapproval triggers |

Not every request needs every gate. Mark omitted gates `NOT APPLICABLE` with a reason; never silently skip a required dependency.

### Parallel work

Parallelize only independent work, such as:

- threat model and source-inventory discovery after the decision frame;
- positive and benign fixture design after observable semantics are fixed;
- operations metrics and rollback planning after control failure modes are known.

Do not parallelize a downstream implementation that depends on unresolved product, schema, authorization, or trigger semantics.

## Handoff contract

Every work package contains:

| Field | Required content |
|---|---|
| ID/title | stable identifier and outcome |
| Owner | accountable domain role |
| Input | exact artifact/evidence and version |
| Scope | product/release/surface/environment/time/data |
| Requirement | testable MUST/SHOULD/MUST NOT statement |
| Assumptions | labeled evidence class |
| Deliverable | artifact and format |
| Dependencies | predecessor IDs/evidence |
| Acceptance | observable pass/fail criteria |
| Safety | authorization, data handling, blast radius |
| Failure/recovery | expected error path, rollback/recovery owner |
| Evidence | location, retention, sanitization |
| Approver | named role, not the artifact author alone |
| Non-claims | what remains untested/unapproved |

Avoid “configure as needed,” “validate,” or “owner: security” without specifics.

## RACI-style minimum

For each consequential control name:

- **Accountable:** one decision owner.
- **Responsible:** implementation/operator role.
- **Consulted:** relevant platform, data, privacy, legal, business, or threat-intelligence owner.
- **Informed:** monitoring/on-call and impacted service owner.
- **Approver:** policy/change/risk authority where different.
- **Recovery owner:** can stop, revert, restore, or manually contain failure.

One person may hold multiple roles only when policy allows it; record the separation-of-duties decision.

## Stopping conditions

Return `HOLD` when any material condition remains:

- target product or surface ambiguity changes mechanics or safety;
- required telemetry/schema/coverage cannot be evidenced;
- action or data handling lacks authority;
- no accountable owner or approver exists;
- rollback/recovery is impossible or unowned;
- current official behavior conflicts and no discriminating test is available;
- the requested universal cross-product artifact is not supportable;
- acceptance criteria require a tenant result that was not run.

State the smallest safe next action and who owns it.
