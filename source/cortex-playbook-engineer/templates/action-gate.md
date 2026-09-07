# Protected Action Gate Template

**Artifact classification:** `CONCEPTUAL` until the exact product command, policy, permissions, controlled test, and target readback are verified.  
**Authorization:** completing this document does not authorize an action.

## 1. Action identity

- Gate ID/version/owner: `{{VALUES}}`
- Product/deployment/release: `{{VALUES}}`
- Action class: `{{ISOLATE / DISABLE / BLOCK / TERMINATE / DELETE / NETWORK CHANGE / REVOKE / REMEDIATE / MUTATE OBJECT / NOTIFY / OTHER}}`
- Exact command/capability: `{{TENANT-VERIFIED VALUE OR UNKNOWN}}`
- Read/write impact: `{{LOW IMPACT / MODIFIES SYSTEM / DESTRUCTIVE}}`
- Target type and hard maximum count: `{{VALUES}}`

## 2. Authority and policy

- Requesting authority/change reference: `{{REFERENCE}}`
- Organizational policy and allowed environment: `{{REFERENCE}}`
- Accountable business/service owner: `{{OWNER}}`
- Required approver and separation of duties: `{{ROLE}}`
- Effective Cortex and external-system identity: `{{ROLE/ACCOUNT ALIAS}}`
- Object/data/integration-command permissions tested: `{{EVIDENCE}}`

## 3. Evidence and confidence

| Evidence ID | Observation | Source/time | Integrity/coverage | Confidence contribution | Alternative explanation |
|---|---|---|---|---|---|
| `{{E-001}}` | `{{FACT}}` | `{{SOURCE}}` | `{{LIMIT}}` | `{{VALUE}}` | `{{ALTERNATIVE}}` |

- Confidence definition and threshold: `{{RULE}}`
- Independent corroboration: `{{EVIDENCE}}`
- Unknown/conflicting data: `{{DETAIL}}`
- Freshness deadline before action: `{{BOUND}}`

No single AI/reputation score is authorization. Unknown is not benign.

## 4. Target and blast radius

- Canonical target identifiers (sanitized aliases in this document): `{{LIST}}`
- Current state/readback source and time: `{{EVIDENCE}}`
- Scope and exclusions: `{{DETAIL}}`
- Criticality/dependencies/users: `{{DETAIL}}`
- Expected operational effect: `{{DETAIL}}`
- Worst credible unintended effect: `{{DETAIL}}`
- Batch/canary order and stop condition: `{{DETAIL}}`

## 5. Idempotency, timeout, and partial failure

- Idempotency key/duplicate result: `{{CONCEPTUAL OR VERIFIED IMPLEMENTATION}}`
- Attempt limit, interval/backoff, total deadline: `{{BOUNDS}}`
- Per-attempt timeout: `{{BOUND}}`
- Timeout reconciliation before retry: `{{READBACK}}`
- Already-in-state behavior: `{{DETAIL}}`
- Per-target result ledger: `{{LOCATION}}`
- Partial-batch policy: `{{STOP/CONTINUE/RECOVER/ESCALATE}}`

## 6. Approval decision

Evidence presented to approver:

- target/scope and current state;
- observations, confidence, alternatives, and gaps;
- exact proposed action and expected effect;
- blast radius, exclusions, timeout/retry, and partial-failure plan;
- recovery/rollback and verification;
- notification and evidence retention.

Decision fields:

- Approver identity and authentication evidence: `{{VALUE}}`
- Decision: `{{APPROVE / REJECT / REQUEST MORE EVIDENCE / EXPIRE}}`
- Approved target/scope/action: `{{VALUE}}`
- Decision time/expiry: `{{VALUE}}`
- Conditions: `{{VALUE}}`
- Late/duplicate/conflicting decision behavior: `{{VALUE}}`
- Audit reference: `{{VALUE}}`

No-response defaults to reject/escalate, never approval.

## 7. Execution plan

This section remains non-executable until separately authorized.

- Pre-action validation/readback: `{{STEP}}`
- Least-scope action: `{{CAPABILITY}}`
- Canary/batch order: `{{STEP}}`
- Post-action independent readback: `{{STEP}}`
- Continued-threat/side-effect check: `{{STEP}}`
- Stop/escalation criteria: `{{STEP}}`

Do not insert guessed commands, arguments, task IDs, or API calls.

## 8. Recovery and rollback

- Reversibility classification: `{{REVERSIBLE / RECOVERABLE / IRREVERSIBLE / UNKNOWN}}`
- Recovery/rollback capability and validation evidence: `{{DETAIL}}`
- Recovery owner/on-call: `{{OWNER}}`
- Maximum recovery window: `{{BOUND}}`
- Dependencies and data backup/snapshot: `{{DETAIL}}`
- Rollback trigger and verification: `{{DETAIL}}`
- If recovery fails: `{{ESCALATION}}`

## 9. Notification and evidence

- Recipients/purpose/minimum content: `{{DETAIL}}`
- Sensitive-data redaction: `{{DETAIL}}`
- Delivery/duplicate/failure behavior: `{{DETAIL}}`
- Evidence fields: request, decision, identity, target aliases, timestamps, command version, returned status, readback, partial state, recovery, residual risk.
- Evidence location/hash/access/retention: `{{DETAIL}}`

## 10. Validation status

| Level | Result | Evidence | Claim boundary |
|---|---|---|---|
| `S` | `{{PASS/FAIL/NOT RUN/N/A - RATIONALE}}` | `{{REFERENCE}}` | `{{BOUNDARY}}` |
| `D` | `{{PASS/FAIL/NOT RUN/N/A - RATIONALE}}` | `{{REFERENCE}}` | `{{BOUNDARY}}` |
| `C` | `{{PASS/FAIL/NOT RUN/N/A - RATIONALE}}` | `{{REFERENCE}}` | `{{BOUNDARY}}` |
| `E` | `{{PASS/FAIL/NOT RUN/N/A - RATIONALE}}` | `{{REFERENCE}}` | `{{BOUNDARY}}` |

**Gate outcome:** `{{BLOCK / ELIGIBLE FOR CONTROLLED TEST / APPROVED UNDER SEPARATE AUTHORIZATION}}`  
**Residual risk and owner:** `{{DETAIL}}`
