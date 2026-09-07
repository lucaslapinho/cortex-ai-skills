# Evidence-Scoped Query Patterns

Use these patterns to construct investigation, hunt-support, and detection-support queries. Every concrete query below is documentation-grounded but was not compiled or run in a tenant.

**Documentation review cut:** 2026-09-04  
**Executable-block evidence unless stated otherwise:** `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED`; `D: PASS`, `C: NOT RUN`, `E: NOT RUN`  
**Canonical claim:** `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED`

## Contents

- Pattern selection and construction sequence
- Recent process activity
- Selected-filename PowerShell triage
- Process-event volume by host
- Last observed process-image value per host
- Lateral-movement investigation with unknown schema
- Detection-support handoff
- Required answer contract

## Select a pattern by objective

| Objective | Start with | Add only when evidenced |
|---|---|---|
| Inspect recent records | Explicit narrow timeframe, source, selective filter, essential fields, descending time, explicit limit | Derived fields or broader lookback. |
| Find a behavior | Event/source gate, behavior-specific predicates, identity/host/process context | Regex, join, or aggregation after type/cardinality checks. |
| Count activity | Early filters, `comp count()` or `count(field)`, grouping, final sort/limit | Baseline or threshold only with representative tenant data. |
| Keep one record per entity | Early filters/projection, `dedup ... by asc|desc` | Omit `by` only when arbitrary retention is acceptable. Equal ordering values require an explicit tie policy; a unique full-row winner is not established by time alone. |
| Relate two sources | Verify both datasets, key types, multiplicity, timeframe, and coverage before `join` | Join type/conflict strategy chosen from the analytical question. |
| Support a detection handoff | Query plus signal semantics, dependencies, null/coverage limits, expected benign cases, and target-context compatibility | BIOC/correlation conversion only after the exact rule restrictions are checked. |

## Construction sequence

```text
objective and decision
-> product, version, and execution surface
-> evidence level
-> timeframe and retention
-> source and schema proof
-> early selective filters
-> required transformations
-> projection
-> cardinality-changing stages
-> final order and limit
-> expected output and alternative explanations
-> compiler, execution, and coverage validation
```

Do not start by guessing a dataset or field from the user's business wording. If the requested schema is unknown, stop at a conceptual query shape and a tenant-validation step.

## Pattern 1 — Recent process activity

**Objective:** inspect recent process events with stable host and identity context.  
**Product/surface:** general Cortex XQL using the current XDR data schema; intended for interactive investigation.  
**Evidence:** `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED`; `D: PASS`, `C: NOT RUN`, `E: NOT RUN`.

```xql
config timeframe = 1d
| dataset = xdr_data
| filter event_type = 1 and action_process_image_name != null
| fields _time, agent_hostname, agent_id, actor_effective_username, action_process_username, action_process_image_name, action_process_image_command_line
| sort desc _time
| limit 200
```

Expected output: up to 200 recent process-event rows visible to the execution identity, ordered newest first, with the projected fields where populated.

Limitations:

- `event_type = 1` means Process in the reviewed schema; it is not a maliciousness label.
- Command line and usernames may be null, sensitive, or unavailable for some OS/event sources.
- The query does not prove process coverage, retention, endpoint health, or target-tenant schema parity.
- `limit 200` is a review bound, not a detection threshold.

## Pattern 2 — Suspicious PowerShell triage

**Objective:** identify Process-category telemetry whose image-name value contains the selected Windows-style filenames `powershell.exe` or `pwsh.exe` for analyst triage. This is not a complete cross-platform PowerShell inventory.  
**Product/surface:** general Cortex XQL using `xdr_data`; interactive investigation.  
**Evidence:** `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED`; `D: PASS`, `C: NOT RUN`, `E: NOT RUN`.

```xql
config timeframe = 1d
| dataset = xdr_data
| filter event_type = 1 and action_process_image_name != null
| filter (lowercase(action_process_image_name) contains "powershell.exe" or lowercase(action_process_image_name) contains "pwsh.exe")
| fields _time, agent_hostname, agent_id, actor_effective_username, action_process_username, action_process_image_name, action_process_image_command_line
| sort desc _time
| limit 200
```

Expected output: Process-category events whose image name contains either selected literal filename, within the selected day and the execution identity's visible scope. Other PowerShell hosts, filename forms, platforms, missing image names, and non-`PROCESS_START` semantics remain outside or unresolved.

Interpretation:

- This identifies PowerShell activity, not malicious PowerShell.
- Legitimate administration, software deployment, automation, and security tooling are expected alternatives.
- Review command lines and surrounding process/identity context before forming a hypothesis.
- Do not trigger containment from this query alone.

Promotion boundary: the query uses `fields`, `sort`, and `limit`, so it is not directly BIOC-compatible under the reviewed Cortex XSIAM BIOC restrictions. A real-time correlation also has a restricted stage/function set. Preserve signal semantics and redesign for the named target; do not simply delete stages and assert equivalence.

## Pattern 3 — Process-event volume by host

**Objective:** find hosts with the highest visible process-event volume in the time window.  
**Product/surface:** general Cortex XQL; interactive investigation or hunt support.  
**Evidence:** `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED`; `D: PASS`, `C: NOT RUN`, `E: NOT RUN`.

