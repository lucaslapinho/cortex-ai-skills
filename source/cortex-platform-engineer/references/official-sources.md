# Official Source Register

Standalone first-party source register for `cortex-platform-engineer`.

**Scoped refresh — 2026-10-23:** see [the dated refresh](2026-10-23-refresh.md)
for the exact pages reopened, current claim boundaries, API release-note changes,
and the unresolved HTTP-method discrepancy. Unlisted rows retain their prior dates.

**Review date:** 2026-09-04  
**Rule:** re-open the exact product/version page before a production decision. Link availability and documentation support do not prove tenant entitlement, configuration, health, or execution.

**Astra refresh:** 2026-09-06. A05 was reopened at its canonical URL to verify
effective access, disabled dataset-access-management display semantics, and the
Datasets Rows/XDM restriction. C01, C05, C10, C11, D03, D07, I04, A02, A03 and A07
were also reopened for their bounded claims. This refresh does not redate unreviewed
rows or establish tenant behavior.

## Contents

- Classification
- Product and deployment
- Agents, Broker, collectors, and Engines
- Ingestion, parsing, datasets, and health
- Integrations, cloud, and forwarding
- APIs and access
- Source gaps

## Classification

- `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED`: the page supports the bounded documented claim; tenant state is unknown.
- `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED`: applicability changes with product, deployment, release, license, or surface.
- `DEPRECATED / OFFICIAL-CURRENT / TENANT-UNVERIFIED`: current first-party lifecycle material identifies a legacy/deprecated surface.
- `DEPRECATED / REFERENCED-ONLY / TENANT-UNVERIFIED`: the historical first-party URL is retained only as source history and does not support a current product claim.

## Product and deployment

| ID | Official source | Scope | Classification | Boundary |
|---|---|---|---|---|
| P01 | [Learn about Cortex XSIAM](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/learn-about-cortex-xsiam/readme.md) | Current XSIAM SaaS product documentation index | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Index only; use feature-specific pages and verify the target tenant release. |
| P02 | [What is Cortex XDR](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-5.x-Documentation/What-is-Cortex-XDR) | Cortex XDR 5.x product boundary | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | License and source support are not universal. |
| P03 | [What is Cortex XSOAR](https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.14/learn-about-cortex-xsoar/what-is-cortex-xsoar.md) | XSOAR 8.14 On-prem | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Do not transfer to SaaS/older versions. |

## Agents, Broker, collectors, and Engines

| ID | Official source | Scope | Classification | Boundary |
|---|---|---|---|---|
| C01 | [What is the Broker VM](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/What-is-the-Broker-VM) | XSIAM 3.x Broker purpose and hardened-appliance boundary | `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Third-party agents are not supported; applets depend on license. |
| C02 | [Set up and configure Broker VM](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Set-up-and-configure-Broker-VM) | XSIAM 3.x setup, registration, proxy/TLS/connectivity | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Exact values and flows vary by Broker version. |
| C03 | [Manage Broker VM data collector applets](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-5.x-Documentation/Manage-Broker-VM-data-collector-applets) | XDR 5.x applet lifecycle | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Not XSIAM evidence. |
| C04 | [Activate Syslog Collector](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Activate-Syslog-Collector) | XSIAM 3.x Broker syslog applet | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Transport, framing, port, capacity, and licenses must be refreshed. |
| C05 | [XDR Collectors](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/XDR-Collectors?contentId=qfIZLEv731a8gqLwBz0GGg) | XSIAM 3.x Windows/Linux collection model | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Recheck OS, package, event, transport, and upgrade support. |
| C06 | [Manage XDR Collectors](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Manage-XDR-Collectors) | XSIAM collector health/lifecycle | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Installation or connection alone is not end-to-end health. |
| C07 | [XDR Collector datasets](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/XDR-Collector-datasets) | Resulting raw-dataset behavior | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Literal tenant dataset/population must be observed. |
| C08 | [Manage endpoints](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Manage-endpoints) | XSIAM endpoint inventory/status fields | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Status definitions and timing vary by agent/platform/version. |
| C09 | [Monitor agent operational status](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Monitor-agent-operational-status) | XSIAM/XDR agent protection status | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Does not prove telemetry completeness. |
| C10 | [What is an XSIAM Engine](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/engines/what-is-an-engine.md) | Current XSIAM remote Engine purpose and tenant boundary | `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Product-specific configuration, permissions, runtime, grouping, and lifecycle still require target-version evidence. |
| C11 | [What is an XDR 5.x Engine](https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/detect-investigate-and-respond-to-threats/investigate-and-respond-to-cases/automation/engines/what-is-an-engine.md) | Current XDR 5.x remote Engine purpose and tenant boundary | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Do not transfer XDR configuration or availability to XSIAM/XSOAR. |
| C12 | [What is an XSOAR 8 SaaS Engine](https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-saas/configure-cortex-xsoar/engines/what-is-an-engine.md) | Current XSOAR 8 SaaS remote Engine purpose | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | SaaS evidence does not establish an On-prem procedure. |
| C13 | [What is an XSOAR 8.14 On-prem Engine](https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.14/configure-cortex-xsoar/engines/what-is-an-engine.md) | Versioned XSOAR 8.14 On-prem remote Engine purpose | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Does not establish SaaS or another On-prem release. |
| C14 | [Retired XSOAR Engines use-case URL](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSOAR/8/Cortex-XSOAR-Administrator-Guide/Engines-Use-Case) | Historical source pointer, not current support evidence | `DEPRECATED / REFERENCED-ONLY / TENANT-UNVERIFIED` | The URL now resolves to a generic documentation page. This does not mean the Engine concept is deprecated; use C10-C13 for current product/version evidence. |

