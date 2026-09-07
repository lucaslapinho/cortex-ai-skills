# Suspicious PowerShell Triage

This example demonstrates a bounded process-telemetry query for triage. It identifies rows matching two selected Windows-style image filenames; it is not a complete cross-platform PowerShell inventory and does **not** establish maliciousness.

## Context and evidence

| Item | Value |
|---|---|
| Objective | List recent Process-category events whose documented image-name field contains the selected Windows-style filenames `powershell.exe` or `pwsh.exe` for analyst triage. |
| Product | Cortex XSIAM 3.x |
| Surface | Interactive XQL / Query Center against `xdr_data` |
| Timeframe | Previous 1 day at execution time |
| Canonical class | `VERIFIED` |
| Qualifiers | `OFFICIAL-CURRENT`, `TENANT-UNVERIFIED` |
| S validation | `NOT RUN` — no independent response evaluation was performed for this example. |
| D validation | `PASS` — the cited current official references support the displayed stages, functions, dataset, fields, and stated schema interpretation. |
| C validation | `NOT RUN` — no target-tenant schema or Query Center compilation was inspected. |
| E validation | `NOT RUN` — the query was not executed and no tenant result was observed. |
| Tenant evidence | None. Dataset availability, population, permissions, compilation, results, and performance were not observed. |
| Review date | 2026-09-04 |

The current schema reference documents `event_type` as an integer with `Process = 1`, along with the fields used below. That category can include multiple process subtypes; this query does not restrict `event_sub_type` to `PROCESS_START`, so it supports process-activity triage rather than an execution-only count. The current command reference documents `config`, `dataset`, `filter`, `lowercase()`, `contains`, `fields`, `sort`, and `limit`. This establishes documented syntax and field definitions, not tenant availability.

## Query

**VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED**  
**Product/context: Cortex XSIAM 3.x, interactive Query Center, `xdr_data`**

- `S: NOT RUN` — no independent response evaluation was performed for this example.
- `D: PASS` — the cited current official references support the displayed stages, functions, dataset, fields, and stated schema interpretation.
- `C: NOT RUN` — no target-tenant schema or Query Center compilation was inspected.
- `E: NOT RUN` — the query was not executed and no tenant result was observed.

```xql
config timeframe = 1d
| dataset = xdr_data
| filter event_type = 1 and action_process_image_name != null
| filter (lowercase(action_process_image_name) contains "powershell.exe" or lowercase(action_process_image_name) contains "pwsh.exe")
| fields _time, agent_hostname, agent_id, actor_effective_username, action_process_username, action_process_image_name, action_process_image_command_line
| sort desc _time
| limit 200
```

## Explanation

1. `config timeframe = 1d` bounds the search and, as required, is first.
2. `dataset = xdr_data` makes the source explicit rather than relying on a tenant default.
3. The first filter retains documented Process-category events with a non-null image name; it does not prove the event is specifically `PROCESS_START`.
4. The second filter normalizes the image-name string to lowercase and checks for either selected literal filename. Parentheses make the `or` grouping explicit; other PowerShell hosts, filename forms, or platforms can be missed.
5. `fields` keeps timestamp, endpoint, user, image, and command-line context needed for triage.
6. `sort desc _time` orders the visible events newest first.
7. `limit 200` applies after sorting, so it returns at most the newest 200 matching rows rather than an arbitrary pre-sort subset.

## Expected output

The output grain is one visible matching process event per row, with at most 200 rows.

| Column | Intended interpretation |
|---|---|
| `_time` | Documented data-entry timestamp; when original time is unknown, the schema says insertion time is used. Confirm tenant display, source clock quality, and fallback effects before chronology-sensitive conclusions. |
| `agent_hostname`, `agent_id` | Endpoint context; neither alone proves business ownership or criticality. |
| `actor_effective_username`, `action_process_username` | User context when populated; null or differing values require investigation. |
| `action_process_image_name` | Filename of the documented action process image path. |
| `action_process_image_command_line` | Command line recorded for the process, subject to collection and truncation limits. |

