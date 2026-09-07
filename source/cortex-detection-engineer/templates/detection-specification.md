# Detection specification template

**Artifact class:** `CONCEPTUAL` unless exact rule-editor/compiler and tenant evidence is attached. This template is not import JSON and does not authorize deployment.

## Identity

- Detection ID/revision: `<DET-ID>/<REV>`
- Name: `<descriptive behavior>`
- Owner/reviewer: `<OWNER>` / `<REVIEWER>`
- Objective and decision: `<observable security decision>`
- Product/version/license: `<XSIAM-or-XDR>/<VERSION>/<ENTITLEMENT>`
- Rule surface: `<IOC|BIOC|BIOC-prevention|scheduled-correlation|real-time-correlation|Analytics-review|candidate>`
- Evidence snapshot: `<YYYY-MM-DD>`
- Status/qualifiers: `<CANONICAL-STATUS> / <QUALIFIERS>`
- `S`: `<PASS|FAIL|NOT RUN|N/A>` — `<independent controlled evaluation evidence or reason not run>`
- `D`: `<PASS|FAIL|NOT RUN|N/A>` — `<exact dated official-source evidence or reason not run>`
- `C`: `<PASS|FAIL|NOT RUN|N/A>` — `<exact tenant/editor acceptance evidence or reason not run>`
- `E`: `<PASS|FAIL|NOT RUN|N/A>` — `<exact tenant execution/result evidence or reason not run>`

## Threat behavior and model

- Observable behavior: `<actor, action, target, sequence, time>`
- Preconditions/opportunity: `<...>`
- Protected asset/security property: `<...>`
- Adverse outcome: `<...>`
- Benign alternatives: `<...>`
- Evasions/variants: `<...>`
- Severity rationale: `<asset + impact + confidence>`

## ATT&CK interpretation

- Framework version/access date: `<...>`
- Tactic/technique/sub-technique: `<...>`
- Behavior-to-mapping rationale: `<...>`
- Alternatives/uncertainty: `<...>`
- Non-claim: `Mapping does not prove compromise or effective tenant coverage.`

## Telemetry and coverage contract

| Observation | Source/path | Dataset or preset | Event category/subtype | Fields/types/nulls | Time/retention | Access | Evidence |
|---|---|---|---|---|---|---|---|
| `<clause>` | `<source>` | `<verified-or-placeholder>` | `<exact>` | `<...>` | `<...>` | `<...>` | `<...>` |

- Coverage gaps and false-negative effect: `<...>`
- Known-positive/control availability: `<...>`
- Missing-telemetry escalation: `<...>`

## Query or logic contract

- Admission criteria: `<...>`
- Sequence/window: `<...>`
- Entity keys/normalization/nulls: `<...>`
- Aggregation/threshold: `<...>`
- Duplicate/delay/replay handling: `<...>`
- Before/after row grain: `<...>`
- Required output/triage fields: `<...>`
- XQL canonical status and qualifiers: `<CANONICAL-STATUS> / <PROVENANCE-AND-TENANT-QUALIFIERS>`; documented syntax, tenant schema, compilation, and execution are separate evidence dimensions, not one readiness ladder.
- Exact rule-context validation remaining: `<...>`

## Expected signal

- One match means: `<...>`
- It does not mean: `<...>`
- Analyst verification: `<...>`
- Rule/event provenance: `<...>`
- Expected Issue fields: `<...>`
- Case/grouping expectation: `<hypothesis, not guarantee>`

## Baseline, threshold, and suppression

- Population/period/seasonality: `<...>`
- Metric and denominator: `<...>`
- Candidate threshold/window: `<...>`
- Boundary inclusivity: `<...>`
- Expected volume/capacity: `<...>`
- Suppression key/duration/null behavior: `<none-or-verified-design>`
- Evidence or measurement plan: `<...>`

## Validation fixtures

| ID | Family | Input/condition | Expected observation | Result/evidence |
|---|---|---|---|---|
| `<F-01>` | Positive | `<...>` | `<...>` | `NOT RUN` |
| `<F-02>` | Benign | `<...>` | `<...>` | `NOT RUN` |
| `<F-03>` | Negative | `<...>` | `<...>` | `NOT RUN` |
| `<F-04>` | Boundary/null/delay/duplicate | `<...>` | `<...>` | `NOT RUN` |
| `<F-05>` | Volume/missing telemetry | `<...>` | `<...>` | `NOT RUN` |

## FP/FN and tuning

| Risk | Mechanism | Discriminator or compensating control | Change | New risk | Owner/expiry |
|---|---|---|---|---|---|
| FP/FN | `<...>` | `<...>` | `<...>` | `<...>` | `<...>` |

## Rule readiness and safety

- Product/rule restrictions checked: `<...>`
- Permissions/identity: `<...>`
- State changes requested: `<none-or-exact>`
- Approval/change window: `<...>`
- Blast radius/dependencies: `<...>`
- Export/recovery/rollback: `<...>`
- Post-change verification/partial failure: `<...>`
- Downstream response gate: `<separate deterministic approval>`

## Monitoring and retirement

- Health/volume/quality/coverage metrics: `<...>`
- Safeguard and exception monitoring: `<...>`
- Review cadence and owner: `<...>`
- Rollback/disable triggers: `<...>`
- Retirement/successor criteria: `<...>`

## Known gaps and next validation step

- Unknowns: `<...>`
- Smallest discriminating step: `<...>`
- Safe failure: `Do not deploy or claim readiness while essential evidence is missing.`

## Official references

- `<specific official page and review date>`
