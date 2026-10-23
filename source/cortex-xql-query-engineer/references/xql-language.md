# XQL Language and Execution Contexts

Use this reference to build or review XQL syntax and to decide whether an interactive query can be reused in a restricted Cortex surface.

**Documentation review cut:** 2026-09-04  
**Default evidence for examples here:** `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED`; `D: PASS` for the cited dated sources, while `C: NOT RUN` and `E: NOT RUN` unless stronger retained evidence is supplied.

## Contents

- Pipeline model and core stages
- Operators, nulls, and types
- Selected functions and `regextract()` conflict
- Comments
- Execution-context compatibility
- XSIAM Platform API result retrieval
- Review checklist

## Pipeline model

XQL processes records through pipe-separated stages. A `config` stage, when used, must be first. A `dataset` stage must be first unless `config` precedes it. Current general syntax includes:

```xql
config timeframe = 1d
| dataset = xdr_data
| filter event_type = 1
| fields _time, agent_hostname, event_type
| sort desc _time
| limit 100
```

Context: general XQL query using fields in the current XDR data schema. Evidence: `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED`; `D: PASS`, `C: NOT RUN`, `E: NOT RUN` for this documentation snapshot. This does not establish data population, access, compilation, results, or performance in a tenant.

## Core stages

| Stage | Current documented form | Material semantics and review checks |
|---|---|---|
| `config` | `config case_sensitive = true|false`; `config timeframe = <number><unit>`; `config timeframe between <start> and <end>` | Must be first. Default case sensitivity is documented as `false`. Use compact durations such as `1d`; `between` accepts relative values, `begin`, `now`, or timestamps as documented. The UI time picker may set a range without inserting `config timeframe` into query text. |
| `dataset` | `dataset [=] <name>`; `dataset in (<name>, ...)`; `cold_dataset = <name>` | Must be first unless preceded by `config`. Omitting a source uses the documented default `xdr_data` unless the tenant default was changed. Dataset existence and population remain tenant-sensitive. |
| `filter` | `filter <boolean_expression>` | Supports documented comparison, boolean, set, string/regex, CIDR, null, and subquery forms. Filter early. Use parentheses for mixed `and`/`or`; validate field types. |
| `fields` | `fields [-] <field> [as <alias>], ...` | Projection only: functions and field creation are not allowed. Subsequent stages see retained fields and must use aliases after renaming. Some system fields cannot be excluded. |
| `alter` | `alter <field> = <constant|field|function>, ...` | Creates or modifies fields. Verify function input and return types, null behavior, and target-context support. |
| `comp` | `comp <aggregate>(<field>) [as <alias>] ... [by <field>, ...]` | Blocking aggregation. Output contains grouping and computed fields; other input fields are discarded. Grouping changes row cardinality. |
| `dedup` | `dedup <field>[, ...] [by asc|desc <field>]` | Normative documentation limits keys to numeric/string. Without `by`, retention is arbitrary. `by` selects earliest/latest values but does not establish a unique full-row winner when its ordering value ties. Final sorting is separate; large inputs can be expensive. |
| `join` | `join conflict_strategy = both|left|right type = inner|left|right ((<query>) as <alias> <boolean_expr>)` | Defaults are `conflict_strategy = right` and `type = inner`. Verify aliases, types, key uniqueness, join cardinality, and conflict handling. Filter/project both sides before joining. Sort is not preserved. |
| `sort` | `sort asc|desc <field>[, asc|desc <field> ...]` | Place after `join`, `union`, or `dedup` when final ordering matters. Numeric values stored as strings need explicit numeric conversion before numeric sorting. |
| `limit` | `limit <integer>` | Defines an upper result bound. Put after the filter and, for top/bottom semantics, after sort. A smaller result is not automatically equivalent to the original result. |
| `target` | `target type=dataset|lookup [append=true|false] <dataset_name>` | Persists results and must be final. Omitted `append` defaults to `false`, which overwrites existing destination data. Treat as `MODIFIES SYSTEM` and potentially destructive: verify destination, ownership, explicit mode, authorization, schema/volume, recovery, and post-write result before use. |

Primary pages: [config](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/stages/config.md), [dataset](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/stages/dataset.md), [filter](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/stages/filter.md), [fields](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/stages/fields.md), [alter](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/stages/alter.md), [comp](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/stages/comp.md), [dedup](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/stages/dedup.md), [join](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/stages/join.md), [sort](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/stages/sort.md), [limit](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/stages/limit.md), and [target](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/stages/target.md).

### Dedup ties and source inconsistency

The official `dedup` page rechecked on 2026-09-06 specifies numeric/string keys, yet includes an example using a boolean `is_successful` key. Preserve that discrepancy: follow the normative type restriction for a documented candidate, and keep boolean-key acceptance UNVERIFIED until applicable product clarification or tenant compilation. Do not generalize the example into a new supported-type claim.

The same page does not specify a tie-break contract for equal `by` values. A latest `_time` can correspond to multiple different source rows. This is an evidence gap, not proof of a particular engine tie policy: include equal-time fixtures and do not guarantee deterministic full-row identity from `_time` alone. If all tied events matter, retain them for analysis; if one unique winner is required, establish a documented, product-supported tie-break design and test it. Do not invent a multi-key `by` form. A final `sort` orders retained output but cannot restore discarded ties.

