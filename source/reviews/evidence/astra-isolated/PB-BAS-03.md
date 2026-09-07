# Astra forward output — cortex-playbook-engineer

Model requested: `gpt-6-astra`, high reasoning; ephemeral CLI, manual inline runtime load.

Runtime: 20 files / 151241 bytes; ordinal SHA-256 `ee2624e64bbb650b98a9a7e7594bc8c3896d6f49bbc12fcf19801578f119ed4a`.

Isolation: 0 tool/action events. Runtime files plus Fixture/Prompt only; no oracle text supplied. One fresh ephemeral process contains this case only. No self-grading result is assigned here. Independent adjudication is required.

## Input PB-BAS-03

### Fixture

A parent workflow invokes a reusable enrichment sub-playbook. The child needs an observable and must return a normalized verdict and provenance.

### Prompt

Specify the parent/child contract using the packaged context-contract template and explain how to avoid hidden context coupling.

Local Markdown links are rebased for publication only; wording and attribution are unchanged. Raw response/event files remain in the evaluation archive outside the publication tree.

## Retained response

**PB-BAS-03**

Use separate child context with explicit input and output mappings. The parent supplies one validated observable; the child returns a verdict and source-linked provenance. Neither side should depend on undeclared context values.

**Artifact class:** `CONCEPTUAL`. Product is unspecified; this design conditionally targets Cortex XSIAM sub-playbooks. Deployment, release/build, license, installed content, execution identity, and tenant schemas remain unknown. An XSOAR implementation requires its own release-specific validation.

Contract names below are documentation labels, not verified Cortex paths. Proposed contracts and controls are `CONCEPTUAL / TENANT-UNVERIFIED`. Product guidance comes from the supplied 2026-09-04 snapshot, whose register reports targeted refreshes on 2026-09-06; no documentation was independently accessed here, and staleness remains possible.

**Contract identity:** Enrichment boundary, draft v1. Proposed owner: playbook engineering; accountable individuals and parent/child artifact versions are unresolved.

| ID | Name and meaning | Producer → consumer | Type and cardinality | Requiredness and default | Validation; empty/error behavior |
|---|---|---|---|---|---|
| IN-01 | Observable: kind, value, association key, source reference, observation time | Parent validation stage → child enrichment stage | One object; scalar members | Required; no default observable | Validate supported kind, format, length, freshness, and permitted scope. Missing, null, malformed, stale, or oversized input rejects the call; never substitute an observable. Accepted kinds and bounds require owner approval. |
| OUT-01 | Normalized verdict: association key, assessment, processing status, reason | Child normalization stage → parent decision stage | One object; scalar members | Required for every accepted invocation; no benign default | Proposed assessment: Unknown, Benign-supported, Suspicious, or Malicious-supported. Processing status: Complete, Degraded, or Failed. Missing/wrong-type output is a contract failure. Required-source failure yields Unknown with Degraded/Failed status; an unhandled child failure routes through the parent error path. |
| OUT-02 | Provenance: evidence supporting or limiting the assessment | Child evidence collector → parent decision and evidence stages | Array of records; zero to an approved maximum | Required array; no silent default when omitted | Each record carries association key, source identifier, source-record reference if available, observation/retrieval times, outcome, and sanitized evidence reference. Empty is permitted only with an explicit no-evidence/failed outcome in OUT-01. Missing output is a contract failure; malformed records cannot support a verdict. |

The assessment is analytical advice. It does not authorize containment, notification, or Case/Issue changes. “No result” must remain distinguishable from evidence supporting benign activity.

The following completes scope, mapping, sensitivity, and retention **for each value**:

