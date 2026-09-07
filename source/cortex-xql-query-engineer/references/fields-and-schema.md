# Fields, Types, and Schema Evidence

Use this reference to validate field names and types, choose output columns, or diagnose null and alias behavior. It deliberately includes only a small officially documented field set used by this Skill's examples.

**Documentation review cut:** 2026-09-04  
**Schema status:** the fields below are documented in the current general XDR data schema; no target tenant was inspected.

## Contents

- Verified example field set
- Process category and subtype invariant
- Field validation hierarchy
- Projection and aliases
- Derived fields
- Null behavior and missing fields
- Type-sensitive operations
- Aggregation changes the schema
- XDM and project namespace boundaries
- Reusable field contract

## Verified example field set

| Field | Current documented type | Current documented meaning | Evidence |
|---|---|---|---|
| `_time` | `INTEGER` | Data entry timestamp; if unknown, the insertion time is used. | `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED` |
| `agent_hostname` | `STRING` | Hostname of the agent. | `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED` |
| `agent_id` | `STRING` | Unique identifier per agent. | `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED` |
| `event_type` | `INTEGER` | Event-type identifier; the current schema maps the Process category to `1`. This does not by itself identify `PROCESS_START`. | `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED` |
| `action_process_image_name` | `STRING` | File name from the action process image path. | `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED` |
| `action_process_image_command_line` | `STRING` | Command used to execute the process. | `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED` |
| `action_process_username` | `STRING` | Name assigned to the action process user SID. | `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED` |
| `actor_effective_username` | `STRING` | Name assigned to the effective actor SID; on Windows it includes the domain. | `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED` |

