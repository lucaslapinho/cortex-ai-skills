# Indicator lifecycle and governance

## Contents

- [Lifecycle is a policy](#lifecycle-is-a-policy)
- [Conceptual state model](#conceptual-state-model)
- [Expiration](#expiration)
- [Reactivation and repeated observations](#reactivation-and-repeated-observations)
- [Source withdrawal and revocation](#source-withdrawal-and-revocation)
- [Exclusion and deletion](#exclusion-and-deletion)
- [Governance controls](#governance-controls)
- [Audit record](#audit-record)
- [Lifecycle validation](#lifecycle-validation)

## Lifecycle is a policy

An indicator lifecycle connects source observations, managed state, enrichment, distribution eligibility, and downstream action. It must define who owns each transition, what evidence triggers it, how conflicts are handled, and how a decision is reversed.

Do not treat “active” as true, “expired” as false, or “deleted” as harmless. Lifecycle state expresses operational treatment under a policy, not ground truth about the indicator.

## Conceptual state model

The following model is a design aid, not a claim that every label is a native Cortex field:

```text
observed
  -> validate and normalize
     -> rejected or review-required
     -> managed-active
          -> enriched / relationship-updated
          -> distribution-eligible (separate policy)
          -> expired
               -> reactivated by applicable new evidence
          -> source-withdrawn or revoked (mapping must be verified)
          -> excluded (scope-specific)
          -> deleted (approved destructive action)
```

Record `CONCEPTUAL` for policy-only states such as quarantine or review-required unless the target product/version and tenant configuration prove a native equivalent.

## Expiration

Expiration answers when an indicator should stop being treated as current for applicable workflows. It is not deletion.

Current XSIAM documentation establishes, within its documented scope, that:

- a default expiration can be associated with an indicator type profile;
- a feed configuration can select an expiration behavior, including type-based, fixed interval, never, or when removed from the feed, where the integration supports it;
- manually expiring an indicator overrides other expiration mechanisms;
- an expired indicator remains stored and searchable;
- new data can reactivate an expired indicator;
- when an indicator is observed in multiple feeds, feed reliability and, at equal reliability, feed recency affect which feed's expiration applies;
- some feeds retrieve only new indicators and cannot determine source removal;
- disabling a feed changes its indicators to use indicator-type expiration in the documented scenario.

These are `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED`. Recheck exact current pages and tenant configuration before use.

An expiration design should state:

| Element | Required decision |
|---|---|
| Clock | Which timestamp begins the interval and in which timezone? |
| Policy owner | Feed, indicator type, manual operator, script/playbook, or another verified mechanism? |
| Source conflict | Which documented or approved rule governs multiple sources? |
| Never-expire | Who approves it, for which types, and how stale risk is reviewed? |
| Removal-based | Can this exact integration observe removals? How are outages distinguished? |
| Downstream propagation | How is the item removed or deactivated at every consumer? |
| Reactivation | What new evidence qualifies, and is redistribution separately authorized? |
| Audit | Before/after state, reason, actor, evidence, timestamp, and affected consumers? |

## Reactivation and repeated observations

Separate:

- a source replay of an old observation;
- a genuinely new observation time;
- a revised source assertion;
- a different source observing the same normalized indicator;
- an enrichment result with no new source observation.

Only applicable evidence should refresh lifecycle state. Do not reset freshness merely because a polling job fetched the same unchanged object again. Confirm how the installed integration handles source timestamps and revisions.

Reactivation in Cortex documentation does not automatically authorize re-export or re-block. Distribution and control policies must evaluate the new state independently.

## Source withdrawal and revocation

“Removed,” “revoked,” “deleted,” and “expired” are not synonyms:

- **source removal** means the item no longer appears in a source view; it could be intentional, a windowing effect, pagination failure, or outage;
- **revocation** is an assertion in a source/protocol model and may signal that a prior object should no longer be used;
- **expiration** is a time/lifecycle decision in the managed platform;
- **deletion** removes the managed record;
- **downstream removal** changes a consumer's list or policy state.

Do not claim a generic STIX revocation property maps to a particular Cortex field or transition. Validate the exact integration mapping and observe a bounded test. If mapping is unknown, preserve the source assertion and mark the Cortex behavior `UNVERIFIED`.

## Exclusion and deletion

Current XSIAM documentation distinguishes at least two exclusion intents in named contexts:

- exclude an indicator type or individual value from enrichment while retaining the indicator;
- exclude values so they are not created or used in automation after deletion/exclusion workflow.

The documented supported types and behavior are version-sensitive. Do not assume an exclusion applies to ingestion, enrichment, playbooks, export, or downstream controls unless the exact control says so.

Deletion is destructive and generally appropriate for a documented correction, privacy/retention requirement, or other approved governance need—not routine freshness management. Before deletion:

1. identify exact indicators and consumers;
2. retain a sanitized before-state and reason;
3. evaluate relationship, audit, case/issue, and downstream impacts;
4. obtain authorization;
5. define recovery or reconstruction from source;
6. verify Cortex and downstream state afterward.

## Governance controls

Assign owners for:

- source contract and credentials;
- indicator type and normalization policy;
- source reliability assessment;
- confidence/reputation/verdict mappings;
- enrichment privacy and cost controls;
- tags and controlled vocabulary;
- expiration and exception policy;
- relationships and graph limits;
- distribution filters and service availability;
- security-control approval and rollback;
- audit, retention, privacy, and legal handling;
- monitoring, incident response, and source offboarding.

Use least privilege and separate ability to view intelligence, edit indicators, configure integrations, manage exclusions, export data, and operate detection/prevention controls. Exact permissions must come from current product documentation and tenant evidence.

## Audit record

For every material lifecycle transition, record:

```text
transition_id: {{NONSECRET_ID}}
product_context: {{PRODUCT_VERSION_LICENSE_DEPLOYMENT}}
indicator_reference: {{SANITIZED_OR_HASHED_REFERENCE}}
prior_state: {{OBSERVED_STATE}}
new_state: {{OBSERVED_OR_PROPOSED_STATE}}
trigger: {{SOURCE_EVENT_POLICY_MANUAL_ACTION}}
evidence_class: {{CANONICAL_CLASS}}
source_and_time: {{SOURCE_UTC}}
actor_or_automation: {{SANITIZED_IDENTITY}}
approval: {{REFERENCE_OR_NOT_REQUIRED_WITH_REASON}}
affected_consumers: {{LIST_OR_UNKNOWN}}
rollback: {{METHOD_AND_OWNER}}
verification: {{CORTEX_AND_CONSUMER_READBACK}}
limitations: {{UNVERIFIED_ITEMS}}
```

The field names above are documentation fields, not Cortex API or indicator fields.

## Lifecycle validation

- [ ] Product, version, entitlement, integration, and tenant applicability known
- [ ] Original source observation and transformation provenance retained
- [ ] Expiration owner, clock, precedence, exceptions, and consumer effect defined
- [ ] Source replay does not automatically refresh evidence age
- [ ] Reactivation is distinct from redistribution and re-enforcement
- [ ] Source removal, revocation, expiration, exclusion, deletion, and downstream removal are distinct
- [ ] No native state or field invented
- [ ] Destructive actions are approved and recoverable
- [ ] Cortex and consumer readback are separate
- [ ] Unavailable tenant evidence remains `NOT RUN`
