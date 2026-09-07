# Playbook Design Template

**Artifact classification:** `{{CONCEPTUAL | CONFIGURATION GUIDANCE | VERIFIED IMPORTABLE ARTIFACT}}`  
**Default when target evidence is incomplete:** `CONCEPTUAL`  
**Format:** design record only; never convert this template into YAML/JSON by guessing fields.

Use `VERIFIED IMPORTABLE ARTIFACT` only when the exact schema, dependencies, controlled import, functional test, and independent review evidence are attached.

## 1. Name and purpose

- **Design ID:** `{{PB-DESIGN-ID}}`
- **Name:** `{{NAME}}`
- **Business/security purpose:** `{{PURPOSE}}`
- **Owner:** `{{OWNER}}`
- **Non-goals:** `{{OUT-OF-SCOPE}}`

## 2. Product and execution surface

- **Product:** `{{CORTEX XSIAM | CORTEX XSOAR}}`
- **Deployment/release/build:** `{{VALUE OR UNKNOWN}}`
- **Primary object:** `{{ISSUE / CASE / INCIDENT / JOB / MANUAL / SUB-PLAYBOOK / OTHER VERIFIED OBJECT}}`
- **Execution mode:** `{{TRIGGERED / MANUAL / SUB-PLAYBOOK / JOB}}`
- **Content relationship:** `{{CUSTOM / SYSTEM / ATTACHED / DETACHED / DUPLICATED / UNKNOWN}}`
- **Tenant/license state:** `{{EVIDENCE OR TENANT-UNVERIFIED}}`

## 3. Evidence status

| Claim | Canonical status | Qualifiers | Source/date | Tenant gap |
|---|---|---|---|---|
| `{{CLAIM}}` | `{{STATUS}}` | `{{QUALIFIERS}}` | `{{SOURCE}}` | `{{GAP}}` |

List conflicts, legacy literals, and staleness risk. Do not call local/project material official.

## 4. Trigger and prerequisites

- **Trigger object and condition:** `{{DESCRIPTION}}`
- **Rule/job/manual source:** `{{EXACT VERIFIED SURFACE OR UNKNOWN}}`
- **Enablement/order/replay behavior:** `{{DETAIL}}`
- **Deduplication/idempotency key:** `{{CONCEPTUAL DESIGN}}`
- **Expected volume/concurrency:** `{{BOUND}}`
- **Required packs, sub-playbooks, scripts, integrations, instances:** `{{VERSIONED INVENTORY}}`
- **Execution identity and permissions:** `{{EVIDENCE}}`
- **Credentials/engines/network:** `{{REFERENCES ONLY; NO SECRET VALUES}}`

## 5. Inputs, outputs, and context

### Inputs

| ID | Name/meaning | Source | Type/cardinality | Required/validation | Sensitivity | Empty/error path |
|---|---|---|---|---|---|---|
| `{{PB-IN-001}}` | `{{VALUE}}` | `{{SOURCE}}` | `{{TYPE/GRAIN}}` | `{{RULE}}` | `{{CLASS}}` | `{{PATH}}` |

### Outputs

| ID | Name/meaning | Type/cardinality | Destination/consumer | Write behavior | Empty/error semantics | Evidence |
|---|---|---|---|---|---|---|
| `{{PB-OUT-001}}` | `{{VALUE}}` | `{{TYPE/GRAIN}}` | `{{TARGET}}` | `{{OBSERVE/SET/APPEND/MERGE/OVERWRITE}}` | `{{STATE}}` | `{{SOURCE}}` |

### Context

| ID | Product scope | Literal path or placeholder | Writer/readers | Scope/sharing | Collision/concurrency | Status |
|---|---|---|---|---|---|---|
| `{{PB-CTX-001}}` | `{{PRODUCT/RELEASE}}` | `{{PATH OR UNVERIFIED PLACEHOLDER}}` | `{{OWNERS}}` | `{{ISSUE/CASE/CHILD/SHARED/INCIDENT}}` | `{{CONTROL}}` | `{{STATUS}}` |

For each input and output ID, also complete this per-value record; a shared retention paragraph does not establish every value's contract:

```text
Input/output ID:
Producer and consumer:
Requiredness and default/no-default policy:
Missing, empty, and error behavior:
Namespace/path evidence and mapping/write behavior:
Sensitivity and redaction:
Run lifetime and post-run retention:
Retention/deletion owner:
Unresolved dimensions and validation owner:
```

Keep the type, cardinality, meaning, and validation rule in the I/O tables above. Use [context-contract.md](context-contract.md) for each parent/child boundary.

## 6. Integrations, commands, and permissions

| Task capability | Exact content item | Pack/version | Instance/engine | Inputs/outputs verified | Effective command role | Read/write class | Status |
|---|---|---|---|---|---|---|---|
| `{{CAPABILITY}}` | `{{NAME OR UNKNOWN}}` | `{{VERSION}}` | `{{TARGET}}` | `{{EVIDENCE}}` | `{{ROLE TEST}}` | `{{CLASS}}` | `{{STATUS}}` |

