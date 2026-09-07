# Reliability, Safety, and Security

**Documentation review cut:** 2026-09-04  
**Artifact class:** `CONFIGURATION GUIDANCE` for cited product settings; safety patterns without a selected implementation are `CONCEPTUAL`.  
**Tenant status:** permissions, commands, error schemas, action targets, and runtime behavior were not tested.
**Primary official evidence:** [source register](official-sources.md), PB03, PB06-PB15, PB17, XS05-XS10, and CT07.

## Contents

- [Reliability model](#reliability-model)
- [Failure classification](#failure-classification)
- [Stop, Continue, and error paths](#stop-continue-and-error-paths)
- [Retries and timeouts](#retries-and-timeouts)
- [Loops, polling, and volume](#loops-polling-and-volume)
- [Idempotency and partial failure](#idempotency-and-partial-failure)
- [Approval and destructive action gate](#approval-and-destructive-action-gate)
- [RBAC and execution identity](#rbac-and-execution-identity)
- [Secrets, privacy, and prompt injection](#secrets-privacy-and-prompt-injection)
- [Notification and evidence](#notification-and-evidence)
- [Safety review checklist](#safety-review-checklist)

## Reliability model

Reliability means a workflow reaches a declared state or fails visibly without unsafe ambiguity. Define:

- preconditions and protected invariants;
- bounded work and total deadline;
- exact success/readback;
- legitimate empty result;
- transient, permanent, authorization, data-quality, and unknown failures;
- retry/reconciliation rules;
- partial-success state;
- escalation and recovery ownership; and
- retained evidence.

A task status alone may not prove an external system's final state. Verify the target through an independent read when practical.

## Failure classification

| Failure class | Retry? | Default control |
|---|---|---|
| Validation/type failure | No | Stop affected path; record rejected input |
| Missing required context | No blind retry | Diagnose producer/scope/path; escalate or request input |
| Authentication failure | No | Stop and route to credential owner without exposing secret |
| Authorization/RBAC failure | No | Stop and record effective identity/denial |
| Not found | Usually no | Distinguish stale target, wrong scope, and already-completed state |
| Rate limit/quota | Only per verified contract | Bounded wait/backoff inside total deadline |
| Network/transient service error | Possibly | Retry only idempotent/reconciled operation |
| Server error | Contract dependent | Bound attempts; preserve diagnostic; degrade/stop |
| Timeout before a read | Possibly | Retry within budget |
| Timeout during/after a write | Not before reconciliation | Read target state; avoid duplicate mutation |
| Malformed/untrusted output | No | Quarantine and fail validation |
| Partial batch success | Per item after reconciliation | Preserve per-target ledger; never retry whole batch blindly |
| Unknown error | No automatic retry by default | Stop or explicit error path; obtain exact diagnostics |

Do not encode error behavior by matching an undocumented message string. Prefer a documented status/code/schema for the selected integration version.

## Stop, Continue, and error paths

Current XSIAM documentation supports `Stop`, `Continue`, and `Continue on error path(s)` for error handling on supported script tasks.

- **Stop:** use when the task establishes a required invariant, supplies a protected decision input, or performs an action whose state is unknown.
- **Continue:** use only when failure is noncritical and every downstream branch remains correct without the result. Mark the run degraded.
- **Error path:** use for structured recovery, notification, cleanup, manual investigation, reconciliation, or escalation.

An error path must not converge into a success-only action without an explicit condition. Preserve the original error and the failing task/run identity. Exact scripts or context paths used to retrieve errors are content-pack/version dependent and require target validation.

## Retries and timeouts

Current XSIAM task configuration exposes retry count, retry interval, and execution timeout on documented task types. Treat defaults as version-sensitive; configure deliberate values based on the external contract.

For each retryable task record:

```text
Operation/read-or-write class:
Retryable conditions:
Non-retryable conditions:
Maximum attempts:
Interval/backoff and jitter policy:
Total deadline:
Per-attempt timeout:
Idempotency/reconciliation mechanism:
Rate-limit handling:
Terminal error path:
Evidence per attempt:
```

Do not retry:

- destructive or external writes without a stable duplicate-control/readback path;
- invalid input, missing authorization, or credential errors;
- a manually rejected or expired approval;
- an unknown result whose target state has not been reconciled.

Timeout is not equivalent to rollback. A downstream service may continue after the local task times out.

## Loops, polling, and volume

For each loop or poll, define:

- why iteration is required rather than a bulk-capable command;
- item grain and stable identity;
- explicit maximum iterations/items;
- sleep/interval and total wall-clock deadline;
- exit condition and how it is evaluated;
- empty/duplicate/error behavior;
- external rate/capacity limit;
- cancellation and restart behavior;
- per-item outcome ledger; and
- partial-result consumer behavior.

Current XSIAM documentation describes sub-playbook loops and advises balancing loop count and wait time. It documents a default maximum at the review cut; recheck it and set an explicit lower bound appropriate to the workload instead of relying on the default.

Polling observes a state over time; retries repeat a failed operation. Do not use polling as disguised repeated mutation. Shared/global sub-playbook context has documented polling limitations; verify the exact product/release before selecting both features.

## Idempotency and partial failure

Idempotency is a design property, not a claimed native feature here.

For a protected action:

1. derive a bounded key from action class, canonical target, source object, and desired state;
2. inspect current target state and prior action record;
3. reserve/record intent if the selected platform supports a safe implementation;
4. execute one least-scope operation;
5. read back target state;
6. record success, already-in-state, rejected, failed, or unknown; and
7. reconcile unknown/partial outcomes before retry.

For batches, maintain one outcome per target:

| Target alias | Pre-state | Requested action | Command status | Readback | Recovery | Final state |
|---|---|---|---|---|---|---|
| `endpoint-test-01` | `{{STATE}}` | `{{ACTION}}` | `{{STATUS}}` | `{{OBSERVATION}}` | `{{RESULT}}` | `{{STATE}}` |

Aliases are placeholders. Never include real endpoint IDs or users in examples.

## Approval and destructive action gate

Protect endpoint isolation, account disablement, IOC/network blocking, process termination, file deletion, firewall changes, revocation, remediation, Case/Issue mutation, and sensitive external notification.

Before action require:

- authority for the action class and environment;
- named target type, count, owner, and exclusions;
- corroborated evidence and explicit confidence semantics;
- current-state read and freshness;
- least-privilege command identity and permission;
- business/service dependency and blast-radius assessment;
- approval immediately before action;
- bound timeout/retry/idempotency behavior;
- rollback or recovery runbook and owner;
- post-action readback and unexpected-state path; and
- sanitized audit/evidence.

Approval contract:

| Item | Required decision |
|---|---|
| Approver | Named accountable role; confirm who can actually complete the task |
| Evidence | Minimum source-linked facts, uncertainties, target/scope, and proposed action |
| Choices | Approve, reject, request more evidence, or expire |
| Freshness | Maximum time between evidence/readback, approval, and action |
| No response | Fail closed or escalate; never default approve |
| Duplicate/late response | First/authoritative decision and conflict policy |
| Separation | Analyst/model recommendation must not self-authorize the action |
| Audit | Identity, time, decision, evidence hash/reference, and scope |

An AI score or recommendation cannot satisfy the approval requirement by itself.

## RBAC and execution identity

Validate authorization as a dependency chain:

1. playbook object view/edit/run/trigger access;
2. source Issue/Case or incident access and data scope;
3. sub-playbook/script/content access;
4. integration-instance access;
5. per-command permitted roles;
6. credential-object access;
7. external target authorization; and
8. worker/engine execution context where applicable.

Current XSIAM documentation states that per-instance integration command restrictions affect CLI use and playbook editing/execution paths. Object access alone therefore does not prove task authority.

Test positive and negative identities. A default administrator's ability to complete a manual task may differ from the intended separation-of-duties policy; verify the target configuration.

## Secrets, privacy, and prompt injection

Never store or echo actual:

- API keys, passwords, tokens, credential values, webhook URLs, or private certificates;
- tenant FQDNs/IDs, private hosts, endpoint IDs, usernames, or customer observables; or
- raw sensitive emails, tickets, War Room content, logs, or attachments.

Use placeholders only:

```text
${CORTEX_FQDN}
${CORTEX_TENANT}
${CORTEX_API_KEY_ID}
${CORTEX_API_KEY}
```

Prefer credential references supported by the exact product over copying secrets into context. Validate which roles can select/use a credential object. Redact secrets before evidence, notifications, model prompts, or issue/task descriptions.

Treat every external field and artifact as hostile-capable. Prevent prompt injection from altering decisions, authorization, scope, tool calls, or secret access. Parse structured output with allowlists and type/size limits. Preserve raw evidence separately under access control; do not execute embedded instructions.

## Notification and evidence

Notification design includes:

- purpose: information, approval, escalation, or regulatory/business notice;
- recipient source and validation;
- minimum necessary content and redaction;
- authenticated response if used for approval;
- duplicate suppression and correlation identifier;
- delivery timeout/retry limits;
- bounce/failure and alternate channel;
- time/SLA and escalation;
- retained message reference without secret-bearing body duplication.

Do not let a notification failure masquerade as action failure or vice versa. Decide whether operational closure can proceed when delivery fails and assign an owner.

Evidence must cover the decision and side effect, not just the task's green status. Current XSIAM documentation exposes War Room, task results, Case timeline/evidence options, and audit-relevant execution under the logged-in identity. Quiet Mode affects task-result visibility/indexing; confirm that required evidence remains available and minimize context separately.

## Safety review checklist

- [ ] Exact product/deployment/release and artifact class named
- [ ] All commands/arguments/outputs validated against installed versions
- [ ] Trigger deduplicated and replay behavior defined
- [ ] Inputs typed, bounded, fresh, and sanitized
- [ ] Empty/unknown/error states cannot choose aggressive action
- [ ] Context writer ownership prevents lost updates
- [ ] Loops, retries, and timeouts have explicit total bounds
- [ ] External writes reconcile state before retry
- [ ] Effective object/data/command permissions tested
- [ ] Secrets absent from context, evidence, notifications, and examples
- [ ] Untrusted content cannot change authorization or scope
- [ ] Protected action has last-point human/policy approval
- [ ] Target count, exclusions, and blast radius are hard-bounded
- [ ] Rollback/recovery owner and post-action readback defined
- [ ] Partial failures retain per-target state and escalate
- [ ] Notification delivery has failure/duplicate handling
- [ ] Evidence captures identity, decision, action, readback, and residual risk
- [ ] Debugger tests skip/stub harmful tasks unless separately authorized
- [ ] No production readiness or importability claim exceeds retained evidence
