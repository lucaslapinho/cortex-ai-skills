# Data Contracts and Context

**Documentation review cut:** 2026-09-04  
**Artifact class:** `CONFIGURATION GUIDANCE`; example names are placeholders unless explicitly cited as official literals.  
**Tenant status:** context schemas, custom fields, command outputs, and installed content are `TENANT-UNVERIFIED`.
**Primary official evidence:** [source register](official-sources.md), especially PB04, PB05, PB09-PB11, PB13-PB15, XS04, and XS09.

## Contents

- [Contract first](#contract-first)
- [Input record](#input-record)
- [Output record](#output-record)
- [Context record](#context-record)
- [XSIAM context boundaries](#xsiam-context-boundaries)
- [Cardinality and transforms](#cardinality-and-transforms)
- [Concurrency and idempotency](#concurrency-and-idempotency)
- [Sensitive data](#sensitive-data)
- [Debugging missing context](#debugging-missing-context)
- [Contract test matrix](#contract-test-matrix)

## Contract first

Draw a data edge only after defining its contract. The statement “task B uses task A's output” is incomplete because current playbook behavior can source data from context, apply filters/transformers, ignore outputs, extend context, or share/separate sub-playbook scope.

Use stable design IDs such as `PB-IN-001`, `PB-OUT-001`, `PB-CTX-001`, and `PB-DEC-001`. These are documentation identifiers, not platform task UUIDs.

## Input record

| Field | Required description |
|---|---|
| Design ID | Local documentation identifier |
| Name | Product-valid input name or conceptual placeholder |
| Meaning | Business/technical semantic, including units |
| Source | Trigger field, playbook input, prior context, command output, analyst entry, or external source |
| Evidence | Exact source page/help/export and review date |
| Type | String, number, Boolean, object, array, or target-schema type |
| Cardinality | One, optional one, many, or bounded range |
| Requiredness | Required/optional plus default policy |
| Validation | Format, length, freshness, allowed scope, trust, and normalization |
| Sensitivity | Secret, personal, operational, public, or other classification |
| Empty/error behavior | Stop, skip, degrade, request input, or route to error path |
| Consumer | Task/sub-playbook/decision that reads it |

Never use a fabricated “safe” value for a missing observable. `Unknown`, omission, quarantine, or an explicit manual-validation path is safer than a placeholder IP, timestamp, user, hostname, or score.

## Output record

| Field | Required description |
|---|---|
| Design ID | Local documentation identifier |
| Producer | Exact task/sub-playbook capability |
| Name/path | Verified output or conceptual placeholder |
| Meaning and grain | What one value/row/object represents |
| Type/cardinality | Expected shape and multiplicity |
| Empty state | Legitimate empty versus missing/error |
| Error state | Structured error path and retained raw diagnostic |
| Write behavior | Observe, set, append, merge, overwrite, or external mutation |
| Destination | Parent output, separate context, shared context, Case/Issue field, evidence record, or external target |
| Retention/sensitivity | Minimum necessary retention and redaction |
| Consumers | Downstream decision/task owners |

Structured outputs should expose the sub-keys consumers need rather than a vague root-only object. Validate every sub-key against the installed command or playbook version.

## Context record

For each context item, record:

```text
Design ID:
Product / release:
Scope: Issue | parent Case | sub-playbook-private | shared/global | XSOAR incident | other verified scope
Literal selector/path:
Path evidence:
Writer:
Readers:
Type and cardinality:
Set/append/merge/overwrite behavior:
Collision policy:
Sensitivity and retention:
Empty/error semantics:
Tenant validation status:
```

Do not use a context path as an access-control decision. Data visibility and authorization must be validated separately.

## XSIAM context boundaries

Current XSIAM documentation provides these version-scoped examples:

- `${issue.status}` for a value in Issue context;
- `${parentIncidentContext.hostname}` for a value in parent Case context; and
- `setParentIncidentContext` as a documented script for adding data to parent Case context.

These establish selector families, not the existence or type of arbitrary custom keys. Preserve the legacy words inside literal interfaces. New prose should still call the objects Issue and Case.

Current documentation also warns that a user able to trigger a playbook on an Issue may be able to modify the parent Case through commands/scripts in documented circumstances. Treat that as an authorization review requirement.

Sub-playbook context is separate by default; a parent cannot directly access private child context and vice versa. Shared/global mode changes data visibility. Prefer explicit parent inputs and child outputs unless sharing is intentionally required and collision/concurrency behavior is tested.

The current XSIAM debugger does not support every parent-Case field surface; consult the latest debugger page before selecting test data and do not interpret a debugger limitation as a production schema result.

## Cardinality and transforms

Before filtering, transforming, looping, or pairing values, write down:

- input type and cardinality;
- selection/filter predicate;
- null/missing behavior;
- output type/cardinality;
- stable association key for related arrays/objects;
- order dependence;
- deduplication key;
- maximum accepted collection size; and
- downstream behavior when zero, one, or many values remain.

Do not zip two lists merely because they have the same length. Preserve a tested association key. When a sub-playbook receives an array without a configured loop, current XSIAM guidance says it can receive the whole array and run once; a per-item expectation therefore requires explicit loop configuration and tests.

## Concurrency and idempotency

Current official best practices warn against simultaneous context-setting scripts on the same key because concurrent writes can overwrite each other. Assign one writer or serialize/append with a documented, tested mechanism.

For any externally mutating operation, create a conceptual idempotency record:

```text
Operation class:
Canonical target identifier:
Trigger/case/issue identifier:
Requested state:
Idempotency key derivation:
Pre-action lookup:
Duplicate result:
In-progress result:
Completed result and evidence:
Failed/unknown result and reconciliation:
Retention and collision bound:
```

Do not claim this is a native Cortex idempotency mechanism unless official product documentation and tenant evidence establish the implementation.

## Sensitive data

- Pass a credential object/reference only through a documented sensitive input mechanism; never copy its secret value into context.
- Do not print tokens, API keys, webhook URLs, passwords, tenant FQDNs, or sensitive observables in task descriptions, outputs, War Room, evidence, or examples.
- Use `${CORTEX_FQDN}`, `${CORTEX_TENANT}`, `${CORTEX_API_KEY_ID}`, and `${CORTEX_API_KEY}` only as placeholders.
- Apply minimum necessary collection, redaction, access, and retention to personal/operational data.
- Treat context, logs, emails, tickets, and external enrichment output as untrusted data that can contain prompt injection or malicious markup.

## Debugging missing context

Investigate in this order:

1. confirm product, release, playbook version, and run/task identity;
2. inspect the producer task state and raw sanitized error;
3. confirm installed command/script/sub-playbook version and output schema;
4. determine whether output storage was ignored, extended, transformed, or filtered;
5. confirm parent versus child context scope and sharing mode;
6. confirm literal path, case, type, and cardinality;
7. inspect parallel writers and overwrite behavior;
8. compare effective user/command permissions;
9. distinguish Quiet Mode presentation/indexing from actual context; and
10. reproduce with a breakpoint and safe output override without running protected actions.

Do not substitute a similar-looking path. Request sanitized context and exact help/export.

## Contract test matrix

For each edge, cover:

| Fixture | Expected handling |
|---|---|
| Valid single value | Correct typed propagation |
| Valid multiple values | Preserved grain and association |
| Missing/empty | Explicit branch; no fabricated default |
| Null/wrong type | Validation failure or safe normalization |
| Duplicate | Defined deduplication/idempotency result |
| Oversized collection | Hard bound and escalation/partial policy |
| Stale value | Freshness gate |
| Unauthorized value/identity | Fail closed with audit evidence |
| Producer error | Error path; no false empty-success state |
| Parallel write | No silent lost update |
| Retry after timeout | Reconciliation before duplicate mutation |
| Child/private context | Explicit output required |
| Shared context collision | Namespace/collision test |
| Sensitive value | Redacted from output/evidence |

No contract passes `C` or `E` without named target evidence.