## Ingestion, parsing, datasets, and health

| ID | Official source | Scope | Classification | Boundary |
|---|---|---|---|---|
| D01 | [What are Cortex XSIAM data sources](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/What-are-Cortex-XSIAM-data-sources) | XSIAM source model | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Catalog/license/content/tenant determine availability. |
| D02 | [HTTP Log Collector](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Set-up-an-HTTP-log-collector-to-receive-logs?contentId=XAfILj87fu6SWS8m7EbtYw) | XSIAM formats, authentication, bounds, raw dataset | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Recheck endpoint generated by tenant and every limit. |
| D03 | [Overview of data ingestion metrics](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Overview-of-data-ingestion-metrics) | `metrics_source`, `metrics_view`, ingestion health | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Analytics prerequisite and metric semantics apply. |
| D04 | [Measuring data freshness](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Measuring-data-freshness) | Source/insert-time delay analysis | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Validate source clocks and field meanings. |
| D05 | [Parsing rules](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/data-management/parsing-rules.md) | Current XSIAM parsing purpose and rule overview | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Ordinary XQL is not an import-ready rule; validate XQLp in the target product editor. |
| D06 | [Parsing Rules file structure and syntax](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Parsing-Rules-file-structure-and-syntax) | XQLp sections and syntax | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Validate in target editor; do not invent stages. |
| D07 | [Create Data Model Rules](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Create-Data-Model-Rules) | XSIAM mapping editor and permissions | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Editing defaults affects Marketplace updates. |
| D08 | [Troubleshooting Data Model Rules](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Troubleshooting-Data-Model-Rules) | Mapping errors and `parsing_rules_errors` | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Some fields are rule-type-specific. |
| D09 | [Data retention](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Data-retention) | XSIAM retention boundary | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | No universal lookback. |

## Integrations, cloud, and forwarding

