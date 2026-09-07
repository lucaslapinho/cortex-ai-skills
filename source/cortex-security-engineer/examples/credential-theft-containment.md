# Example: Credential-Theft Containment Program

## Scenario

The requester asks: “Detect credential dumping in Cortex and automatically isolate every matching endpoint.”

Supplied facts:

- the organization uses “Cortex,” but product/release and tenant access are not supplied;
- no telemetry/schema, baseline, detection artifact, response policy, permission, owner, or recovery evidence is supplied;
- no specialist Skill is assumed installed.

## Outcome first

**Decision: `HOLD` automatic isolation; proceed to a read-only requirements and validation package.**

Reason: the behavior, product/surface, telemetry, trigger quality, authorization, blast radius, and recovery path are unresolved. A future query or detection match would still not authorize containment.

Evidence status: `CONCEPTUAL / TENANT-UNVERIFIED`.

- `S: NOT RUN` — no independent response evaluation exists for the proposed control.
- `D: NOT RUN` — no exact current product/surface documentation was selected and reviewed for this conceptual request.
- `C: NOT RUN` — no tenant schema, rule, permission, policy, or configuration target was inspected.
- `E: NOT RUN` — no detection, isolation, recovery, or downstream result was executed or observed.

## Requirement record

- `REQ-001`: The security owner MUST define the credential-access behaviors and protected asset classes that justify investigation.
- `REQ-002`: The control MUST preserve enough host, user, process, parent/causal, time, and source context for a responder to distinguish approved administration, security testing, endpoint tooling, and suspicious activity.
- `REQ-003`: No isolation may occur without the approved response policy, corroborating evidence, target eligibility, least-scope limit, human approval, and recovery path.
- `REQ-004`: Missing telemetry, denied permissions, enrichment failure, duplicate signals, timeout, and partial isolation MUST produce visible, owned outcomes rather than silent success.

Numeric response objectives, severity, confidence thresholds, and maximum batch size remain risk-owner inputs.

## Threat and risk frame

Behavior of concern: access to credential material followed by use or staging that could enable privilege escalation or lateral movement. This is not reduced to one tool or filename.

Benign alternatives include authorized security assessment, endpoint/security tooling, forensic collection, and tightly controlled administration. False-negative paths include alternate techniques, memory protections, renamed or indirect tooling, non-Windows identity abuse, unmonitored assets, missing source coverage, null context, delayed ingestion, and restricted data scope.

Control abuse risk: false or low-quality signals could isolate critical endpoints, disrupt services, hide evidence, or be exploited as denial of service.

ATT&CK mappings may organize the design but do not prove behavior or product coverage.

## Telemetry contract

| ID | Required observable | Evidence now | Smallest validation |
|---|---|---|---|
| `TEL-001` | process/causal activity relevant to the defined behavior | `UNVERIFIED` | identify product/release; observe source, schema, types, subtypes, coverage, nulls |
| `TEL-002` | identity/logon and privilege context | `UNVERIFIED` | verify supported source and entity semantics |
| `TEL-003` | endpoint identity, criticality, management, and current response eligibility | `UNVERIFIED` | verify inventory source, ownership, scope, and response state |
| `TEL-004` | ingestion/retention/access health | `UNVERIFIED` | non-production known-positive and restricted-identity checks |

No dataset or field names are invented.

## Domain sequence

| Gate | Owner | Deliverable | Acceptance |
|---|---|---|---|
| G0 | Security/risk owner | behavior, asset scope, success and unacceptable outcomes | owner approves requirement frame |
| G1 | Platform owner | exact product/release/license, source/schema/coverage, RBAC/SBAC and response permission record | observed non-production readiness |
| G2 | XQL/Hunt owner | bounded observable/hypothesis logic and positive/benign/negative/null fixtures | reviewable result semantics; no absence/maliciousness overclaim |
| G3 | Detection owner | exact rule-surface design, grouping/tuning, FP/FN, issue context, lifecycle | independent editor/fixture/volume evidence |
| G4 | Playbook owner | enrichment and human-review flow; isolation branch remains approval-gated | denied, duplicate, timeout, partial-failure, and manual paths pass |
| G5 | Cross-domain owners | integrated non-production path including recovery | exact evidence linked end to end |
| G6 | Change/risk approver | promotion decision | explicit accepted residual risk and release artifact |
| G7 | Control owner | health/outcome monitoring, tuning/exception and retirement model | owned operational evidence |

Optional mechanics handoffs: `cortex-platform-engineer`,
`cortex-xql-query-engineer`, `cortex-threat-hunter`,
`cortex-detection-engineer`, and `cortex-playbook-engineer`. The consuming host may
apply its own selector; these are platform-neutral Skill names.

Standalone fallback: each owner receives the semantic contract and fixtures above; exact syntax/settings remain withheld until current official and tenant evidence exists.

## Consequential-action gate

Isolation requires:

- deterministic signal and corroboration policy;
- exact target identity, asset class, criticality, and exclusions;
- approved human decision point and emergency override;
- least-scope and maximum-batch policy;
- effective action identity and command permission;
- idempotency for duplicate/retried signals;
- handling when endpoint is offline, already isolated, unmanaged, or partially acted on;
- recovery/unisolation owner, tested compensating path, and post-action state verification;
- audit record that links signal, case, approval, action ID, result, and recovery.

Until these pass, output is an investigation recommendation only.

## Validation set

- known-positive controlled credential-access behavior;
- approved security-test and administration fixtures;
- similar but out-of-scope process/identity events;
- null host/user/process/causal context;
- collection lag, boundary time, and restricted SBAC;
- duplicate signal and repeated approval;
- denied integration/response command;
- endpoint offline and partial batch failure;
- isolation recovery and evidence reconciliation.

Each component and the integrated path records `S/D/C/E` separately.

## Operations and non-claims

Monitor source health, schema/access drift, signal/case volume, dispositions, known-positive/negative fixtures, exceptions, action outcomes, partial failures, and recovery. Every exception needs owner, expiry, before/after coverage evidence, and a false-negative regression fixture.

No tenant, field, query, rule, case, playbook, permission, action, result, deployment, or efficacy claim is made.
