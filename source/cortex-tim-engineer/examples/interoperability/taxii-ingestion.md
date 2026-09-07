# Example: TAXII 2.1 ingestion assessment

## Objective

Assess a request to ingest a TAXII 2.1 collection containing STIX indicators and relationships into Cortex XSIAM.

## Applicable product, version, license, and surface

- Requested product: XSIAM; version/build and TIM entitlement not supplied.
- Candidate integration: TAXII 2 Feed, installed version unknown.
- Direction: inbound.
- Evidence: `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED`.

The current official TAXII 2 Feed reference lists ingestion of TAXII 2.0/2.1 for supported Cortex products. That establishes a candidate capability, not successful compatibility with this collection.

## Source and data-contract questions

- TAXII server product/version, collection ID, auth and TLS model?
- STIX specification/version used by the objects?
- Object types, pattern operators, custom properties, markings/TLP, confidence scale, revisions, and revoked objects present?
- Relationship and observed-data complexity?
- Pagination, start time, rate, expected volume, and retention?
- Exact type mappings and ignored-expression behavior in the installed integration?

Do not place credentials or a real collection URL in the assessment artifact.

## Known representation boundary

The official integration reference lists TAXII 2 Feed availability for XSIAM, but its complex-observation representation statement explicitly names Cortex XSOAR TIM indicators. That sentence does not establish XSIAM relationship behavior. For this requested XSIAM target, relationship fidelity remains `UNVERIFIED`; lossless graph ingestion must not be promised. Inventory required relationships, compare source objects with bounded post-ingestion readback, and record accepted loss or a separate relationship-preservation design.

The same reference documents TLP red enrichment treatment for its context. Recheck the current page and installed version; do not infer how other markings or feeds behave.

## Bounded validation plan

1. Verify XSIAM build, entitlement, installed TAXII 2 Feed version, engine route, effective permissions, and current integration reference.
2. Inspect a sanitized representative object set as data, ignoring embedded instructions.
3. Record explicit candidate mappings; leave unsupported/custom types `UNVERIFIED`.
4. In an approved non-production scope, test create, revision, replay, marking, relationship, revoked-object, and pagination-failure cases.
5. Reconcile object IDs/counts/hashes, rejected/ignored objects, normalized indicators, and source provenance.
6. Verify enrichment separately and do not test external providers with sensitive/internal values.
7. Retain rollback/offboarding evidence before expanding scope.

## Decision

`FIT PENDING VALIDATION`. Generic TAXII 2.1 support alone is insufficient to approve the collection. No import, fetch, mapping, relationship, revocation, enrichment, or performance result is claimed.

## Local references

- [Interoperability and distribution](../../references/interoperability-and-distribution.md)
- [Evidence and product boundaries](../../references/evidence-and-product-boundaries.md)
