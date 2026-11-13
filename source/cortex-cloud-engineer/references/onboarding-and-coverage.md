# Onboarding and coverage

Document baseline: 2026-11-13; provider support and entitlement require recheck. Source identifiers refer to [official sources](official-sources.md).

| Provider | Documented onboarding boundary | Checks before calling it covered |
|---|---|---|
| AWS | Account scope supports generated CloudFormation or Terraform; organization/OU onboarding uses CloudFormation in the reviewed guide. | Scope/trust/template deployment, selected regions/resources, collection/audit path, scan status and exclusions. [C01] |
| Azure | The guide distinguishes full Azure onboarding from Entra ID-only collection; generated Terraform or ARM is scope-dependent. Entra-only does not provide workload scanning. | Tenant/subscriptions, deployment versus runtime identity, policy assignments and onboarding errors. Do not turn deployment privilege into permanent runtime entitlement. [C02] |
| GCP | Generated Terraform establishes provider-side trust and permissions for the chosen scope. | Organization/project scope, permissions, enabled collection, scans, regions and quota; no inferred AWS feature parity. [C03] |
| OCI | Tenancy onboarding uses generated Terraform; compartment refinement and disk/registry scanning depend on the selected configuration. | Tenancy/compartments, identity/policy deployment, supported resource/scan types. The reviewed path uses Cortex-managed scanning; do not assume customer-outpost parity. [C04] |

Cloud scan is the documented default recommendation; an outpost moves scanning infrastructure into a customer-owned cloud account and adds capacity, identity, network, lifecycle and cost responsibilities. The reviewed guide calls for a dedicated outpost account and binds an outpost instance to one Cortex Cloud tenant. DSPM on SaaS is listed for cloud scan, not outpost scan. Regional processing claims do not eliminate the need to inspect metadata, egress and contractual data-handling requirements. Verify custom-outpost support and restrictions before promising isolation or air-gapped coverage. [C05]

Kubernetes connector discovery and cluster visibility are separate from installing runtime protection components. Verify cluster distribution/version, identity, namespaces, RBAC, API reachability, ingestion and agent/runtime coverage independently. Use current generated instructions and inspect requested privileges before applying any manifest. [C08]

For an XSIAM handoff, foundational CSP onboarding covers its documented inventory/audit/analytics scope; comprehensive onboarding depends on the documented Cloud Runtime, Cloud Posture or XSIAM Premium entitlement. Licensing documentation is not proof of a tenant's purchased or enabled capabilities. Do not advertise DSPM, scans or runtime enforcement as included in every XSIAM license. [P01]
