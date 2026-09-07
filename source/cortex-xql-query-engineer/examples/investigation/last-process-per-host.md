# Last Recorded Process per Host

This is a current first-party command-reference example, retained as a reproducible learning case rather than evidence of a tenant's schema population or activity.

## Context and evidence

| Item | Value |
|---|---|
| Objective | Return the last recorded non-null process-image field value across all admitted `xdr_data` rows for each visible agent hostname, then retain at most three groups. The sample has no Process-category filter. |
| Product | Cortex XSIAM 3.x using the current general Cortex XQL command reference |
| Surface | Interactive Query Center against `xdr_data` |
| Canonical class | `VERIFIED` |
| Qualifiers | `OFFICIAL-EXAMPLE`, `TENANT-UNVERIFIED` |
| S validation | `NOT RUN` — no independent response evaluation was performed for this example. |
| D validation | `PASS` — the cited current official example and command/schema references support the displayed query for the stated documentation scope. |
| C validation | `NOT RUN` — no target-tenant schema or Query Center compilation was inspected. |
| E validation | `NOT RUN` — the query was not executed and no tenant result was observed. |
| Source revision | Current `last()` command-reference page reviewed 2026-09-04 |
| Tenant evidence | None; compilation, execution, rows, ordering, and performance were not observed. |

## Query

**VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED**  
**Product/context: Cortex XSIAM 3.x, interactive Query Center, `xdr_data`**

- `S: NOT RUN` — no independent response evaluation was performed for this example.
- `D: PASS` — the cited current official example and command/schema references support the displayed query for the stated documentation scope.
- `C: NOT RUN` — no target-tenant schema or Query Center compilation was inspected.
- `E: NOT RUN` — the query was not executed and no tenant result was observed.

```xql
config timeframe = 1d
| dataset = xdr_data
| filter action_process_image_name != null
| comp last(action_process_image_name) as last_process by agent_hostname
| fields agent_hostname, last_process
| limit 3
```

## Explanation

1. The timeframe is bounded to one day.
2. The explicit `xdr_data` source avoids reliance on a changed tenant default.
3. Null process-image values are excluded before aggregation.
4. `comp` changes the grain from admitted event rows to one group per `agent_hostname`. The query does not filter `event_type`, so a populated process-image field must not be used to relabel every input as a Process event. The official `last()` example describes the value as the chronologically newest recorded non-null field value in each group; without controlled tenant evidence, this remains documented intent rather than a guarantee about timestamp quality or event meaning.
5. After `comp`, only the group field and computed alias are available here; `fields` projects them.
6. `limit 3` caps displayed groups. Because there is no `sort`, it does not guarantee which three host groups appear.

## Expected output

The output has at most three rows and two columns: `agent_hostname` and the alias `last_process`. That alias names a field value; it does not prove that the newest admitted row is a Process event, a process start, or current process state. It is a visibility snapshot, not a detection, and the query does not provide the original event timestamp or command line after aggregation. Validate category/subtype scope and chronological behavior with controlled records if either is material to the decision.

Zero rows are inconclusive until dataset visibility, endpoint coverage, retention, permissions, hostname and image-name population, and the timeframe are checked.

## False positives, false negatives, and limitations

- “False positive” is not a useful verdict for this inventory-style query; ordinary system processes are expected.
- The three-row limit can omit nearly every host in a tenant and must not be mistaken for fleet coverage.
- Hosts with null `agent_hostname` or `action_process_image_name`, no visible events, collection gaps, retention gaps, or restricted data scope can be absent.
- `_time` is the documented data-entry timestamp and can fall back to insertion time when the original time is unknown. A latest recorded field value can therefore differ from source execution order because of delayed ingestion, clock problems, missing events, or coverage gaps.
- Grouping by hostname can merge records if names are reused or ambiguous. If identity precision matters, validate and include a tenant-observed stable key.

## Optimization notes

`comp` is a blocking aggregation and must examine the bounded input before it can produce groups. The final `limit` reduces output but does not prove the aggregation processed only three hosts. Keep the smallest useful timeframe, add only semantically justified early filters, and inspect group cardinality. Do not add a pre-aggregation limit merely to make the query faster: it would change the population and can change the “last” result. No performance measurement was run.

## Troubleshooting

- **Unknown field or dataset:** inspect current tenant schema/autocomplete and verify product/release; do not substitute a similar name from memory.
- **No results:** check ingestion, retention, collection status, RBAC/SBAC scope, null population, and the one-day window.
- **Unexpected process:** retrieve the underlying event using tenant-verified timestamp and identity fields rather than interpreting the aggregate alone.
- **Unexpected host count:** remember the final limit and verify whether hostname reuse or null values affect grouping.

## Rule-conversion boundary

- This query is not BIOC-compatible as written because it uses an aggregate plus `fields` and `limit`, outside the documented BIOC query subset.
- It is not real-time-correlation compatible as written because `config timeframe`, `comp`, and `limit` are outside the documented real-time stage set (only `config case_sensitive` is listed for `config`).
- Scheduled-correlation eligibility, rule action, signal meaning, and volume were not validated.
- It is not XQLp; parsing rules use a modified grammar and different source model.

## Official references

- [`last()` function and first-party example](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/functions/last.md)
- [`comp` stage](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/stages/comp.md)
- [`fields` stage](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/stages/fields.md)
- [`limit` stage](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/stages/limit.md)
- [`xdr_data` field reference](https://cortex-docs.paloaltonetworks.com/xql-schema-reference/xdr-data-fields.md)

Use [the tenant validation record](../../templates/tenant-validation.md) to record any real test.
