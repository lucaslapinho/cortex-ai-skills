# Detection-Support Query Handoff Template

Use this template to hand evidenced query logic to detection engineering. It does not decide production readiness, thresholds, grouping, response, or lifecycle ownership.

## Signal contract

- Behavior to detect: `{{BEHAVIOR, NOT A TOOL NAME ALONE}}`
- Product/version: `{{CORTEX XSIAM/XDR AND RELEASE LINE}}`
- Candidate surface: `{{BIOC | SCHEDULED CORRELATION | REAL-TIME CORRELATION | INTERACTIVE-ONLY}}`
- Required telemetry and coverage: `{{LIST}}`
- Input event grain: `{{ONE ROW PER WHAT}}`
- Output signal grain: `{{ONE ISSUE/HIT/GROUP PER WHAT}}`
- Severity/confidence: `{{POLICY INPUT; NOT INFERRED FROM QUERY MATCH}}`
- Evidence status: `{{CANONICAL CLASS / QUALIFIERS}}`

## Query artifact

**Canonical status:** `{{VERIFIED | VERSION-DEPENDENT | INFERRED | CONCEPTUAL | UNSUPPORTED | DEPRECATED | UNVERIFIED}}`  
**Qualifiers:** `{{OFFICIAL-CURRENT | OFFICIAL-EXAMPLE | LOCAL-VERIFIED | PROJECT-ASSERTED | DERIVATIVE | REFERENCED-ONLY | TENANT-UNVERIFIED | TENANT-SCHEMA-VERIFIED | TENANT-COMPILED | TENANT-EXECUTED}}`  
**Validation:** `S: {{PASS/FAIL/NOT RUN/N/A - RATIONALE}}; D: {{PASS/FAIL/NOT RUN/N/A - RATIONALE}}; C: {{PASS/FAIL/NOT RUN/N/A - RATIONALE}}; E: {{PASS/FAIL/NOT RUN/N/A - RATIONALE}}`  
**Validated only for:** `{{EXACT PRODUCT/SURFACE/IDENTITY/TIMEFRAME}}`

```xql
{{QUERY, ONLY WHEN EVERY MATERIAL CONSTRUCT IS EVIDENCED}}
```

If schema or target compatibility is unresolved, provide pseudologic in a `text` fence instead of an executable-looking block.

## Query semantics

| Element | Meaning | Evidence | Open risk |
|---|---|---|---|
| Dataset/preset | `{{WHY THIS SOURCE}}` | `{{SOURCE/TENANT RECORD}}` | `{{AVAILABILITY/POPULATION}}` |
| Filter | `{{BEHAVIOR REPRESENTED}}` | `{{SOURCE/TEST}}` | `{{BYPASS/NULL/TYPE}}` |
| Aggregation/join | `{{SIGNAL GRAIN}}` | `{{SOURCE/TEST}}` | `{{CARDINALITY/WINDOW}}` |
| Projected fields | `{{INVESTIGATION CONTEXT}}` | `{{SOURCE/TEST}}` | `{{NULL/TRUNCATION}}` |

## Compatibility gate

