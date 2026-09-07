# Astra forward output — cortex-playbook-engineer

Model requested: `gpt-6-astra`, high reasoning; ephemeral CLI, manual inline runtime load.

Runtime: 20 files / 150928 bytes; ordinal SHA-256 `ac23c52e0f5d57cfcacd713d9e8d58a3906fa6e4750bf3374c1fa72da0883976`.

Isolation: 0 tool/action events. Runtime files plus Fixture/Prompt only; no oracle text supplied. Multiple cases share a single process for this Skill; they are not independently randomized sessions. No self-grading result is assigned here. Independent adjudication is required.

## Input PB-BAS-03

### Fixture

A parent workflow invokes a reusable enrichment sub-playbook. The child needs an observable and must return a normalized verdict and provenance.

### Prompt

Specify the parent/child contract using the packaged context-contract template and explain how to avoid hidden context coupling.

## Input PB-REG-03

### Fixture

A reviewer proposes using the XSIAM debugger to run the entire containment branch against an existing issue because “debug mode is only a simulation.” The graph has parallel tasks, and the reviewer expects a breakpoint in one branch to stop a side-effecting task already running in the other branch.

### Prompt

Review the proposed test plan and report S, D, C, and E separately with their results and rationales.

## Retained response

**PB-BAS-03**

Use explicit parent-to-child input mapping and declared child outputs. Keep the child’s context separate and give the parent sole ownership of the destination values.

**Artifact class: `CONCEPTUAL`.** Product was not supplied; this design selects **Cortex XSIAM as an explicit assumption**. Target deployment/build, license/entitlement, playbook versions, installed integrations, permissions, and literal context paths remain unknown. Confirm the product before configuration; this contract does not establish XSOAR compatibility.

The proposed contract is `CONCEPTUAL`. XSIAM context behavior is `VERSION-DEPENDENT / DERIVATIVE / TENANT-UNVERIFIED`, based on the supplied documentation summaries. The source snapshot is dated **2026-09-04**, with a reported targeted refresh on **2026-09-06**; no source was independently reopened here.

**Contract identity**

Contract `EnrichmentContract-v1` is a documentation label, not an installed object. The proposed owner is the playbook maintainer; the accountable individual remains unresolved. Parent, child, content versions, and update relationships must be recorded before implementation.

The child enriches **one observable per invocation**. It produces an evidence assessment; it performs no containment, notification, or Case/Issue mutation.

| ID | Name and meaning | Producer → consumer | Type and cardinality | Requiredness, default, and validation |
|---|---|---|---|---|
| IN-01 | `Observable`: entity to enrich, with source provenance | Parent validation stage → child validation/enrichment | Exactly one object containing one observable kind, value, source reference, and observation timestamp | Required; no default. Validate supported kind, corresponding value format, provenance, freshness, and permitted data scope. Supported kinds, length limits, and freshness window remain unresolved; maintainer and security owner must define them. |
| OUT-01 | `Verdict`: normalized assessment and completeness | Child normalization stage → parent decision stage | Exactly one object: `assessment` = Unknown, Good, Suspicious, or Bad; `outcome` = Complete, Partial, InvalidInput, or Error | Required on every handled path; no implicit success or benign default. Only Complete or Partial may carry a non-Unknown assessment, and only under an explicit source-normalization rule. |
| OUT-02 | `Provenance`: evidence supporting or limiting the verdict | Child evidence collector → parent investigation/evidence stage | Required array containing 0–10 source-attempt records; proposed hard limit of ten configured sources, one record per source | No implicit empty default. Each record contains source reference, retrieval time, status, sanitized evidence reference or its explicit absence reason, and interpretation/coverage limits. Source observation time may be absent only with that gap recorded. |

These names and fields are **conceptual contract labels**, not verified Cortex paths or integration output keys. The ten-source bound is a design choice requiring capacity validation.

**Per-value propagation and lifecycle**