| ID | Namespace/path evidence and mapping/write behavior | Sensitivity and redaction | Run lifetime | Post-run retention and deletion owner | Unresolved dimensions and validation owner |
|---|---|---|---|---|---|
| IN-01 | Exact parent source and child input paths unresolved. Parent explicitly copies validated members into the declared child input. Child observes the input without modifying the parent source. | Operational and potentially personal; reject secret-bearing input and omit unnecessary raw content from diagnostics. | Parent validation through child completion; no additional working copy needed afterward. | Proposed: no extra raw-observable copy in retained evidence. Existing source/context retention must be explicitly assessed; data-governance owner specifies deletion policy. | Source schema, kinds, size/freshness limits, mapping, runtime retention behavior: playbook engineering and platform owner. |
| OUT-01 | Exact producer, child output declaration, and parent destination paths unresolved. Child normalizer is the sole writer; parent explicitly maps the returned object into an invocation-specific result. | Operational and potentially sensitive; keep reason text bounded and sanitized. | Child normalization through parent decision and evidence handoff. | Proposed: retain a sanitized verdict with the investigation record. Duration, storage, access, and deletion mechanism unresolved; data-governance owner decides. | Enum mapping, output schema, destination, retention implementation: playbook engineering and platform owner. |
| OUT-02 | Exact collector, child output, and parent destination paths unresolved. Collector assembles records; one child aggregator writes the final array. Parent copies the declared output explicitly. | Potentially sensitive operational metadata; use access-controlled evidence references without credentials or secret-bearing URLs. | Child collection through parent decision and evidence handoff. | Proposed: retain sanitized provenance with the investigation record; avoid duplicating raw source data. Duration, reference availability, access, and deletion unresolved; evidence/data-governance owner decides. | Source schemas, maximum record count, evidence-store mapping, retention and reference lifetime: integration, platform, and evidence owners. |

These unresolved dimensions prevent implementation approval; the contract is reviewable as a draft.

To avoid hidden context coupling:

1. **Declare every dependency.** Pass the observable explicitly. If the child later needs policy, freshness limits, or source selection from the parent, add versioned inputs instead of reading parent context implicitly.
2. **Map outputs explicitly.** Connect verified producer fields to declared child outputs, then to parent destinations. Inspect the actual context selector, filter, and transformer behind “From Previous Tasks.”
3. **Keep separate context.** Do not enable sharing merely to fix a missing output. The supplied XSIAM guidance describes separate context and explicit I/O; exact release applicability remains `VERSION-DEPENDENT / DERIVATIVE / TENANT-UNVERIFIED`.
4. **Preserve association.** Match input, verdict, and provenance by the association key. Never correlate separate arrays by position.
5. **Assign one writer.** Parallel enrichment branches return distinct source results to a single aggregator. Concurrent child calls use separate invocation destinations.
6. **Validate authorization separately.** Context separation provides data-flow isolation; it does not establish confidentiality or command permission.

The child flow is: validate input → enrich through tenant-verified read capabilities → normalize evidence → return both outputs. The parent checks schema, association, processing status, and provenance before choosing its next branch. Unknown, conflicting, failed, or missing evidence routes to investigation rather than a successful benign outcome.

This contract accepts one observable per invocation. Collection iteration requires a separate bounded loop contract. Before implementation, integration owners must supply exact command help, versions, instance health, permissions, output schemas, timeout and rate behavior. Retry only documented transient, idempotent reads within an explicit attempt limit and total deadline.

Planned fixtures cover valid single input, missing/empty/null values, wrong types, duplicates, oversized input, stale evidence, producer failure, missing outputs, conflicting sources, unauthorized access, concurrent invocations, and sensitive content. Verify that each preserves association and cannot convert failure into benign success. These checks have not run.

The smallest next step is to confirm the product/release and supply sanitized parent input mappings, child output declarations, and installed producer schemas. Refresh the applicable official [sub-playbook guidance](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/playbooks/build-your-playbook/add-objects-from-the-task-library/add-sub-playbooks.md) and [context guidance](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/context-data/use-context-data-in-a-playbook.md) before configuration.

| Level | Result | Rationale |
|---|---|---|
| S | NOT RUN | No independent evaluation of this contract is available. |
| D | NOT RUN | Supplied documentation summaries informed the design; current official sources were not independently checked. |
| C | NOT RUN | No exact target schema, validator acceptance, or controlled import evidence exists. |
| E | NOT RUN | No parent/child execution, propagation, or permission test was performed. |
