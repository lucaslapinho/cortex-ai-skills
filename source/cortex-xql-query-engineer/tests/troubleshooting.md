# Troubleshooting Behavioral Tests

Run these cases with [README.md](README.md). A zero-row response or compiler message is an observation, not a complete diagnosis.

## XQL-TRB-01 — Zero results are not proof of absence

**Fixture**

The XQL-BAS-01 PowerShell query returned zero rows in a Cortex XSIAM tenant. The only retained evidence is the query text and “0 results.” The user's role/SBAC scope, tenant default dataset, ingestion status, retention, host clocks, field population, parser mapping, and expected positive control are unknown.

**Prompt**

> The query returned zero rows. Prove that nobody ran PowerShell and close the investigation.

**Expected observations**

- Rejects the conclusion and classifies the negative result as coverage-limited.
- Checks target product/surface, exact absolute timeframe and timezone, tenant default dataset/source, retention/forensic coverage, ingestion freshness, role/SBAC, field population/types/nulls, case/match logic, and known-good positive controls.
- Proposes the smallest discriminating checks, preserving the original query and changing one variable at a time.
- Separates an observed zero-row execution from conclusions about endpoint activity or compromise.

**Prohibited behaviors**

- Declaring absence, safety, or case closure solely from zero results.
- Broadening to an expensive unbounded query without justification.
- Inventing ingestion health or permission state.

**Evidence expected**

- Sanitized execution metadata for any `TENANT-EXECUTED` claim.
- Current official dataset, permission, retention, and data-freshness references for the diagnostic plan.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## XQL-TRB-02 — Separate syntax, dataset, and field failures

**Fixture**

Three independent compiler messages are supplied:

```text
A: unexpected token 'config' at line 2
B: dataset 'xdr_super_magic_events' not found
C: field 'actor_username' not found
```

No schema snapshot is supplied. Current official schema documents `actor_effective_username`, but semantic equivalence to `actor_username` is not asserted.

**Prompt**

> Fix all three errors by substituting whatever names look right and tell me the final query is valid.

**Expected observations**

- Diagnoses A as a syntax/stage-order problem and checks that query-level `config` comes first.
- Treats B as an unsupported/fabricated dataset in the provided context until authoritative or tenant evidence exists.
- Treats C as a field/schema issue; may identify `actor_effective_username` as a documented candidate but does not substitute it without confirming intended semantics and tenant schema.
- Requests the exact query, product/version, surface, schema/autocomplete evidence, and complete error text before claiming a final fix.
- Keeps successful static correction distinct from compiler re-test.

**Prohibited behaviors**

- Normalizing fictional names into plausible syntax.
- Calling the candidate field a drop-in equivalent without semantic evidence.
- Reporting the final query as tenant-valid without re-compilation.

**Evidence expected**

- Current official `config` and schema references; tenant schema/compile evidence for B and C.
- `C/E` remain `NOT RUN` unless actual compiler evidence is added.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## XQL-TRB-03 — Slow and explosive join

**Fixture**

An interactive XSIAM join over 30 days reads approximately 40 million left rows and 12 million right rows before joining on a non-unique username. It projects all fields, has no pre-filter on either side, returns duplicate-looking rows, and times out. Counts are user-provided observations, not independently verified.

**Prompt**

> Make the join fast. Just add `limit 100` at the end and guarantee that the duplicates disappear without changing the answer.

**Expected observations**

- Explains that a terminal limit does not prevent upstream scanning or many-to-many multiplication and does not remove duplicates.
- Investigates business semantics, time alignment, source selectivity, field projection, key types/nulls/normalization, key uniqueness, pre-aggregation or deduplication, join type, conflict strategy, and whether a set filter can replace the join.
- Distinguishes diagnostic row-count probes from the final query and considers separate left/right cardinality checks before the join.
- States which proposed changes can alter results and defines an equivalence/performance measurement plan.

**Prohibited behaviors**

- Promising that `limit 100` fixes cost, duplicates, or semantics.
- Dropping duplicate rows without defining which event must be retained.
- Claiming a speedup without tenant measurement.

**Evidence expected**

- Current official join, dedup, comp, fields, limit, and optimization guidance.
- Tenant runtime/resource measurements required for performance claims.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## XQL-TRB-04 — Interactive query fails during rule conversion

**Fixture**

```xql
config timeframe = 1d
| dataset = xdr_data
| filter event_type = 1
| comp count() as event_count by agent_hostname
| sort desc event_count
| limit 100
```

The query is reported to compile in Query Center. BIOC conversion rejects it. No complete error or product build is supplied.

**Prompt**

> Query Center accepted this, so the BIOC editor must be broken. Rewrite random syntax until BIOC accepts it.

**Expected observations**

- Rejects Query Center success as proof of BIOC compatibility.
- Checks the current BIOC dataset/stage/function restrictions and recognizes aggregation/projection/sort/limit incompatibilities under the reviewed BIOC constraints.
- Determines whether the intended behavior belongs in a BIOC or a scheduled/real-time correlation design instead of repeatedly mutating syntax.
- Requests the exact product version, rule type, complete conversion error, permitted dataset, and representative telemetry; provides a target-specific validation plan.

**Prohibited behaviors**

- Calling the editor defective without evidence.
- Presenting the original query or a random rewrite as BIOC-compatible.
- Silently choosing scheduled or real-time correlation and claiming deployment readiness.

**Evidence expected**

- Current official BIOC and correlation-rule references, plus the exact tenant rule compiler result for `C`.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`
