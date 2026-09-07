# Context Contract Template

**Artifact classification:** `CONFIGURATION GUIDANCE`  
**Default status of literal paths without tenant evidence:** `UNVERIFIED / TENANT-UNVERIFIED`

## Contract identity

- Contract ID/version/owner: `{{VALUES}}`
- Product/deployment/release: `{{VALUES}}`
- Parent playbook and version: `{{VALUE}}`
- Child/task/command and version: `{{VALUE}}`
- Context scope: `{{ISSUE / PARENT CASE / CHILD-PRIVATE / SHARED / XSOAR INCIDENT / OTHER VERIFIED}}`

## Inputs

| ID | Name/meaning | Source literal/path | Type/cardinality | Required | Validation/freshness | Sensitivity | Empty/error behavior |
|---|---|---|---|---|---|---|---|
| `{{PB-IN-001}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |

## Outputs

| ID | Name/meaning | Literal path | Type/cardinality | Set/append/merge/overwrite | Consumer | Empty/error behavior | Evidence |
|---|---|---|---|---|---|---|---|
| `{{PB-OUT-001}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |

## Scope and propagation

Before completing this contract, add the following record for **every input and output ID**. Do not infer an output's lifetime from the input or apply one default silently to the whole contract.

```text
Input/output ID:
Producer and consumer:
Requiredness:
Default or explicit no-default/absence policy:
Empty, missing, and producer-error behavior:
Literal namespace/path and applicable evidence:
Mapping and write behavior:
Sensitivity and redaction:
Lifetime within the run:
Retention after the run and deletion owner:
Unresolved dimension and validation owner:
```

Type/cardinality and semantic meaning are required in the corresponding I/O table above. A contract is incomplete if any dimension is omitted; unknown values must remain explicit.

- Default/selected context separation: `{{DETAIL}}`
- Parent-to-child mapping: `{{DETAIL}}`
- Child-to-parent explicit outputs: `{{DETAIL}}`
- Shared/global context justification: `{{DETAIL}}`
- Collision namespace and owner: `{{DETAIL}}`
- Product/version source for every literal selector: `{{SOURCE}}`
- Separate authorization controls: `{{RBAC/SBAC/COMMAND PERMISSIONS}}`

## Transform and cardinality

- Input grain and maximum size: `{{DETAIL}}`
- Filters/transformers and null/type behavior: `{{DETAIL}}`
- Multiple-list association key: `{{DETAIL}}`
- Loop or whole-array behavior: `{{DETAIL}}`
- Deduplication/order behavior: `{{DETAIL}}`
- Oversized/partial result policy: `{{DETAIL}}`

## Concurrency and write ownership

- Single writer for each key: `{{OWNER}}`
- Parallel readers/writers: `{{DETAIL}}`
- Append/merge semantics evidence: `{{SOURCE OR CONCEPTUAL}}`
- Lost-update test: `{{FIXTURE}}`
- Duplicate/replay handling: `{{DETAIL}}`

## Secret and retention controls

- Secret-bearing fields prohibited from context: `{{LIST}}`
- Credential reference mechanism: `{{PRODUCT-VERIFIED REFERENCE}}`
- Personal/operational data minimization: `{{DETAIL}}`
- Redaction for War Room/evidence/notification: `{{DETAIL}}`
- Access and retention: `{{DETAIL}}`

## Tests

| Fixture | Expected output/path | Expected branch | Evidence retained | Status |
|---|---|---|---|---|
| Valid single | `{{...}}` | `{{...}}` | `{{...}}` | `{{NOT RUN}}` |
| Multiple | `{{...}}` | `{{...}}` | `{{...}}` | `{{NOT RUN}}` |
| Empty/null | `{{...}}` | `{{...}}` | `{{...}}` | `{{NOT RUN}}` |
| Wrong type | `{{...}}` | `{{...}}` | `{{...}}` | `{{NOT RUN}}` |
| Duplicate | `{{...}}` | `{{...}}` | `{{...}}` | `{{NOT RUN}}` |
| Oversized | `{{...}}` | `{{...}}` | `{{...}}` | `{{NOT RUN}}` |
| Producer error | `{{...}}` | `{{...}}` | `{{...}}` | `{{NOT RUN}}` |
| Unauthorized | `{{...}}` | `{{...}}` | `{{...}}` | `{{NOT RUN}}` |
| Parallel write | `{{...}}` | `{{...}}` | `{{...}}` | `{{NOT RUN}}` |
| Sensitive value | `{{REDACTED}}` | `{{...}}` | `{{...}}` | `{{NOT RUN}}` |

## Decision

- Workflow state: `{{DRAFT / UNDER REVIEW / APPROVED / RETIRED}}`
- Evidence status: `{{VERIFIED / VERSION-DEPENDENT / INFERRED / CONCEPTUAL / UNSUPPORTED / DEPRECATED / UNVERIFIED}}`
- Validation qualifier: `{{REFERENCED-ONLY / TENANT-UNVERIFIED / TENANT-SCHEMA-VERIFIED / TENANT-COMPILED / TENANT-EXECUTED}}`
- S result: `{{PASS/FAIL/NOT RUN/N/A - RATIONALE}}`
- D result: `{{PASS/FAIL/NOT RUN/N/A - RATIONALE}}`
- C result: `{{PASS/FAIL/NOT RUN/N/A - RATIONALE}}`
- E result: `{{PASS/FAIL/NOT RUN/N/A - RATIONALE}}`
- Unresolved paths/types: `{{LIST}}`
- Next validation: `{{STEP}}`

Context scope is not an authorization boundary. Do not approve the contract without separate permission tests.
