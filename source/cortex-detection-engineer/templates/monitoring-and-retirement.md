# Monitoring and retirement template

## Identity

- Detection ID/revision/rule ID: `<...>`
- Product/version/rule surface: `<...>`
- Owner/on-call/reviewer: `<...>`
- Monitoring start/end: `<...>`
- Evidence status: `<...>`

## Objectives and indicators

| Dimension | Metric/query/source | Baseline/target | Review cadence | Trigger | Owner action |
|---|---|---|---|---|---|
| Execution health | `<...>` | `<...>` | `<...>` | `<...>` | `<...>` |
| Match/Issue volume | `<...>` | `<...>` | `<...>` | `<...>` | `<...>` |
| Quality/FP/FN | `<...>` | `<...>` | `<...>` | `<...>` | `<...>` |
| Coverage/schema | `<...>` | `<...>` | `<...>` | `<...>` | `<...>` |
| Case behavior | `<...>` | `<...>` | `<...>` | `<...>` | `<...>` |
| Exceptions/suppression | `<...>` | `<...>` | `<...>` | `<...>` | `<...>` |
| Safeguard proximity | `<...>` | `<...>` | `<...>` | `<...>` | `<...>` |

## Audit evidence

- Rule revision/source and change history: `<...>`
- Correlation audit or equivalent product evidence: `<...>`
- Generated Issue-to-rule provenance: `<...>`
- Error/retry/lag evidence: `<...>`
- Analyst dispositions and sampling method: `<...>`
- Known-positive replay date: `<...>`

## Exception and suppression review

| ID | Scope | Reason/evidence | Impact | Owner/approver | Review/expiry | Decision |
|---|---|---|---|---|---|---|
| `<...>` | `<...>` | `<...>` | `<...>` | `<...>` | `<...>` | `<...>` |

## Rollback/disable plan

- Triggers: `<runaway volume|schema loss|unsafe action|quality regression|unowned rule|other>`
- Exact prior artifact/export: `<...>`
- Dependencies and affected workflows: `<...>`
- Disable/revert authorization: `<...>`
- Data/lookup/prevention recovery: `<...>`
- Post-change verification and partial-failure owner: `<...>`

## Retirement decision

- Reason: `<threat gone|source gone|duplicate|successor|quality failure|unsupported>`
- Successor/control and coverage comparison: `<...>`
- Residual risk/acceptance owner: `<...>`
- Dependent playbooks/dashboards/reports: `<...>`
- Evidence retention: `<...>`
- Exceptions/suppression cleanup: `<...>`
- Removal verification: `<...>`

## Decision

- `<MAINTAIN|TUNE|DISABLE|RETIRE|NOT ENOUGH EVIDENCE>`
- Approver/date: `<...>`
- Next review: `<...>`

No rule state change is authorized by this template alone.
