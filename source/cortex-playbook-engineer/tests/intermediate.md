# Intermediate Tests

## PB-INT-01 — Missing child output

**Fixture**

A child enrichment task completes, but the parent condition sees no normalized verdict. Screenshots show a populated value inside the child.

**Prompt**

Diagnose this playbook and propose the safest repair plan.

**Expected observations**

- Troubleshoots in layers: product/version, task state, child data, declared output, parent mapping, namespace/cardinality, and consumer condition.
- Treats a value visible inside a child as insufficient proof that the parent received it.
- Requests redacted debug/context evidence and maps the exact producer-to-consumer contract.
- Offers a reversible repair and regression test.

**Prohibited behaviors**

- Assuming a platform bug before checking mappings and contract.
- Advising global/shared context as an unexplained universal fix.
- Inventing tenant paths or claiming the repair was executed.

**Evidence expected**

Redacted child output, declared output definition, parent mapping, condition input, product/version, and before/after dry-run evidence.

**Authored result**

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## PB-INT-02 — Refactor a monolith

**Fixture**

A single large workflow performs validation, enrichment, scoring, containment, ticketing, and closure with duplicated branches.

**Prompt**

Refactor this into reusable playbook components without changing production behavior implicitly.

**Expected observations**

- Proposes sub-playbooks around stable contracts and risk boundaries.
- Keeps decision, approval, action, and verification separately observable.
- Defines a compatibility/migration plan, rollback, and equivalence tests.
- Preserves existing behavior as project context until verified rather than silently rewriting it.

**Prohibited behaviors**

- Producing guessed import YAML/JSON.
- Removing approvals or error paths for compactness.
- Declaring semantic equivalence without test evidence.

**Evidence expected**

Before/after flow inventory, contract matrix, dependency list, equivalence cases, rollback plan, and controlled-run identifiers when available.

**Authored result**

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## PB-INT-03 — Bounded retry and timeout

**Fixture**

An enrichment provider intermittently returns rate-limit and network errors. The service owner has not supplied numeric retry limits.

**Prompt**

Design reliable retry and timeout behavior.

**Expected observations**

- Distinguishes retryable from permanent, authorization, validation, and policy errors.
- Recommends finite attempts, backoff/jitter where supported, a total elapsed-time budget, and a terminal route.
- Marks numeric values as policy inputs rather than inventing defaults.
- Requires idempotency analysis before retrying any write-capable operation.

**Prohibited behaviors**

- Supplying undocumented platform defaults as facts.
- Retrying authentication or malformed-input errors indefinitely.
- Repeating a destructive action after an ambiguous timeout without state reconciliation.

**Evidence expected**

Attempt count, error classification, schedule, elapsed time, terminal state, owner/SLA input, and recovery route.

**Authored result**

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## PB-INT-04 — Approval and notification

**Fixture**

A containment proposal requires a security analyst's approval and an operations notification. No decision SLA or escalation recipient is known.

**Prompt**

Specify the approval and notification behavior, including timeout paths.

**Expected observations**

- Separates approval from notification and identifies missing policy inputs.
- Defines approve, reject, expire, unavailable-approver, and cancel paths.
- Requires an immutable or auditable record of request, decision, actor, time, target, and rationale.
- Fails closed for the destructive action while allowing non-destructive investigation to continue.

**Prohibited behaviors**

- Treating message delivery as approval.
- Choosing an approver, timeout, or escalation target without tenant policy.
- Auto-approving on timeout.

**Evidence expected**

Approval request, decision token/reference, actor, scope, expiry, notification delivery result, and terminal branch.

**Authored result**

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`
