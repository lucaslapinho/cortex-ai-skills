# Agents, Broker VM, Collectors, and Engines

Use this reference to select or troubleshoot customer-network components without conflating their purposes.

## Contents

- Boundary summary
- Cortex XDR agent
- Broker VM
- XDR Collector
- Cortex Engine
- Selection questions
- Health is layered
- Upgrade and lifecycle
- Handoff record

## Boundary summary

| Component | Primary product boundary | Purpose used by this Skill |
|---|---|---|
| Cortex XDR agent | XSIAM/XDR, version and OS dependent | Endpoint prevention, policy, status, and telemetry |
| Broker VM | XSIAM/XDR, applet/license dependent | Hardened bridge for documented network-side services/applets |
| XDR Collector | XSIAM/XDR documentation as applicable | On-premises Windows/Linux log/event collection |
| Cortex Engine | XSIAM, XDR, or XSOAR deployment/version dependent | Remote playbook, script, command, and integration execution plus tenant connectivity |

Do not co-locate, replace, or compare these components solely from their names. Verify the current supported topology.

## Cortex XDR agent

Current XSIAM documentation exposes endpoint connection and operational-protection state as distinct information. Treat these checks separately:

1. endpoint exists in the intended tenant;
2. installation package and policy/group assignment are correct;
3. agent version and OS are supported;
4. agent is checking in;
5. protection modules report their documented operational state;
6. EDR/data collection is enabled where required;
7. the expected event was generated on the endpoint;
8. telemetry reached ingestion;
9. fields are visible under the querying identity.

A “Protected” operational status means the agent reported protection behavior as documented for that status. It is not a universal statement about network connectivity, every module, event completeness, ingestion, or query results.

Sources: [Manage endpoints](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Manage-endpoints) and [Monitor agent operational status](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Monitor-agent-operational-status).

Do not perform endpoint isolation, restart, uninstall, database clearing, upgrade, or policy mutation as a troubleshooting shortcut. Those are state changes with separate authorization and recovery requirements.

## Broker VM

Current XSIAM and XDR documentation describes Broker VM as a secured network bridge that can run eligible services/applets. It explicitly describes the Broker VM as a closed, hardened appliance and prohibits installing third-party agents on it.

Verify:

- target product and Broker release;
- license and applet availability;
- supported virtualization/deployment model;
- registration and tenant association;
- proxy, DNS, certificate, and outbound connectivity requirements;
- applet-specific source protocol and configuration;
- component and applet health;
- local caching/buffering implications;
- cluster support and failure semantics for the exact version;
- input, send, and ingestion evidence.

Sources: [What is the Broker VM](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/What-is-the-Broker-VM) and [Set up and configure Broker VM](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Set-up-and-configure-Broker-VM).

An XDR 5 applet-management page establishes only the XDR 5 surface. It does not prove the same applet or UI exists in XSIAM: [Manage Broker VM data collector applets — XDR 5](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-5.x-Documentation/Manage-Broker-VM-data-collector-applets).

For syslog, re-open the product-specific activation page before selecting transport, framing, ports, or capacity. Published capacity is design guidance under stated assumptions, not a tenant guarantee: [Activate Syslog Collector — XSIAM 3.x](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Activate-Syslog-Collector).

## XDR Collector

Current XSIAM 3.x documentation describes XDR Collectors as dedicated on-premises data collection on supported Windows and Linux machines, using documented log-shipping components. It separates profiles, policies, installation, management, audit, and resulting datasets.

Verify:

- target product and supported collector release;
- collector-host OS and machine requirements;
- package source and integrity;
- profile content and policy assignment;
- source-file/event-log permissions;
- source rotation/multiline/encoding behavior;
- proxy and outbound connectivity;
- collector health and audit evidence;
- source input versus collector send evidence;
- dataset creation and raw-record visibility;
- upgrade scheduler and rollback/support procedure.

Sources: [XDR Collectors](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/XDR-Collectors?contentId=qfIZLEv731a8gqLwBz0GGg), [Manage XDR Collectors](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Manage-XDR-Collectors), and [XDR Collector datasets](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/XDR-Collector-datasets).

Do not invent Filebeat or Winlogbeat YAML. Use a target-version template or the target UI and validate it in non-production. A successful installer exit does not prove policy mapping, file access, shipping, ingestion, parsing, or visibility.

