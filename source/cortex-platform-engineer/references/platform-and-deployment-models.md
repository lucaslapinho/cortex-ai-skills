# Platform and Deployment Models

Use this reference to frame a target architecture before choosing components or procedures.

**Review cut:** 2026-09-04  
**Status:** `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` unless a row says otherwise.

## Contents

- Architecture intake
- Cortex XSIAM
- Cortex XDR
- Cortex XSOAR
- Deployment and management planes
- Component selection matrix
- Availability and resiliency
- Ownership model
- Architecture acceptance criteria

## Architecture intake

Capture:

| Dimension | Required value |
|---|---|
| Product | XSIAM, XDR, XSOAR, or explicitly separated combination |
| Deployment | SaaS, On-prem, or Unknown |
| Version/build | Exact value or documentation review cut |
| License | Plan/add-on/activation facts or Unknown |
| Environment | Production, non-production, lab, or design-only |
| Regions/zones | Actual locations and data-residency constraints or Unknown |
| Identity plane | Gateway/tenant/local identity model as documented |
| Data plane | Sources, collection components, transport, ingestion, storage/query |
| Control plane | Console/API/configuration owners and change approval |
| Response plane | Integrations, automation, and action authorization |

Do not draw one combined “Cortex” box when the request spans products. Show explicit product and tenant boundaries.

## Cortex XSIAM

The current XSIAM 3.x documentation is the baseline for this Skill’s XSIAM statements. It documents a SaaS security-operations platform with endpoint and external data sources, XQL, data management, analytics/detections, integrations, and automation capabilities whose availability depends on license and permissions.

Useful architecture layers:

1. source and endpoint plane;
2. collection plane: agent, documented data source, integration, XDR Collector, or Broker applet;
3. tenant ingestion and data-management plane;
4. raw and normalized data/query plane;
5. Case/Issue, analytics, detection, automation, and forwarding consumers;
6. identity, RBAC, SBAC, dataset access, and audit controls.

This is a conceptual decomposition, not a claim about a tenant’s internal implementation.

Sources: [Cortex XSIAM documentation](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/) and [Cortex XSIAM data sources](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/What-are-Cortex-XSIAM-data-sources).

## Cortex XDR

The current XDR 5.x overview documents a cloud-powered XDR product that analyzes Cortex endpoint and other supported sources, with a unified endpoint agent and license-dependent capabilities. XDR version and license materially affect external data ingestion and collection routes.

Keep separate:

- endpoint protection and agent management;
- EDR data collection;
- external-source ingestion where entitled;
- Broker VM and applet behavior for the documented XDR version;
- Query Center/data visibility;
- Case/Issue and response surfaces;
- Cortex Cloud features or release notes.

Source: [What is Cortex XDR](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-5.x-Documentation/What-is-Cortex-XDR).

## Cortex XSOAR

XSOAR’s platform boundary is orchestration, automation, integrations, scripts, case/incident workflow, and threat intelligence where licensed. Deployment model and version are mandatory:

- XSOAR SaaS documentation does not establish an On-prem procedure.
- XSOAR 8.14 On-prem documentation does not establish an older or SaaS topology.
- A Cortex XSOAR Engine can bridge its named tenant to remote services and run playbooks, scripts, commands, and integrations under the deployment-specific documented model; it is not an ingestion Broker VM. Current pages exist separately for XSOAR 8 SaaS and versioned On-prem releases. The old Administrator Guide page is `DEPRECATED` as a source, not evidence that Engines are deprecated.
- XSOAR roles and integration-command permissions belong to the target XSOAR deployment/version and must not be copied into XSIAM by name.

Sources: [What is Cortex XSOAR 8.14 On-prem](https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.14/learn-about-cortex-xsoar/what-is-cortex-xsoar.md), [XSOAR 8 SaaS Engine](https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-saas/configure-cortex-xsoar/engines/what-is-an-engine.md), and [XSOAR 8.14 On-prem Engine](https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.14/configure-cortex-xsoar/engines/what-is-an-engine.md). The [retiring Administrator Guide page](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSOAR/8/Cortex-XSOAR-Administrator-Guide/Engines-Use-Case) is retained only as deprecated source-history evidence.

