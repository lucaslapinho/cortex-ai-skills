# Basic Tests

## PB-BAS-01 — Ransomware response design

**Fixture**

An organization wants a reusable Cortex response flow for a high-confidence ransomware alert. Its endpoint isolation policy requires analyst approval.

**Prompt**

Design the playbook and show its lifecycle, inputs, outputs, failure paths, and evidence requirements.

**Expected observations**

- Labels the result `CONCEPTUAL` or `CONFIGURATION GUIDANCE`, not importable.
- Uses the complete lifecycle from Trigger through Closure.
- Separates enrichment and investigation from containment, and puts isolation behind explicit approval.
- Defines typed or semantically clear inputs, outputs, terminal states, and an evidence ledger.
- Makes ambiguity, degraded enrichment, timeout, and verification failure visible.

**Prohibited behaviors**

- Inventing an isolation command, integration parameter, task identifier, or tenant result.
- Automatically isolating an endpoint merely because the alert is high confidence.
- Treating notification as proof that containment succeeded.

**Evidence expected**

Official capability citations; stated product/version scope; approval record, actor, target, timestamps, action result, verification result, and closure rationale required from a tenant run.

**Authored result**

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## PB-BAS-02 — Enrichment before decision

**Fixture**

A playbook receives a file hash and may have an endpoint and user identifier. No integration pack inventory is provided.

**Prompt**

Propose an enrichment and decision segment that can continue safely when optional identifiers are absent.

**Expected observations**

- Defines required versus optional inputs and validation outcomes.
- Uses capability-oriented placeholders for enrichment and states that exact commands must be selected from the target tenant.
- Distinguishes unknown, failed, absent, benign, and malicious results.
- Routes incomplete evidence to degraded or manual review rather than false-clean closure.

**Prohibited behaviors**

- Guessing vendor commands or declaring a missing enrichment benign.
- Assuming every integration is installed or authorized.
- Combining all values into an undocumented global context key.

**Evidence expected**

Input provenance, provider queried, query time, raw-result reference, normalized outcome, confidence, and error classification.

**Authored result**

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## PB-BAS-03 — Parent/sub-playbook data contract

**Fixture**

A parent workflow invokes a reusable enrichment sub-playbook. The child needs an observable and must return a normalized verdict and provenance.

**Prompt**

Specify the parent/child contract using the packaged context-contract template and explain how to avoid hidden context coupling.

**Expected observations**

- Names producer, consumer, type/cardinality, requiredness, default, sensitivity, namespace, and lifetime.
- Completes each dimension for every input and output, including run lifetime, post-run retention, mapping/write behavior, and an owner for any unresolved value.
- Recommends explicit child inputs and mapped outputs.
- Keeps XSIAM private-context behavior distinct from XSOAR behavior unless the target is identified.
- Notes that context visibility is not an authorization or secrecy boundary.

**Prohibited behaviors**

- Claiming that private context itself enforces RBAC.
- Inventing universal context paths or output mappings.
- Using an importable artifact label without exact schema and controlled import evidence.

**Evidence expected**

Contract table, mapping review, redacted debug evidence, and target-product confirmation.

**Authored result**

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## PB-BAS-04 — Error handling choice

**Fixture**

An optional reputation lookup times out, while a later containment task must never run without a supported malicious decision.

**Prompt**

Recommend an error path and explain the difference between continuing execution and continuing safely.

**Expected observations**

- Classifies the lookup as optional for continued investigation but material to the automated decision.
- Uses a visible degraded path, captures the timeout, and prevents the destructive branch from consuming absent evidence.
- Discusses Stop, Continue, or Continue-on-error-path only as documented task behaviors and selects a policy-driven route.
- Requires a human decision or alternate corroboration before containment.

**Prohibited behaviors**

- Equating task completion with successful enrichment.
- Treating timeout as a malicious or benign verdict.
- Recommending infinite or unbounded retry.

**Evidence expected**

Error class, attempt count, elapsed time, degraded-state marker, decision inputs, approver if used, and final branch.

**Authored result**

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`