A row means only that visible telemetry matched the filename condition. Zero rows mean no matching rows were visible under this identity, dataset, timeframe, and query logic; they do not prove PowerShell did not execute.

## False positives and false negatives

Likely benign matches include authorized administration, endpoint management, software deployment, troubleshooting, build automation, and signed operational scripts. Establish who ran the process, the parent/child chain using tenant-verified fields, script origin, command intent, endpoint role, and change window before assigning risk.

Because `contains` is a substring test, an unrelated filename that embeds either string can also match; inspect the returned value before interpreting it.

Likely missed activity includes renamed or copied binaries, alternate hosts or interpreters, in-memory execution not represented by the selected field, null/truncated fields, uncollected endpoints, telemetry delay, retention gaps, excluded data scope, and activity outside the one-day window. The substring condition can also miss forms that do not retain either filename.

## Optimization notes

- The one-day bound, process event filter, early null check, explicit projection, and final limit constrain work and output.
- `sort` can be costly and is needed here only for “newest first.” Remove it only if order is irrelevant, and do not claim a speedup without measurement.
- `lowercase()` is evaluated for matching rows. A target-specific case-insensitive equivalent may be considered only after proving identical semantics in the selected surface.
- Narrowing the timeframe or adding endpoint/user constraints can change coverage. Record the analytic invariant and compare representative results before calling the change an optimization.
- No tenant runtime or result-equivalence measurement was performed.

## Troubleshooting

If compilation fails, verify the target product/release, Query Center surface, exact schema/type for every field, and current stage/function support. If the query returns zero rows, check `xdr_data` visibility, endpoint collection, retention, ingestion delay, field population, clock skew, Query Center permissions, SBAC/data scope, and whether the filename value has the assumed form. Inspect tenant schema/autocomplete or a bounded sample; do not invent alternate fields.

## Rule-conversion boundary

- **BIOC:** not eligible as written. Current BIOC documentation limits the query to `filter`, `alter`, and non-aggregate functions and requires an `event_type` filter; this query also contains `fields`, `sort`, and `limit`. Removing those stages creates a different artifact that still requires rule-editor and tenant validation.
- **Real-time correlation:** not eligible as written because `config timeframe`, `sort`, and `limit` are outside the documented limited real-time stage set (only `config case_sensitive` is listed for `config`). A real-time design also needs target action and volume validation.
- **Scheduled correlation:** compatibility and detection semantics were not tested. An interactive Query Center query must not be represented as a scheduled rule merely because its syntax is accepted.
- **XQLp:** not applicable; an ordinary dataset query is not a parsing-rule file.

## Official references

- [config stage](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/stages/config.md)
- [filter stage](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/stages/filter.md)
- [fields stage](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/stages/fields.md)
- [sort stage](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/stages/sort.md)
- [limit stage](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/stages/limit.md)
- [lowercase function](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/functions/lowercase.md)
- [`xdr_data` field reference](https://cortex-docs.paloaltonetworks.com/xql-schema-reference/xdr-data-fields.md)
- [Action-actor field reference](https://cortex-docs.paloaltonetworks.com/xql-schema-reference/xdr-data-fields-by-actor/action-actor.md)
- [Actor-actor field reference](https://cortex-docs.paloaltonetworks.com/xql-schema-reference/xdr-data-fields-by-actor/actor-actor.md)
- [BIOC restrictions](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/threat-management/detection-rules/what-are-detection-rules/whats-a-bioc/create-a-bioc-rule.md)
- [Correlation-rule restrictions](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/threat-management/detection-rules/what-are-detection-rules/whats-a-correlation-rule/create-a-correlation-rule.md)

Use [the tenant validation record](../../templates/tenant-validation.md) before advancing the execution claim.