## Deployment and management planes

Document these boundaries independently:

| Plane | Questions |
|---|---|
| Tenant/service plane | Which product tenant or On-prem instance owns storage, processing, and object lifecycle? |
| Customer-network plane | Which endpoint, collector host, Broker VM, Engine, proxy, or source is customer-managed? |
| Cloud-provider plane | Which account, role, stream, queue, bucket, or event service is involved? |
| Identity plane | Which identity system creates users, API keys, service identities, roles, and scopes? |
| Content plane | Which Marketplace/content pack/parser/mapping version owns behavior? |
| Query/consumer plane | Where is data expected to be visible and under whose scope? |
| Operations plane | Who monitors health, cost/capacity, freshness, retention, and audit logs? |

Mark every network hop that crosses a trust zone. Record who controls DNS, proxy, certificates, firewall policy, keys, and source permissions at that hop.

## Component selection matrix

| Need | Candidate to verify | Deciding evidence |
|---|---|---|
| Endpoint protection/EDR telemetry | Cortex XDR agent | Supported OS/version, agent policy, EDR collection, endpoint status, license |
| Documented on-prem applet/bridging service | Broker VM | Product/version applet list, license, topology, Broker health, source route |
| Windows/Linux log shipping | XDR Collector | Supported OS, Filebeat/Winlogbeat profile, policy, source format, product license |
| SaaS/vendor source fetch | Product data source or integration | Catalog entry, auth, fetch mode, supported objects, content dependency |
| Custom HTTP push into XSIAM | HTTP Log Collector | Current source page, format, auth, dataset naming, limit/version scope |
| Product-scoped remote automation/integration execution | Cortex Engine | XSIAM/XDR/XSOAR product, deployment/version, routing, integration assignment, container/runtime requirements |
| Outbound notification/data delivery | Product forwarding integration/configuration | Object type, destination compatibility, filter/scope, format, retry/audit behavior |

“Candidate to verify” is not a recommendation until the target evidence is supplied.

## Availability and resiliency

Do not promise high availability from component count alone. Record:

- failure domain and shared dependencies;
- supported clustering or load-balancing mechanism for the exact version;
- source replay or buffering behavior;
- duplicate semantics and ordering;
- health-check scope and alerting;
- upgrade/failover procedure;
- capacity assumptions and observed peak;
- recovery objective and data-loss tolerance;
- controlled failover evidence.

Broker VM clusters, XSOAR Engine groups, multiple integration instances, and multiple XDR Collectors have different semantics. Do not use “HA” as a generic synonym.

## Ownership model

At minimum identify:

| Role | Accountable for |
|---|---|
| Source owner | Event generation, source clock, export policy, source credentials |
| Network owner | DNS, proxy, certificates, routing, firewall rules |
| Platform owner | Tenant configuration, collection components, license, upgrades |
| Data owner | Parser, mapping, dataset, retention, privacy |
| Identity owner | RBAC, SBAC, API/service identities, credential rotation |
| Detection/consumer owner | Query/detection/automation expectations and downstream quality |
| Change approver | Risk acceptance, window, rollback authority |

A single person can hold multiple roles, but the responsibilities must still be explicit.

## Architecture acceptance criteria

An architecture is reviewable when it:

- names products, deployments, versions, licenses, and environments;
- shows the entire data/object path and every trust boundary;
- distinguishes control, data, identity, and response planes;
- records owners and observable evidence per layer;
- avoids unverified literal values;
- defines capacity, retention, privacy, and failure assumptions;
- includes safe changes, rollback, and post-change evidence;
- identifies which assertions remain `UNVERIFIED`.

Use [templates/architecture-record.md](../templates/architecture-record.md).
