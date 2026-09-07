# Detection tuning plan template

## Identity and observed problem

- Detection ID/revision: `<...>`
- Product/rule surface: `<...>`
- Owner/reviewer: `<...>`
- Observation window and identity scope: `<...>`
- Observed defect: `<false-positive pattern|false-negative gap|volume|latency|grouping|schema drift>`
- Evidence status: `<...>`

## Baseline and quality evidence

- Population/segmentation: `<...>`
- Match and Issue counts with denominators: `<...>`
- Analyst dispositions and label quality: `<...>`
- Known positive recall fixtures: `<...>`
- Coverage/null/source health: `<...>`
- Seasonality/change events: `<...>`

## FP/FN model

| Type | Mechanism | Evidence | Proposed discriminator | Residual/new risk |
|---|---|---|---|---|
| FP/FN | `<...>` | `<...>` | `<...>` | `<...>` |

## Proposed controlled change

- One-variable change where possible: `<...>`
- Logic/threshold/window/suppression/exception delta: `<...>`
- Why it preserves the original behavior: `<...>`
- Rule-context compatibility to recheck: `<...>`
- State change and authorization: `<...>`

## Test matrix

| Fixture | Prior revision | Candidate | Expected | Result |
|---|---|---|---|---|
| Positive | `<...>` | `<...>` | `<...>` | `NOT RUN` |
| Benign | `<...>` | `<...>` | `<...>` | `NOT RUN` |
| Negative | `<...>` | `<...>` | `<...>` | `NOT RUN` |
| Boundary/null | `<...>` | `<...>` | `<...>` | `NOT RUN` |
| Duplicate/delay | `<...>` | `<...>` | `<...>` | `NOT RUN` |
| High volume | `<...>` | `<...>` | `<...>` | `NOT RUN` |

## Shadow/canary and decision

- Population and duration: `<...>`
- Quality and capacity acceptance thresholds: `<...>`
- Case grouping/suppression checks: `<...>`
- Stop/rollback triggers: `<...>`
- Owner/approver: `<...>`
- Decision: `<reject|iterate|promote>`

## Exception governance

- Exact scope, justification, owner, approver, review and expiry: `<...>`
- Attacker-mimicry risk: `<...>`
- Known-positive replay with exception: `<...>`
- Removal verification: `<...>`

## Safe failure

Do not deploy a tuning change based only on lower volume. Preserve the prior revision and reject changes that lose required positive fixtures or depend on missing tenant evidence.
