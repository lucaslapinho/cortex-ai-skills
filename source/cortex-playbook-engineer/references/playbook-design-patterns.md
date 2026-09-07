# Playbook Design Patterns

**Documentation review cut:** 2026-09-04  
**Artifact class:** every pattern below is `CONCEPTUAL` unless a named product configuration is explicitly cited.  
**Import status:** no pattern is YAML/JSON or a `VERIFIED IMPORTABLE ARTIFACT`.
**Primary official evidence for native concepts:** [source register](official-sources.md), PB01-PB12, PB15-PB17, and CT08.

## Contents

- [Pattern selection](#pattern-selection)
- [End-to-end response controller](#end-to-end-response-controller)
- [Parent and reusable sub-playbooks](#parent-and-reusable-sub-playbooks)
- [Enrichment fan-out and deterministic join](#enrichment-fan-out-and-deterministic-join)
- [Approval-gated response](#approval-gated-response)
- [Degraded enrichment](#degraded-enrichment)
- [Idempotent job or replay handling](#idempotent-job-or-replay-handling)
- [Advisory AI](#advisory-ai)
- [Evidence and closure](#evidence-and-closure)
- [Anti-patterns](#anti-patterns)

## Pattern selection

Select a pattern only after naming the product, object, trigger, installed capabilities, risk, and artifact class. A design pattern explains control intent; it does not prove that a native task, command, or setting exists.

For each pattern define:

- entry and exit state;
- typed inputs and outputs;
- one owner for each state mutation;
- success, empty, error, timeout, retry, and cancellation paths;
- concurrency and duplicate-trigger behavior;
- approval and authority;
- evidence and recovery; and
- tenant validation plan.

## End-to-end response controller

**Class:** `CONCEPTUAL`

```text
Trigger
  -> Validate object, scope, freshness, and minimum evidence
  -> Enrich only validated entities
  -> Evaluate deterministic decision table
  -> Assemble investigation record and alternatives
  -> Request approval for protected action
  -> Apply least-scope containment
  -> Verify state/readback
  -> Remediate under separate authorization
  -> Verify behavior and residual risk
  -> Notify with minimum necessary data
  -> Persist evidence and close or escalate
```

Keep containment and remediation separate. A failed enrichment must not accidentally choose the most aggressive branch. A successful action command without readback is an indeterminate state, not completion.

## Parent and reusable sub-playbooks

**Class:** `CONFIGURATION GUIDANCE` for current XSIAM sub-playbook concepts; exact artifact remains tenant-unverified.

Use the parent for orchestration and business policy. Give each sub-playbook one responsibility, for example:

```text
Parent response controller
  -> ValidateTrigger sub-playbook
  -> CollectEvidence sub-playbook
  -> EnrichEntities sub-playbook
  -> AssessResponse sub-playbook
  -> ExecuteApprovedAction sub-playbook
  -> VerifyAndClose sub-playbook
```

Names above are conceptual, not installed playbook names. Each sub-playbook should expose generic explicit inputs and structured outputs. Record its pack/version relationship and whether it is custom, duplicated, detached, or attached to content updates.

Decompose when it improves reuse, testing, ownership, or readability. Current XSIAM best-practices guidance suggests considering decomposition for large playbooks; treat any numeric threshold as guidance, not a universal correctness rule.

## Enrichment fan-out and deterministic join

**Class:** `CONCEPTUAL`

Parallel read-only enrichment can reduce latency when data dependencies allow it:

```text
Validated entity
  +-> Source A enrichment --+
  +-> Source B enrichment --+-> Normalize -> Correlate by stable entity key -> Decision
  +-> Source C enrichment --+
```

Controls:

- validate each source independently;
- set per-source timeout/retry budgets;
- preserve source, retrieval time, confidence, and raw-result reference;
- distinguish empty, unknown, unavailable, stale, and error;
- join by a stable entity key, not list position;
- avoid simultaneous writes to one context key;
- define minimum evidence for each decision; and
- retain conflicting results rather than overwriting them.

Do not use a single reputation score as the action gate. Official DBotScore semantics include `0 = Unknown`; Unknown is not Good.

## Approval-gated response

**Class:** `CONCEPTUAL`, with current XSIAM manual/communication task capability available as possible implementation guidance.

```text
Candidate action
  -> Revalidate entity and current state
  -> Calculate exact scope and exclusions
  -> Show evidence, confidence, blast radius, and recovery to approver
  -> Decision: Approve | Reject | Request more evidence | Expire
  -> On Approve: recheck authorization and state, then act once
  -> Read back result
  -> Recover/escalate on partial or unexpected state
```

The approval result requires an authenticated, typed, auditable decision. Define who can complete the task, how late/duplicate answers behave, and what happens when SLA/no-response is reached. Never default expiry to approval.

## Degraded enrichment

**Class:** `CONCEPTUAL`

Use when optional evidence sources can fail without corrupting the core investigation:

| Failure class | Example design response |
|---|---|
| Optional source unavailable | Continue on explicit degraded branch; label evidence incomplete |
| Required identity/source unavailable | Stop action decision and escalate |
| Transient, idempotent failure | Retry within a bounded budget, then degrade/stop |
| Authentication/authorization failure | Do not retry blindly; preserve error and route to owner |
| Rate limit/quota | Honor known contract, slow/queue within deadline, avoid request storm |
| Timeout after possible external write | Reconcile target state before retrying |
| Malformed or hostile output | Quarantine, validate, and prevent it from changing control flow |

Current XSIAM supports Stop, Continue, and Continue on error path(s) for supported script task configurations. Use Continue only when downstream decisions remain sound without the output.

## Idempotent job or replay handling

**Class:** `CONCEPTUAL`

Scheduled/event-triggered Jobs and repeated Issues can create duplicate work. Before mutation:

```text
Derive bounded idempotency key
  -> Inspect prior state/evidence
  -> If completed: return existing result
  -> If in progress: avoid concurrent duplicate or escalate stale lease
  -> If unknown/failed: reconcile external target
  -> Execute once under authorization
  -> Persist outcome and readback
```

The idempotency key should combine the operation class, canonical target, trigger/Case/Issue identity, and requested state while avoiding secrets. Define retention and collision behavior. Do not call this a native Cortex feature unless the implementation is documented and tested.

## Advisory AI

**Class:** `CONCEPTUAL`

AI-produced summaries, classifications, or recommendations are untrusted advisory data:

```text
Sanitized bounded evidence
  -> AI advisory analysis
  -> Schema/content validation
  -> Deterministic policy and corroboration
  -> Human approval for protected action
```

Require a typed output schema, confidence semantics, source references, uncertainty, and failure path. Block prompt injection from Issue fields, email, logs, URLs, context, and retrieved documents. Do not allow a model to retrieve secrets, broaden scope, choose its own action target, or authorize containment.

## Evidence and closure

**Class:** `CONFIGURATION GUIDANCE` where using current XSIAM War Room/Case timeline/evidence options; exact settings remain tenant-unverified.

Create an append-only logical record containing:

- playbook/run/task and source object IDs;
- artifact version/hash and execution identity;
- sanitized input/output references;
- decisions, alternatives, confidence, approvals, and timestamps;
- errors, retries, timeouts, skipped/stubbed tasks, and degraded state;
- exact action request, target class/scope, returned status, and readback;
- recovery/rollback result;
- notifications and delivery result; and
- closure criteria, residual risks, and owner.

Quiet Mode can reduce task-result visibility/indexing while context remains available. If audit/evidence is required, design an intentional minimal record and validate it in the target release.

Closure requires both:

1. **Analytical closure:** evidence supports the conclusion at stated confidence, with alternatives/gaps recorded.
2. **Operational closure:** approved actions were verified or explicitly handed to an owner, notifications completed or failed visibly, and recovery/residual risk is assigned.

Do not invent a product close reason or silently close on incomplete evidence.

## Anti-patterns

| Anti-pattern | Why it fails | Safe replacement |
|---|---|---|
| Exact command guessed from its purpose | Can invoke a nonexistent or wrong integration action | State the capability and require installed command help |
| Plausible YAML generated without export schema | Looks import-ready but is unverified | Conceptual graph plus controlled-import checklist |
| `DBotScore <= 1` treated as benign | Conflates Unknown with Good | Preserve all official score states and corroborate |
| Empty output treated as clean | Hides errors, filters, context scope, and permissions | Distinguish empty, missing, error, and unknown |
| Global shared context everywhere | Creates coupling, collision, and lost-update risk | Explicit inputs/outputs and namespaced shared data only when justified |
| Parallel writers to one key | Can overwrite results | One writer, serialized merge, or tested append mechanism |
| Retry every error | Duplicates writes and amplifies permanent failures | Retry classified transient/idempotent cases only |
| Timeout treated as no action | External side effect may have completed | Reconcile current target state before retry |
| Manual task assumed to be approval | Completion identity and decision may be uncontrolled | Authenticated typed approval contract and audit |
| High confidence enables auto-containment | Confidence is not authorization or scope control | Independent evidence, policy/human gate, least scope, recovery/readback |
| Quiet Mode used for secrecy | Context and errors can remain available | Proper access control, minimization, and secret handling |
| Debugger assumed harmless | Tasks can still execute and change real state | Skip/stub harmful tasks and use reversible isolated targets |
| Child context treated as secure enclave | Context scope is not RBAC | Validate object/data/command permissions separately |
| Hard-coded placeholder observable | Pollutes evidence and can cause action on fictitious data | Reject/omit and route to data-quality error |
