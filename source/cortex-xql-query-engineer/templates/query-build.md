# XQL Query Build Template

Use this template to turn a security question into a bounded XQL query or, when evidence is insufficient, a validation-ready query design. Replace every `{{PLACEHOLDER}}`. Never leave a placeholder inside a block labeled executable.

## 1. Objective

- Security question: `{{QUESTION}}`
- Decision the results will support: `{{DECISION}}`
- Intended consumer: `{{INVESTIGATOR | HUNTER | DETECTION AUTHOR | OTHER}}`
- Read-only scope: `{{YES/NO; EXPLAIN IF NO}}`

## 2. Product and execution context

| Item | Value |
|---|---|
| Product | `{{CORTEX XDR / CORTEX XSIAM}}` |
| Product version/release line | `{{KNOWN VALUE / UNKNOWN}}` |
| Surface | `{{QUERY CENTER / SAVED QUERY / API / WIDGET / BIOC / SCHEDULED CORRELATION / REAL-TIME CORRELATION / XQLP}}` |
| Edition/license | `{{KNOWN VALUE / REQUIRES VALIDATION}}` |
| Identity and data scope | `{{ROLE/SBAC SCOPE WITHOUT SECRETS / REQUIRES VALIDATION}}` |
| Timeframe | `{{BOUNDED WINDOW}}` |
| Source review date | `{{YYYY-MM-DD}}` |

If product or surface is unknown and the choice changes syntax or compatibility, state the ambiguity and stop before producing an executable block.

## 3. Evidence status

- Canonical class: `{{VERIFIED | VERSION-DEPENDENT | INFERRED | CONCEPTUAL | UNSUPPORTED | DEPRECATED | UNVERIFIED}}`
- Qualifiers: `{{OFFICIAL-CURRENT | OFFICIAL-EXAMPLE | TENANT-UNVERIFIED | TENANT-SCHEMA-VERIFIED | TENANT-COMPILED | TENANT-EXECUTED | OTHER APPLICABLE QUALIFIERS}}`
- `S`: `{{PASS | FAIL | NOT RUN | N/A}} — {{RATIONALE}}`
- `D`: `{{PASS | FAIL | NOT RUN | N/A}} — {{RATIONALE}}`
- `C`: `{{PASS | FAIL | NOT RUN | N/A}} — {{RATIONALE}}`
- `E`: `{{PASS | FAIL | NOT RUN | N/A}} — {{RATIONALE}}`
- Evidence IDs/links: `{{SOURCE RECORDS OR DIRECT OFFICIAL LINKS}}`
- Unverified conditions: `{{DATASET | FIELD TYPES | POPULATION | PERMISSIONS | LICENSE | RETENTION | COMPILER | RESULTS | PERFORMANCE}}`

Do not use `TENANT-COMPILED` or `TENANT-EXECUTED` unless the corresponding evidence is recorded below.

## 4. Assumptions and telemetry contract

| Assumption | Why it matters | Status | Smallest check |
|---|---|---|---|
| `{{ASSUMPTION}}` | `{{EFFECT ON QUERY OR INTERPRETATION}}` | `{{EVIDENCE CLASS / QUALIFIERS}}` | `{{CHECK}}` |

### Dataset

- Dataset or data model: `{{EXACT NAME ONLY IF VERIFIED}}`
- Why it represents the required telemetry: `{{RATIONALE}}`
- Tenant discovery evidence: `{{SCHEMA SCREENSHOT/EXPORT/QUERY RECORD | NOT AVAILABLE}}`
- Retention and ingestion coverage: `{{OBSERVED VALUE | REQUIRES VALIDATION}}`

### Fields

| Field | Purpose | Expected type | Official evidence | Tenant evidence | Null behavior |
|---|---|---|---|---|---|
| `{{FIELD}}` | `{{FILTER/PROJECT/GROUP/JOIN}}` | `{{TYPE / UNKNOWN}}` | `{{LINK / NONE}}` | `{{OBSERVED / NOT OBSERVED}}` | `{{HANDLING}}` |

Do not infer a field from a filename, a local namespace, a sample result, or a similar product. If a required dataset or field is unknown, provide a discovery plan instead of a guessed query.

## 5. Query

Choose exactly one status and keep the label immediately above the block.

### Option A — documentation-grounded constructs, tenant not validated

**Query evidence:** `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED`  
**Validation:** `S: {{PASS/FAIL/NOT RUN/N/A - RATIONALE}}; D: PASS - {{DATED SOURCES AND RATIONALE}}; C: NOT RUN - {{NO TENANT COMPILER/IMPORT EVIDENCE}}; E: NOT RUN - {{NO TENANT EXECUTION EVIDENCE}}`  
**Product/surface:** `{{PRODUCT AND SURFACE}}`

```xql
{{FULLY SUBSTITUTED QUERY USING ONLY EVIDENCED CONSTRUCTS}}
```

### Option B — unresolved schema or semantics

