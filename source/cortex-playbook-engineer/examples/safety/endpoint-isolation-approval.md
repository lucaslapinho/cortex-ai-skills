# Should Endpoint Isolation Require Approval?

**Artifact classification:** `CONCEPTUAL`  
**Applicable product/surface:** Cortex response playbook; exact XSIAM/XSOAR product, release, integration, and command not supplied  
**Evidence status:** per-instance command restrictions and debugger side-effect warnings are officially documented for current XSIAM; this policy decision remains environment-specific  
**Execution status:** no command selected, no tenant checked, no action performed

## Decision

Yes by default. Endpoint isolation is a disruptive state change with possible business impact. Require a human or previously approved deterministic policy gate immediately before the action unless the organization supplies a validated exception with equivalent authorization, scope, recovery, and audit controls.

An Issue severity, filename, reputation result, detection confidence, or AI recommendation is not enough by itself.

## Required evidence before approval

- exact target endpoint identity, current connection/state, owner, and criticality;
- corroborated malicious behavior with source/time/coverage and alternatives;
- freshness of evidence and target state;
- maximum target count and explicit exclusions;
- business/service dependencies and expected user impact;
- exact tenant-verified isolation capability, integration instance, command permission, and execution identity;
- confirmed recovery/de-isolation capability and owner;
- timeout, retry, duplicate, and partial-batch behavior; and
- post-action readback plan.

## Conceptual gate

```text
Candidate endpoint
  -> Validate identity and evidence freshness
  -> Check exclusions and criticality
  -> Read current state
  -> Assemble exact action/scope/recovery plan
  -> Authenticated approval: approve | reject | request evidence | expire
  -> Revalidate approval scope and current state
  -> Execute once using tenant-verified capability
  -> Read back isolation state and continued behavior
  -> Recover/escalate on failure, partial, or unexpected state
  -> Record sanitized evidence and notify owners
```

## No-response and error policy

- Approval expiry/no response: do not isolate; escalate.
- Target changed after approval: invalidate approval and re-evaluate.
- Permission denied: stop and preserve the effective identity/denial.
- Timeout: treat state as unknown; read back before retry.
- Already isolated: record prior state; do not duplicate action.
- Partial batch: stop wider rollout and maintain per-target results.
- Readback contradicts returned success: mark failure/unknown and invoke recovery owner.
- Recovery unavailable: block action except under separately documented emergency authority.

## Debugger safety

Current XSIAM guidance says debugger tasks execute under the logged-in user's permissions and can cause real side effects. Therefore skip the isolation task and override a typed synthetic result while testing upstream/downstream logic. Verify no parallel path can still reach the action. A real reversible action test requires separate authorization, a noncritical test target, exact scope, monitoring, and recovery.

## Policy exception evidence

An autonomous exception would require, at minimum:

- formally approved policy and action class;
- independently validated deterministic criteria;
- hard target/volume/exclusion bounds;
- least-privilege service identity and negative-permission tests;
- proven idempotency, timeout reconciliation, and recovery;
- canary/stop controls and continuous monitoring;
- audited production evidence with acceptable false-action rate; and
- named accountable owner with periodic review.

Without that evidence, keep approval mandatory. Do not label a generic “confidence above 20%” threshold safe.

## Validation status

| Level | Result | Rationale |
|---|---|---|
| S | NOT RUN | This example is an authored design, not an independent response evaluation. |
| D | PASS | PB10 and PB15 in the local source register were re-opened on 2026-09-06 and support the XSIAM debugger and command-permission claims only. |
| C | NOT RUN | No target command schema, validator, or import was checked. |
| E | NOT RUN | No isolation, readback, or recovery was performed. |

## References

- [Reliability, safety, and security](../../references/reliability-safety-security.md)
- [Protected action gate](../../templates/action-gate.md)
- [Testing and troubleshooting](../../references/testing-deployment-troubleshooting.md)
- [Official source register](../../references/official-sources.md)
