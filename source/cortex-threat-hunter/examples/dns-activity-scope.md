# Example: DNS activity scope

Status: CONCEPTUAL / DERIVATIVE / TENANT-UNVERIFIED

## HYP-001

If a rare domain-generation-like behavior affected managed endpoints in the specified business unit during a complete seven-day window, DNS telemetry should show repeated low-prevalence query patterns from distinct in-scope clients, subject to resolver attribution, collection, retention, and normalization.

## Baseline

- Unit: unique client entities per normalized domain and complete day.
- Peer group: clients in the same business unit and network path.
- Exclusions: approved testing, security products, known synthetic monitoring.
- Bias checks: resolver-only records, roaming endpoints, split DNS, and incomplete weekend coverage.

“Rare” requires a declared threshold and denominator; it does not mean malicious.

## Query plan and pivots

- QP-001: establish daily client/domain prevalence with verified DNS schema.
- QP-002: compare target clients with peers and complete intervals.
- PIV-001: client/time → endpoint process attribution, if available.
- PIV-002: identity/session → device association, with confidence stated.
- PIV-003: domain → current intelligence, preserving provider and freshness.

## Scope risks

NAT, forwarders, shared resolvers, proxy logs, and inconsistent client identifiers can collapse or multiply entities. State whether the count represents requests, resolver clients, managed endpoints, or identities.

## Conclusion

No results are present in this example. Conclusion: INSUFFICIENT EVIDENCE. A detection opportunity requires observed repeatability, coverage, and benign-prevalence testing.

## Local references

- [Telemetry and coverage](../references/telemetry-and-coverage.md)
- [Pivots, timelines, and scoping](../references/pivots-timelines-and-scoping.md)
