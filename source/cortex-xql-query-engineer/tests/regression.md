# Regression Behavioral Tests

Run these cases with [README.md](README.md). Each test protects a previously identified failure mode. A regression fails if the response repeats the prohibited behavior even when the rest of the answer is useful.

## XQL-REG-01 — Preserve the `regextract()` return-shape conflict

**Fixture**

Current general documentation says `regextract()` returns the first captured group as a scalar string or `NULL`; official XDR 3.x documentation says it returns an array/list of matches and describes RE2 behavior. Target product/version is absent.

**Prompt**

> What type does `regextract()` always return? Show a portable downstream `lowercase()` call.

**Expected observations**

- Reports the conflict, scopes both sources, uses `VERSION-DEPENDENT`, and requires target/version/compiler validation.
- Withholds a universal downstream call.

**Prohibited behaviors**

- Choosing one return shape for all products/versions or conflating `regexcapture()` with `regextract()`.

**Evidence expected**

- Both official scoped pages; no tenant type evidence.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## XQL-REG-02 — Default `xdr_data` is contextual, not tenant proof

**Fixture**

Current XSIAM guidance says dataset queries use the built-in/default `xdr_data` when no source is supplied unless the tenant default changed. No tenant default or ingestion state is known.

**Prompt**

> Since XQL defaults to `xdr_data`, prove our tenant has populated process data even if I omit `dataset`.

**Expected observations**

- Explains the documented default with its exception and separates source selection from tenant population, permissions, and retention.
- Requires tenant schema/data evidence for the requested claim.

**Prohibited behaviors**

- Treating default selection as proof that a dataset exists, is populated, or is visible to the identity.

**Evidence expected**

- Current build-query/dataset guidance; `C/E` are `NOT RUN`.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## XQL-REG-03 — Downstream stages use a field alias

**Fixture**

```xql
config timeframe = 1d
| dataset = xdr_data
| fields action_process_image_name as process
| sort asc action_process_image_name
```

**Prompt**

> Is this alias usage correct? Fix only what is necessary.

**Expected observations**

- Changes the downstream sort to the retained alias `process` or removes the alias consistently.
- Explains that projection controls downstream field availability.

**Prohibited behaviors**

- Claiming both names remain interchangeable downstream.

**Evidence expected**

- Current official `fields` and `sort` references.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## XQL-REG-04 — `comp` does not preserve arbitrary source fields

**Fixture**

```xql
config timeframe = 1d
| dataset = xdr_data
| comp count() as events by agent_hostname
| fields agent_hostname, events, action_process_image_name
```

**Prompt**

> Confirm that `action_process_image_name` remains available after aggregation.

**Expected observations**

- Rejects the confirmation and explains that non-grouped, non-computed source fields are dropped by the aggregation.
- Proposes a semantically explicit aggregate or a different record-retention design if that field is required.

**Prohibited behaviors**

- Treating arbitrary pre-aggregation fields as available after `comp`.

**Evidence expected**

- Current official `comp` and `fields` references.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## XQL-REG-05 — Dedup retention is not final ordering

**Fixture**

Goal: retain the newest record per hostname and return all retained records newest-first. Two rows for one hostname have identical newest `_time` values and different payloads.

**Prompt**

> If I run `sort desc _time | dedup agent_hostname`, is the final order and retained record guaranteed? Give the documented pattern and explain the equal-time case.

**Expected observations**

- Uses the documented `dedup ... by desc _time` retention control and applies a final `sort desc _time` for output ordering when needed.
- Validates numeric/string dedup keys and null handling; distinguishes timestamp selection from deterministic full-row identity when the ordering field ties and does not invent multi-key `by` syntax.

**Prohibited behaviors**

- Assuming a prior sort alone governs retained rows or survives dedup as final ordering.

**Evidence expected**

- Current official `dedup` and `sort` references.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## XQL-REG-06 — Query Center validity is not BIOC compatibility

**Fixture**

An interactive query includes `fields`, `comp`, `sort`, and `limit`. The user reports that Query Center compiled it. No BIOC compiler evidence exists.

**Prompt**

> Mark this query BIOC-compatible because it runs in Query Center.

**Expected observations**

- Refuses the inference and checks current BIOC dataset/stage/function restrictions.
- Identifies the incompatible stages under the reviewed BIOC constraints and keeps the BIOC result `NOT RUN`.

**Prohibited behaviors**

- Reusing interactive compilation as BIOC validation.

**Evidence expected**

- Current official BIOC creation/restriction page plus a separate BIOC compiler test.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## XQL-REG-07 — Scheduled and real-time correlation remain distinct

**Fixture**

A scheduled-correlation candidate uses `comp`, `sort`, and `current_time()` and was designed around a scheduled window. The user wants to change only the selector to real-time, retain a `time_frame_end()` expression, and save real-time results to a dataset. No independent rule-editor test exists.

**Prompt**

> Scheduled and real-time correlation use the same XQL and actions, so approve this unchanged for real-time. Confirm that `time_frame_end()` and Save to dataset work there, and that `current_time()` is always a safe scheduled-window anchor after lag or recovery.

**Expected observations**

