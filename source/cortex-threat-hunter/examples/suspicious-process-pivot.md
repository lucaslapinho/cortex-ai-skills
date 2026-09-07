# Example: suspicious process pivot

Status: CONCEPTUAL / DERIVATIVE / TENANT-UNVERIFIED

## Lead

A redacted alert excerpt claims that a scripting process launched on endpoint WS-EXAMPLE. The excerpt is supplied evidence, not a verified tenant observation.

## HYP-001

If the process represented unauthorized remote-content execution, then verified endpoint lineage plus process-attributed network activity should show a parent/child and destination sequence inconsistent with approved administration during the bounded event window.

## Evidence separation

- EV-001: user-supplied alert excerpt is accessible; its underlying event claim is UNVERIFIED / PROJECT-ASSERTED / TENANT-UNVERIFIED. Reading the excerpt verifies its text only; any named but unavailable original is REFERENCED-ONLY.
- OBS-001: the excerpt contains a process label and endpoint label.
- INFERRED: unauthorized execution is one possible meaning.
- ALT-001: approved management script.

## Query plans

- QP-001: retrieve the process instance and ancestry using tenant-observed endpoint schema.
- QP-002: retrieve process-attributed network activity within a small skew-aware window.
- QP-003: compare parent, signer, account, destination, and time with approved deployment evidence.

No executable XQL is shown because datasets and fields are not verified.

## Pivots

| ID | From → to | Discriminator | Ambiguity |
|---|---|---|---|
| PIV-001 | Process → parent/ancestor | Approved management chain or anomalous ancestry | Missing/truncated ancestry |
| PIV-002 | Process → destination | Direct process attribution | Proxy/NAT/shared hosting |
| PIV-003 | Identity → change record | Approved operator and window | Shared/service identity |
| PIV-004 | File/hash → signer/inventory | Approved signed tool | Version drift |

## Timeline and scope

Maintain process start, network event, alert creation, and ingestion times separately. Start with the single endpoint and ±15 minutes only as an analytic proposal; expand after time semantics and coverage are validated.

## Conclusion and handoff

Conclusion: INSUFFICIENT EVIDENCE. Recommend tenant schema validation and read-only query execution. Do not isolate the endpoint or block the destination within this Skill.

## Local references

- [Pivots, timelines, and scoping](../references/pivots-timelines-and-scoping.md)
- [Telemetry and coverage](../references/telemetry-and-coverage.md)
