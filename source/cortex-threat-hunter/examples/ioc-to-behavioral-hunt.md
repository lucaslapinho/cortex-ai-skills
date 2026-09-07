# Example: IOC to behavioral hunt

Status: CONCEPTUAL / DERIVATIVE / TENANT-UNVERIFIED

## Lead and hypothesis

Lead: an external report lists DOMAIN-EXAMPLE as suspicious. The report's provenance, freshness, and confidence must be recorded.

HYP-001: if in-scope systems interacted with the indicator as part of an unauthorized behavior, then primary DNS/network/endpoint telemetry should show bounded interactions with corroborating process, identity, or cloud-control activity that is inconsistent with legitimate shared infrastructure use.

The IOC is a pivot seed, not a verdict.

## Coverage

- DNS visibility may be incomplete because of caching, resolver concentration, or encrypted DNS.
- Firewall/proxy rows may identify shared egress rather than the originating endpoint.
- Endpoint network events may lack process association.
- Intelligence freshness and score semantics may differ by provider.

## Query plan

1. Resolve the indicator and variants using a recorded source/retrieval time.
2. Identify tenant-observed DNS/network schemas and event-time fields.
3. Count unique endpoints/identities/resources separately from raw events.
4. Validate shared resolver/proxy/CDN explanations.
5. Pivot to primary process, identity, or cloud audit telemetry only where correlation keys are reliable.

## Baseline and alternatives

Compare prevalence across comparable networks and complete time intervals. Do not compare resolver traffic directly with endpoint counts.

- ALT-001 legitimate service using shared hosting;
- ALT-002 security scanner or sinkhole;
- ALT-003 stale/incorrect intelligence;
- ALT-004 proxy/resolver artifact.

## Conclusion and detection handoff

Without primary telemetry, confidence remains LOW or INSUFFICIENT EVIDENCE. Do not create an IOC detection solely from the example. If repeatable behavior emerges, hand off the behavioral sequence and retain the IOC only as enrichment.

## Local references

- [Hunt methodology](../references/hunt-methodology.md)
- [Findings and detection handoff](../references/findings-and-detection-handoff.md)
