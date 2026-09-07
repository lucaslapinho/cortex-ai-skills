# XQL Optimization Without Semantic Drift

Use this reference when asked to make an XQL query faster, cheaper, smaller, or more reliable. Optimization must preserve the user's analytical decision unless an intentional semantic change is stated and accepted.

**Documentation review cut:** 2026-09-04  
**Default performance status without tenant measurements:** `INFERRED / OFFICIAL-CURRENT / TENANT-UNVERIFIED`.

Official guidance supports narrow time ranges, early selective filtering, early field reduction, explicit limits, and deliberate management of joins and blocking stages. It does not prove a particular rewrite is faster in a named tenant.

## Contents

- Establish the equivalence contract first
- Optimization order
- Result-limit context
- Static review versus measured optimization
- Equivalence validation
- Measurement record
- Restricted-context optimization
- Optimization anti-patterns

## Establish the equivalence contract first

Record before editing:

- objective and the decision the result supports;
- product, version, execution surface, and identity scope;
- original query and observed symptom;
- required rows, columns, ordering, grouping, and duplicate semantics;
- null handling and type conversions;
- acceptable approximation, sampling, or truncation, if any;
- representative timeframe and data volume;
- target latency/resource goal and how it will be measured.

If these are unknown, provide candidate improvements with explicit assumptions rather than silently changing semantics.

## Optimization order

### 1. Bound time and source

- Use the smallest timeframe that still answers the question.
- Specify the intended dataset rather than relying on a tenant default when reproducibility matters.
- Do not widen the timeframe merely to overcome zero results until ingestion, retention, permissions, and schema are checked.
- Select cold or forensic data only when the objective requires it and the target tenant supports it.

### 2. Filter early and selectively

- Put high-selectivity, low-complexity predicates before joins, aggregation, deduplication, and sorting.
- Preserve boolean meaning with explicit parentheses.
- Filter null inputs before type-sensitive functions when that matches the objective.
- Do not add a filter solely to shrink results if it discards cases the original decision requires.

### 3. Project required fields

- After primary filters, retain only fields needed by later filters, joins, grouping, sorting, and final output.
- Do not remove a field before its last use.
- Remember that aliases replace original names downstream.
- Create derived fields with `alter`, not `fields`.

### 4. Control cardinality-changing stages

| Stage | Optimization questions | Semantic risks |
|---|---|---|
| `comp` | Can filters/projected inputs be reduced first? Are group keys necessary? Is the aggregate type correct? | Discards ungrouped/uncomputed fields; changes rows to groups; `count()` and `count(field)` differ on nulls. |
| `dedup` | Is uniqueness required? Can the input be reduced? Is retained earliest/latest row explicit? | Without `by`, retention is arbitrary; stage does not preserve earlier sort; can hide meaningful repeated activity. |
| `join` | Can a set filter or analyst pivot replace it? Are both sides filtered/projected? Are key types and multiplicity known? | One-to-many/many-to-many expansion, null-key loss, conflicts, and join-type changes can alter evidence. |
| `sort` | Is global order needed? Is the field numeric or a numeric-looking string? Can a bounded top/bottom result satisfy the objective? | Earlier ordering is lost across join/union/dedup; string sorting can misorder numbers. |
| `limit` | Is the limit for analyst review, API transport, or top/bottom semantics? Does it follow the intended sort? | Before sort it selects an arbitrary subset; any limit can hide relevant rows or groups. |

### 5. Place sort and limit deliberately

For “newest N” or “largest N,” sort before limit:

```xql
| sort desc _time
| limit 200
```

Status: `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED` when used with a documentation-grounded preceding schema; `D: PASS`, `C: NOT RUN`, `E: NOT RUN` absent tenant evidence.

Place final sort after `join`, `union`, or `dedup` when final order matters. Current documentation notes that a following limit can reduce the memory required for sort, but actual improvement remains tenant-measured.

## Result-limit context

At this review cut, the current general `limit` reference states:

