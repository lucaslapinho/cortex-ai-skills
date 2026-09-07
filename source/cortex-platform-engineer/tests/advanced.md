# Advanced Behavioral Tests

Run with [README.md](README.md). Advanced cases reward explicit boundaries over superficial completeness.

## PLAT-ADV-01 — XSIAM and XSOAR hybrid architecture

**Fixture**

- Cortex XSIAM receives security data.
- Cortex XSOAR 8.14 On-prem runs an integration against an internal service.
- The user wants “one Cortex collector layer.”
- No network diagram, Engine topology, license, identity, or tenant state is supplied.

**Prompt**

> Collapse the platform into one architecture, reuse the same roles and collector configuration, and show the data and command paths.

**Expected observations**

- Keeps XSIAM ingestion and XSOAR orchestration/Engine boundaries separate.
- Draws distinct data, control, identity, credential, and command paths.
- Requires product/deployment/version-specific roles and configuration rather than reusing names.
- Identifies owners, trust zones, failure evidence, and cross-product handoff contracts.

**Prohibited behaviors**

- Calling an XSOAR Engine a Broker VM/XDR Collector.
- Assuming one tenant, role model, dataset, or API across products.

**Evidence expected**

- XSIAM current documentation and XSOAR 8.14 On-prem plus Engine documentation.
- C/E per product `NOT RUN`.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no product/editor/API validation; E: NOT RUN — no tenant execution.`

## PLAT-ADV-02 — Capacity and high availability

**Fixture**

A global enterprise plans a new collector tier but provides no observed event sizes/rates, burst profile, loss tolerance, component version, region, license, or failure-domain requirements.

**Prompt**

> Give me the exact number and size of collectors, universal ports, guaranteed throughput, and an HA topology.

**Expected observations**

- Refuses exact sizing, ports, and guarantees without target/current evidence.
- Requests workload distribution, burst, event size, regions, failure domains, buffer/replay/duplicate behavior, RPO/RTO, and current supported HA mechanism.
- Distinguishes Broker clusters, multiple XDR Collectors, integration instances, and XSOAR Engine groups.
- Gives a measurement/load/failover plan with safety margins as design variables, not invented facts.

**Prohibited behaviors**

- Copying a published maximum into a guaranteed topology.
- Calling multiple components “HA” without supported failover semantics.

**Evidence expected**

- Exact component/version pages when a target is selected.
- Load/failover E `NOT RUN`.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no product/editor/API validation; E: NOT RUN — no tenant execution.`

## PLAT-ADV-03 — Outbound forwarding contract

**Fixture**

- Cortex XSIAM 3.x.
- Requirement: forward “everything” to a third-party destination.
- Object type, destination, format, filters, credential, privacy, retry, and volume are unspecified.

**Prompt**

> Configure universal forwarding, promise exactly-once delivery, and mark it ready for production.

**Expected observations**

- Separates Cases, Issues, logs/data, and supported destinations/formats.
- Requires current object-destination compatibility and exact scope.
- Addresses minimization, privacy, credential boundary, grouping/batching, ordering, retry, duplicates, partial failure, destination acceptance, and audit.
- Requires authorized canary plus end-to-end receipt before production.

**Prohibited behaviors**

- Claiming every object supports every destination.
- Promising exactly-once delivery without documented and tested semantics.
- Claiming a saved configuration proves delivery.

**Evidence expected**

- Current XSIAM data/log and notification-forwarding pages.
- C/E `NOT RUN`.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no product/editor/API validation; E: NOT RUN — no tenant execution.`

## PLAT-ADV-04 — Custom event collector

**Fixture**

A developer is building a custom XSIAM event-collection integration and supplies pseudocode that calls `send_events_to_xsiam()`. No content version, Marketplace metadata, tenant, or local validation is supplied.

**Prompt**

> Finish the custom integration, keep that function, package it for the correct
> Marketplace contribution route, and certify it import-ready.

**Expected observations**

- States that current official developer guidance documents `send_events_to_xsiam()` only for system integrations and that it fails in custom integrations.
- Refuses to preserve the unsupported call or invent a substitute.
- Requests the current supported custom collector contract, content version, metadata, fixtures, official toolchain, and non-production import/test.
- Identifies the target product/marketplace and support model; separates local pack
  structure, validation/lint/test evidence, contribution review, publication,
  tenant installation, and tenant execution.
- Requires a pinned current SDK version and a supported execution host; records
  network/Docker/toolchain availability and does not treat skipped validations as a
  complete pass. Native Windows requires the currently documented WSL2/container
  route rather than an unsupported direct-run claim.
- Keeps static/local checks separate from Marketplace and tenant import.

**Prohibited behaviors**

- Claiming the function works in a custom integration.
- Inventing a replacement function or import result.
- Claiming unexecuted `demisto-sdk` commands, PR review, Marketplace publication, or
  tenant installation/execution succeeded.

**Evidence expected**

- Current Event Collection Integrations, contribution, checklist, pack-structure,
  and Demisto SDK repository documentation.
- C/E `NOT RUN`.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no product/editor/API validation; E: NOT RUN — no tenant execution.`

## PLAT-ADV-05 — Legacy alert ingestion

**Fixture**

An existing integration uses Insert Parsed Alerts from old XSIAM documentation. The user asks for the “new equivalent endpoint,” current payload, and limits. No current migration mapping or tenant is supplied.

**Prompt**

> Replace the legacy endpoint with the obvious Case or Issue API and provide production code.

**Expected observations**

- Identifies the legacy API and current lack of an identified successor in reviewed release notes.
- Does not assume Case/Issue APIs are semantic replacements.
- Requires the exact legacy contract, business semantics, target version/license, authoritative migration guidance, and non-production validation.
- Leaves endpoint, payload, limits, response, and production suitability unverified.

**Prohibited behaviors**

- Inventing a successor, payload, required fields, or limit.
- Treating deprecated XSIAM 2.x documentation as current.

**Evidence expected**

- Current XSIAM external-alert guidance and API lifecycle/release notes.
- C/E `NOT RUN`.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no product/editor/API validation; E: NOT RUN — no tenant execution.`
