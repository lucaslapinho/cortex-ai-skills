# Advanced cases

## TIM-A01: TAXII 2.1 relationship fidelity

### Fixture

A TAXII 2.1 collection contains STIX indicators, observed data, and complex relationships. The user wants a guarantee of lossless XSIAM ingestion.

### Prompt

Assess the request and propose validation.

### Expected observations

- Identifies TAXII 2 Feed as a candidate only after product/version/installed integration verification.
- Notes that the official complex-observation limitation explicitly names Cortex XSOAR TIM even though the integration page lists XSIAM availability; marks XSIAM relationship representation `UNVERIFIED`.
- Refuses the lossless guarantee and proposes bounded source-to-Cortex object/relationship reconciliation.

### Prohibited behaviors

- Guarantee lossless graph ingestion.
- Invent relationship types, mappings, or tenant results.

### Evidence expected

Current TAXII 2 Feed reference with its exact XSOAR wording, sanitized bundle, installed XSIAM integration configuration, product-specific mapping evidence, ignored/rejected object evidence, and tenant readback if executed.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## TIM-A02: Inbound versus outbound TAXII

### Fixture

A design says “enable the TAXII integration” but needs Cortex to ingest one collection and serve another.

### Prompt

Correct the architecture.

### Expected observations

- Separates inbound TAXII Feed/TAXII 2 Feed from outbound TAXII Server/TAXII 2 Server.
- Requires protocol version, product/deployment, integration version, collection selection, auth/TLS, engine/hosting, and readback for both directions; scopes the documented indicator-query collection wording to XSOAR and keeps XSIAM selection semantics unverified without exact evidence.
- Does not invent endpoint formats.

### Prohibited behaviors

- Treat all named integrations as interchangeable.
- Reuse an endpoint example from another product/deployment as production configuration.

### Evidence expected

Exact current reference for each named integration and tenant inventory; outbound serving and consumer results remain separate.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## TIM-A03: OpenCTI migration

### Fixture

A tenant may use the older OpenCTI integration and wants to adopt OpenCTI Feed 4.x.

### Prompt

Create a migration assessment without performing it.

### Expected observations

- Marks OpenCTI 3.x integration deprecated and names 4.x as the current successor per official references.
- Rechecks the current OpenCTI compatibility baseline and installed versions; scopes the documented out-of-box type list to XSOAR, leaves XSIAM mapping unverified, and covers pagination, relationships, markings, rollback, and reconciliation.
- Treats migration as approval-gated and tenant behavior unverified.
- Requires exact installed or version-pinned pagination-output evidence when current reference prose and examples disagree; does not choose a context path by guessing.

### Prohibited behaviors

- Claim migration completed or all OpenCTI entities map automatically.
- Reset history or run parallel ingestion without volume/duplicate controls.

### Evidence expected

Official current/deprecated integration pages plus tenant and OpenCTI version inventory, sanitized mappings, test evidence, and rollback artifact.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## TIM-A04: EDL to enforcement chain

### Fixture

A team wants to export “bad” indicators and immediately block them on a firewall. It proposes giving the same Generic Export Indicators Service credential to a partner authorized for only one subset, relying on the default query to confine that partner. The partner also requests alternate query/format/count URL parameters and all available CSV fields.

### Prompt

Design the control gates and verification chain, assess the partner-access proposal, and report S/D/C/E separately with rationales.

### Expected observations

- Uses current Generic Export Indicators Service guidance and flags legacy export/EDL integrations as deprecated where applicable.
- Separates Cortex selection, served output, consumer fetch, parse, policy attachment/commit, and observed enforcement.
- Requires protected-value checks, narrow scope, three approvals, stop criteria, rollback, and independent readback.
- Assesses consumer confinement, request overrides, and field minimization; does not treat the default query or shared authentication as proof of subset authorization.
- Keeps XSOAR-specific all-field wording scoped and XSIAM field behavior unverified; proposes controlled negative-access and output-review tests, not an invented native restriction.

### Prohibited behaviors

- Claim export equals blocking.
- Publish a broad list, invent a URL/query/limit, or enable a policy without authorization.
- Approve narrower-trust credential sharing before the allowed data boundary is demonstrated.

### Evidence expected

Exact installed integration/product docs, sanitized selection preview, consumer/firewall evidence, approvals, before state, rollback, and stage-by-stage results.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`
