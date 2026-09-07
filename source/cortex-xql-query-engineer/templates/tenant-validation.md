# Tenant Validation Record

Use this record to advance a query from documented syntax to observed tenant behavior. Complete it in a non-production tenant when practical and never include API keys, tokens, full operational identifiers, or unnecessary result data.

## Validation identity

| Item | Value |
|---|---|
| Validation ID/date | `{{ID}}` / `{{YYYY-MM-DD}}` |
| Tester/owner | `{{ROLE OR TEAM}}` |
| Product/version/release | `{{EXACT VALUE}}` |
| Tenant | `{{SAFE ALIAS; NO FQDN OR SECRET}}` |
| Surface | `{{QUERY CENTER/API/BIOC/SCHEDULED CORRELATION/REAL-TIME CORRELATION/XQLP}}` |
| Execution identity | `{{SAFE IDENTITY ALIAS}}` |
| RBAC/SBAC/data scope | `{{EFFECTIVE SCOPE}}` |
| Edition/license | `{{OBSERVED ENTITLEMENT}}` |
| Environment | `{{DEVELOPMENT/NON-PRODUCTION/PRODUCTION}}` |
| Source review date | `{{YYYY-MM-DD}}` |

## Query under validation

- Query artifact/hash: `{{PATH OR SHA-256}}`
- Objective: `{{OBJECTIVE}}`
- Starting canonical status and qualifiers: `{{VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED | OTHER CANONICAL COMBINATION}}`
- Starting validation: `S: {{PASS/FAIL/NOT RUN/N/A - RATIONALE}}; D: {{PASS/FAIL/NOT RUN/N/A - RATIONALE}}; C: {{PASS/FAIL/NOT RUN/N/A - RATIONALE}}; E: {{PASS/FAIL/NOT RUN/N/A - RATIONALE}}`
- Official sources for every stage/function/operator: `{{LINKS}}`
- Target dataset/model: `{{NAME}}`
- Target timeframe/timezone: `{{BOUNDED WINDOW}}`

```xql
{{EXACT QUERY TESTED}}
```

## Gate 1 — Schema observation

Record direct observation from the named tenant; documentation alone does not pass this gate.

| Construct | Expected | Observed tenant value/type | Population/null sample | Evidence reference | Result |
|---|---|---|---|---|---|
| Dataset/model | `{{NAME}}` | `{{OBSERVATION}}` | `{{COUNT/SAMPLE, MINIMIZED}}` | `{{SCREENSHOT/EXPORT/LOG ID}}` | `{{PASS/FAIL/NOT RUN/N/A + RATIONALE}}` |
| Field | `{{NAME/TYPE}}` | `{{NAME/TYPE}}` | `{{NULL RATE OR BOUNDED SAMPLE}}` | `{{EVIDENCE}}` | `{{PASS/FAIL/NOT RUN/N/A + RATIONALE}}` |

If this gate passes, the maximum new claim is `TENANT-SCHEMA-VERIFIED`. It does not establish compilation.

## Gate 2 — Bounded compilation

- Minimal probe or editor validation used: `{{EXACT RECORD}}`
- Timeframe and limit: `{{VALUES}}`
- Compiler/editor/API response: `{{SAFE ERROR OR ACCEPTANCE RECORD}}`
- Product surface and identity: `{{VALUES}}`
- Result: `{{PASS/FAIL/NOT RUN/N/A + RATIONALE}}`

If this gate passes, the maximum new claim is `TENANT-COMPILED`. A green editor indication or accepted API request does not establish successful execution or correct semantics.

## Gate 3 — Bounded execution

- Execution start/end and timezone: `{{TIMESTAMPS}}`
- Actual query window: `{{WINDOW}}`
- Result status/count: `{{STATUS/COUNT}}`
- Runtime/queue metrics available: `{{OBSERVATION | NOT AVAILABLE}}`
- Result sample handling: `{{REDACTED SAMPLE/HASH/SECURE LOCATION}}`
- Coverage evidence: `{{INGESTION HEALTH, RETENTION, CLOCK, PARSER/MAPPING}}`
- Permission evidence: `{{EFFECTIVE SCOPE AND NEGATIVE-ACCESS CHECK IF REQUIRED}}`
- Result: `{{PASS/FAIL/NOT RUN/N/A + RATIONALE}}`

If this gate passes, use `TENANT-EXECUTED` only for this product, version, identity, surface, query, timeframe, and date. Do not generalize it to other tenants or future releases.

## Gate 4 — Semantic and negative testing

