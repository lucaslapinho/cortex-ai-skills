# Example: lifecycle for multi-source indicators

## Objective

Design a lifecycle for domain indicators collected from two external feeds and optionally distributed to a consumer. This is a plan, not a tenant change.

## Applicable product, version, license, and surface

- Target: Cortex XSIAM, exact version/build unknown.
- License/add-on, feed integrations, and consumer: unknown.
- Evidence: `CONCEPTUAL / DERIVATIVE / TENANT-UNVERIFIED`.
- Official baseline: current XSIAM documentation describes indicator expiration, reactivation, manual-expiration precedence, multi-feed expiration precedence, and continued storage/search of expired indicators. Applicability must be rechecked.

## Scope and six-layer classification

- Collection: two inbound feeds.
- Management: validation, normalized domain identity, provenance, duplicate/conflict presentation.
- Enrichment: optional and separately gated for public domains only.
- Lifecycle: active, expired, and reactivated are applicable; “review-held” is a conceptual policy state.
- Distribution: narrow, approved selection only.
- Security control: explicitly out of scope until separately approved.

## Proposed lifecycle

| Transition | Evidence/trigger | Decision |
|---|---|---|
| Observed to review-held | Invalid syntax, missing provenance, protected/internal domain, or prohibited marking | Retain/reject according to approved policy; do not enrich or distribute |
| Observed to active | Type-valid value with source/timestamp/marking and accepted policy | Preserve both source observations and transform provenance |
| Active to expired | Exact feed/type/manual policy says the indicator is no longer current | Do not call this deletion; verify downstream removal separately |
| Expired to active | Applicable genuinely new source observation | Re-evaluate distribution; do not automatically re-block |
| Any to deleted | Approved correction, retention, or privacy action | Retain before state and reconstruction/rollback plan |

## Normalization and duplicate handling

The domain normalization rule is not supplied, so it remains `UNVERIFIED`. The implementation owner must validate case, trailing-dot, Unicode/IDN, and defanging behavior before defining identity. Both original values remain attached to their source observations.

For multi-feed expiration, use the current XSIAM reliability/recency rule only after product version and feed configuration are verified. Do not reuse that rule as a verdict or confidence merge formula.

## Confidence, reputation, and tags

The feeds' assessment models are unknown. No conversion is proposed. Source reliability, assertion confidence, managed verdict, DBotScore, and tags remain separate. Unknown/DBotScore `0` is not benign.

## Distribution and control gate

Distribution eligibility requires accepted marking, current lifecycle state, allowlist/protected-domain check, named consumer, narrow selection, expected count limit, approval, rollback, and Cortex/consumer readback. Security-policy attachment or enforcement requires a second approval and consumer-side validation.

## Validation plan

1. Verify XSIAM version, entitlement, exact feeds, installed integration versions, and effective permissions.
2. Inspect sanitized representative source objects and exact mappings.
3. Test create/update/replay/conflict/expire/reactivate cases with bounded non-production evidence.
4. Confirm expired records remain searchable in the named environment.
5. Verify distribution removal and reactivation behavior at an isolated consumer.

## Limitations and handoff

No schema, mapping, feed fetch, lifecycle transition, export, consumer refresh, enforcement, or performance result was inspected. Implementation awaits the product owner, source owner, TIM administrator, and downstream control owner.

## Local reference

- [Lifecycle and governance](../../references/lifecycle-and-governance.md)
