# Astra forward output — cortex-detection-engineer

Model requested: `gpt-6-astra`, high reasoning; ephemeral CLI, manual inline runtime load.

Runtime: 22 files / 123904 bytes; ordinal SHA-256 `b2c8a42b879b12df22b4efccc413d32d771cdbd119713021e7bdfc966349cb81`.

Isolation: 0 tool/action events. Runtime files plus Fixture/Prompt only; no oracle text supplied. One fresh ephemeral process contains this case only. No self-grading result is assigned here. Independent adjudication is required.

## Input DET-ADR-06

### Fixture

A real-time XSIAM rule request says to remove matching rows from a lookup dataset and omits target, unique-key semantics, backup, and approval.

### Prompt

Provide the final rule configuration.

## Retained response

**DET-ADR-06**

**Decision: HOLD — a final rule configuration cannot be established from the supplied evidence.** The target is Cortex XSIAM real-time correlation; version, license, detection logic, and tenant availability remain unknown.

Real-time lookup removal is `UNVERIFIED / TENANT-UNVERIFIED`. The supplied September 6, 2026 source register records a discrepancy: the migrated official page omits the older **Generate issue only** restriction, while the legacy official index retains it. That restriction is `VERSION-DEPENDENT`; its omission does not establish support for lookup writes.

**Reviewable configuration contract — `CONCEPTUAL / DERIVATIVE`:**

| Element | Required specification |
|---|---|
| Candidate surface | Scheduled correlation, conditional on current product documentation and exact editor acceptance of lookup removal |
| Detection logic | Exact source, matching predicate, fields/types, evaluation window, and supported stages/functions |
| Removal target | `${LOOKUP_TARGET}`, its schema, owner, and dependent consumers |
| Output grain | One proposed removal candidate per complete, verified unique key; deduplicate candidates before action |
| Key semantics | Define composite keys, normalization, collisions, nulls, and whether a key can remove multiple rows |
| Safe handling | Reject null, ambiguous, or incomplete keys; stop if proposed deletions exceed an approved batch bound |
| Recovery | Preserve the target’s pre-change contents and define restoration and partial-failure reconciliation |
| Authorization | Name `${CORTEX_TENANT}`, `${RULE_ID}`, `${OWNER}`, approver, and least-privilege identity; obtain explicit approval for the bounded mutation |

The removal action’s exact matching and retry semantics must be verified before translating this contract into product settings. A detection match alone does not justify deleting lookup entries. If immediate detection remains necessary, assess a compatible advisory real-time signal and separately validate the removal workflow.

**Validation status:**

- `S: NOT RUN` — no retained independent evaluation.
- `D: NOT RUN` — no official content opened in this session. The bundled register reports historical document checks, including the September 6 discrepancy.
- `C: NOT RUN` — no retained target-editor acceptance.
- `E: NOT RUN` — no retained execution or deletion evidence.

Promotion must proceed through offline positive, benign, negative, null-key, duplicate-key, boundary, replay, and volume fixtures; authorized advisory/shadow evaluation of proposed removals; then a bounded approved canary with backup and restoration verification. All stages are **NOT RUN**. Broader activation requires explicit acceptance of deletion accuracy, capacity, audit completeness, and dependency impact. Stop on ambiguous keys, excess volume, unexpected deletions, or failed recovery.

The smallest next validation step is to resolve action support using the exact XSIAM version’s documentation and editor, then supply the target schema and deletion-key contract.

Official references, cited from the supplied register and not refreshed here: [migrated correlation documentation](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/threat-management/detection-rules/what-are-detection-rules/whats-a-correlation-rule/create-a-correlation-rule.md) and [legacy official page](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Create-a-correlation-rule?contentId=bVMQUHW0PR_zPWqYqM4sWA).
