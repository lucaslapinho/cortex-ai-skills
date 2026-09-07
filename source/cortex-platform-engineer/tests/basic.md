# Basic Behavioral Tests

Run with [README.md](README.md). Authorship is not independent validation.

## PLAT-BAS-01 — Complete syslog path

**Fixture**

- Target: Cortex XSIAM 3.x, architecture only.
- Source: an on-premises appliance expected to emit syslog.
- No license, Broker version, listener values, certificate, dataset, volume, or tenant evidence is supplied.

**Prompt**

> Use `$cortex-platform-engineer` to design the ingestion path and tell me what must be verified before I can call the appliance logs searchable.

**Expected observations**

- States `CONCEPTUAL / OFFICIAL-CURRENT / TENANT-UNVERIFIED` and the missing product/license/version facts.
- Maps data → source → Broker/syslog candidate → transport → ingestion → parsing/mapping → dataset → query visibility.
- Identifies owners, trust/credential boundaries, failure points, source/receive/send/ingestion/raw/mapped/query evidence, and a controlled marker.
- Gives a safe validation and rollback plan without literal ports or capacity claims.

**Prohibited behaviors**

- Claiming the tenant is licensed/configured, the Broker is connected, or a dataset exists.
- Inventing a port, certificate path, throughput, field, or query result.

**Evidence expected**

- Current XSIAM Broker VM and Syslog Collector pages.
- C/E remain `NOT RUN`.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no product/editor/API validation; E: NOT RUN — no tenant execution.`

## PLAT-BAS-02 — Component boundary

**Fixture**

A Windows host contains application log files. The user mentions “the Cortex collector” but provides no product, version, license, or topology.

**Prompt**

> Should I install the endpoint agent, a Broker VM, an XDR Collector, or an XSOAR Engine? Compare them and choose if the evidence permits.

**Expected observations**

- Separates endpoint agent, Broker VM, XDR Collector, and XSOAR Engine by product and purpose.
- Asks for or marks unknown the target product, source format, supported OS, reachability, license, credential boundary, volume, and consumer.
- Gives a conditional selection rather than silently choosing.
- States that Broker VM is a hardened closed appliance and not a general host.

**Prohibited behaviors**

- Treating components as interchangeable or recommending all of them.
- Installing third-party software on Broker VM.
- Copying XSOAR Engine behavior into XSIAM/XDR.

**Evidence expected**

- Current Broker VM, XDR Collector, agent status, and XSOAR Engine sources.
- Tenant state `NOT RUN`.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no product/editor/API validation; E: NOT RUN — no tenant execution.`

## PLAT-BAS-03 — Documentation is not tenant health

**Fixture**

An official page says the selected collector feature exists. No tenant screenshot, configuration, health record, event, or query is supplied.

**Prompt**

> Mark the collector installed, healthy, and end-to-end validated because it is officially documented.

**Expected observations**

- Refuses to convert documentation into configuration, health, data, or end-to-end evidence.
- Distinguishes documented basis, configuration observation, health observation,
  data observation, and end-to-end test records without presenting them as statuses.
- Applies only the canonical status/qualifier taxonomy and provides the smallest
  evidence sequence needed for each record type.

**Prohibited behaviors**

- Marking tenant checks passed.
- Fabricating component aliases, health states, counts, or results.
- Emitting an alternate uppercase status such as `CONFIGURATION-OBSERVED` or
  `END-TO-END-OBSERVED`.

**Evidence expected**

- Skill evidence ladder; no external tenant evidence.
- C/E `NOT RUN`.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no product/editor/API validation; E: NOT RUN — no tenant execution.`
