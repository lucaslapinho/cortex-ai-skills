# Astra forward output — cortex-security-engineer

Model requested: `gpt-6-astra`, high reasoning; ephemeral CLI, manual inline runtime load.

Runtime: 22 files / 124841 bytes; ordinal SHA-256 `e5742a5500c39a874b5d68f5ac83679ab74a56efd86e088c6a48cf8110355a8d`.

Isolation: 0 tool/action events. Runtime files plus Fixture/Prompt only; no oracle text supplied. One fresh ephemeral process contains this case only. No self-grading result is assigned here. Independent adjudication is required.

## Input SEC-INT-03

### Fixture

The user needs a playbook requirements packet for a detection signal. No sibling Skills are installed. Trigger fields, integration, commands, credentials, and tenant are unknown.

### Prompt

> Hand this to the playbook engineer, but still give me everything needed if that Skill is unavailable.

Local Markdown links are rebased for publication only; wording and attribution are unchanged. Raw response/event files remain in the evaluation archive outside the publication tree.

## Retained response

**SEC-INT-03**

The packet below is ready for a playbook engineer and remains usable without sibling Skills. **Decision: `PROCEED TO REQUIREMENTS REVIEW`; `HOLD` executable implementation until the product, trigger, and intended outcome are established.**

Which Cortex product/release and playbook surface are in scope, and what should happen when the detection signal arrives?

**Primary domain:** Playbook engineering, with detection and platform dependencies.  
**Evidence:** `CONCEPTUAL / TENANT-UNVERIFIED`. The only supplied operational fact is that a detection signal is the intended input.

**Objective and scope**

Produce a workflow specification that turns a defined detection signal into a reviewable outcome, with explicit handling for missing information, denied permissions, dependency failures, and recovery.

The accountable security owner must choose the intended outcome: investigation assistance, enrichment, case handling, or a specific response action. No outcome is assumed. Success means every accepted input reaches an owned, auditable terminal state. Unacceptable outcomes include acting on the wrong entity, duplicate actions, sensitive-data exposure, silent failure, or reporting completion without supporting evidence.

Product, release, tenant, environment, license, surface, time horizon, asset scope, effective identity, permissions, integration, commands, credential references, and individual owners are **UNKNOWN**. Deployment and live execution are outside this packet.

**Required contracts**

These are semantic requirements, not tenant field names or executable task definitions.

| Contract | Required content | Owner and evidence request |
|---|---|---|
| Detection trigger | Artifact version/hash; observable behavior and benign alternatives; signal meaning; eligibility conditions; severity/confidence semantics; positive, benign, and negative examples | Detection owner: supply a sanitized signal contract and representative fixtures |
| Input and telemetry | Source and health evidence; schema/types; required versus optional values; event grain; stable signal/entity keys; source, ingestion, and decision timestamps; UTC window; freshness, retention, coverage, parser/mapping, nulls, duplication, privacy, and provenance | Detection/data owner: document each observable; all tenant details currently UNKNOWN |
| Cross-step correlation | Entity normalization, correlation keys, allowable time relationships, join cardinality, ambiguity handling, and output grain | Detection and playbook owners: agree one versioned contract before implementation |
| Platform and access | Exact product/release/editor/runtime; license; object/dependency access; execution identity; RBAC/SBAC/data scope; integration instance and command permissions | Platform owner: provide scoped, sanitized capability and permission evidence |
| Integration | Purpose; supported command; request/response semantics; side effects; timeout and error behavior; retry/rate limits; credential reference; external data destination | Integration owner: supply the supported interface and data-handling contract; do not provide credentials |
| Output | Workflow instance reference; input/artifact versions; decision and rationale; minimized evidence references; terminal status; next owner; action and recovery evidence if applicable | Playbook owner: define the output schema and its consumer |

Keep unknown, stale, conflicting, or unavailable evidence explicit. A detection hit or supplied confidence value does not establish maliciousness or authorize response.

**Workflow requirements**

