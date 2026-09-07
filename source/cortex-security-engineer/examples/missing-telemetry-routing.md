# Example: Telemetry-Gap Routing

## Scenario

A detection owner asks for a production rule for anomalous SaaS administrator logins. The supplied query draft names a plausible tenant-specific dataset and fields, but there is no schema export, sample, parser mapping, source health, retention, identity scope, compiler output, or tenant access.

## Decision

**`HOLD` executable query and detection mechanics; proceed with a platform-owned telemetry contract and a conceptual detection handoff.**

Dataset/fields: `UNVERIFIED / TENANT-UNVERIFIED`. No executable block should repeat them as confirmed schema.

## Why platform comes first

Detection quality depends on:

- the exact SaaS source and collection method;
- authentication versus administrative-audit event semantics;
- actor, target, application, IP/device/session, outcome, privilege, and timestamp fields;
- parser/mapping behavior and schema types;
- source and ingestion time, delay, duplication, and clock;
- tenant population, coverage, retention, and sampling;
- role, dataset access, and dataset-row SBAC;
- a known-positive fixture and expected normal administration.

A name that resembles `vendor_product_raw` is not evidence of existence or meaning.

## Work packages

| Order | Owner | Deliverable | Acceptance |
|---:|---|---|---|
| 1 | Security/risk owner | define “administrator,” “login,” “anomalous,” assets, impact, success and unacceptable outcomes | approved requirement and benign/evasion paths |
| 2 | Platform/data owner | source onboarding, parser/schema, health, retention, identity and scope record | observed sanitized non-production evidence |
| 3 | Hunt/XQL owner | smallest bounded discovery and semantic validation plan | known-positive/benign/negative/null observations; no result overclaim |
| 4 | Detection owner | target-specific candidate, grouping/baseline/FP/FN/lifecycle | editor and representative non-production evidence |
| 5 | Security Engineer | integrated decision, operations and promotion gates | owner/approver/evidence/recovery complete |

## Standalone platform request

Ask the platform/data owner to return:

- product/release/license and source/integration identity;
- dataset/schema export or authoritative editor observation with date;
- sanitized records for successful, failed, non-admin, and admin activities;
- field types, null/population, timestamp semantics, grain and duplication;
- coverage by tenant/application/account and known blind spots;
- freshness/retention/parser health;
- safe identity plus RBAC/SBAC/dataset-row scope;
- failed-source and restricted-identity observations;
- evidence location/hash and privacy controls.

No configuration change is authorized by this request.

If a later raw-dataset check succeeds but XDM returns no rows, add an access-model
check before attributing the gap to normalization. XSIAM's current documentation
does not support XDM queries under Datasets Rows filters; the platform/identity
owner must inspect the effective scope and no-filter policy. Keep the evidence
bounded and retain all access restrictions while selecting an approved raw-query
or another supported design. See the
[product-specific permission chain](../references/product-surface-map.md#permission-and-entitlement-chain),
rechecked on 2026-09-06.

## Conceptual analytic contract

```text
Within an owner-approved bounded window:
select observed administrative-authentication events
where the actor and successful outcome semantics are tenant-verified
derive only owner-approved anomaly features from an evidenced baseline
retain actor, target, source, device/session, privilege, time, and provenance context
emit candidates for review; do not infer compromise or response authorization
```

The detection owner later decides whether the behavior belongs in an eligible rule surface and how to group, baseline, suppress, score, monitor, roll back, and retire it.

## Non-claims

No source is asserted onboarded or healthy. No dataset, field, event, query, rule, alert, case, execution, detection efficacy, or tenant permission is claimed.
