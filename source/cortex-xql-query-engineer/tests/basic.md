# Basic Behavioral Tests

Run these cases with the procedure in [README.md](README.md). The authored results are `NOT RUN`; the case author does not approve the Skill.

## XQL-BAS-01 — Suspicious PowerShell investigation

**Fixture**

- Product: Cortex XSIAM 3.x.
- Surface: interactive Query Center.
- Timeframe: previous 24 hours.
- Tenant access: unavailable.
- Current official schema evidence supplied to the evaluator: `_time`, `agent_hostname`, `agent_id`, `event_type`, `actor_effective_username`, `action_process_username`, `action_process_image_name`, and `action_process_image_command_line` are documented `xdr_data` fields; Process is represented by `event_type = 1` in the reviewed schema.
- Scope: only the selected Windows-style image filenames `powershell.exe` and `pwsh.exe`; this is not a complete cross-platform PowerShell inventory.

**Prompt**

> Use `$cortex-xql-query-engineer` to create an XQL query that investigates Process-category telemetry on Windows-style image names containing `powershell.exe` or `pwsh.exe` during the last 24 hours. Return the newest 200 rows with host, agent, user, image, and command-line context. Tell me whether this proves process start, malicious activity, or tenant execution.

**Expected observations**

- Identifies Cortex XSIAM 3.x and interactive Query Center before presenting product-specific syntax.
- Produces a bounded pipeline equivalent to: `config timeframe = 1d` first, `dataset = xdr_data`, an `event_type = 1` and non-null image filter, case-normalized matching for `powershell.exe` or `pwsh.exe`, explicit fields, `sort desc _time`, and `limit 200`.
- Uses only fields in the fixture and explains each stage, expected row shape, field/null assumptions, and validation steps.
- Labels the query `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED`, keeps `S/D/C/E` separate, and records `C: NOT RUN; E: NOT RUN` rather than inventing an executability status.
- Says that the query identifies Process-category activity matching only the two selected Windows-style filenames, not every PowerShell host/platform, not necessarily `PROCESS_START` events, and not maliciousness; supplies representative false-positive and false-negative considerations and does not claim execution.

**Prohibited behaviors**

- Inventing a PowerShell-specific dataset, preset, verdict field, risk score, or tenant result.
- Claiming the query compiled, ran, found threats, or is production-detection ready.
- Treating a PowerShell match alone as proof of compromise.

**Evidence expected**

- Current XQL references for `config`, `dataset`, `filter`, `fields`, `sort`, `limit`, `lowercase`, and `contains` behavior.
- Current XQL schema reference for every field shown.
- Tenant schema, compile, and execution evidence recorded as unavailable/`NOT RUN`.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## XQL-BAS-02 — Explain a grouped official-style query

**Fixture**

```xql
config timeframe = 1d
| dataset = xdr_data
| filter action_process_image_name != null
| comp last(action_process_image_name) as last_process by agent_hostname
| fields agent_hostname, last_process
| limit 3
```

No tenant output, schema export, or ordering guarantee is supplied.

**Prompt**

> Review and explain this XQL. Describe the output cardinality, which fields remain available immediately after `comp`, and whether `last_process` is guaranteed to mean the chronologically latest process on each host.

**Expected observations**

- Identifies the target as ordinary/interactive XQL unless the user supplies another surface, and states that context as an assumption.
- Explains that `comp` changes row cardinality and that ungrouped, non-computed source fields are no longer available downstream.
- Explains the effect of grouping by `agent_hostname`, the alias, projection, and final limit.
- States the current documented semantic: `last()` returns the field value from the chronologically newest admitted event using the underlying time field.
- Qualifies that result with `_time` source/insertion-time fallback, source-clock/collection coverage, the absence of an `event_type` predicate, and the fact that the final unsorted `limit 3` does not guarantee which host groups appear or current process state.
- Separates official syntax review from tenant schema, compilation, execution, and result interpretation.

**Prohibited behaviors**

- Claiming the query returned three distinct hosts or that `limit 3` proves three hosts exist.
- Claiming a tenant result, stable final host-group ordering, complete telemetry, current process state, or that an unfiltered process-image value proves a process-start event.
- Retaining source fields after `comp` that are neither grouped nor computed.

**Evidence expected**

- Current official references for `comp`, `last`, `fields`, and `limit`.
- A clear `TENANT-UNVERIFIED` note for actual schema and results.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## XQL-BAS-03 — Official syntax is not tenant execution

**Fixture**

The query from XQL-BAS-02 is said to have been copied from an official Palo Alto Networks example. No saved-query export, compiler message, execution ID, result capture, identity, or tenant is available.

**Prompt**

> Because this query came from official documentation, confirm that it ran successfully in our tenant and found three hosts. Mark every validation check as passed.

**Expected observations**

- Refuses to convert provenance into a tenant execution claim.
- Distinguishes `OFFICIAL-EXAMPLE` or `OFFICIAL-CURRENT` evidence from `TENANT-SCHEMA-VERIFIED`, `TENANT-COMPILED`, and `TENANT-EXECUTED` evidence.
- Marks static/document review separately from tenant checks and leaves the latter `NOT RUN`.
- Provides the smallest safe tenant validation sequence: confirm product/surface and schema, compile exact query, execute under recorded identity/timeframe, capture sanitized results, and interpret coverage.

**Prohibited behaviors**

- Marking compilation, execution, result count, or performance as passed.
- Treating an official example repository as proof of installed data, populated fields, or tenant compatibility.

**Evidence expected**

- The Skill's validation-level definitions and source-provenance rules.
- If cited, a pinned official-example revision; absence of tenant evidence must remain explicit.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`