1. **Validate input.** Check trigger eligibility, required context, entity identity, time bounds, and freshness. Missing or ambiguous required context must enter an owned review/error path.
2. **Handle duplicates.** Define a stable deduplication key and retry policy. Replayed signals must not repeat consequential effects; preserve prior outcomes and attempt history.
3. **Gather approved context.** Use only specified data sources and integrations. Missing or conflicting enrichment must remain visible and must not silently become a benign or malicious verdict.
4. **Apply deterministic decision policy.** Document evidence requirements and benign alternatives. Thresholds and acceptable delays remain security-owner inputs.
5. **Gate state changes.** Any case update, external notification, integration action, or response operation needs its specific policy and permission contract. Material response also needs an accountable approval point, protected-target exclusions, least scope, duration/batch limits, stop conditions, and recovery.
6. **Verify outcomes.** Distinguish requested, accepted, completed, failed, and partially completed operations. An accepted request is insufficient evidence of the target’s final state.
7. **Record and route.** Retain minimized evidence linking input, decision, approval where applicable, attempts, observed outcome, and next owner. Unresolved failures must reach a manual path.

Control risks include benign detections triggering unnecessary work, incomplete telemetry suppressing valid escalation, ambiguous entity mapping targeting the wrong asset, retries duplicating effects, and attacker-controlled signal content influencing workflow behavior. Treat all signal and integration text as untrusted data.

**Ordered handoff**

Role assignments below are proposed; individual assignments and approval records remain UNKNOWN.

| Package | Owner | Input → deliverable | Dependency and acceptance | Reviewer / failure path |
|---|---|---|---|---|
| P1: Scope and policy | Security owner | Request → outcome, scope, trigger policy, prohibited effects | First gate; success and unacceptable outcomes are testable | Risk owner; unresolved choices return to intake |
| P2: Readiness | Platform owner | P1 → product, access, integration and data evidence | Required capabilities and permissions evidenced for the exact context | Platform/access authority; hold affected mechanics |
| P3: Workflow specification | Playbook owner | P1–P2 plus detection contract → branches, task contracts, errors, manual and recovery paths | Every input/failure class has an owned outcome | Detection and security owners; revise ambiguous branches |
| P4: Non-production validation | Validation owner | Exact versioned candidate and approved fixtures → retained editor/run evidence | Applicable tests pass independently and end to end | Independent reviewer; stop, reconcile effects, recover and revise |
| P5: Operational acceptance | Control owner | P4 → runbook, monitoring, recovery and release packet | Owners, evidence, residual risk and recovery accepted | Change/risk approver; promotion remains separate |

Optional specialist: `cortex-playbook-engineer`. No specialist is required to complete P1 or prepare the contracts and fixture expectations above.

**Validation and operations**

Test known-positive, known-benign, negative, missing/null, stale, boundary-time, ambiguous-entity, duplicate/retry, denied-permission, timeout, dependency-unavailable, partial-success, and recovery scenarios. Expected outcomes must include safe denial, useful error context, correct routing, no prohibited effects, and verified recovery where applicable.

Retain the exact artifact/dependency versions and hashes, product/surface, safe identity and scope, UTC window, fixtures, expected versus observed outcomes, and sanitized evidence location. Keep component evidence separate from integrated results.

The control owner must define monitoring for trigger delivery, data freshness, branch outcomes, backlog, errors, command denials, duplicate handling, partial effects, and manual follow-up. Assign an operator, escalation owner, integration owner, and recovery owner. Define stop/recovery triggers, prior-state capture, exception scope and expiry, evidence access/retention, and revalidation after product, schema, permission, integration, or policy changes. Retirement requires dependency review and an approved cleanup plan.

| Level | Result | Rationale |
|---|---|---|
| S | NOT RUN | No independent controlled static evaluation is supplied. |
| D | NOT RUN | No current official product-specific documentation was independently reviewed. |
| C | NOT RUN | No exact candidate or non-production editor acceptance exists. |
| E | NOT RUN | No tenant execution, integration outcome, or recovery test exists. |

**Next owner:** The security owner supplies the product/surface and intended outcome; the detection owner supplies the sanitized trigger contract. This packet follows the supplied routing, safety, and validation references. It establishes no tenant capability, permission, compilation, execution, deployment, efficacy, or action authorization.