| Test | Fixture/known event | Expected | Observed | Result |
|---|---|---|---|---|
| Known positive | `{{SAFE FIXTURE}}` | `{{MATCH}}` | `{{OBSERVATION}}` | `{{PASS/FAIL/NOT RUN/N/A + RATIONALE}}` |
| Known benign | `{{SAFE FIXTURE}}` | `{{NO MATCH OR EXPLAINED MATCH}}` | `{{OBSERVATION}}` | `{{PASS/FAIL/NOT RUN/N/A + RATIONALE}}` |
| Null/missing field | `{{FIXTURE}}` | `{{EXPECTED BRANCH}}` | `{{OBSERVATION}}` | `{{PASS/FAIL/NOT RUN/N/A + RATIONALE}}` |
| Boundary time | `{{FIXTURE}}` | `{{EXPECTED BRANCH}}` | `{{OBSERVATION}}` | `{{PASS/FAIL/NOT RUN/N/A + RATIONALE}}` |
| Restricted identity | `{{SAFE IDENTITY ALIAS}}` | `{{EXPECTED ACCESS}}` | `{{OBSERVATION}}` | `{{PASS/FAIL/NOT RUN/N/A + RATIONALE}}` |

No-result output passes only when the test expected zero rows and the required coverage, retention, permissions, parser, clock, and fixture evidence are present.

## Gate 5 — Optimization and scale

| Measurement | Baseline | Candidate | Interpretation |
|---|---|---|---|
| Result set/hash or semantic comparison | `{{VALUE}}` | `{{VALUE}}` | `{{EQUIVALENT/CHANGED/INCONCLUSIVE}}` |
| Runtime/queue/bytes metric | `{{VALUE}}` | `{{VALUE}}` | `{{OBSERVATION}}` |
| Aggregation groups | `{{VALUE}}` | `{{VALUE}}` | `{{CARDINALITY}}` |
| Join fan-out | `{{VALUE}}` | `{{VALUE}}` | `{{RISK}}` |

Do not claim optimization when only row count decreased or no comparable runtime metric was captured. First prove the intended result semantics were preserved.

## Gate 6 — Target-surface compatibility

Complete this only when the query will leave its validated interactive surface.

| Target | Editor/parser validation | Restrictions reviewed | Historical/fixture test | Volume/safeguard test | Result |
|---|---|---|---|---|---|
| BIOC | `{{EVIDENCE}}` | `{{EVIDENCE}}` | `{{EVIDENCE}}` | `{{EVIDENCE}}` | `{{PASS/FAIL/NOT RUN/N/A + RATIONALE}}` |
| Scheduled correlation | `{{EVIDENCE}}` | `{{EVIDENCE}}` | `{{EVIDENCE}}` | `{{EVIDENCE}}` | `{{PASS/FAIL/NOT RUN/N/A + RATIONALE}}` |
| Real-time correlation | `{{EVIDENCE}}` | `{{EVIDENCE}}` | `{{EVIDENCE}}` | `{{EVIDENCE}}` | `{{PASS/FAIL/NOT RUN/N/A + RATIONALE}}` |
| XQLp | `{{EVIDENCE}}` | `{{EVIDENCE}}` | `{{EVIDENCE}}` | `{{NOT APPLICABLE/DETAIL}}` | `{{PASS/FAIL/NOT RUN/N/A + RATIONALE}}` |

Never reuse a Query Center pass as the target-surface pass.

## Troubleshooting ledger

| Attempt | Symptom | Evidence | Hypothesis | Discriminating change | Outcome |
|---|---|---|---|---|---|
| `1` | `{{SYMPTOM}}` | `{{RECORD}}` | `{{HYPOTHESIS}}` | `{{ONE BOUNDED CHANGE}}` | `{{RESULT}}` |

Change one material variable at a time where practical. Preserve the original query and compiler/runtime errors.

## Final claim

- Canonical class and qualifiers: `{{CLASS / QUALIFIERS}}`
- Final validation: `S: {{PASS/FAIL/NOT RUN/N/A - RATIONALE}}; D: {{PASS/FAIL/NOT RUN/N/A - RATIONALE}}; C: {{PASS/FAIL/NOT RUN/N/A - RATIONALE}}; E: {{PASS/FAIL/NOT RUN/N/A - RATIONALE}}`
- False positives observed: `{{SUMMARY}}`
- False negatives/coverage gaps: `{{SUMMARY}}`
- Residual limitations: `{{SUMMARY}}`
- Next required validation: `{{STEP}}`
- Approver for production use: `{{ROLE/POLICY; QUERY VALIDATION DOES NOT AUTHORIZE DEPLOYMENT OR RESPONSE}}`

Any gate marked `NOT RUN` remains an explicit limitation; never convert it into a pass in prose.