- ordinary XQL without an explicit limit has a default maximum of 1,000,000 results;
- basic queries, and XDM queries in Cortex XSIAM, with no stage beyond `fields` default to 1,000 results;
- the 1,000 basic-query default does not apply to widgets, correlation rules, public APIs, saved queries, or scheduled queries, which retain the documented 1,000,000 limit when unspecified.

Classification: `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED`. Always set an explicit review-appropriate limit and recheck the target context instead of relying on a default.

Source: [limit stage](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/stages/limit.md) and [XQL query best practices](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/XQL-Query-best-practices).

## Static review versus measured optimization

Use distinct claims:

| Evidence | Permitted wording |
|---|---|
| Documentation plus static inspection | “This rewrite follows documented selectivity/projection guidance and is expected to reduce downstream input.” |
| Target compiler only | “The rewritten query compiled in the recorded tenant/surface.” |
| Controlled execution | “Under the recorded timeframe, identity, and tenant, the rewrite changed runtime/processed volume from A to B while passing the stated equivalence checks.” |
| One production observation | “The improvement was observed in this deployment/window”; do not universalize it. |

Do not say “optimized,” “faster,” or “lower cost” as a measured fact based only on fewer query lines, fewer output rows, or adherence to best practices.

## Equivalence validation

Compare the original and candidate on the same product, tenant, identity, timeframe, and stable data snapshot where possible.

Minimum checks:

1. Both compile in the same target surface.
2. Output columns, types, aliases, and ordering meet the contract.
3. Total row/group counts match, or a justified difference is recorded.
4. Key sets and duplicate multiplicity match where relevant. Include equal-time rows with different payloads: retaining a maximum timestamp is not a guarantee of the same full-row winner after deduplication, and discarding ties can change investigative meaning.
5. Null and empty-string handling match.
6. Aggregate values match, including row count versus non-null count.
7. Earliest/latest retention matches for `dedup` and `last()`.
8. Join unmatched rows and conflicts match the chosen join semantics.
9. Known positive and known benign fixtures remain represented as intended.
10. Results are not declared equivalent merely because the first visible page looks similar.

Without a live tenant, mark these checks `NOT RUN` and provide them as the validation plan.

## Measurement record

Preserve:

| Attribute | Required value |
|---|---|
| Product/tenant/surface | Exact context. |
| Query versions | Full original and candidate or stable hashes. |
| Identity and data scope | User/API key and RBAC/SBAC constraints. |
| Timeframe/data snapshot | Exact bounds and whether ingestion was still changing. |
| Runs | Warm-up policy, repeat count, retries, and failures. |
| Metrics | Runtime, scanned/processed volume or available query metrics, returned rows, and error state. |
| Equivalence | Checks performed and deviations. |
| Result | Observed improvement, regression, or inconclusive. |
| Limits | Caching, concurrency, retention, load, and tenant-specific conditions. |

## Restricted-context optimization

Do not “optimize” an interactive query for BIOC or real-time correlation by mechanically deleting unsupported stages. First separate:

- signal predicate;
- analyst-only display fields and ordering;
- aggregation or history requirement;
- target rule's supported source/stages/functions;
- state/schedule requirement;
- hit volume and false-positive controls.

If the semantics require aggregation or a join, a BIOC is not an equivalent target under the reviewed constraints. If real-time restrictions cannot express the behavior, select a scheduled design or retain an investigative query and label the handoff.

## Optimization anti-patterns

Reject or qualify:

- unbounded lookbacks “for completeness”;
- broad joins before filtering either side;
- `dedup` used only to make noisy data disappear;
- a limit placed before the sort for top/bottom questions;
- grouping by extra fields that explode cardinality;
- counting a nullable field when row count is intended;
- assuming source order survives a join or dedup;
- removing output/context fields needed to assess false positives;
- claiming zero results prove safe absence;
- claiming performance from documentation without tenant measurement;
- changing an interactive query into restricted rule syntax without separate compatibility review.

See [query-patterns.md](query-patterns.md) for concrete query shapes and [troubleshooting.md](troubleshooting.md) when the symptom may be ingestion, schema, permission, or coverage rather than query performance.