Sources: [XDR data fields](https://cortex-docs.paloaltonetworks.com/xql-schema-reference/xdr-data-fields.md), [action actor fields](https://cortex-docs.paloaltonetworks.com/xql-schema-reference/xdr-data-fields-by-actor/action-actor.md), and [actor actor fields](https://cortex-docs.paloaltonetworks.com/xql-schema-reference/xdr-data-fields-by-actor/actor-actor.md).

These entries support documentation-grounded example syntax; they do not establish:

- that a named XSIAM or XDR tenant exposes the same schema revision;
- that the field is populated for the selected event, operating system, integration, or timeframe;
- that the querying identity can see the row or column;
- that a restricted rule context accepts the field;
- that `event_type = 1` alone identifies malicious process activity.

## Process category and subtype invariant

Keep these propositions separate in every build, review, and explanation:

- `event_type = 1` is documentation evidence for the broad Process category in the reviewed `xdr_data` schema.
- It is not sufficient evidence that every admitted row is a process start or execution. Current BIOC guidance shows `PROCESS_START` as a distinct subtype.
- The presence or non-null value of an `action_process_*` field does not independently prove the row's event category or subtype.
- A query with no `event_type` predicate must be described as operating on all admitted rows that populate the selected field, not as a Process-event query.
- A start-only design must verify the target product/editor's current `event_sub_type` representation, add that predicate, and test positive Process Start and negative non-start Process fixtures. Do not invent a numeric subtype value.

The distinction is semantic, not cosmetic: it changes counts, deduplication populations, baselines, and detection coverage.

## Field validation hierarchy

| Evidence observed | Classification | What to do |
|---|---|---|
| Field appears only in a user prompt, project summary, filename, or old query | `UNVERIFIED / TENANT-UNVERIFIED` | Keep it out of executable code; request schema or mark a conceptual placeholder. |
| Current product-specific official schema documents it | `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | It may appear in a documentation-grounded query for that scope; record `D: PASS`, `C: NOT RUN`, and `E: NOT RUN` unless tenant evidence exists. |
| First-party sample uses it | `VERSION-DEPENDENT / OFFICIAL-EXAMPLE / TENANT-UNVERIFIED` unless separately in current schema | Pin the example revision and verify current schema before reuse. |
| Tenant schema/autocomplete shows name and type | `TENANT-SCHEMA-VERIFIED` | Record product, tenant, identity, surface, and date. |
| Compiler accepts the full query | `TENANT-COMPILED` | Record exact query and compiler evidence; do not claim results. |
| Execution returns or evaluates the field | `TENANT-EXECUTED` | Record timeframe, identity scope, raw result evidence, and null/coverage observations. |

Autocomplete is useful evidence but can lag indexing or configuration. Preserve the observation date and supplement it with a bounded probe where authorized.

## Projection and aliases

The `fields` stage is projection, not transformation:

```xql
| fields _time, agent_hostname, action_process_image_name as process_name
```

Status: `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED` for the current documented fields and general XQL context; `D: PASS`, `C: NOT RUN`, `E: NOT RUN`.

Rules:

- `fields` does not accept functions and cannot create values; use `alter` for derived fields.
- Subsequent stages see only retained fields, plus documented non-excludable system fields.
- After `as process_name`, downstream stages must use `process_name`, not `action_process_image_name`.
- In dataset queries, current documentation identifies `_time`, `_insert_time`, `_raw_log`, `_product`, `_vendor`, `_tag`, `_snapshot_id`, `_snapshot_log_count`, `_snapshot_collection_ts`, and `_id` as non-excludable if present. In XDM queries, `_time` cannot be excluded if present.
- Project only the fields needed for the next stages and the final analytical decision.

Do not place `fields` before a later filter, join, aggregation, or sort that still needs a removed field.

## Derived fields

Create or modify a field with `alter`:

```xql
| alter process_name_normalized = lowercase(action_process_image_name)
```

Status: `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED` for general XQL with the documented input field; `D: PASS`, `C: NOT RUN`, `E: NOT RUN`. `lowercase()` requires a string and returns `NULL` when its input is `NULL`.

Before deriving a value, record:

- input field and type;
- function page and target-context compatibility;
- null and conversion behavior;
- derived field name and expected type;
- whether overwriting an existing field is intended;
- downstream stages that depend on the result.

## Null behavior and missing fields

Use explicit null handling when it changes interpretation:

```xql
| filter action_process_image_name != null
```

A field not visible in results can mean:

- the field is invalid for the product/schema;
- the field exists but is null in all returned rows;
- the selected event type or source does not populate it;
- a preceding `fields`, `comp`, or alias removed/renamed it;
- the identity cannot see the relevant rows;
- ingestion, parsing, mapping, retention, or timeframe excluded the data.

For Cortex XSIAM BIOC testing, current documentation says the Schema tab displays a field only when at least one result contains a non-null value. Absence from that view is therefore not by itself proof that the schema lacks the field.

## Type-sensitive operations

| Operation | Required check |
|---|---|
| Comparison | Both operands have compatible types; numeric-looking strings are not silently assumed numeric. |
| `contains`, regex, `lowercase` | Input is a string and null behavior is acceptable. |
| Sort | Convert numeric strings with a documented function before expecting numeric order. |
| Join | Left/right key types and normalization match; key multiplicity and null keys are understood. |
| `dedup` | Keys are string or numeric; null-key treatment is deliberate; retention order is explicit with `by` when it matters; final display order is handled separately. |
| `comp count()` | Counts rows. |
| `comp count(field)` | Counts non-null field values, not all rows. |
| `last(field)` | Returns the newest field value by event chronology; a null newest value yields null. |
| JSON extraction | Choose the function whose documented return shape matches object, scalar, object array, or scalar array. |
| `regextract()` | Resolve the official scalar-versus-array version conflict before downstream type assumptions. |

## Aggregation changes the schema

After `comp`, only grouping fields and computed columns remain. For example:

```xql
| comp count() as process_events by agent_hostname
```

The downstream schema contains `agent_hostname` and `process_events`; it no longer contains `_time`, `event_type`, or process fields unless they were grouped or computed. Status: `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED` when appended to a documentation-grounded query; `D: PASS`, `C: NOT RUN`, `E: NOT RUN` absent tenant evidence.

Review every stage as a schema transformation:

```text
source fields
-> filter dependencies
-> derived fields
-> projected fields
-> join conflict resolution
-> aggregation/dedup cardinality
-> final output contract
```

## XDM boundary

The current [XSIAM Data Model schema](https://cortex-docs.paloaltonetworks.com/xsiam-data-model-schema/readme.md) is the canonical reference for XDM fields, aliases, constants, and fieldsets. It does not prove that the target tenant has mapped or populated a field. Keep raw-dataset names and XDM fields in separate schema records; do not substitute one for the other by semantic similarity.

## Project namespace boundary

Names such as `SOCFramework.*`, `SOCN1.*`, and `Assessment.*` are local project contracts. They are not XQL fields unless a target tenant schema independently shows them. Endpoint/application exports with `Endpoint ID` and `Endpoint Name` headers do not establish the source dataset or XQL field names.

If a requested name is not in current official documentation or target schema:

1. label it `UNVERIFIED`;
2. state where the name came from;
3. request the exact schema/autocomplete/export evidence;
4. offer a conceptual placeholder, not a plausible replacement;
5. never transform `xdr_super_magic_events` or `detect_malware_now()` into believable Cortex syntax.

## Reusable field contract

Record this for each nontrivial query:

| Attribute | Value |
|---|---|
| Literal field | Exact spelling. |
| Product/source | Product, dataset or data model, and version. |
| Type | Documented or tenant-observed type. |
| Evidence | Canonical class and qualifiers. |
| Population | Event/source conditions and observed null rate, or `Unknown`. |
| Use | Filter, join key, grouping, derived input, sort, or display. |
| Transformation | Alias/function and resulting type. |
| Sensitivity | PII, credential, command line, hostname, identifier, or other handling note. |
| Limitation | Permissions, OS/event coverage, retention, version, or context restriction. |

See [xql-language.md](xql-language.md) for stage semantics, [datasets.md](datasets.md) for source proof, and [troubleshooting.md](troubleshooting.md) for field-related failures.