**Query evidence:** `CONCEPTUAL / TENANT-UNVERIFIED`  
**Validation:** `S: {{PASS/FAIL/NOT RUN/N/A - RATIONALE}}; D: {{PASS/FAIL/NOT RUN/N/A - RATIONALE}}; C: NOT RUN - {{NO TENANT COMPILER/IMPORT EVIDENCE}}; E: NOT RUN - {{NO TENANT EXECUTION EVIDENCE}}`

```text
config timeframe = {{BOUNDED_WINDOW}}
| dataset = {{TENANT_VERIFIED_DATASET}}
| filter {{TENANT_VERIFIED_BOOLEAN_EXPRESSION}}
| fields {{TENANT_VERIFIED_OUTPUT_FIELDS}}
| limit {{REASONED_LIMIT}}
```

Before converting Option B to XQL, verify every placeholder and the target surface. Do not present it in an `xql` code fence.

## 6. Stage-by-stage explanation

| Stage | Purpose | Semantic risk | Evidence |
|---|---|---|---|
| `{{STAGE}}` | `{{PURPOSE}}` | `{{TYPE/NULL/CARDINALITY/ORDER/CONTEXT RISK}}` | `{{SOURCE OR TENANT RECORD}}` |

Call out these non-obvious effects when used:

- `fields` removes non-retained fields; downstream stages must use an alias after `as`.
- `comp` changes row cardinality and drops original non-grouped/non-computed fields.
- `join` requires verified key semantics, compatible types, a deliberate join type and conflict strategy, and cardinality analysis.
- `sort` after `join` or `union` is required when final ordering matters.
- `limit` after `sort` selects the requested top/bottom rows; an earlier limit can change the population.

## 7. Expected output and interpretation

- Grain: `{{ONE ROW PER EVENT/HOST/USER/GROUP}}`
- Columns: `{{COLUMN AND MEANING}}`
- Expected ordering: `{{ORDER | UNSPECIFIED}}`
- Expected volume: `{{ESTIMATE | UNKNOWN}}`
- Positive result means: `{{BOUNDED INTERPRETATION}}`
- Zero rows mean: `{{NO MATCHES VISIBLE UNDER THIS TIMEFRAME, IDENTITY, COVERAGE, AND LOGIC}}`
- Zero rows do **not** establish: `{{ABSENCE OF ACTIVITY/COMPROMISE}}`

## 8. False positives, false negatives, and limitations

- Likely benign explanations: `{{LIST}}`
- Likely missed activity: `{{LIST}}`
- Collection, parser, retention, clock, permission, or null gaps: `{{LIST}}`
- Query-logic limitations: `{{LIST}}`
- Required corroboration: `{{LIST}}`

## 9. Optimization review

Record semantic equivalence before and after any optimization.

| Check | Decision | Evidence or measurement |
|---|---|---|
| Narrowest useful timeframe | `{{VALUE}}` | `{{RATIONALE}}` |
| Selective filters early | `{{YES/NO}}` | `{{RATIONALE}}` |
| Required fields only | `{{YES/NO}}` | `{{RATIONALE}}` |
| Sort required | `{{YES/NO}}` | `{{RATIONALE}}` |
| Limit position preserves meaning | `{{YES/NO}}` | `{{RATIONALE}}` |
| Aggregation cardinality bounded | `{{YES/NO/NOT USED}}` | `{{RATIONALE}}` |
| Join key uniqueness and fan-out checked | `{{YES/NO/NOT USED}}` | `{{MEASUREMENT}}` |
| Result equivalence tested | `{{NOT RUN / METHOD AND RESULT}}` | `{{EVIDENCE}}` |

Do not claim a performance gain without measurement in the declared tenant/context. A smaller result set is not proof of semantic equivalence.

## 10. Troubleshooting

If compilation fails, separate:

1. language syntax and stage order;
2. target-surface restrictions;
3. dataset/field existence and type;
4. product/version differences;
5. permissions/license.

If execution returns zero rows, check source ingestion, parser/mapping, retention, selected timeframe, clock skew, identity/SBAC scope, null population, field values, and filter logic before concluding absence.

## 11. Validation checklist

- [ ] Product, version, surface, timeframe, identity scope, and license are declared or marked unknown.
- [ ] Every stage, function, operator, dataset, and field has the appropriate evidence.
- [ ] `config`, if used, is first; dataset selection follows it.
- [ ] Boolean precedence is explicit with parentheses where needed.
- [ ] Field types, nulls, aliases, cardinality, and ordering are accounted for.
- [ ] The output grain and bounded interpretation are stated.
- [ ] False-positive and false-negative paths are documented.
- [ ] Query Center validity is not represented as BIOC, correlation, or XQLp compatibility.
- [ ] Any `target` is final, explicitly sets `append=true|false`, and has destination ownership, authorization, recovery, volume, and post-write checks; otherwise the query remains read-only.
- [ ] No compilation, execution, result, or performance claim exceeds the recorded evidence.
- [ ] Secrets, operational endpoint identifiers, and unnecessary personal data are absent.

For a tenant run, continue with [tenant-validation.md](tenant-validation.md). For a rule handoff, continue with [detection-query.md](detection-query.md).