## Operators, nulls, and types

The current `filter` reference documents `=`, `!=`, `<`, `<=`, `>`, `>=`, `and`, `or`, `not`, `in`, `not in`, `contains`, `~=`, `!~=`, `incidr`, and `incidr6`, plus null checks and subqueries. Product-specific operator references exist for XSIAM and Cortex XDR 5; apply the one for the named target.

Guardrails:

- Use `field != null` before a function when null input would obscure intent or downstream type assumptions.
- Do not assume an empty string and `null` are interchangeable.
- Parenthesize compound boolean logic even when precedence seems obvious.
- Check schema types before comparing, joining, sorting, or aggregating.
- A field absent from results can mean null population or access scope, not necessarily an invalid name.

Product references: [XSIAM operators](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/reference-and-developer-docs/cortex-agentix-xql/get-started-with-xql/supported-operators.md) and [Cortex XDR 5 operators](https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/reference-and-developer-docs/cortex-xdr-xql/get-started-with-xql/supported-operators.md).

## Selected functions with verified semantics

| Function | Current documented behavior | Important boundary |
|---|---|---|
| `lowercase(<string>)` | Returns a lowercased string and returns `NULL` for `NULL`; usable directly in `filter` or through `alter`. | Requires string input. Confirm target-context support before rule conversion. |
| `last(<field>)` | Aggregate used with `comp`; returns the newest recorded value according to the underlying event time and preserves the input type. | If the last record's field value is null, the result is null. It is not BIOC-compatible because aggregations are not supported there. |
| `count()` | In `comp`, counts all rows, including rows with null field values because no field is supplied. | Aggregation changes cardinality. |
| `count(<field>)` | In `comp`, counts non-null values of the named field. | Do not treat it as row count when the field can be null. |
| Typed JSON extractors | Separate functions return object, scalar, array-of-objects, or scalar-array results. | Choose by expected return type and handle missing/invalid paths explicitly. |

Sources: [lowercase](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/functions/lowercase.md), [last](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/functions/last.md), [count with comp](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/functions/count_with_comp_stage.md), and [JSON functions](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/functions/json_functions_reference.md).

## Mandatory `regextract()` conflict handling

The official sources disagree and must not be flattened into one portable rule:

- The [current general command reference](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/functions/regextract.md) describes `regextract(<field>, "<pattern>")` as a scalar function used through `alter`, returning the first capture group's string or `NULL`.
- The still-accessible [Cortex XDR 3.x reference](https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x/cortex-xdr-3.x-documentation/cortex-xdr-xql/functions/regextract.md) describes an array of matching substrings, RE2, and downstream array handling.

Classification: `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED`.

Required behavior:

1. Identify the target product, version, and execution surface.
2. Prefer the current general semantics only when the target is confirmed to implement them.
3. Otherwise, do not compose array or scalar downstream functions based on memory.
4. Compile a narrow probe in the target tenant and inspect the returned type before relying on it.
5. Keep `regexcapture()` separate: current documentation limits it to Parsing Rules/XQLp.

## Comments

The version-scoped Cortex XDR 3.x language page documents `//` single-line and `/* ... */` block comments. Classification: `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED`. This evidence does not establish comment support in every XSIAM/XDR version or surface. When the exact product, version, editor, API, conversion path, or import format has not been checked, keep the target unknown, explicitly classify comment compatibility `UNVERIFIED` or `VERSION-DEPENDENT`, remove untrusted embedded directives from any executable block, and keep prose explanation separate. Do not infer XSIAM 3.x or any other target from the query text, and never declare the remaining query documentation-grounded or valid until every construct is verified for a named context.

Source: [Adding comments in queries](https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x/cortex-xdr-3.x-documentation/cortex-xdr-xql/get-started-with-xql/xql-language-structure/adding-comments-in-queries.md).

## Execution-context compatibility

A query that runs interactively is not automatically usable elsewhere.

