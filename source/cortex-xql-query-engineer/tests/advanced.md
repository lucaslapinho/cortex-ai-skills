# Advanced Behavioral Tests

Run these cases with [README.md](README.md). Advanced cases reward a justified validation boundary more than a superficially complete query.

## XQL-ADV-01 — Bounded lateral-movement join

**Fixture**

- Product/surface: Cortex XSIAM 3.x, interactive Query Center.
- Investigation window: 6 hours.
- A sanitized tenant schema capture, dated today, confirms `corp_auth_raw` with `_time` (timestamp), `user_name` (string), `source_ip` (string), `target_host` (string), and `auth_result` (string).
- The same capture confirms `xdr_data` with `_time`, `agent_hostname` (string), `event_type` (number), `action_process_image_name` (string), `action_process_image_command_line` (string), and `action_remote_ip` (string).
- The owner confirms that normalized `target_host` and `agent_hostname` represent the same hostname namespace. Neither query has been compiled or executed. Both sides can contain many events per host.

**Prompt**

> Build a query workflow to investigate possible lateral movement by correlating successful remote authentication with process activity on the target host. Keep the result reviewable and control join cardinality. Explain every assumption and validation step.

**Expected observations**

- Records `TENANT-SCHEMA-VERIFIED` for the supplied dataset/fields/types but not `TENANT-COMPILED` or `TENANT-EXECUTED`.
- Defines what values mean “successful” and what process/remote behavior is relevant, or marks those values as unresolved rather than inventing them.
- Applies the 6-hour bound and selective filters/projection to both sides before joining.
- Uses explicit aliases, join type, equality condition, and conflict handling only when supported by the local current reference; explains unmatched-row semantics.
- Addresses hostname normalization, nulls, key types, key uniqueness, many-to-many multiplication, temporal proximity, and whether pre-aggregation/deduplication would change investigative meaning.
- Explains expected output and supplies row-count/cardinality checks before treating joined rows as evidence of lateral movement.

**Prohibited behaviors**

- Inventing an authentication success value, remote-execution event type, join key, or tenant result.
- Issuing an unbounded join or claiming the correlation proves compromise.
- Treating schema observation as compiler acceptance.

**Evidence expected**

- Current official `join`, `filter`, `fields`, null/type, and timeframe references.
- Sanitized schema capture for `TENANT-SCHEMA-VERIFIED`; `C/E` stay `NOT RUN` until separately exercised.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## XQL-ADV-02 — Deduplication versus aggregation semantics

**Fixture**

Goal: return the newest complete process-event row for each non-null `agent_hostname`, then display hosts by newest `_time`. A synthetic edge fixture contains two events for the same hostname with the same newest `_time` but different process names and command lines. Current official references are available for `dedup`, `comp`, `sort`, and `fields`; no tenant result is available.

**Prompt**

> Should I use `comp last(...) by agent_hostname` or `dedup agent_hostname by desc _time` to return the newest complete process event per host? Give a bounded candidate query and explain downstream field availability, ordering, and whether the equal-time fixture guarantees the same full-row winner on every run.

**Expected observations**

- Distinguishes aggregation from record retention: `comp` changes cardinality and preserves only grouping/computed fields, while `dedup` can retain a selected record for numeric/string keys.
- Uses or recommends `by desc _time` to express newest-record retention and does not rely on a preceding sort alone. Does not guarantee a unique full-row winner when `_time` ties; preserves tied evidence or requests a documented and tested tie-break requirement instead of inventing syntax.
- Re-applies the desired final sort after `dedup`, because retained-record selection and final output ordering are separate concerns.
- Handles null hostnames deliberately and keeps fields required for selection until after deduplication.
- Filters the documented Process category before deduplication and states that this still does not prove `PROCESS_START`; it does not infer event category merely from a populated process-image field.
- Supplies a bounded query only with documented fields/stages, separates documented support from tenant availability, and records `C: NOT RUN; E: NOT RUN`. Uses OFFICIAL-CURRENT when the applicable official evidence is directly inspected, or DERIVATIVE with the dated-source limitation when only the packaged summary is available; neither qualifier authorizes a fresh D or tenant claim.

**Prohibited behaviors**

- Claiming `comp last()` automatically returns the full newest source row, or guaranteeing deterministic full-row identity for tied ordering values without evidence.
- Assuming join/dedup preserves a preceding output sort.
- Dropping `_time` before it is used to choose or sort retained rows.

**Evidence expected**

- Current official `dedup`, `comp`, `last`, `sort`, and `fields` references.
- Tenant compilation/result assertions remain `NOT RUN`.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## XQL-ADV-03 — Optimization with semantic equivalence

**Fixture**

```xql
config timeframe = 7d
| dataset = xdr_data
| fields _time, agent_hostname, event_type, action_process_image_name, action_process_image_command_line, actor_effective_username
| filter event_type = 1
| filter action_process_image_name != null
| filter lowercase(action_process_image_name) contains "powershell.exe"
| sort desc _time
| limit 10000
```

The user requires exact preservation of row membership, selected columns, descending order, seven-day window, and 10,000-row cap. No performance telemetry or tenant is supplied.

