# Example: Legacy External Alert-Ingestion Migration

## Objective

Assess a request to migrate an existing Insert Parsed Alerts integration to a “new Platform API.”

## Product and evidence

- Product: Cortex XSIAM.
- Existing target version/artifact: not supplied.
- Status: `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED`.

Current XSIAM administrative guidance still discusses external alert ingestion. Current XSIAM Platform API release notes list Insert Parsed Alerts as a legacy Alert API without an identified successor and identify XSIAM 2.x API documentation as deprecated/unmaintained.

Sources: [Ingest external alerts](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Ingest-external-alerts) and [legacy APIs without identified successors](https://cortex-docs.paloaltonetworks.com/xsiam-api/api-release-notes#legacy-apis-without-identified-successor-apis).

## Finding

No current official evidence in the reviewed sources identifies a direct Platform API successor for this legacy operation. It would be unsafe to invent an endpoint, map it automatically to a Case/Issue API, or reuse an old payload/limit as current.

## Migration evidence required

- exact current integration code and legacy endpoint;
- version-pinned legacy API schema and response behavior;
- business semantics: external alert insertion, Case/Issue creation, or another outcome;
- current tenant version/license;
- vendor support or current official migration guidance;
- data classification and required fields;
- retry/idempotency and duplicate behavior;
- non-production test tenant;
- fallback, monitoring, and cutover/rollback owner.

## Safe next step

Create a semantic contract for the current workflow, open a product-specific migration question with authoritative support, and test only a documented candidate in non-production. Preserve legacy literal identifiers in the compatibility layer, while using Case/Issue terms in new prose.

## Validation

No endpoint, payload, role, limit, request, import, or tenant result is supplied. C/E remain `NOT RUN`.