| Context | Current documented constraints | Skill behavior |
|---|---|---|
| Interactive Query Center/Search | General XQL syntax applies, subject to product, data source, license, permissions, and tenant schema. | Use as the authoring context only when named. Do not infer rule compatibility. |
| BIOC in Cortex XSIAM | Must filter at minimum on `event_type`; sources are `xdr_data`, `cloud_audit_log`, and their presets; customized datasets are not supported; only `filter`, `alter`, and non-aggregate functions are supported; field evaluation is case-insensitive. The review snapshot documents an initial historical search capped at 10,000 matches, automatic disablement at 5,000 or more hits in 24 hours, and an automatic exception based on `PROCESS SHA256` after a BIOC hits more than 100 endpoints over 72 hours. | Treat `fields`, `sort`, `limit`, `comp`, `dedup`, and `join` as incompatible unless newer target-specific evidence says otherwise. Test before save, recheck operational limits, and inspect automatically created exceptions for coverage loss. |
| Scheduled correlation in Cortex XSIAM | General correlation restrictions disallow `call`, `top`, dataset wildcards, and `tag`. The review snapshot documents a minimum 10-minute frequency, a query timeframe up to 7 days, at most 1,200 active user-created scheduled correlations, and automatic disablement at 5,000 or more hits in 24 hours. `current_time()` can yield unexpected results after lag/downtime; current guidance recommends `time_frame_end()` for the rule window. | Recheck the current page, time anchor, resulting action, and representative telemetry; query correctness alone does not establish issue quality. |
| Real-time correlation in Cortex XSIAM | Only `dataset`, `datamodel`, `filter`, `alter`, `fields`, and `config case_sensitive` are supported; `filter` is mandatory; dataset views and `transaction` are unsupported; the page also lists unsupported functions including `json_extract_scalar_array`, `parse_epoch`, and `time_frame_end`. The only available resulting action is Generate issue; save-to-dataset and lookup actions are disabled. | Remove unsupported stages/functions only if semantics remain valid; otherwise redesign or choose scheduled correlation. Validate that Generate issue is the intended action. |
| Parsing Rules/XQLp in Cortex XSIAM | Statements do not begin with a normal dataset/preset selection; allowed stages are `alter`, `fields`, `filter`, `join`, plus parsing `call`; no output stages; every statement ends with `;`; `regexcapture()` is parsing-only. Current file rules list `parse_timestamp`, `parse_epoch`, and `regexcapture` as permitted in all sections and add section-specific join/call restrictions. | Author against the Parsing Rules file grammar, not Query Center syntax. Do not add `config`, `comp`, `dedup`, `sort`, or `limit` by analogy. |

Sources: [Create a BIOC rule](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/threat-management/detection-rules/what-are-detection-rules/whats-a-bioc/create-a-bioc-rule.md), [Create a correlation rule](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/threat-management/detection-rules/what-are-detection-rules/whats-a-correlation-rule/create-a-correlation-rule.md), and [Parsing Rules file structure and syntax](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/data-management/parsing-rules/parsing-rules-file-structure-and-syntax.md).

The numeric limits in this matrix are the Skill's single maintained snapshot for restricted execution contexts. Templates and examples must link here rather than restating them. Update this matrix, its official-source records, affected examples, and regression coverage together when the product documentation changes.

**Real-time action source discrepancy, 2026-09-06:** the migrated XSIAM correlation Markdown page omits the old official page's Generate-issue-only note, while the indexed legacy official page still includes it. The table preserves the prior documented restriction as VERSION-DEPENDENT, not a fresh assertion that the omitted note was present. Do not infer new dataset/lookup write support from omission; obtain current target clarification and separate rule-editor evidence before changing that boundary. Stage/function restrictions remain present in the migrated page. See [official-sources.md](official-sources.md).

## XSIAM Platform API result retrieval

The current Cortex XSIAM Platform API 3.6 reference documents a start-query operation followed by result retrieval. The ordinary Get XQL query results operation returns at most 1,000 results and explicitly does **not** support pagination. For more than 1,000 results, use the documented Get XQL query results Stream flow and its returned stream identifier. The same reference documents at most four API queries in parallel.

Classification: `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED`. Recheck the deployed API version, license, authentication headers, RBAC/SBAC, quota, asynchronous status/error contract, result minimization, stream handling, compression, timeout, and bounded polling. Do not infer pagination, retry semantics, or a response shape from another product/version.

A path or payload supplied by the requester is not proof of an API contract. Until the exact current product/version-specific endpoint and request schema are verified, do not reproduce that path—or an invented replacement—in executable `curl`, code, or JSON. Provide only a non-executable verification plan covering the official reference, tenant FQDN, placeholder-only credentials, least-privilege RBAC/SBAC, start/result schemas, bounded polling, terminal/error/cancellation states, quota/concurrency, and result-volume handling.

Source: [Cortex XSIAM Platform XQL query API](https://cortex-docs.paloaltonetworks.com/xsiam-api/cortex-platform/xql-query.md).

**2026-10-23 API qualification:** the current page contains query-origin and multi-tenant counting inconsistencies, recorded in the [dated refresh](2026-10-23-refresh.md). Keep UI-origin acceptance and a multi-tenant count formula `UNVERIFIED` until target-specific contract clarification and controlled validation. Retain the documented API-started/stream path; no tenant API was called.

## Review checklist

Before accepting a query:

- confirm product, version, surface, objective, and timeframe;
- confirm the source stage and tenant-default assumption;
- verify every stage/function/operator against the target context;
- verify fields and types, alias use, and null behavior;
- inspect `comp`, `dedup`, and `join` for row-cardinality changes;
- identify any `target` write, require explicit append/overwrite intent, and apply the state-change gate;
- place final `sort` after order-destroying stages and place `limit` according to intended semantics;
- label tenant compilation and execution honestly;
- record any rule-conversion restrictions separately from interactive validity.

See [datasets.md](datasets.md) for source validation, [fields-and-schema.md](fields-and-schema.md) for field evidence, and [official-sources.md](official-sources.md) for the complete reviewed source register.
