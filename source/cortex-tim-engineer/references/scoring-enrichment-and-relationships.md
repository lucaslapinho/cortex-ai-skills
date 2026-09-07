# Scoring, enrichment, and relationships

## Contents

- [Do not collapse assessment dimensions](#do-not-collapse-assessment-dimensions)
- [DBotScore boundary](#dbotscore-boundary)
- [Conflict and merge behavior](#conflict-and-merge-behavior)
- [Enrichment design](#enrichment-design)
- [Cache and exclusion](#cache-and-exclusion)
- [Relationships](#relationships)
- [Decision use](#decision-use)
- [Validation checklist](#validation-checklist)

## Do not collapse assessment dimensions

| Dimension | Subject | Required context | Common error |
|---|---|---|---|
| Source reliability | Producer/feed | Named scale, assessor, review period | Treating a reliable source as proof every indicator is malicious |
| Confidence | A specific assertion | Owner, range, semantics, timestamp | Assuming STIX confidence maps directly to Cortex verdict |
| Reputation/verdict | Indicator assessment | Product/integration and terminology | Calling Unknown benign |
| DBotScore | Normalized integration result where applicable | Integration output contract | Treating it as a probability |
| Custom score | Organization/integration calculation | Formula, inputs, range, version | Inventing a formula from prose |
| Tags | Classification/routing metadata | Controlled vocabulary and owner | Using a tag alone as maliciousness evidence |
| Marking/TLP | Handling/distribution constraint | Applicable policy/version | Treating it as confidence or severity |

Use the source's exact term in the source layer and the Cortex product's exact term in the managed layer. Preserve both when mapping is verified.

## DBotScore boundary

Official Cortex integration guidance describes DBotScore as a normalized result used by integrations. Where the exact integration returns it, the documented convention is:

| Score | Meaning shown in current official material |
|---:|---|
| 0 | Unknown |
| 1 | Good or Benign, depending on the named official context |
| 2 | Suspicious |
| 3 | Bad or Malicious, depending on the named official context |

Guardrails:

- `0` is Unknown, not Good/Benign.
- DBotScore is ordinal categorical output, not a percentage or confidence probability.
- Do not assume every integration produces DBotScore.
- Do not infer a mapping from a vendor's numeric score without its exact integration contract.
- Preserve the integration/source and retrieval timestamp.
- Treat conflicting provider results as evidence to explain, not values to average by default.

## Conflict and merge behavior

Documented merge rules are product- and version-specific. An official XSOAR 8.9 on-premises indicator-verdict page describes legacy behavior in which source reliability influences field selection, equal reliability can use recency, verdict ties choose the more severe verdict, and tags/multi-select values append. XSOAR 8.9 reached EOL on 2026-04-07, so this is `DEPRECATED / OFFICIAL-CURRENT / TENANT-UNVERIFIED` and may be used only to interpret that named legacy scope.

Do not transfer that rule wholesale to:

- XSIAM without applicable corroboration;
- confidence, expiration, relationship, or every custom field;
- a different XSOAR release or customized indicator type;
- a source-native STIX/MISP/OpenCTI field;
- a tenant with scripts or custom logic not inspected.

Current XSIAM feed documentation separately describes reliability-sensitive expiration conflict behavior. Keep the two rules separate.

When behavior is unknown, produce a conflict table rather than choosing a winner:

| Source | Observation time | Source reliability | Native assessment | Normalized assessment | Marking | Evidence |
|---|---|---|---|---|---|---|
| `{{SOURCE_A}}` | `{{UTC}}` | `{{DECLARED_OR_UNKNOWN}}` | `{{VALUE}}` | `{{UNVERIFIED}}` | `{{VALUE}}` | `{{ARTIFACT}}` |
| `{{SOURCE_B}}` | `{{UTC}}` | `{{DECLARED_OR_UNKNOWN}}` | `{{VALUE}}` | `{{UNVERIFIED}}` | `{{VALUE}}` | `{{ARTIFACT}}` |

## Enrichment design

Enrichment is a separate operation from collection and storage. Define:

1. exact indicator types eligible for each provider;
2. exact integration and installed version;
3. authentication, permissions, cost, quotas, rate limits, and data-handling restrictions;
4. automatic versus analyst-requested execution;
5. cache lookup and bypass semantics;
6. exclusion and allowlist behavior;
7. response provenance, timestamp, error, and staleness handling;
8. conflict presentation and decision policy;
9. sensitive-data egress limits;
10. monitoring and circuit-breaking behavior.

Never send an internal or personal value to an external enrichment provider merely because it resembles a supported indicator type. Apply classification and egress policy first.

## Cache and exclusion

The current XSIAM indicator-type-profile documentation describes a default cache of 4,320 minutes (three days) for standard automatic enrichment in its documented context and says direct reputation commands bypass that cache. This is not a universal cache guarantee. Confirm product/version, indicator type profile, integration path, and any customization.

Current XSIAM documentation also distinguishes controls that:

- exclude supported indicator types or individual values from enrichment;
- exclude indicators from creation/automation;
- delete already-created indicators.

The exact supported types and UI/behavior are version-specific. One current enrichment-exclusion page lists IP, Domain, Email, URL, and File for its scope. Do not expand that list from intuition, and do not describe enrichment exclusion as deletion.

## Relationships

Relationships require at least:

- subject and object identities;
- direction;
- relationship semantics from an applicable schema;
- source and observation timestamp;
- confidence/assessment owner if provided;
- start/end or validity semantics if provided;
- marking and distribution constraints;
- transform/mapping provenance;
- cycle and fan-out controls for traversal.

The list is a conceptual evidence contract, not a Cortex relationship schema. Use exact product/tenant evidence for native fields and relationship types.

The current TAXII 2 Feed integration reference lists the integration for XSOAR and XSIAM, but its complex-observation statement explicitly refers to Cortex XSOAR TIM indicators. That limitation is therefore `VERSION-DEPENDENT / OFFICIAL-CURRENT` for the stated XSOAR integration context; its applicability to XSIAM relationship representation is `UNVERIFIED`. Consequently:

- do not promise lossless STIX graph ingestion for either product without exact product and tenant evidence;
- inventory which objects and relationships matter;
- compare source objects with post-ingestion readback in a bounded test;
- record ignored expressions or relationship loss as a design decision;
- do not fabricate missing relationships from co-occurrence.

For graph traversal, use visited-set, depth, node-count, and time limits. Cycles are normal graph structure, not evidence of duplicated indicators.

## Decision use

Assessment values may inform a policy, but they do not by themselves authorize a control action. A safe decision record identifies:

- input assertions and provenance;
- exact mapping/calculation, if any;
- threshold and policy owner;
- allowlist and protected-asset checks;
- indicator age and expiration state;
- false-positive and collateral-impact analysis;
- human approval or explicitly authorized automation boundary;
- downstream consumer, rollback, and verification.

“Confidence above 80” is meaningless unless the scale, source, mapping, and policy are named. “Malicious” is insufficient to justify a block without product context and change control.

## Validation checklist

- [ ] Product/version/license/integration scope recorded
- [ ] Source reliability, confidence, reputation/verdict, DBotScore, custom score, tags, and markings kept distinct
- [ ] Exact scale and owner documented for every numeric value
- [ ] DBotScore `0` handled as Unknown
- [ ] Merge/conflict rule tied to an exact official or tenant source
- [ ] Enrichment type, provider, cache, exclusion, quota, and privacy boundary verified
- [ ] Relationship schema not invented
- [ ] STIX/TAXII relationship loss assessed where applicable
- [ ] No score or tag automatically treated as enforcement authorization
- [ ] Tenant result status remains explicit