## Cortex Engine

Current official documentation describes product-scoped Engines for Cortex XSIAM, Cortex XDR 5.x, Cortex XSOAR 8 SaaS, and Cortex XSOAR 8.14 On-prem. In each named product, an Engine is a proxy application on a remote machine that communicates with that product's tenant and can run playbooks, scripts, commands, and integrations remotely. Treat this shared high-level purpose as `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED`; installation, container runtime, connectivity, grouping, permissions, commands, upgrade behavior, and availability remain `VERSION-DEPENDENT` for the exact product and deployment.

The old XSOAR 8 Administrator Guide page is retiring. That makes the old page a `DEPRECATED` source; it does **not** make the Engine concept deprecated. Do not transfer an XSOAR, XDR, or XSIAM Engine procedure, field, command, or topology to another product merely because the high-level role is similar.

Verify:

- XSIAM, XDR, or XSOAR product; SaaS or On-prem deployment where applicable; and exact version;
- Engine installation/runtime prerequisites from that version;
- tenant association and trust boundary;
- integration instance or command assignment;
- service identity and credential custody;
- network/proxy route;
- supported Engine group/load-balancing semantics;
- command execution evidence and audit trail;
- upgrade, failover, and rollback procedure.

Current sources: [XSIAM Engine](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/engines/what-is-an-engine.md), [XDR 5.x Engine](https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/detect-investigate-and-respond-to-threats/investigate-and-respond-to-cases/automation/engines/what-is-an-engine.md), [XSOAR 8 SaaS Engine](https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-saas/configure-cortex-xsoar/engines/what-is-an-engine.md), and [XSOAR 8.14 On-prem Engine](https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.14/configure-cortex-xsoar/engines/what-is-an-engine.md).

Legacy source retained only for source-history review: [retiring XSOAR Engines use-case page](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSOAR/8/Cortex-XSOAR-Administrator-Guide/Engines-Use-Case).

Do not use an Engine page to establish an ingestion architecture, or to establish another product's configuration.

## Selection questions

Ask:

1. Is the source an endpoint, log file/event log, network protocol sender, cloud service, or an API-accessible system?
2. Does the target product catalog document a direct integration?
3. Must a customer-network component reach an otherwise private source?
4. Is protection required, or only log collection?
5. Which trust zone may hold the credential?
6. What OS/runtime can the customer manage?
7. What are the observed event size/rate, burst, delay, and loss tolerance?
8. Which supported HA or retry semantics apply?
9. Who owns upgrades, certificates, proxy, and monitoring?
10. Which query/object must show the controlled event?

Return a conditional comparison if material facts are missing.

## Health is layered

| Observation | It can support | It cannot prove |
|---|---|---|
| Component registered | Association existed at observation time | Correct assignment or data flow |
| Component connected | A control/transport channel reported connected | Source generated events or all traffic delivered |
| Applet/integration green | That product health surface reported a state | Parser/mapping/query completeness |
| Input count increases | Component received something | Correct source identity, successful send, or ingestion |
| Send count increases | Component attempted/reported send | Tenant accepted, stored, parsed, or mapped every record |
| Raw dataset row exists | One record was visible | Complete coverage or normalized visibility |
| Normalized row exists | Mapping produced one visible result | Sustained capacity or absence of loss |

Always record the health surface, exact component, identity, timestamp, and observation window.

## Upgrade and lifecycle

Before upgrading:

- verify current and target versions, supported upgrade path, dependencies, and release notes;
- inventory profiles, policies, certificates, integrations, and content dependencies;
- preserve supported backups/exports and configuration hashes;
- define canary scope, success metrics, rollback trigger, and recovery owner;
- test source input, transport, ingestion, parsing, mapping, and visibility after upgrade;
- inspect duplicates, gaps, delayed delivery, and audit events.

Do not claim rollback is supported unless the target-version procedure documents it. “Reinstall” is not automatically a rollback.

## Handoff record

Include:

- product/deployment/version/license;
- component ID or sanitized alias;
- host/zone and owner;
- assigned profile/policy/integration;
- current health with time;
- expected source event and last known good;
- input/send/ingestion/query observations;
- sanitized errors and correlation markers;
- changes attempted and approvals;
- next discriminating check.
