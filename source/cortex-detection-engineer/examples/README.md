# Example index

These examples demonstrate detection-engineering decisions. They are not imported, compiled, executed, deployed, or observed in a Cortex tenant. Every expected result is an expectation, not a reported outcome.

| Need | Read | Demonstrates |
|---|---|---|
| Behavior-to-detection design | [Suspicious PowerShell](design/suspicious-powershell.md) | Threat model, telemetry contract, conceptual logic, fixtures, FP/FN, and safe promotion |
| Hunt promotion | [Hunt to detection](design/hunt-to-detection.md) | Repeatability and coverage gates before production-rule selection |
| Rule-type choice | [Scheduled versus real time](design/scheduled-vs-real-time.md) | Current XSIAM surface restrictions and action boundary |
| Volume tuning | [Overbroad correlation](tuning/overbroad-correlation.md) | Root-cause tuning without treating suppression as selectivity |
| No-match diagnosis | [Missing telemetry](troubleshooting/missing-telemetry.md) | Coverage-aware negative evidence and platform handoff |

Before reuse, revalidate product/version/license, official-source freshness, tenant schema/types, rule editor/compiler, fixtures, volume, permissions, Issue/Case behavior, owner, and rollback.

Each example uses synthetic identifiers only and remains within the runtime package so a copied Skill can demonstrate its own contract without root or sibling files.
