# Example: credential-access hypothesis

Status: CONCEPTUAL / DERIVATIVE / TENANT-UNVERIFIED

## Executive assessment

This is a hunt plan, not evidence that credential access occurred.

## HYP-001

If a non-approved process accessed credential-relevant operating-system resources on managed endpoints during the last seven complete days, then endpoint process/file/module telemetry may show a rare access sequence followed by identity or network activity attributable to the same process context, subject to collection and lineage coverage. Approved security, backup, and administration software are competing explanations.

## Context and ATT&CK

The behavior may be consistent with a credential-access technique, but the exact mapping and ATT&CK version must be verified after the observable is established. Mapping is INFERRED and is not evidence.

## Telemetry and gaps

| ID | Need | Status | Consequence |
|---|---|---|---|
| GAP-001 | Endpoint process/lineage and relevant resource-access observables | UNVERIFIED | Primary behavior cannot yet be tested |
| GAP-002 | Approved software/service-account inventory | UNVERIFIED | Benign alternatives remain |
| GAP-003 | Identity activity after the event | UNVERIFIED | Downstream misuse cannot be corroborated |

## Baseline and QP-001

Compare the target process/resource relationship with same-OS, same-role peers across complete daily intervals. Separate security tooling and maintenance windows. Resolve DATASET_ENDPOINT_ACTIVITY, FIELD_EVENT_TIME, FIELD_PROCESS_INSTANCE, FIELD_PARENT_PROCESS, FIELD_RESOURCE, FIELD_ENDPOINT_ID, and FIELD_IDENTITY using tenant schema evidence.

Expected signal: rare process/resource behavior with an unusual parent and a time-correlated identity or network event.

Falsifier: the behavior is common for an approved tool across comparable peers and matches change records.

## Pivots and timeline

- PIV-001: process instance → parent lineage; test whether initiation was administrative.
- PIV-002: endpoint/time → identity events; test whether authentication behavior changed.
- PIV-003: hash/signer → approved software inventory; test the primary benign alternative.

Preserve raw event and ingestion times; do not impose exact ordering when clocks are unverified.

## Scope, alternatives, and conclusion

Unit: unique process instances and unique endpoints, not raw event count.

- ALT-001 approved security/backup software — unresolved until signer/inventory/change evidence is tested.
- ALT-002 administrator action — unresolved until identity/session/change evidence is tested.

Conclusion: INSUFFICIENT EVIDENCE. No tenant observations were supplied.

## Handoff

Send QP-001 unresolved tokens to an XQL specialist. A detection opportunity is premature until the signal is observed, baseline is stable, and benign alternatives are characterized.

## Local references

- [Hunt methodology](../references/hunt-methodology.md)
- [Pivots, timelines, and scoping](../references/pivots-timelines-and-scoping.md)