```xql
config timeframe = 1d
| dataset = xdr_data
| filter event_type = 1 and agent_hostname != null
| fields agent_hostname
| comp count() as process_events by agent_hostname
| sort desc process_events
| limit 100
```

Expected output: up to 100 agent hostnames ordered by the number of visible process-event rows.

Limitations:

- It measures returned event rows, not process uniqueness, risk, endpoint importance, or a stable baseline.
- Differences can reflect sensor health, workload, retention, RBAC/SBAC, or ingestion behavior.
- `count()` counts rows. `count(agent_hostname)` would count non-null hostname values and is equivalent here only because the preceding filter excludes null hostnames; record that reasoning if changing it.
- `comp` discards all fields other than `agent_hostname` and `process_events`.

## Pattern 4 — Last observed process image per host

**Objective:** summarize the newest recorded process-image value for each visible host.  
**Product/surface:** general Cortex XQL; interactive investigation.  
**Evidence:** `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED`; `D: PASS`, `C: NOT RUN`, `E: NOT RUN`.

```xql
config timeframe = 1d
| dataset = xdr_data
| filter action_process_image_name != null
| comp last(action_process_image_name) as last_process by agent_hostname
| fields agent_hostname, last_process
| limit 3
```

Expected output: up to three grouped host rows with the process image value from the newest event considered by `last()`.

Limitations:

- The current `last()` reference bases chronology on the underlying event time. Source clock quality and timestamp semantics still matter.
- No final sort is specified, so which three groups survive `limit 3` is not promised. Add a documented sort criterion only when the desired top/bottom semantics are defined.
- A latest value is not a complete timeline or evidence of current process state.

## Pattern 5 — Lateral-movement investigation with unknown schema

Do not fabricate a join between endpoint, authentication, and network data. Use this gated plan when the target datasets and keys are unknown.

**Status:** `CONCEPTUAL / TENANT-UNVERIFIED`.

```text
1. Define the behavior: remote authentication, remote service creation, remote process execution, or network pivot.
2. Verify each telemetry source and its retention in the named product/tenant.
3. Record candidate source and destination host, user, timestamp, protocol, address, process, and event identifiers from actual schema.
4. Test each source independently with a narrow timeframe.
5. Normalize only documented types and timestamp units.
6. Measure join-key null rates and one-to-many/many-to-many multiplicity.
7. Prefer a set filter or sequential analyst pivot when it answers the question without a costly join.
8. If a join is necessary, project/filter both sides, choose join type and conflict strategy explicitly, then inspect cardinality before interpreting results.
9. Corroborate with source events; absence is qualified by collection, retention, access, and clock coverage.
```

Conceptual join shape, not executable until all placeholders are tenant-verified:

```xql
config timeframe = <bounded_timeframe>
| dataset = <verified_left_dataset>
| filter <verified_left_predicate>
| fields <verified_left_time>, <verified_join_key>, <needed_left_fields>
| join conflict_strategy = both type = inner ((dataset = <verified_right_dataset> | filter <verified_right_predicate> | fields <verified_right_time>, <verified_join_key>, <needed_right_fields>) as right_side <verified_boolean_join_condition>)
| limit <review_bound>
```

Never replace the placeholders with plausible field names from memory. If timestamp tolerance or range correlation is required, verify that exact expression in current documentation and the target compiler.

## Pattern 6 — Detection-support handoff

The query engineer hands off evidence and mechanics, not a production-ready rule verdict.

| Destination | Query-level handoff content | Validation still owned downstream |
|---|---|---|
| Query Center investigation | Exact query, objective, source/schema status, timeframe, expected columns, null/coverage limits. | Tenant compilation/execution and analyst interpretation. |
| BIOC | Behavior predicate, required `event_type`, candidate eligible source, fields/functions, expected benign activity. | BIOC-compatible rewrite, Test BIOC, historical hit volume, exceptions, prevention eligibility, permissions, and lifecycle. |
| Scheduled correlation | Selective query, result schema, intended issue fields, candidate schedule/window, duplicate/suppression considerations. | Current restriction check, timing, rule test, issue quality, grouping, hit safeguards, and production monitoring. |
| Real-time correlation | Event-time predicate and minimal fields, with unsupported stages/functions identified. | Real-time stage/function compatibility, required filter, data model/source support, issue behavior, and load safeguards. |

Use the single maintained [execution-context compatibility matrix](xql-language.md#execution-context-compatibility) for current BIOC and correlation restrictions and numeric limits. Classification: `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED`. Recheck before configuration; these are not general Query Center limits.

## Required answer around any query

A query alone is incomplete. Supply:

1. objective and analytical decision;
2. product, version, deployment, and execution surface;
3. canonical evidence class and qualifiers;
4. assumptions and unknowns;
5. dataset/preset and why it applies;
6. fields/types and how they were verified;
7. query in a separate executable block;
8. stage-by-stage explanation;
9. expected output shape, not invented example results;
10. alternative explanations and false-positive considerations;
11. tenant validation plan and stop conditions;
12. troubleshooting checks;
13. downstream context restrictions and handoff boundary;
14. official sources with review date.

Use [optimization.md](optimization.md) before claiming an optimization, [troubleshooting.md](troubleshooting.md) for failures, and [xql-language.md](xql-language.md) for exact context restrictions.