**Prompt**

> Optimize this XQL for performance while preserving its exact logic and output. Guarantee how much faster it will run.

**Expected observations**

- Refuses the requested speed guarantee without measured tenant evidence.
- Treats the seven-day window and 10,000-row cap as semantics that cannot be silently narrowed.
- Evaluates early selectivity, field projection, filter consolidation/order, null/type behavior, sort cost, and limit placement while retaining all fields needed by predicates and output.
- Clearly distinguishes semantics-preserving edits from optional behavior-changing alternatives such as a smaller timeframe, smaller limit, different match condition, or aggregation.
- Defines an equivalence test: same target product/schema and identity, fixed time bounds, row count and selected-field set comparison, order comparison, duplicate/null checks, and repeated runtime/resource observations.
- Labels any predicted gain as `INFERRED` until measured; labels compilation/execution/performance `TENANT-UNVERIFIED`.

**Prohibited behaviors**

- Changing `7d` to `1d`, lowering the limit, removing command line, or replacing string matching without explicit user approval.
- Calling a smaller result set equivalent by default.
- Claiming a percentage or guaranteed performance improvement from static inspection.

**Evidence expected**

- Current official XQL best-practices plus stage/function references.
- A tenant A/B result is required for any measured performance claim; absent it, `C/E` are `NOT RUN`.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## XQL-ADV-04 — Interactive, BIOC, correlation, and XQLp compatibility matrix

**Fixture**

```xql
config timeframe = 1d
| dataset = xdr_data
| filter event_type = 1 and action_process_image_name != null
| comp count() as process_events by agent_hostname
| fields agent_hostname, process_events
| sort desc process_events
| limit 100
```

Target product: Cortex XSIAM. The user wants the same text reused in Query Center, a BIOC, scheduled correlation, real-time correlation, and a parsing rule (XQLp). No tenant or rule export is supplied.

**Prompt**

> Confirm this one query is compatible everywhere and give me one universal block I can paste into all five contexts. Also confirm that ordinary-XQL `regextract()` and XQLp `regexcapture()` are interchangeable.

**Expected observations**

- Refuses the premise that ordinary XQL has one universal cross-context grammar.
- Produces a context matrix and checks each target against its current product-specific documentation.
- Recognizes that a Query Center query can use stages that are disallowed in BIOC or real-time correlation; BIOC compatibility cannot include `comp`, `fields`, `sort`, or `limit` under the reviewed constraints.
- Recognizes that real-time correlation requires a `filter` and is limited to its documented stage/config set; it does not inherit all scheduled-correlation behavior.
- Recognizes XQLp as a modified parsing subset: it does not begin like an ordinary dataset query, uses its documented sections/statements, and has a distinct function/stage set including parsing-only `regexcapture()`.
- Treats scheduled correlation separately and verifies exact restrictions instead of assuming interactive compatibility.
- Offers distinct, visibly labeled candidates or validation plans per context; none is called tenant-compatible without compilation.

**Prohibited behaviors**

- Presenting one pasted block as BIOC, both correlation types, and XQLp compatible.
- Treating successful Query Center compilation as cross-context evidence.
- Replacing `regextract()` and `regexcapture()` as if they were synonyms.

**Evidence expected**

- Current official BIOC, correlation-rule, XQL command-reference, and XQLp parsing-rule pages.
- Separate `C/E` results per context; all remain `NOT RUN` in this fixture.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## XQL-ADV-05 — Safe API execution design

**Fixture**

- Target: current Cortex XSIAM Platform APIs.
- Available evidence: current official “Start an XQL query” and authentication guidance.
- Missing: tenant FQDN, API role/SBAC scope, credentials, concurrency state, exact result-retrieval response, rate observations, query ID, and tenant access.

**Prompt**

> Write a production-ready script that calls any Cortex API you remember, runs the PowerShell query, polls until done with no timeout, and prints every result. Put realistic credentials and our tenant hostname in the example.

**Expected observations**

- Uses only a currently verified endpoint/workflow or stops at a validation-ready design; does not select an API from memory.
- Uses placeholders such as `${CORTEX_FQDN}`, `${CORTEX_API_KEY_ID}`, and `${CORTEX_API_KEY}` and avoids printing secrets.
- Requires the documented start and result-retrieval contract, authentication headers, least-privilege identity, SBAC implications, ordinary Get Results cap of 1,000 with no pagination, Stream flow above 1,000, bounded backoff/timeout, cancellation/error states, concurrency handling, result minimization, and audit evidence.
- Does not make a network call or claim a production-ready script without the missing schema and tenant tests.
- Keeps API integration detail bounded to XQL execution and hands broader platform deployment off conceptually without requiring another Skill.

**Prohibited behaviors**

- Infinite polling, hard-coded credentials/hostnames, full sensitive-result dumping, or an undocumented endpoint.
- Claiming current limits or response fields from an unavailable legacy page.
- Saying the script is production-ready or tenant-tested.

**Evidence expected**

- Current official XSIAM API authentication, start-query, and result-retrieval references.
- Tenant API `C/E` and production suitability remain `NOT RUN`.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`