| ID | Empty, missing, and error behavior | Namespace, mapping, and write behavior | Sensitivity and redaction | Run lifetime, post-run retention, and owner |
|---|---|---|---|---|
| IN-01 | Missing, null, malformed, stale, or out-of-scope input prevents enrichment. Return Unknown/InvalidInput where the child can handle the failure; never fabricate an observable. | Literal source and child-input paths are unresolved; maintainer must validate against the target export. Parent copies its validated object through an explicit input mapping. Child treats it as immutable. | Operational and potentially personal data. Reject secret-bearing input; use sanitized references in evidence. | Child copy needed until child completion. Parent original follows its source-record policy. Actual cleanup mechanism and post-run retention are unresolved; platform and data-retention owners must establish them. |
| OUT-01 | Missing/null output or an unhandled child failure is a contract failure: parent routes to investigation/error handling. Handled producer failure returns Unknown/Error. Legitimate lack of findings returns Unknown with an explicit completeness outcome. | Child declares the output; parent explicitly maps it to a destination reserved for this invocation. Literal paths remain unresolved; maintainer validates them. Child writes its result once; parent is the sole destination writer. | Operational security assessment. Exclude raw sensitive evidence and secret values. | Available until parent decision and evidence capture finish. Post-run retention duration, storage, and deletion mechanism remain unresolved; incident-response and data-retention owners must assign them. |
| OUT-02 | Empty array is allowed only when no source was queried, with the reason recorded in the verdict path. An attempted source must yield a record, including failure or no-data status. Missing/null array is a contract failure. Never silently truncate excess records. | Child builds its own records and declares the array output. Parent explicitly copies it to its investigation record. Literal paths remain unresolved; maintainer validates them. Parallel tasks return independent results to one collector; they do not append concurrently to one shared key. | Source references and diagnostics may contain operational or personal data. Redact identifiers, URLs, and errors as necessary; keep credentials out entirely. | Available through parent investigation and evidence capture. Post-run evidence retention and deletion owner are unresolved; data-retention owner must set the period and platform owner must validate enforcement. |

All required contract dimensions are stated; unresolved values remain implementation dependencies.

**Avoid hidden coupling**

1. Map each input from its verified source explicitly. “From Previous Tasks” does not establish the selected context source, filter, type, or cardinality.
2. Keep child context separate and export only the declared verdict and provenance. Context separation does **not** establish confidentiality or authorization.
3. Do not let the child read undeclared parent or global values, including policy settings. If policy must vary by caller, add a fully specified input contract.
4. Preserve association between the observable and its results using an explicit invocation/observable association maintained by the parent. Do not correlate parallel arrays by position.
5. Normalize each source through documented mappings. Unknown, no data, source error, and contradictory evidence remain distinguishable. A reputation assessment alone cannot authorize response.
6. Return source-specific results to one collector. Required-source failure blocks a conclusive assessment; optional-source failure produces Partial with the missing coverage recorded.

Command names, arguments, output schemas, instance routing, and effective permissions remain unresolved. The integration owner must validate them. Read timeouts, retry budgets, service limits, and a total child deadline also require explicit values before implementation; retry only documented transient, idempotent reads.

Acceptance fixtures should cover valid single input, prohibited multiple input, empty/null/wrong type, duplicate invocation, oversized input/results, conflicting evidence, producer timeout/error, missing declared output, private-context propagation, permission denial, and concurrent invocations. These are planned checks, not observed results.

The smallest next step is to confirm the product and obtain the sanitized parent/child definitions and producer output schema. Relevant official references are [PB05: Add sub-playbooks](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/playbooks/build-your-playbook/add-objects-from-the-task-library/add-sub-playbooks.md) and [PB09: Use context data](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/context-data/use-context-data-in-a-playbook.md). Reopen them for the target release before configuration.

**Design decision:** draft contract suitable for discussion; implementation and release remain blocked by the stated tenant gaps.

| Level | Result | Rationale |
|---|---|---|
| S | NOT RUN | No independent static or behavioral evaluation of this contract is available. |
| D | NOT RUN | Supplied summaries provide documentation provenance, including a reported refresh; current official sources were not independently inspected in this session. |
| C | NOT RUN | No target schema, validator acceptance, or controlled import evidence exists. |
| E | NOT RUN | No parent/child propagation, permission, error-path, or enrichment execution was performed. |

**PB-REG-03**

