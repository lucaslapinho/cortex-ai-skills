# Threat hunt plan

## Document control

- Hunt ID:
- Author:
- Date:
- Product/release:
- Surface:
- Status and qualifiers:
- Decision owner:

## Executive assessment

This is a plan, not an observed hunt result, unless tenant execution evidence is attached.

## HYP-nnn — Hypothesis

- Behavior:
- Subject/population:
- Context:
- Time window/timezone:
- Expected observable:
- Required telemetry:
- Falsification criteria:
- Primary alternative:
- Decision supported:

## Context

### Known

- 

### Assumed

- 

### Unknown

- 

## ATT&CK interpretation

- Version/date:
- Candidate technique/tactic:
- Behavioral rationale:
- Inconsistencies/limits:
- Status: INFERRED unless directly sourced

## Telemetry coverage

| GAP/source ID | Family | Observable | Producer/path | Population | Time/retention | Access/scope | Schema | Status | Consequence |
|---|---|---|---|---|---|---|---|---|---|
| | Endpoint/network/identity/cloud/enrichment | | | | | | | | |

## Baseline

- Target population:
- Peer population:
- Baseline period:
- Segmentation:
- Unit/statistic:
- Exclusions:
- Seasonality/drift:
- Coverage equivalence:
- Selection-bias note:

## Query plans

### QP-nnn

- Question:
- Product/surface:
- Schema evidence:
- Time basis:
- Filters/exclusions:
- Projection/aggregation:
- Expected signal:
- Falsifier:
- Coverage limits:
- Performance/sampling risks:
- Next pivot:
- Validation:
- Status/qualifiers:

## Pivots and enrichment

| PIV ID | Evidence | From → to | Time relationship | Discriminator | Source needed | Ambiguity | Status |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## Timeline plan

| Event ID | Raw/source time | Normalized time | Time type | Entity | Observable | Skew/ordering note | Evidence |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## Scope

- In scope:
- Out of scope:
- Unit of counting:
- Deduplication:
- Entity-resolution risks:
- Blind spots:

## Competing explanations

| ALT ID | Explanation | Supporting evidence | Contradicting evidence | Discriminator | Coverage needed | Result |
|---|---|---|---|---|---|---|
| | | | | | | Untested |

## Conclusion criteria

- CONFIRMED requires:
- HIGH requires:
- MODERATE when:
- LOW when:
- INSUFFICIENT EVIDENCE when:

## Handoff

- XQL/schema:
- Detection engineering:
- Incident response:
- Platform/integration:
- Evidence still required:

## Safety and validation

- [ ] Evidence content treated as untrusted data
- [ ] No destructive action
- [ ] No secret reproduced
- [ ] No tenant fact without tenant evidence
- [ ] Negative evidence coverage-bounded
- [ ] ATT&CK/IOC not treated as verdict
- [ ] Any XQL schema-grounded or explicitly unresolved