If any exact command or schema is unknown, keep the design capability-level and list the target help/export needed.

## 7. Stage-by-stage flow

| Step | Stage | Input and validation | Decision/action | Output | Success | Empty/error/partial path | Evidence |
|---|---|---|---|---|---|---|---|
| 1 | Trigger | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |
| 2 | Validation | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |
| 3 | Enrichment | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |
| 4 | Decision | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |
| 5 | Investigation | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |
| 6 | Approval | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |
| 7 | Containment | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |
| 8 | Remediation | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |
| 9 | Verification | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |
| 10 | Notification | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |
| 11 | Evidence | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |
| 12 | Closure | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |

Explain any omitted stage.

## 8. Conditions, loops, and concurrency

- **Decision table:** `{{TRUE/FALSE/UNKNOWN/ERROR/CONFLICTING STATES}}`
- **Loop item grain/source:** `{{VALUE}}`
- **Maximum iterations/items and total deadline:** `{{BOUNDS}}`
- **Exit/timeout/empty behavior:** `{{DETAIL}}`
- **Parallel branches and join rule:** `{{DETAIL}}`
- **Shared-key writer ownership:** `{{DETAIL}}`
- **Rate/volume bound:** `{{DETAIL}}`

## 9. Approval and action gate

- **Protected action:** `{{ACTION CLASS}}`
- **Evidence/confidence threshold:** `{{RULE}}`
- **Approver and separation of duties:** `{{ROLE}}`
- **Choices/no-response/expiry:** `{{DETAIL}}`
- **Target/scope/exclusions:** `{{HARD BOUNDS}}`
- **Least-privilege identity:** `{{ROLE EVIDENCE}}`
- **Blast radius/dependencies:** `{{ASSESSMENT}}`
- **Recovery/rollback owner:** `{{DETAIL}}`
- **Post-action readback:** `{{DETAIL}}`

Use [action-gate.md](action-gate.md) for full review.

## 10. Reliability

| Task/path | Timeout | Retryable failures | Attempt/interval/total bound | Idempotency/reconciliation | Terminal error/fallback |
|---|---|---|---|---|---|
| `{{TASK}}` | `{{BOUND}}` | `{{CLASSES}}` | `{{BOUNDS}}` | `{{CONTROL}}` | `{{PATH}}` |

Describe cancellation, partial-batch behavior, restart, and already-in-state handling.

## 11. Notification, evidence, War Room, and SLA

- **Recipients/purpose/authentication:** `{{DETAIL}}`
- **Minimum content/redaction:** `{{DETAIL}}`
- **Delivery failure and duplicate handling:** `{{DETAIL}}`
- **SLA/reminders/escalation:** `{{DETAIL}}`
- **War Room/task/timeline/evidence behavior:** `{{PRODUCT-VERIFIED DESIGN}}`
- **Quiet Mode decision and tradeoff:** `{{DETAIL}}`
- **Audit fields and retention:** `{{DETAIL}}`

## 12. Security and privacy

- Secret references and prohibited outputs: `{{DETAIL}}`
- Prompt-injection/untrusted-content boundary: `{{DETAIL}}`
- Data minimization, access, and retention: `{{DETAIL}}`
- Negative-permission tests: `{{DETAIL}}`

## 13. Test and deployment plan

| Level | Planned check | Environment/identity | Protected-task control | Expected evidence | Status |
|---|---|---|---|---|---|
| `S` | `{{CHECK}}` | `{{ENV}}` | `{{CONTROL}}` | `{{EVIDENCE}}` | `{{PASS/FAIL/NOT RUN/N/A - RATIONALE}}` |
| `D` | `{{CHECK}}` | `{{ENV}}` | `N/A` | `{{EVIDENCE}}` | `{{PASS/FAIL/NOT RUN/N/A - RATIONALE}}` |
| `C` | `{{CHECK}}` | `{{TARGET}}` | `{{CONTROL}}` | `{{EVIDENCE}}` | `{{PASS/FAIL/NOT RUN/N/A - RATIONALE}}` |
| `E` | `{{CHECK}}` | `{{TARGET}}` | `{{CONTROL}}` | `{{EVIDENCE}}` | `{{PASS/FAIL/NOT RUN/N/A - RATIONALE}}` |

## 14. Expected result and closure

- **Expected result:** `{{CONTRACT, NOT FABRICATED OBSERVATION}}`
- **Analytical closure:** `{{CRITERIA}}`
- **Operational closure:** `{{CRITERIA}}`
- **Residual risks/owner:** `{{DETAIL}}`
- **Unsupported/unknown close fields:** `{{DETAIL}}`

## 15. Limitations, handoff, and references

- Tenant/version gaps: `{{LIST}}`
- Adjacent owner handoffs: `{{LIST}}`
- Official references: `{{EXACT URLS}}`
- Next smallest validation step: `{{STEP}}`

## Classification decision

**Final artifact classification:** `{{CLASS}}`  
**Why this level is justified:** `{{EVIDENCE}}`  
**Missing evidence before promotion:** `{{GAPS}}`