**Reject the proposed test plan as written.** The supplied XSIAM documentation states that debugger tasks execute normally and can cause real side effects. A breakpoint in one branch does not stop tasks already running in another branch.

**Artifact class: `CONFIGURATION GUIDANCE`.** Product: Cortex XSIAM; surface: playbook debugger using an existing Issue. Target tenant build, license/entitlement, containment integration, execution identity, permissions, and exact graph are unknown.

The debugger behavior above is `VERSION-DEPENDENT / DERIVATIVE / TENANT-UNVERIFIED` here: it is supported by the supplied documentation summaries, including their reported **2026-09-06 PB10 refresh**, but was not independently checked against the target. The broader snapshot is dated **2026-09-04** and may become stale.

| Severity | Exact location in the supplied proposal | Impact | Required remediation | Disposition |
|---|---|---|---|---|
| CRITICAL | “Run the entire containment branch … because ‘debug mode is only a simulation.’” | Containment tasks may change real external state under the logged-in user’s permissions. Using an existing Issue as test data does not make those tasks harmless. | Before starting, skip or stub every protected task and supply typed synthetic outputs. Conduct real containment testing only with exact authorization, bounded reversible targets, recovery, and readback. | OPEN; blocks the proposed run |
| HIGH | Expectation that “a breakpoint in one branch” stops a side-effecting task already running in the other | The parallel action can continue after the breakpoint is reached. A pause cannot establish that no action occurred. | Review every reachable parallel path and prevent protected tasks from starting. If any task has already started, reconcile its platform/external effects; do not infer cancellation from the breakpoint. | OPEN; blocks the proposed run |

These locations identify the supplied proposal text. No task IDs, edges, or live execution state were provided.

**Replacement test plan**

1. **Inventory all effects before launch.** The playbook maintainer identifies containment, remediation, Case/Issue writes, external notifications, and other mutations across every branch and nested playbook.
2. **Prepare isolated fixtures and identity.** Prefer synthetic data in an approved development environment with a least-privilege test identity. Existing-Issue selection preserves the original test-data Issue/context according to the supplied guidance; tasks can still affect other state.
3. **Prevent protected execution.** Skip or stub every mutating task before any branch starts. Override downstream outputs with typed synthetic success, denial, timeout, partial, and unknown-state results. An output override alone is not evidence that the underlying action was prevented.
4. **Use breakpoints for inspection.** Place them to examine inputs, context, decisions, and approval handling. Account explicitly for already-running parallel tasks; debugger skips and overrides are session-scoped according to the supplied guidance.
5. **Exercise failure paths.** Include rejected/expired approval, unauthorized identity, timeout after a possible action, contradictory readback, partial batch completion, and notification failure. Unknown action state must prevent success-only closure.
6. **Retain bounded evidence.** Record artifact version/hash, fixture, identity, protected-task controls, run/task references, sanitized outputs, expected versus observed branches, and any actual side effects.
7. **Test real containment separately when authorized.** Start with one named noncritical test endpoint, fresh corroborated evidence, an authenticated last-point approval, validated command permissions, recovery owner, and independent state readback. A timeout requires reconciliation before retry.

If a side-effecting task has already started, the run must be treated as potentially state-changing. The response owner should establish its actual outcome and invoke authorized recovery when necessary; no cancellation command can be selected from the evidence supplied.

The official refresh target is [PB10: Test your playbook](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/playbooks/build-your-playbook/test-your-playbook.md), followed by the exact installed command help and target permission configuration.

**Test-plan decision:** blocked pending correction. That decision is separate from validation results; this authored review does not establish an independent S evaluation or an observed execution failure.

| Level | Result | Rationale |
|---|---|---|
| S | NOT RUN | Findings assess the supplied proposal; no independent graph or behavioral evaluation was retained. |
| D | NOT RUN | The supplied register reports a PB10 refresh supporting real effects and parallel-task behavior, but no current official-document check occurred in this session. |
| C | NOT RUN | No exact artifact, validator result, schema acceptance, or controlled import was supplied. |
| E | NOT RUN | No debugger execution, containment, cancellation, external readback, or recovery was observed. |
