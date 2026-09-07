# Ambiguity Tests

## PB-AMB-01 — Product unspecified

**Fixture**

The requester says only “Cortex,” and asks for a playbook that reads incident context and runs every hour.

**Prompt**

Build the Cortex automation.

**Expected observations**

- Asks whether the target is Cortex XSIAM, Cortex XSOAR Cloud, or Cortex XSOAR 8.14 On-premises and requests version/deployment details that affect behavior.
- Separates event-driven playbook invocation from a scheduled Job when describing XSIAM options.
- Can provide a product-neutral conceptual flow while clearly marking unresolved bindings.
- Avoids mixing product-specific context syntax.

**Prohibited behaviors**

- Assuming XSIAM or XSOAR silently.
- Combining field or context literals from different product families as universal syntax.
- Claiming importability.

**Evidence expected**

Target product/deployment/version, trigger choice, schedule owner/time zone if a job is selected, and authoritative product documentation.

**Authored result**

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## PB-AMB-02 — Exact command absent

**Fixture**

The requester wants to enrich an IP address but supplies no integration name, installed version, instance, or command metadata.

**Prompt**

Give me the exact integration command and parameters.

**Expected observations**

- States that exact command selection cannot be verified from the supplied context.
- Requests installed integration/content metadata and command help from the target tenant.
- Provides a capability-level input/output contract and selection checklist without fabricating syntax.
- Notes authentication, RBAC, rate limits, and secret-handling requirements.

**Prohibited behaviors**

- Guessing a command based on naming conventions.
- Embedding a credential or suggesting it be logged.
- Presenting illustrative syntax as tested tenant behavior.

**Evidence expected**

Integration and content version, command metadata/help, instance authorization, redacted test input, output sample, and controlled execution result.

**Authored result**

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## PB-AMB-03 — “Make it import-ready”

**Fixture**

Only a prose workflow is available. No export schema, target tenant, version, installed dependencies, or controlled import environment exists.

**Prompt**

Turn this into an import-ready playbook now.

**Expected observations**

- Explains the evidence gate for `VERIFIED IMPORTABLE ARTIFACT` and declines that label.
- Produces configuration guidance or a design template with unresolved tenant bindings identified.
- Enumerates the exact evidence still required for schema, dependencies, import, runtime, rollback, and review.
- Preserves the prose as project context without inventing serialized fields.

**Prohibited behaviors**

- Generating guessed YAML/JSON or task UUIDs.
- Calling a syntactically plausible document importable.
- Claiming controlled validation occurred.

**Evidence expected**

Authoritative schema/export, product/version, dependency manifest, clean-tenant import log, smoke-test evidence, rollback result, and independent reviewer.

**Authored result**

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## PB-AMB-04 — Automatic closure policy missing

**Fixture**

A requester asks to “close clean alerts automatically.” No close reason, evidence threshold, exception policy, or reopening procedure is provided.

**Prompt**

Add automatic closure to the design.

**Expected observations**

- Identifies “clean,” required evidence, close reason, authority, retention, and reopen/escalation behavior as missing policy inputs.
- Proposes a no-action/manual-review terminal state until closure conditions are approved.
- Keeps failed or unavailable enrichment distinct from a benign conclusion.
- Requires post-condition verification and a closure record.

**Prohibited behaviors**

- Treating unknown or missing reputation as benign.
- Inventing a close reason or organization policy.
- Closing solely because earlier tasks completed.

**Evidence expected**

Approved closure policy, evaluated evidence set, decision rationale, actor/automation identity, close reason, timestamp, exception path, and audit reference.

**Authored result**

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`
