# Detection validation plan template

## Scope

- Detection ID/revision/hash: `<...>`
- Product/version/license/rule surface: `<...>`
- Tenant alias/environment: `<none|non-production>`
- Identity role/SBAC scope: `<...>`
- Owner/evaluator/date: `<...>`
- Official-source snapshot: `<...>`

## Level plan

| Level | Method | Evidence to retain | Current result | Rationale |
|---|---|---|---|---|
| `S` | Oracle-free controlled response or design review | Prompt, response, scorer result | `NOT RUN` | Independent evaluation not performed |
| `D` | Current official-page review | URLs, dates, product/version, supported claim | `NOT RUN` | Applicable current pages not yet inspected for this artifact |
| `C` | Exact rule editor/compiler/schema check | Artifact hash, identity, acceptance/error | `NOT RUN` | No exact tenant/editor acceptance evidence |
| `E` | Bounded execution/deployment | Timeframe, fixtures, results, Issues/Case/action evidence | `NOT RUN` | No exact tenant execution or observed outcome |

Replace each result with exactly `PASS`, `FAIL`, `NOT RUN`, or `N/A` and retain its level-specific rationale. `N/A` requires a genuinely inapplicable dimension, not missing access.

## Fixtures

| ID | Type | Source/integrity | Condition | Expected observation | Privacy | Result |
|---|---|---|---|---|---|---|
| `<FX-01>` | Positive | `<...>` | `<...>` | `<...>` | Synthetic | `NOT RUN` |
| `<FX-02>` | Benign | `<...>` | `<...>` | `<...>` | Synthetic | `NOT RUN` |
| `<FX-03>` | Negative | `<...>` | `<...>` | `<...>` | Synthetic | `NOT RUN` |
| `<FX-04>` | Below/at/above boundary | `<...>` | `<...>` | `<...>` | Synthetic | `NOT RUN` |
| `<FX-05>` | Null/type/subtype | `<...>` | `<...>` | `<...>` | Synthetic | `NOT RUN` |
| `<FX-06>` | Duplicate/delayed/replayed | `<...>` | `<...>` | `<...>` | Synthetic | `NOT RUN` |
| `<FX-07>` | High volume/cardinality | `<...>` | `<...>` | `<...>` | Synthetic | `NOT RUN` |
| `<FX-08>` | Missing telemetry/access | `<...>` | `<...>` | `<...>` | Synthetic | `NOT RUN` |

## Acceptance criteria

- Logic and output grain: `<...>`
- Required positive sensitivity: `<...>`
- Allowed benign/Issue volume: `<...>`
- Known FP/FN limits: `<...>`
- Rule-editor compatibility: `<...>`
- Issue fields/drill-down/grouping: `<...>`
- Execution health/latency: `<...>`
- Safeguard margin: `<...>`
- No response/prevention without separate approval: `<...>`

## Procedure and controls

1. Preserve exact artifact and prior revision.
2. Refresh product-specific sources.
3. Validate schema/types and effective identity.
4. Run editor/compiler check.
5. Run fixtures in isolated bounded scope.
6. Review FP/FN, volume, duplicate, delay, grouping, and audit evidence.
7. Stop on unexpected state change, runaway volume, or unsafe output.
8. Retain sanitized evidence and record `S/D/C/E` separately.

## Rollback and partial failure

- Stop condition: `<...>`
- Disable/revert procedure and owner: `<...>`
- Data/lookup/prevention recovery: `<...>`
- Post-rollback verification: `<...>`

## Safe failure

If the exact tenant/editor, fixtures, permissions, or rollback is unavailable, keep `C`/`E` as `NOT RUN` and do not claim readiness.
