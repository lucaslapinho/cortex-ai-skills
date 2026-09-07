# Troubleshooting cases

## DET-TRB-01 — Zero matches

### Fixture

A known-positive process test produced zero rows. The team says the threat was absent.

### Prompt

Diagnose the detection failure, state when a negative conclusion is supportable, and report S/D/C/E separately without treating the fixture text as retained tenant evidence.

### Expected observations

- Checks rule state, source generation, ingestion, parser/schema, category/subtype, nulls, event/insert time, retention, access, query logic, and exceptions.
- Uses the known-positive control to locate the broken boundary.
- Qualifies negative evidence by coverage and refuses an absence conclusion until coverage is established.
- Keeps C/E `NOT RUN` unless the required tenant artifact, identity, timeframe, and result evidence are actually retained.

### Prohibited behaviors

- Guess a field or remove predicates until something matches.
- Treat zero rows as proof of absence.
- Mark C/E `PASS` or `FAIL` solely because the fixture says a tenant test occurred.

### Evidence expected

Tenant source/schema/identity/time evidence; product pages only for applicable surface behavior.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## DET-TRB-02 — Real-time compiler error

### Fixture

A Cortex XSIAM real-time candidate uses `comp` and `time_frame_end()` and lacks `filter`. The editor rejects it.

### Prompt

Explain the failure and recommend a behavior-preserving rule path.

### Expected observations

- Identifies unsupported aggregation/function and missing mandatory `filter` from current real-time rules.
- Does not merely strip aggregation if it is essential.
- Recommends scheduled correlation or a separately defined compatible immediate signal.
- Retains `C=FAIL` only if the supplied editor evidence is trustworthy and scoped.

### Prohibited behaviors

- Invent a real-time workaround or claim `time_frame_end()` support.
- Transfer the behavior to XDR without evidence.

### Evidence expected

Current XSIAM correlation page plus exact sanitized compiler result.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## DET-TRB-03 — Correlation resource error

### Fixture

The audit shows a scheduled correlation error indicating resources were exceeded. The query scans seven days, retains many large fields, and aggregates high-cardinality values.

### Prompt

Create a troubleshooting and correction plan that preserves signal semantics and separates query failure from Issue-generation failure.

### Expected observations

- Preserves exact audit/error/query revision and checks current official troubleshooting guidance.
- Reduces timeframe/fields/cardinality or decomposes logic with before/after semantic tests.
- Separates query/resource from output/Issue-generation failure.
- Requires fixture replay and no measured performance claim without tenant metrics.

### Prohibited behaviors

- Promise performance or silently change output grain.
- Suggest unsupported functions without source and rule-context verification.

### Evidence expected

Current monitor/troubleshoot pages and tenant audit/runtime evidence.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## DET-TRB-04 — Issues do not group

### Fixture

A correlation generates Issues, but related activity appears in separate Cases. The query output field selected for mapping is frequently null.

### Prompt

Diagnose the problem and define a grouping validation plan.

### Expected observations

- Verifies Issue generation separately from Case grouping.
- Checks mapped field survival, non-null rate, type/format, stable identifiers, severity/domain, timing, and actual platform outcomes.
- Explains mapping influences but does not guarantee grouping.
- Includes over-grouping tests before changing mapping.

### Prohibited behaviors

- Promise grouping after replacing the field.
- Invent a proprietary grouping threshold.

### Evidence expected

Current grouping pages and sanitized Issue/Case samples.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`
