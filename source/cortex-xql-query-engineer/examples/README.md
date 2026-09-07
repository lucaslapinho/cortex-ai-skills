# Example index

Examples demonstrate the Skill's reasoning and output contract. They are not tenant-compiled, tenant-executed, production-ready, or universal across Cortex products and execution surfaces.

| Need | Read | What it demonstrates |
|---|---|---|
| Bounded process investigation | [Suspicious PowerShell](investigation/suspicious-powershell.md) | Current officially documented `xdr_data` fields, read-only triage, false positives/negatives, and `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED` with `C/E: NOT RUN`. |
| Aggregation and output grain | [Last process per host](investigation/last-process-per-host.md) | `comp`, `last`, aliasing, field retention, limits, and the boundary between official examples and tenant results. |
| Unknown telemetry and join keys | [Lateral movement](hunting/lateral-movement.md) | A conceptual, validation-first workflow that refuses to invent datasets or fields. |
| Query-to-detection boundary | [Detection handoff](detection/detection-handoff.md) | Separate Query Center, BIOC, scheduled correlation, real-time correlation, and XQLp decisions without deploying a rule. |
| Fabricated schema or function | [Fabricated schema troubleshooting](troubleshooting/fabricated-schema.md) | Fail-closed handling of invented constructs and the smallest safe schema-validation path. |

Before reusing any example, revalidate the target product/version, execution surface, official source freshness, tenant schema, timeframe, access scope, and desired row grain. Preserve its evidence label until stronger evidence is actually recorded.
