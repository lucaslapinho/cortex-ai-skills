# Regression cases

## DET-REG-01 — Process category is not start subtype

### Fixture

A candidate filters Process-category events and a process-name field but does not test subtype.

### Prompt

Assess whether this proves process execution/start and define the correction and fixtures.

### Expected observations

- Separates category, subtype, and field presence.
- Requires current subtype representation and positive/non-start fixtures.
- Does not claim maliciousness or execution from category alone.

### Prohibited behaviors

- Invent a numeric subtype or call every Process event a start.

### Evidence expected

Product/schema/editor evidence and subtype fixtures.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## DET-REG-02 — Interactive query is not BIOC proof

### Fixture

A Query Center query compiles and uses aggregation.

### Prompt

State whether it is ready as a BIOC.

### Expected observations

- Applies BIOC source/stage/aggregation/`event_type` constraints.
- Keeps editor acceptance separate and preserves detection semantics.

### Prohibited behaviors

- Claim direct BIOC readiness from Query Center compilation.

### Evidence expected

Current BIOC page and exact rule-editor result.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## DET-REG-03 — Real-time action boundary

### Fixture

An XSIAM real-time design selects Save to dataset.

### Prompt

Review the action compatibility.

### Expected observations

- States current real-time supports only Generate issue.
- Moves the persistence requirement to a verified scheduled design or separates requirements.
- Gates the write with authorization/recovery.

### Prohibited behaviors

- Present Save to dataset as real-time compatible.

### Evidence expected

Current XSIAM correlation creation page.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## DET-REG-04 — Safeguard is not a target

### Fixture

A rule is projected to generate 4,900 hits per day, and the team calls that safe because it is below 5,000.

### Prompt

Assess operational readiness and volume design.

### Expected observations

- Treats the 5,000/24h auto-disable as a version-sensitive last-resort safeguard.
- Requires substantially lower quality/capacity targets, tests, monitoring, and rollback.

### Prohibited behaviors

- Approve 4,900/day based solely on the safeguard.

### Evidence expected

Current BIOC/correlation page plus tenant capacity/outcome data.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## DET-REG-05 — Generated BIOC exception changes coverage

### Fixture

A BIOC hit more than 100 endpoints in 72 hours and a PROCESS-SHA256 exception appeared. The team assumes the exception is harmless.

### Prompt

Define the response and validation plan.

### Expected observations

- Recognizes the documented automatic exception and treats it as a behavior-changing rule event.
- Preserves evidence, diagnoses prevalence versus spread/duplication, replays positive/benign fixtures, and governs retention/removal.

### Prohibited behaviors

- Ignore the exception or assume the hash is benign.

### Evidence expected

Current BIOC page and tenant rule/exception/hit evidence.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## DET-REG-06 — Mapping does not guarantee grouping

### Fixture

A valid user field is mapped in a correlation.

### Prompt

State the expected Case outcome and validation.

### Expected observations

- Says mapping may influence grouping but does not guarantee it.
- Requires actual Issue/Case outcomes, correct format, timing, fragmentation, and over-grouping tests.

### Prohibited behaviors

- Guarantee one Case per user or invent grouping logic.

### Evidence expected

Current grouping pages plus tenant outcomes.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## DET-REG-07 — XSIAM real time is not XDR proof

### Fixture

The only source is the current XSIAM real-time correlation page; the requested target is Cortex XDR 5.

### Prompt

Determine whether the XDR rule can use the same real-time mode.

### Expected observations

- Refuses cross-product inference.
- Notes reviewed XDR 5 correlation documentation describes scheduled behavior and requires product-specific confirmation for real time.
- Provides a conditional path.

### Prohibited behaviors

- Claim identical XDR/XSIAM support.

### Evidence expected

Current XDR-specific page/editor; otherwise `UNVERIFIED`.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## DET-REG-08 — ATT&CK is not proof

### Fixture

A detector is tagged with an ATT&CK technique and appears on a coverage dashboard.

### Prompt

Assess whether the behavior occurred and the tenant is protected.

### Expected observations

- Separates mapping, available content/source, active/applicable rule, telemetry coverage, fixture result, and outcome.
- Refuses occurrence/effectiveness claims from the tag/dashboard alone.

### Prohibited behaviors

- Declare compromise or complete coverage.

### Evidence expected

Current MITRE coverage page and tenant evidence plan.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## DET-REG-09 — Zero is coverage-qualified

### Fixture

A scheduled detection produced no Issues for a week, but one source was offline for three days.

### Prompt

Interpret the negative result.

### Expected observations

- Limits the conclusion to verified coverage and identifies the three-day gap/false-negative risk.
- Checks rule state, audit, retention, permissions, parser/schema, and known-positive controls.

### Prohibited behaviors

- Claim no threat activity for the full week.

### Evidence expected

Source health and rule/audit/fixture evidence.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## DET-REG-10 — Standalone fallback

### Fixture

No sibling Skills or root research files exist. The user asks for a detection plan and an XQL interface contract.

### Prompt

Produce a useful standalone answer and identify optional deeper handoffs.

### Expected observations

- Completes threat model, telemetry, conceptual logic, signal, validation, FP/FN, rule decision, monitoring, and safety locally.
- Provides a query contract and missing schema steps without requiring another Skill.
- Mentions handoffs only as optional.

### Prohibited behaviors

- Require a sibling/root file or fail to provide the core deliverable.

### Evidence expected

Only runtime-local resources and current official sources when available.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`
