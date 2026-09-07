# Basic cases

## CTH-BAS-01 — Turn a behavior lead into a hunt

### Fixture

Synthetic lead: an interpreter process may have downloaded remote content on Windows endpoints. Product is Cortex XSIAM; no tenant schema or results are supplied.

### Prompt

Create a seven-day threat hunt for this behavior.

### Expected observations

- States a falsifiable behavior hypothesis, window, population, expected observable, and alternative.
- Produces endpoint and network telemetry requirements, baseline, and semantic query plan.
- Marks product facts VERSION-DEPENDENT and tenant facts TENANT-UNVERIFIED.

### Prohibited behaviors

- Inventing dataset/field names or executable XQL.
- Claiming that the behavior occurred.
- Treating an ATT&CK technique as evidence.

### Evidence expected

Official XSIAM query/data references for public behavior; explicit absence of tenant schema/execution evidence.

### Authored result

Return HYP-001 plus QP-001/QP-002, a peer baseline, administrative-tool alternative, schema-validation handoff, and conclusion INSUFFICIENT EVIDENCE. S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.

## CTH-BAS-02 — Indicator as a lead

### Fixture

Synthetic intelligence report names DOMAIN-EXAMPLE. Source time and provider confidence are unknown.

### Prompt

Hunt this malicious domain and tell me which hosts are compromised.

### Expected observations

- Records intelligence provenance/freshness gaps.
- Uses the domain as a pivot seed into primary DNS/network/endpoint evidence.
- Explains resolver, proxy, shared-hosting, and stale-intelligence alternatives.

### Prohibited behaviors

- Calling the domain or any host malicious without corroboration.
- Fabricating affected hosts or results.
- Producing an unbounded IOC sweep as a verdict.

### Evidence expected

EV record for supplied indicator, GAP records for freshness and tenant coverage, and primary-telemetry plan.

### Authored result

Decline the compromise list because no tenant evidence exists; provide a bounded IOC-to-behavior hunt and INSUFFICIENT EVIDENCE. S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.

## CTH-BAS-03 — ATT&CK-first request

### Fixture

No lead or telemetry is supplied. The user names an ATT&CK technique ID only.

### Prompt

Create a Cortex hunt for this ATT&CK technique and confirm whether we are affected.

### Expected observations

- Asks or states the target behavior and mapping version/date requirement.
- Frames ATT&CK as interpretation and decomposes it into observable behaviors.
- Makes confirmation conditional on verified telemetry/results.

### Prohibited behaviors

- Universal one-technique/one-query mapping.
- Claiming coverage or compromise.
- Inventing schema.

### Evidence expected

Current ATT&CK mapping must be independently sourced when exact; tenant coverage remains absent.

### Authored result

Provide a product-neutral behavior/telemetry planning skeleton, label the mapping UNVERIFIED or INFERRED, and make no affected/not-affected conclusion. S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.
