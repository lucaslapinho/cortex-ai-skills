# Telemetry, signal, and query handoff

## Contents

- [Telemetry evidence matrix](#telemetry-evidence-matrix)
- [Time and coverage](#time-and-coverage)
- [Entity and cardinality contract](#entity-and-cardinality-contract)
- [Query handoff](#query-handoff)
- [Signal contract](#signal-contract)
- [Issue and Case fields](#issue-and-case-fields)
- [Missing telemetry](#missing-telemetry)

## Telemetry evidence matrix

Build one row per required observation:

| Observation | Source/product | Dataset or preset | Event category/subtype | Fields and types | Time semantics | Coverage/retention | Access | Evidence status |
|---|---|---|---|---|---|---|---|---|
| `<behavioral clause>` | `<source>` | `<verified or placeholder>` | `<exact semantics>` | `<name:type:nullability>` | `<event/insert>` | `<known gap>` | `<role/scope>` | `<status / qualifiers>` |

For tenant claims, retain the schema/autocomplete/export evidence and identity scope. A documented XDM field is not proof that it is mapped or populated in this tenant.

Required quality checks:

- source emits the relevant event under positive and negative controls;
- parser/mapping preserves the differentiating value;
- event category and subtype are independently verified;
- required fields are non-null often enough for the logic;
- identities/hosts are normalized without merging distinct entities;
- clocks, timezones, latency, and retention support the window;
- RBAC/SBAC does not hide rows;
- expected data loss and blind spots are quantified or marked unknown.

## Time and coverage

Keep these clocks distinct:

| Clock | Meaning |
|---|---|
| Source event time | When the producing system says the event occurred |
| Ingestion/insert time | When Cortex accepted or indexed the record |
| Query window | Data-time interval evaluated by the rule |
| Execution time | When a scheduled rule ran or a real-time path admitted data |
| Issue time | When the product generated the Issue |
| Case/grouping time | When qualification/grouping behavior occurred |

Test late, duplicated, replayed, and out-of-order events. A scheduled window must state how gaps and overlaps are handled. A real-time rule still depends on collection, parsing, ingestion, and supported evaluation behavior.

Negative evidence is valid only within coverage. “No matches” must list sources checked, retention, timeframe, parser/mapping, schema, null behavior, permissions, rule state, and known gaps.

## Entity and cardinality contract

Before aggregation or correlation, define:

- one input row's meaning;
- correlation keys and normalization;
- key uniqueness and null behavior;
- acceptable many-to-many expansion;
- sequence/order semantics;
- one output row's meaning;
- which raw events remain recoverable for drill-down;
- duplicate suppression and replay handling.

For every aggregation, write:

```text
Before: one row = ...
Group keys = ...
Window = ...
Measure = ...
After: one row = ...
Fields discarded = ...
```

Do not use hostname, username, IP, or process name as a stable unique identity without documenting collisions, reassignment, normalization, and scope.

## Query handoff

A detection-focused query contract contains:

1. product, version, rule surface, and objective;
2. dataset/preset and field/type evidence;
3. event category and subtype semantics;
4. admission and exclusion predicates;
5. window, sequence, aggregation, and threshold;
6. null, duplicate, latency, and cardinality handling;
7. output grain and required triage/grouping fields;
8. expected match volume and bound;
9. positive, benign, negative, boundary, and volume fixtures;
10. rule-context restrictions and remaining compiler test;
11. evidence status and exact next validation step.

Executable XQL requires current official support for all shown constructs and adequate dataset/field evidence. When concrete tenant fields are unknown, use visible tokens such as `<PROCESS_IMAGE_FIELD>` rather than plausible names.

Never claim that Query Center success proves BIOC or correlation compatibility. Test the exact rule editor/compiler.

## Signal contract

Define:

| Field | Requirement |
|---|---|
| Signal unit | One row/match represents exactly what? |
| Risk statement | Which hypothesis is supported? |
| Non-claim | What does the match not establish? |
| Triage evidence | Which raw values let an analyst verify it? |
| Provenance | Rule ID/revision/source and contributing event IDs |
| Severity rationale | Asset/impact/confidence, not technique label alone |
| Next step | Smallest investigation that discriminates benign/malicious |
| Safety | Which actions are prohibited without separate approval? |

The expected output is a design expectation until tenant execution is retained. Do not fabricate hit counts, timestamps, Issue IDs, or Case grouping.

## Issue and Case fields

Current XSIAM correlation configuration can map query outputs into Issue fields. Mapping has two separate objectives:

- give analysts useful Issue context and drill-down inputs;
- contribute correctly formatted artifacts that may influence grouping.

Validate non-nullness, type/format, normalization, cardinality, sensitivity, and stability. Field mapping does not guarantee grouping. Avoid overly broad identifiers that over-group unrelated activity.

Preserve current Case/Issue terminology in prose. Retain literal Alert/Incident identifiers only when a supported technical surface requires them. See [official source records S03, S12, and S13](official-sources.md).

## Missing telemetry

Trace:

```text
expected event
  -> source generation
  -> agent/collector/integration
  -> transport and authentication
  -> ingestion health
  -> parsing/mapping
  -> dataset/schema
  -> permissions
  -> query/rule visibility
```

Detection engineering owns the requirement and confidence impact; platform engineering owns concrete collector/parser configuration. A standalone response must still identify the broken boundary and the exact evidence needed without inventing ports, settings, datasets, or fields.

When a required source is absent:

- do not lower the threshold to compensate;
- do not interpret zero rows as absence of behavior;
- mark coverage and false-negative impact;
- identify a compensating observable if supported;
- define the smallest source or schema validation step;
- keep the candidate out of production if the missing source is essential.
