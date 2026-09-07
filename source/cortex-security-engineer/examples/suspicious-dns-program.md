# Example: Suspicious DNS Engineering Program

## Scenario

The requester asks: “Find suspicious DNS, make a detection, enrich domains, and block them automatically.”

The only supplied fact is the desired outcome. Product, release, source, schema, network topology, resolver behavior, TIM entitlement, enforcement point, response policy, and tenant evidence are unknown.

## Decision

**`PROCEED TO G0/G1` for requirement and data readiness; `HOLD` detection deployment and blocking.**

Evidence: `CONCEPTUAL / TENANT-UNVERIFIED`. “Suspicious” and “DNS” must be defined before query or rule mechanics.

## Requirement and threat frame

Candidate behaviors to distinguish:

- domains with a risk-relevant age/reputation/context relationship;
- algorithmic or high-entropy naming patterns;
- unusual query volume, rarity, periodicity, or failed-resolution behavior;
- resolver bypass, encrypted DNS, tunneling, or post-resolution connection patterns;
- a known campaign indicator match.

These are alternatives, not one universal detection. The risk owner must select the behavior and protected assets. Benign alternatives can include CDNs, software updates, telemetry agents, security tools, load tests, newly created business domains, and misconfigured applications.

False-negative paths include endpoint versus resolver visibility, caching, encrypted DNS, missing response records, mobile/off-network assets, NAT/entity ambiguity, delayed or absent enrichment, stale intelligence, sampling, retention, and role/SBAC scope.

## Telemetry contract

| ID | Observable | Required semantics | Current evidence |
|---|---|---|---|
| `TEL-101` | DNS request/response | client, resolver, question, type, answer/status, timestamps, direction and grain | `UNVERIFIED` |
| `TEL-102` | asset/user context | stable entity linkage and scope | `UNVERIFIED` |
| `TEL-103` | subsequent connection/process context | correlation keys/time semantics | `UNVERIFIED` |
| `TEL-104` | intelligence/enrichment | source, indicator type, confidence, first/last seen, expiry, conflicts | `UNVERIFIED` |
| `TEL-105` | enforcement/action state | exact control point, target and verification | `UNVERIFIED` |

Platform owner first verifies exact Cortex product/release, supported ingestion path, schema, parsing/mapping, freshness, retention, duplication, identity scope, and TIM license. No dataset or field is guessed.

## Routed work

1. **Platform:** establish source and access readiness; report gaps rather than claiming visibility.
2. **Threat hunting:** test one behavior hypothesis at a time, retain raw observations, and distinguish absence from coverage failure.
3. **XQL:** translate only the selected observable into exact current syntax after schema evidence; define grain, time, cardinality, and expected output.
4. **Detection:** choose the exact eligible rule surface, baseline representative data, define grouping/suppression/severity and FP/FN tests, then plan lifecycle.
5. **TIM:** govern source provenance, indicator type, scoring/conflict, enrichment failure, expiry/revocation, sharing, and consumer semantics.
6. **Playbook:** enrich and present evidence; blocking remains policy/human-gated with denial, timeout, retry, partial-failure, and recovery paths.
7. **Security Engineer:** maintain the decision record, cross-domain entity/time contracts, approval, integrated validation, operations, and retirement.

Optional siblings can implement mechanics; the sequence is usable without them.

## Example control contracts

### Hunt output

One reviewable candidate per domain/client/time window with the exact observed features, coverage limitations, and benign alternatives. A candidate is not a verdict.

### Detection output

One governed signal per approved grouping key/window, with DNS, asset, identity, enrichment provenance, and pivot context. Target surface and thresholds remain detection-owner decisions.

### TIM output

Enrichment carries source, timestamp, indicator type, confidence/score meaning, conflicts, expiry, and “unknown/unavailable” state. Stale or missing intelligence cannot silently become malicious or benign.

### Response output

Recommendation for the exact enforcement point and target. Execution requires approved policy, corroboration, protected-domain/entity exclusions, least scope/duration, action permission, idempotency, recovery, and post-action verification.

## Validation

- controlled known-positive behavior for the selected hypothesis;
- approved CDN/update/security-tool/business-domain fixtures;
- similar negative domains/requests;
- null client, response, answer, asset, and intelligence;
- resolver caching, duplicate sources, boundary time, ingestion lag, and entity ambiguity;
- stale/conflicting/unavailable indicator sources;
- restricted data and command identity;
- repeated block request, partial enforcement, rollback/unblock, and evidence reconciliation.

No current documentation, tenant compile, execution, or efficacy result is assumed. Record `S/D/C/E` independently.

## Operations

Health: source volume/freshness/parser, coverage by asset/resolver, schema/access, enrichment age/failure, rule/playbook/action state.

Outcomes: signal volume/disposition, benign causes, known misses, exception impact, enrichment value, action completion/partial failure/recovery.

Every tuning or block/allow exception gets owner, rationale, scope, expiry, before/after tests, and dependent-control review.

## Non-claims

This example contains no executable XQL, rule, TIM setting, integration command, API, block action, tenant result, production approval, or efficacy claim.

