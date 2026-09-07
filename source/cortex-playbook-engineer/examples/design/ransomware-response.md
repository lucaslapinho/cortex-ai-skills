# Ransomware Investigation and Containment Design

**Artifact classification:** `CONCEPTUAL`  
**Applicable product/surface:** Cortex XSIAM playbook design; exact tenant release unknown  
**Evidence status:** native playbooks, Issue triggers, sub-playbooks, manual tasks, error handling, context, debugger, and integration permissions are `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED`; all named workflow nodes below are conceptual  
**Execution status:** no import, debugger run, containment, notification, or tenant execution

## Objective

Design a ransomware workflow that preserves evidence, scopes affected assets, obtains accountable approval, applies least-scope containment, verifies it, and leaves remediation/closure under explicit ownership.

It must not isolate an endpoint merely because an Issue name, score, filename, model output, or single detection says “ransomware.”

## Assumptions and prerequisites

- A tenant-verified XSIAM automation rule can select the intended ransomware-related Issue population.
- Exact Issue fields, context paths, installed content, commands, arguments, outputs, and close reasons are unknown.
- Enrichment and response capabilities are specified by purpose until command help and integration versions are supplied.
- Containment authority belongs to an authenticated incident-response approver, not the playbook or AI.
- All target identifiers in design records are sanitized aliases.

## Inputs and outputs

| Design ID | Contract |
|---|---|
| `PB-IN-001` | Source Issue/Case identity, detection provenance, observed time, entity candidates, and sanitized evidence references; exact paths tenant-verified before build |
| `PB-IN-002` | Response policy, critical-asset exclusions, maximum target count, approver role, freshness window, and recovery owner |
| `PB-OUT-001` | Investigation record: validated entities, observations, conflicts, gaps, confidence, and recommended next action |
| `PB-OUT-002` | Per-target action ledger: requested state, approval, returned status, readback, recovery, and final state |
| `PB-OUT-003` | Closure or escalation record with residual-risk owner |

No secret or credential value enters context or evidence.

## Conceptual flow

| Stage | Node | Decision/output | Failure behavior |
|---|---|---|---|
| Trigger | Validate source Issue and rule provenance | Accept only in-scope, fresh, nonduplicate work | Stop/escalate malformed, stale, or ambiguous trigger |
| Validation | Validate endpoint/user/file/network entity candidates | Typed, bounded, deduplicated entity set | Empty/unknown does not become benign; request evidence |
| Enrichment | Query tenant-verified endpoint, identity, file, network, and intelligence capabilities | Source-attributed enrichment with timestamps | Optional source can degrade; required source failure blocks action |
| Decision | Evaluate deterministic evidence table | `Investigate`, `ApprovalCandidate`, `NoContainment`, or `InsufficientEvidence` | Conflicts/unknown route to analyst, never aggressive default |
| Investigation | Build timeline, scope peers, identify active impact, preserve alternatives | Investigation record and proposed scope | Coverage gaps remain explicit |
| Approval | Present evidence, confidence, target list, dependencies, blast radius, and recovery | Approve/reject/request evidence/expire | No response and expiry fail closed |
| Containment | Revalidate current target state; invoke tenant-verified least-scope isolation capability once | Per-target returned status | Permission/timeout/partial response routes to reconciliation |
| Remediation | Handoff separate owner-approved repair steps | Remediation plan/result | Containment success never implies remediation completion |
| Verification | Independently read endpoint state and continued behavior | Confirmed/failed/unknown per target | Unknown state stops closure and triggers recovery/escalation |
| Notification | Inform assigned responders/business owners with minimum data | Delivery record | Failure escalates through alternate route; no duplicate storm |
| Evidence | Record identities, decisions, sanitized inputs/outputs, action/readback, errors | Audit package | Quiet Mode cannot erase required minimal evidence |
| Closure | Check analytical and operational closure criteria | Close with supported tenant field/reason or leave open/escalated | Unsupported close reason is not guessed |

Node names are design labels, not Cortex task or playbook IDs.

## Decision table

| State | Evidence condition | Allowed result |
|---|---|---|
| Insufficient | Required telemetry/identity unavailable or stale | Investigate/escalate; no isolation |
| Conflicting | Sources disagree on target or activity | Analyst review; no isolation |
| Benign-supported | Representative evidence supports an authorized benign explanation | Document/tune handoff; no isolation |
| Suspicious | Multiple observations support malicious behavior but active impact/scope remains uncertain | Continue investigation; optional approval candidate only under policy |
| High-confidence candidate | Corroborated active behavior, exact target, fresh readback, bounded scope, no critical exclusion, recovery ready | Human approval request |
| Approved | Authenticated, unexpired approval matches exact action/targets | Execute once, then read back |

AI output can summarize evidence but cannot set the Approved state.

## Reliability and action controls

- Use a conceptual idempotency key based on action class, canonical endpoint alias, source object, and requested state.
- Reconcile endpoint state after any timeout before retrying.
- Keep one result per endpoint; never retry an entire partially successful batch blindly.
- Hard-bound target count and canary the first authorized target.
- Stop if a target is critical/excluded, identity is unverified, approval scope differs, or recovery is unavailable.
- Require a tenant-verified de-isolation/recovery capability and owner before isolation.
- Treat notification as separate from containment success.

## Test plan

| Test | Expected outcome |
|---|---|
| False-positive administrative encryption fixture | No containment; evidence/tuning handoff |
| Unknown entity/context | Fail closed to investigation |
| Optional enrichment outage | Degraded state; no false benign value |
| Required identity/RBAC denial | Stop action path and preserve error |
| Approval rejected/expired | No action |
| Duplicate trigger | Existing work/result returned or safely reconciled |
| Timeout after isolation request | State readback before any retry |
| Two-target batch with one failure | Per-target partial result and escalation |
| Recovery test | Reversible test target restored and verified |
| Hostile text in Issue/context | Treated as data; cannot alter gate or access secrets |

All are planned. `C` and `E` remain `NOT RUN`.

## Validation status

| Level | Result | Rationale |
|---|---|---|
| S | NOT RUN | The example is a design and test plan; no independent response result is asserted here. |
| D | PASS | PB04, PB05, PB07, PB09, PB10, and PB15 were re-opened on 2026-09-06 for XSIAM triggers, sub-playbooks, errors, context, testing, and permissions. The proposed response policy remains conceptual. |
| C | NOT RUN | No exact target artifact, command schema, or controlled import exists. |
| E | NOT RUN | No workflow, action, notification, or recovery test was performed. |

## Expected result and limitations

Expected—not observed—output is a bounded, auditable investigation and action record. The design cannot claim the endpoint was isolated, evidence was complete, or ransomware was confirmed.

Before configuration, obtain target release, automation-rule predicate, Issue/context schema, installed pack and command help, integration instance/permissions, critical-asset policy, approval identity, exact recovery/readback capability, notification channel, and supported closure fields.

## Official references

- [XSIAM playbooks overview](../../references/official-sources.md#cortex-xsiam-automation-and-playbooks)
- [Reliability and action safety](../../references/reliability-safety-security.md)
- [Playbook design template](../../templates/playbook-design.md)
- [Protected action gate](../../templates/action-gate.md)
