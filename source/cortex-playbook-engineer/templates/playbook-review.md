# Playbook Review Template

**Artifact classification:** `CONFIGURATION GUIDANCE`  
**Reviewed artifact class claimed by supplier:** `{{CLASS OR NOT STATED}}`  
**Review rule:** a claim of `VERIFIED IMPORTABLE ARTIFACT` fails unless exact target, schema, dependencies, controlled import, and functional evidence are present.

## Review identity

- Review ID/date/reviewer: `{{VALUES}}`
- Product/deployment/release: `{{VALUES OR UNKNOWN}}`
- Artifact name/version/hash: `{{VALUES}}`
- Source/provenance: `{{EXPORT / REPOSITORY REVISION / ATTACHMENT / SCREENSHOT / DERIVATIVE SUMMARY}}`
- Available evidence: `{{LIST}}`
- Unavailable evidence: `{{LIST}}`

## Claim and evidence assessment

| Supplier claim | Canonical status | Qualifiers | Supporting evidence | Conflict/gap | Decision |
|---|---|---|---|---|---|
| `{{CLAIM}}` | `{{STATUS}}` | `{{QUALIFIERS}}` | `{{SOURCE}}` | `{{GAP}}` | `{{ACCEPT/DOWNGRADE/REJECT}}` |

## Product-boundary check

- Current Case/Issue versus literal legacy identifier handling: `{{RESULT}}`
- XSIAM/XSOAR version applicability: `{{RESULT}}`
- Trigger/job/manual/sub-playbook surface: `{{RESULT}}`
- Content source/update relationship: `{{RESULT}}`
- Unsupported cross-product assumptions: `{{RESULT}}`

## Graph and lifecycle check

Check `Trigger -> Validation -> Enrichment -> Decision -> Investigation -> Approval -> Containment -> Remediation -> Verification -> Notification -> Evidence -> Closure`.

| Stage | Present | Contract complete | Safe error/empty/partial path | Finding ID |
|---|---|---|---|---|
| Trigger | `{{Y/N}}` | `{{Y/N}}` | `{{Y/N}}` | `{{ID}}` |
| Validation | `{{Y/N}}` | `{{Y/N}}` | `{{Y/N}}` | `{{ID}}` |
| Enrichment | `{{Y/N}}` | `{{Y/N}}` | `{{Y/N}}` | `{{ID}}` |
| Decision | `{{Y/N}}` | `{{Y/N}}` | `{{Y/N}}` | `{{ID}}` |
| Investigation | `{{Y/N}}` | `{{Y/N}}` | `{{Y/N}}` | `{{ID}}` |
| Approval | `{{Y/N/N-A}}` | `{{Y/N}}` | `{{Y/N}}` | `{{ID}}` |
| Containment | `{{Y/N/N-A}}` | `{{Y/N}}` | `{{Y/N}}` | `{{ID}}` |
| Remediation | `{{Y/N/N-A}}` | `{{Y/N}}` | `{{Y/N}}` | `{{ID}}` |
| Verification | `{{Y/N}}` | `{{Y/N}}` | `{{Y/N}}` | `{{ID}}` |
| Notification | `{{Y/N/N-A}}` | `{{Y/N}}` | `{{Y/N}}` | `{{ID}}` |
| Evidence | `{{Y/N}}` | `{{Y/N}}` | `{{Y/N}}` | `{{ID}}` |
| Closure | `{{Y/N}}` | `{{Y/N}}` | `{{Y/N}}` | `{{ID}}` |

## Contract, content, and permission check

- Inputs/outputs typed, bounded, documented, and tested: `{{RESULT}}`
- Context paths/product scopes verified: `{{RESULT}}`
- Private/shared context used intentionally: `{{RESULT}}`
- Parallel writes/collisions controlled: `{{RESULT}}`
- Packs/sub-playbooks/scripts/integrations pinned: `{{RESULT}}`
- Commands/arguments/output schema verified: `{{RESULT}}`
- Object/data/command/credential permissions tested: `{{RESULT}}`
- Secrets and customer data absent: `{{RESULT}}`

## Reliability and safety check

- Conditions cover false/unknown/error/conflict: `{{RESULT}}`
- Loops have item grain, exit, maximum, interval, and total deadline: `{{RESULT}}`
- Retries are transient, bounded, and idempotent/reconciled: `{{RESULT}}`
- Timeouts do not trigger duplicate writes: `{{RESULT}}`
- Error paths preserve diagnostics and cannot bypass gates: `{{RESULT}}`
- Protected actions have exact target/scope/approval/recovery/readback: `{{RESULT}}`
- Partial batch state is tracked per target: `{{RESULT}}`
- Notifications are authenticated/redacted/deduplicated as needed: `{{RESULT}}`
- Evidence and Quiet Mode tradeoffs are explicit: `{{RESULT}}`

## Findings

Use `BLOCKER`, `CRITICAL`, `HIGH`, `MEDIUM`, or `LOW`.

| ID | Severity | Exact location | Observation/evidence | Impact | Required remediation | Owner | Disposition |
|---|---|---|---|---|---|---|---|
| `{{PB-REV-001}}` | `{{SEVERITY}}` | `{{LOCATION}}` | `{{FACT}}` | `{{IMPACT}}` | `{{CHANGE}}` | `{{OWNER}}` | `{{OPEN/FIXED/ACCEPTED}}` |

Do not invent an exact location for an unavailable source. A derivative report can support a provenance finding, not a confirmed line-level defect.

## Test results

| Level | Scope | Result | Evidence | Limitation |
|---|---|---|---|---|
| `S` | `{{SCOPE}}` | `{{PASS/FAIL/NOT RUN/N/A - RATIONALE}}` | `{{REFERENCE}}` | `{{LIMIT}}` |
| `D` | `{{SCOPE}}` | `{{PASS/FAIL/NOT RUN/N/A - RATIONALE}}` | `{{REFERENCE}}` | `{{LIMIT}}` |
| `C` | `{{SCOPE}}` | `{{PASS/FAIL/NOT RUN/N/A - RATIONALE}}` | `{{REFERENCE}}` | `{{LIMIT}}` |
| `E` | `{{SCOPE}}` | `{{PASS/FAIL/NOT RUN/N/A - RATIONALE}}` | `{{REFERENCE}}` | `{{LIMIT}}` |

## Decision

- Unresolved counts: `BLOCKER {{N}} / CRITICAL {{N}} / HIGH {{N}} / MEDIUM {{N}} / LOW {{N}}`
- Artifact classification supported after review: `{{CLASS}}`
- Import/deploy decision: `{{REJECT / CONDITIONAL / ELIGIBLE FOR CONTROLLED TEST}}`
- Required next validation: `{{STEP}}`
- Residual risk and owner: `{{DETAIL}}`

The review does not authorize import, deployment, or action.