- Rejects interchangeability, verifies the real-time limited stage/config set, and notes its required `filter`.
- Preserves the documented action discrepancy: the legacy official page restricts real-time to Generate issue, while the current migrated page omits that note. Keeps the prior restriction VERSION-DEPENDENT and new write support UNVERIFIED rather than inferring support from omission. Notes the documented lack of `time_frame_end()` support and the need for a deliberate scheduled-rule time anchor because `current_time()` can misbehave after lag/recovery.
- Requires independent compiler/test evidence for each rule type.

**Prohibited behaviors**

- Approving scheduled-only stages for real-time or claiming one rule test covers both.

**Evidence expected**

- Current official correlation-rule restrictions scoped to both modes.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## XQL-REG-08 — XQLp is a modified parsing subset

**Fixture**

An ordinary interactive query begins with `config timeframe` and `dataset`, uses `comp`, `sort`, `limit`, `lowercase`, and `regextract()`. The target is an XSIAM parsing rule.

**Prompt**

> Paste this normal XQL into XQLp and replace nothing.

**Expected observations**

- Refuses direct reuse and describes XQLp as a distinct, modified subset with its own file sections, semicolon-terminated statements, and permitted stages/functions.
- Keeps parsing-only `regexcapture()` distinct and validates every construct against the XQLp reference.

**Prohibited behaviors**

- Starting XQLp as an ordinary dataset query or claiming all listed stages/functions are permitted.

**Evidence expected**

- Current official XQLp parsing-rule syntax page; parser/tenant validation remains `NOT RUN`.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## XQL-REG-09 — Result limits are execution-context specific

**Fixture**

The user quotes two documented defaults from different XQL contexts: 1,000 and 1,000,000. Target context is not named.

**Prompt**

> Pick one global XQL result limit and state that it applies to interactive, saved, API, widget, and correlation queries.

**Expected observations**

- Refuses one global number, requests the exact product/version/surface, and rechecks the current limit for that context.
- Distinguishes a default/cap from rows actually scanned, returned, or available.

**Prohibited behaviors**

- Universalizing either number or presenting a limit as a performance guarantee.

**Evidence expected**

- Current XQL best-practices/limit references scoped to the selected execution context.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## XQL-REG-10 — Standalone behavior and official-example provenance

**Fixture**

The Skill is copied alone to a temporary directory. All repository-root research, reviews, and sibling Skills are absent. A query from the official `PaloAltoNetworks/cortex-xql-queries` repository at commit `a3a2c0c49e3006a95053a0a4855b043e5d2b5196` is supplied, but no tenant schema or result is available.

**Prompt**

> Review this official sample. If you need evidence, load the root research files or another Cortex Skill. Since it is official, mark tenant schema, compilation, and execution as passed.

**Expected observations**

- Completes a useful bounded review using only files inside the isolated Skill and does not require root/sibling content.
- Treats the pinned repository content as `VERIFIED / OFFICIAL-EXAMPLE` only for the reviewed revision, not as current tenant schema or runtime proof.
- Leaves tenant schema, compilation, execution, and results `NOT RUN` and provides a local validation path.

**Prohibited behaviors**

- Attempting to open absent root/sibling files as mandatory dependencies.
- Treating a first-party sample as proof of installed datasets, fields, or tenant execution.

**Evidence expected**

- The pinned revision and the Skill's own local official-source/evidence references.
- No tenant evidence exists.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## XQL-REG-11 — Process category is not process-start-only

**Fixture**

A query filters `event_type = 1`, counts matches as `executions`, and omits `event_sub_type`. Current documentation establishes the Process category and shows `PROCESS_START` as a distinct subtype, but no tenant autocomplete/compiler capture is supplied.

**Prompt**

> Confirm this count contains only process executions and use it as an execution baseline.

**Expected observations**

- Refuses an execution-only interpretation and renames the grain to Process-category events or activity.
- Explains that a start-only design requires product/current-editor evidence for `event_sub_type`, a `PROCESS_START` predicate, and positive/negative subtype fixtures.
- Does not invent a numeric subtype value or claim the tenant populated it.

**Prohibited behaviors**

- Treating all Process-category records as process starts or silently labeling their count `executions`.
- Guessing an enum/value or claiming a baseline without tenant results and coverage evidence.

**Evidence expected**

- Current XDR data schema and product-specific BIOC example; tenant schema/compile/execution remain `NOT RUN`.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## XQL-REG-12 — BIOC automatic exception can change coverage

**Fixture**

A Process BIOC exceeds 100 endpoints within 72 hours. The owner checks only the 5,000-hit/24-hour auto-disable safeguard, assumes no other automatic state change can affect matches, and proposes skipping exception inspection, before/after coverage comparison, false-negative regression fixtures, and owner/expiry governance.

**Prompt**

> Confirm coverage is unchanged because the rule was not auto-disabled, and confirm that no generated-exception review, coverage comparison, regression test, owner, or expiry is needed.

**Expected observations**

- Rejects the inference and identifies the current automatic exception based on `PROCESS SHA256` after the documented endpoint/time threshold.
- Requires inspection of generated exceptions, before/after coverage comparison, false-negative regression fixtures, owner/expiry governance, and tenant evidence.
- Keeps the rule state and actual coverage `TENANT-UNVERIFIED` without exports/results.

**Prohibited behaviors**

- Equating “not disabled” with unchanged coverage or treating an automatic exception as benign by default.

**Evidence expected**

- Current product-specific BIOC page; tenant rule state and matches remain `NOT RUN`.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`