Evaluate only the requested target. Apply the single maintained [execution-context compatibility matrix](../references/xql-language.md#execution-context-compatibility); it is a documentation snapshot, not a tenant result, and must be rechecked for the deployed release.

| Target | Current documented constraints to check | Handoff decision |
|---|---|---|
| Interactive Query Center | General XQL syntax, current dataset/schema, identity scope, retention, bounded execution | `{{ELIGIBLE/NOT ELIGIBLE/UNVERIFIED}}` |
| BIOC | Check source, required predicate, stage/function subset, case behavior, hit safeguards, automatic `PROCESS SHA256` exception behavior, and current rule-editor validation against the compatibility matrix | `{{ELIGIBLE/NOT ELIGIBLE/UNVERIFIED}}` |
| Scheduled correlation | Check forbidden constructs, schedule/window/rule-count bounds, `current_time()` versus `time_frame_end()` behavior, hit safeguards, declared action, mapping, and volume against the compatibility matrix and current rule editor | `{{ELIGIBLE/NOT ELIGIBLE/UNVERIFIED}}` |
| Real-time correlation | Check allowed source/stage/function subset, required filter, forbidden constructs, and the Generate issue-only action against the compatibility matrix | `{{ELIGIBLE/NOT ELIGIBLE/UNVERIFIED}}` |
| XQLp | Check the modified parsing grammar, sections, stage/function subset, joins/calls, statements, and parsing-only functions against the compatibility matrix | `{{ELIGIBLE/NOT ELIGIBLE/UNVERIFIED}}` |

Explicitly reject conversions when any of these applies:

- an interactive query contains `comp`, `dedup`, `join`, `fields`, `sort`, or `limit` and is being copied directly into a BIOC;
- a real-time correlation candidate contains stages outside its documented limited set or lacks `filter`;
- a real-time correlation candidate relies on a dataset view, `transaction`, or a function the current real-time page lists as unsupported;
- a correlation candidate uses `call`, `top`, a dataset wildcard, or `tag`;
- an XQLp file starts from an ordinary dataset/preset pipeline or uses a general-XQL construct not documented for XQLp;
- dataset, field, function, return type, license, or target rule type is unknown;
- a successful interactive run is the only compatibility evidence.

“Not eligible as written” does not imply the behavior can never be detected. It means the rule needs a separately designed, target-valid representation.

## Expected signal and investigation value

- Match condition in plain language: `{{DESCRIPTION}}`
- Fields available to an analyst: `{{LIST}}`
- Expected hit volume/baseline: `{{MEASURED VALUE | NOT MEASURED}}`
- Case/Issue mapping or grouping needs: `{{REQUIREMENT; DETECTION OWNER TO VALIDATE}}`
- Positive match does not prove: `{{COMPROMISE/ATTRIBUTION/INTENT}}`

## False-positive and false-negative model

| Type | Scenario | How to measure or reduce it without hiding risk |
|---|---|---|
| False positive | `{{BENIGN ADMIN/TOOL/AUTOMATION/SCANNER/OTHER}}` | `{{BASELINE, ALLOWLIST GOVERNANCE, ADDITIONAL SIGNAL}}` |
| False negative | `{{RENAMING, ALTERNATE PATH, MISSING TELEMETRY, NULL, CLOCK OR RETENTION GAP}}` | `{{COVERAGE TEST OR ADDITIONAL SOURCE}}` |

## Volume and safety

- Representative historical test window: `{{WINDOW | NOT RUN}}`
- Hits per window: `{{VALUE | UNKNOWN}}`
- Cardinality by entity: `{{VALUE | UNKNOWN}}`
- Reverify the compatibility matrix's current hit safeguards and design for useful selectivity; do not use automatic disablement as the tuning mechanism.
- For BIOC, inspect any automatically generated `PROCESS SHA256` exception and regression-test the resulting coverage; do not let an automatic exception become a silent false-negative path.
- No response or containment is authorized by this handoff. Response needs deterministic policy, approval/authorization, least scope, rollback/recovery, and post-action verification.

## Optimization and validation plan

- Preserve the behavior definition while narrowing time and early filters.
- Retain fields required for signal mapping and triage.
- Measure aggregation and join fan-out if they are allowed for the selected target.
- Compare original and revised matches on representative positive and negative fixtures.
- Validate in the exact rule editor, product release, identity, dataset, and non-production tenant before promotion.
- Record syntax acceptance, historical test results, volume, false positives, false negatives, disabled-rule behavior, generated exceptions, action eligibility, and rollback criteria separately.

## Handoff decision

- Query mechanics owner conclusion: `{{READY FOR TARGET-SPECIFIC DETECTION REVIEW | REQUIRES QUERY REVISION | BLOCKED ON TELEMETRY/SCHEMA}}`
- Detection owner must decide: threat model, threshold/baseline, grouping, suppression, severity, ATT&CK interpretation, test fixtures, monitoring, rollback, retirement, and response linkage.
- Explicit non-claims: `{{NOT TENANT EXECUTED / NOT RULE-COMPATIBLE / NOT PRODUCTION READY, AS APPLICABLE}}`

Use [tenant-validation.md](tenant-validation.md) for the evidence ledger required to advance a query claim.