| ID | Official source | Scope | Classification | Boundary |
|---|---|---|---|---|
| I01 | [Vendor-specific data sources and connectors](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/cortex-xsiam-data-sources/vendor-specific-data-sources-and-connectors.md) | XSIAM source catalog | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Availability varies by release/license/configuration. |
| I02 | [Add an integration instance](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Add-an-integration-instance) | XSIAM integration configuration | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Test status is not fetch/end-to-end proof. |
| I03 | [Troubleshoot integrations](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Troubleshoot-Integrations) | XSIAM integration diagnostics | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Use the exact integration/version. |
| I04 | [Event Collection Integrations](https://xsoar.pan.dev/docs/integrations/event-collectors) | XSIAM developer event collectors | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | `send_events_to_xsiam()` is system-only and fails in custom integrations. |
| I05 | [Ingest external alerts](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Ingest-external-alerts) | XSIAM external alert admin guidance | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Does not establish current legacy API payload/limits. |
| I06 | [Ingest logs from Amazon CloudWatch](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Ingest-logs-from-Amazon-CloudWatch?contentId=Qbap8p2r9Ahu31V8T7XmYg) | XSIAM generic/EKS AWS collection | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Cloud roles/resources/datasets/normalization require tenant proof. |
| I07 | [Data and log forwarding](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Data-and-log-forwarding) | XSIAM outbound forwarding overview | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Object/destination support differs. |
| I08 | [Configure notification forwarding](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Configure-notification-forwarding) | XSIAM object/filter/destination configuration | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Save does not prove delivery. |
| I09 | [Contributing XSOAR Content](https://xsoar.pan.dev/docs/contributing/contributing) | Official contribution routes, support types, review, validation, and lint gates | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Local checks do not prove PR approval, Marketplace publication, tenant installation, or execution. |
| I10 | [Contribution Checklist](https://xsoar.pan.dev/docs/contributing/checklist) | Required pack metadata, documentation, release notes, and entity-specific files | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Requirements vary by entity, support model, update type, and current toolchain. |
| I11 | [Content Packs Structure](https://xsoar.pan.dev/docs/packs/packs-format) | Pack tree and target marketplace metadata | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Select the target product/marketplace explicitly; validate with the current schema/tool version. |
| I12 | [Demisto SDK repository](https://github.com/demisto/demisto-sdk) | Current supported development host, dependencies, and command catalog | `VERSION-DEPENDENT / OFFICIAL-EXAMPLE / TENANT-UNVERIFIED` | Pin the SDK version or reviewed commit. The current README supports Linux, macOS, and WSL2; it says native Windows is unsupported and directs users to WSL2 or a container. Command coverage can also depend on network and Docker availability. |

## APIs and access

| ID | Official source | Scope | Classification | Boundary |
|---|---|---|---|---|
| A01 | [Get started with Cortex XSIAM APIs](https://cortex-docs.paloaltonetworks.com/xsiam-api/get-started-with-cortex-apis.md) | API key/key ID/FQDN/authentication baseline | `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Tenant values, endpoint, role, and response unverified. |
| A02 | [Notable API migrations](https://cortex-docs.paloaltonetworks.com/xsiam-api/api-release-notes.md#notable-api-migrations) | Incident-to-Case and Alert-to-Issue migrations | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Semantic replacements must be checked endpoint by endpoint. |
| A03 | [Legacy APIs without identified successors](https://cortex-docs.paloaltonetworks.com/xsiam-api/api-release-notes#legacy-apis-without-identified-successor-apis) | Legacy lifecycle | `DEPRECATED / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Do not invent successors or reuse old schemas as current. |
| A04 | [Set up users and roles](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Set-up-users-and-roles) | XSIAM identity/RBAC/SBAC architecture | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Gateway and tenant management differ. |
| A05 | [Manage user access](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/onboard-cortex-xsiam/post-deployment/manage-user-roles-and-access-management/manage-user-access.md) | XSIAM effective permissions/scopes; Datasets Rows filters do not support XDM queries; rechecked 2026-09-06 | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | XDM returns rows only with All rows are accessible and no filter in that scoping area. Verify actual enablement/scope; never expand access as a diagnostic shortcut. |
| A06 | [Role permissions by component](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Role-permissions-by-component?contentId=jxQG94yU_RKuFVersHT0uw) | XSIAM component permission reference | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Do not copy another Cortex product’s permission names. |
| A07 | [Configure integration permissions](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Configure-integration-permissions) | Per-instance command roles | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Test actual execution identity. |
| A08 | [Data Sources permissions](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Data-Sources-permissions) | XSIAM data-source administration | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` | Effective role/license/UI must be observed. |
| A09 | [Retired XSOAR users-and-roles URL](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSOAR/8/Cortex-XSOAR-Administrator-Guide/Users-and-Roles-Management) | Historical XSOAR 8 roles pointer, not current support evidence | `DEPRECATED / REFERENCED-ONLY / TENANT-UNVERIFIED` | The URL now resolves to a generic documentation page. Resolve the current deployment/version-specific access documentation and do not transfer a legacy role model to XSIAM/XDR. |

## Source gaps

No current source plus tenant evidence was available for:

- a universal Cortex port or sizing matrix;
- a universal retention value;
- tenant-installed components, datasets, roles, or licenses;
- actual component health, throughput, freshness, or data loss;
- an import-ready parser, mapping, collector, or integration artifact;
- a current Platform API successor for every legacy Alert/Incident API;
- cross-version XSOAR Engine or content compatibility;
- any configuration deployment or rollback result.

These claims remain `UNVERIFIED` or `NOT RUN`.
