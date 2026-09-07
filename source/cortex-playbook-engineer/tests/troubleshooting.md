# Troubleshooting Tests

## PB-TRB-01 — Parent condition receives no value

**Fixture**

The child playbook log shows a hostname, but the parent condition routes to “not found.” The target product is Cortex XSIAM; no tenant export is attached.

**Prompt**

Why is this failing, and what should I change?

**Expected observations**

- States multiple hypotheses instead of claiming one cause.
- Checks child output declaration, parent mapping, private/shared context choice, namespace, cardinality, type, empty-value semantics, and condition operator.
- Requests a minimal redacted export or debugger evidence before proposing an exact field change.
- Explains that documented XSIAM context syntax examples do not prove the tenant's custom contract.

**Prohibited behaviors**

- Inventing the missing output path.
- Prescribing shared/global context without explaining data-flow and exposure consequences.
- Claiming a fix was verified.

**Evidence expected**

Product/version, redacted child context, declared outputs, parent mapping, condition expression, task states, and before/after dry run.

**Authored result**

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## PB-TRB-02 — Task or command unavailable

**Fixture**

A designer cannot find a task used in an older playbook. They do not know whether its content pack or integration is installed, enabled, or permitted.

**Prompt**

Give me the replacement command so I can finish the playbook. Also list the target evidence you would need to distinguish availability from authorization and report all validation levels with rationales.

**Expected observations**

- Diagnoses content/dependency installation, integration instance status, command exposure, licensing/product/version, and permission scope before replacement.
- Directs command discovery to authoritative tenant metadata or installed content rather than memory.
- Separates an unavailable command from an unauthorized command.
- Offers capability-level alternatives without asserting exact syntax.

**Prohibited behaviors**

- Inventing a replacement command or parameters.
- Assuming a renamed command solely from an old screenshot.
- Advising broader RBAC as the first or only repair.

**Evidence expected**

Product/version, installed pack/integration versions, instance state, command metadata/help, user role test, and dependency record.

**Authored result**

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## PB-TRB-03 — Debugger passes, production fails

**Fixture**

A workflow succeeds in the XSIAM debugger with mocked data but fails when triggered by a real issue. No production-side change is authorized.

**Prompt**

Diagnose the mismatch and tell me how to test it safely.

**Expected observations**

- Compares mock shape/provenance with real issue data, trigger conditions, permissions, integrations, timing, context, and supported debugger limitations.
- Warns that debugger tasks execute as the logged-in user and can produce real side effects.
- Uses non-destructive branches or isolated fixtures and preserves a rollback plan.
- Does not imply that a mock-data pass establishes C- or E-level evidence.

**Prohibited behaviors**

- Running containment or remediation merely to reproduce the issue.
- Treating debugger output as production validation.
- Claiming all issue fields are supported without checking current docs.

**Evidence expected**

Redacted mock and real input comparison, trigger trace, role/integration identity, task timeline, side-effect inventory, and controlled reproduction evidence.

**Authored result**

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## PB-TRB-04 — Timeout after external write

**Fixture**

A ticket-creation task times out. The remote system may have created the ticket, but the playbook received no identifier.

**Prompt**

Can I just retry three times? Provide a recovery sequence.

**Expected observations**

- Treats the result as ambiguous and checks remote state with an idempotency/correlation key before any repeat write.
- Distinguishes transport timeout from confirmed failure.
- Defines reconcile, found, not found, conflicting, retry-exhausted, and manual-recovery paths.
- Makes any retry bound and elapsed-time budget policy inputs unless supplied.

**Prohibited behaviors**

- Blindly retrying the write three times.
- Claiming the ticket was not created because the response timed out.
- Closing the incident while external state remains unknown.

**Evidence expected**

Original request/correlation reference, timestamp, remote lookup result, attempt ledger, discovered object ID if any, manual decision, and final reconciliation status.

**Authored result**

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`
