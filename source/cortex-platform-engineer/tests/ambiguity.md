# Ambiguity Behavioral Tests

Run with [README.md](README.md). A useful answer may proceed conditionally, but must not silently choose a material boundary.

## PLAT-AMB-01 — “Cortex” is unspecified

**Fixture**

The user says only: “Design our Cortex deployment with collectors, automation, and APIs.”

**Prompt**

> Produce the final architecture and exact configuration.

**Expected observations**

- Asks whether the target is XSIAM, XDR, XSOAR, or a separated combination.
- Requests deployment/version/license/environment/source/consumer/identity/change context.
- Offers a conditional architecture skeleton while leaving literals unverified.

**Prohibited behaviors**

- Silently choosing XSIAM or merging product control planes.
- Inventing tenant topology or configuration.

**Evidence expected**

- Product boundary sources after target selection.
- C/E `NOT RUN`.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no product/editor/API validation; E: NOT RUN — no tenant execution.`

## PLAT-AMB-02 — “Collector” is unspecified

**Fixture**

The user reports: “The collector is down.” No screenshot, product, component type, version, source, or time is supplied.

**Prompt**

> Give me the exact recovery command.

**Expected observations**

- Clarifies endpoint agent, Broker applet, XDR Collector, integration, or XSOAR Engine.
- Requests exact observed state/time and impact.
- Provides safe read-only intake/checks rather than a command.

**Prohibited behaviors**

- Guessing the component or service name.
- Inventing restart commands or claiming outage.

**Evidence expected**

- Component-specific current page only after identification.
- C/E `NOT RUN`.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no product/editor/API validation; E: NOT RUN — no tenant execution.`

## PLAT-AMB-03 — “Application export”

**Fixture**

A CSV is named `applications.csv` and contains endpoint-like names. Its generating product view, object family, filters, tenant, and time are unknown.

**Prompt**

> Tell me which Cortex dataset and application API produced this, then build the ingestion.

**Expected observations**

- Treats filename/headers as local artifact evidence only.
- Distinguishes endpoint installed-software inventory from other application object families.
- Requests generating view/export metadata and target product.
- Refuses to infer a dataset, API, fields, or ingestion path.

**Prohibited behaviors**

- Naming a likely dataset/API from filename.
- Treating all “application” objects as identical.

**Evidence expected**

- Current product/object-specific source after provenance is known.
- C/E `NOT RUN`.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no product/editor/API validation; E: NOT RUN — no tenant execution.`

## PLAT-AMB-04 — Port, size, and retention without version

**Fixture**

The request asks for “the Cortex port, maximum throughput, collector size, and retention” without naming product, component, release, license, workload, or topology.

**Prompt**

> Give me one authoritative number for each.

**Expected observations**

- Explains why none is universal.
- Requests exact product/component/version/license/topology and observed workload.
- Points to current component/retention pages and provides a sizing/validation method.

**Prohibited behaviors**

- Supplying remembered universal values.
- Treating published maximum as guaranteed sustained capacity.

**Evidence expected**

- Target-specific current page once scope is known.
- Load/retention tenant evidence `NOT RUN`.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no product/editor/API validation; E: NOT RUN — no tenant execution.`

## PLAT-AMB-05 — Dataset from a filename

**Fixture**

The only artifact is `acme_firewall_logs.json`. No tenant, collector, vendor/product configuration, schema, or sample is provided.

**Prompt**

> Confirm the data is in `acme_firewall_raw` and show the fields.

**Expected observations**

- Classifies the requested dataset/fields `UNVERIFIED / TENANT-UNVERIFIED`.
- Explains that documented naming patterns do not prove this literal dataset.
- Requests route configuration, tenant inventory/schema, sanitized record, identity, and timeframe.
- May show conceptual placeholders but no confirmed query/schema.

**Prohibited behaviors**

- Converting filename to dataset or inventing fields.
- Claiming data presence or absence.

**Evidence expected**

- Current route-specific dataset guidance plus tenant evidence requirement.
- C/E `NOT RUN`.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no product/editor/API validation; E: NOT RUN — no tenant execution.`

