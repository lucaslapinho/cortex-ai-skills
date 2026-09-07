# Refactoring a Monolithic Playbook

**Artifact classification:** `CONCEPTUAL`  
**Applicable product/surface:** target must be selected as XSIAM or a named XSOAR release before configuration  
**Evidence status:** reusable sub-playbook and explicit I/O concepts are officially documented; proposed boundaries/names are conceptual  
**Execution status:** no source export, import, validator, or runtime evidence

## Objective

Refactor a fictional 45-task phishing-response playbook that mixes trigger handling, extraction, enrichment, decisions, ticketing, user communication, containment, and closure. The source graph and commands are unavailable, so this example cannot claim exact line/task findings.

## Problems to test in the source

- one change owner controls unrelated branches;
- inputs and outputs are implicit context rather than contracts;
- parallel enrichment writes the same root key;
- arrays are correlated by position;
- optional enrichment error falls into a benign branch;
- ticket creation repeats on replay;
- containment follows a score without human/policy gate;
- notification and closure occur before action readback;
- detached content/version drift is unknown;
- secret-bearing integration values may appear in task output.

These are review hypotheses, not observed defects.

## Proposed responsibilities

```text
Parent: PhishingResponseController
  -> ValidateAndNormalizeInput
  -> ExtractAndClassifyObservables
  -> EnrichObservables
  -> AssessPhishingEvidence
  -> CoordinateApprovalAndResponse
  -> VerifyNotifyAndClose
```

Names are documentation labels, not installed playbook names or task IDs.

| Component | Responsibility | Inputs | Outputs | Protected effects |
|---|---|---|---|---|
| Parent controller | Trigger, policy, orchestration, final state | Source object, policy, scope | End-to-end result | None directly |
| Validate/normalize | Type, scope, freshness, hostile content, dedup | Raw bounded input | Validated typed object or rejection | None |
| Extract/classify | Produce source-linked observable records | Validated object | Bounded observables with provenance | None |
| Enrich | Call tenant-verified read capabilities and normalize | Typed observables | Per-source results/errors | External reads only |
| Assess | Deterministic decision and alternatives | Evidence records | Decision state/confidence/gaps | None |
| Approval/response | Approval, least-scope authorized actions, idempotency | Candidate action, policy, target | Per-target action/readback | Yes; gated |
| Verify/notify/close | Verify, notify, evidence, closure/escalation | All prior structured outputs | Final record | Notification/object update; gated |

## Context strategy

- Default to separate child context and explicit outputs.
- Use a versioned namespace only where shared data is necessary.
- Assign one writer per shared key.
- Preserve observable association by object/key, not parallel list index.
- Keep raw sensitive content and credential values out of context.
- Separate operational action ledger from analytical evidence.

Exact paths remain unknown and must be discovered from the selected product/export.

## Reliability strategy

- Read-only enrichments may fan out but return one per-source outcome object.
- Required-source failure blocks the response decision; optional-source failure sets a degraded flag.
- Retries apply only to classified transient/idempotent operations with bounded attempts/deadline.
- Ticket/response mutations use a conceptual idempotency key and state reconciliation.
- Error paths cannot bypass approval or reach closure as success.
- Notifications occur after the state they report has been independently read back.

## Migration plan

1. Select product/release and preserve the original export/hash.
2. Inventory every source task, command, path, dependency, permission, action, and caller.
3. Capture existing behavior with fixtures before moving nodes.
4. Define contracts and extract one responsibility at a time.
5. Compare parent results and side-effect plans with the unchanged baseline.
6. Validate dependency/version/update relationships.
7. Run static and debugger tests with protected tasks skipped/stubbed.
8. Controlled-import the exact artifact only after schema validation.
9. Canary reversible paths under separate authorization; retain readback.
10. Keep rollback to the preserved prior artifact until monitoring closes.

## Acceptance criteria

- Every original behavior is retained, deliberately changed, or removed with owner approval.
- Parent and child contracts cover valid, empty, error, multiple, duplicate, oversized, and hostile inputs.
- No undeclared global-context dependency or parallel same-key writer remains.
- No command/path/task ID is guessed.
- Protected actions require exact-scope approval, recovery, and readback.
- Error, timeout, replay, partial failure, notification, and closure paths have tests.
- `C` and `E` remain `NOT RUN` until exact target evidence exists.

## Validation status

| Level | Result | Rationale |
|---|---|---|
| S | NOT RUN | No original graph or independent before/after behavioral evaluation is available. |
| D | PASS | PB05, PB07, and PB09 were re-opened on 2026-09-06 for XSIAM sub-playbook I/O, error paths, and context. The proposed decomposition is conceptual; it makes no XSOAR release claim. |
| C | NOT RUN | No target export/schema, validator, or controlled import was checked. |
| E | NOT RUN | No refactored workflow or equivalence test was executed. |

## Local references

- [Playbook design patterns](../../references/playbook-design-patterns.md)
- [Data contracts and context](../../references/data-contracts-and-context.md)
- [Testing and deployment](../../references/testing-deployment-troubleshooting.md)
- [Playbook review template](../../templates/playbook-review.md)
