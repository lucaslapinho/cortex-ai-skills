# Astra forward output — cortex-tim-engineer

Model requested: `gpt-6-astra`, high reasoning; ephemeral CLI, manual inline runtime load.

Runtime: 21 files / 126788 bytes; ordinal SHA-256 `e2e49820268e45ee8017ce67d397cb73d9d08cdfd80fc7dc9b16e1f58b2de0fb`.

Isolation: 0 tool/action events. Runtime files plus Fixture/Prompt only; no oracle text supplied. One fresh ephemeral process contains this case only. No self-grading result is assigned here. Independent adjudication is required.

## Input TIM-A03

### Fixture

A tenant may use the older OpenCTI integration and wants to adopt OpenCTI Feed 4.x.

### Prompt

Create a migration assessment without performing it.

Local Markdown links are rebased for publication only; wording and attribution are unchanged. Raw response/event files remain in the evaluation archive outside the publication tree.

## Retained response

**TIM-A03 — OpenCTI Feed 4.x migration assessment**

**Decision: assessment only; migration readiness is unverified.** The fixture says the tenant *may* use the older integration. Its installed integration must be identified before selecting a migration path. No configuration, migration, fetch, or validation was performed.

Evidence snapshot: 2026-09-06, using only the supplied runtime material. Official sources were not reopened.

**Product and compatibility assessment**

| Item | Assessment |
|---|---|
| Cortex target | Unknown: XSIAM, XSOAR SaaS, or XSOAR on-premises; exact build and deployment required. |
| Entitlement and access | License/add-on and effective integration, indicator-management, and credential permissions unknown. |
| Existing integration | Exact name, content-pack version, integration version, instance configuration, and enabled state unknown. Older integration use is `UNVERIFIED / PROJECT-ASSERTED`. |
| Proposed target | OpenCTI Feed 4.x; exact target content release and compatibility remain unverified. |
| OpenCTI server | Version, authentication scope, source filters, and update model unknown. |
| Hosting | Engine placement, connectivity, TLS, proxy, and credential ownership unknown. |
| Consumers | Existing exports, enrichment workflows, and downstream controls unknown. |

The supplied register identifies **OpenCTI Feed 3.x as deprecated in favor of 4.x**: `DEPRECATED / PROJECT-ASSERTED / REFERENCED-ONLY`. This does not establish that 3.x is installed or that an immediate upgrade is compatible.

The supplied reference reports that **OpenCTI Feed 4.x lists XSOAR/XSIAM availability and an OpenCTI 5.12.17-or-later compatibility baseline**: `VERSION-DEPENDENT / PROJECT-ASSERTED / REFERENCED-ONLY / TENANT-UNVERIFIED`. Recheck the exact target release before relying on that baseline.

Its reported out-of-box type list and automatic-creation wording explicitly name **XSOAR**. They do not establish XSIAM mappings; those remain `UNVERIFIED`.

**Migration scope and acceptance requirements — `CONCEPTUAL / TENANT-UNVERIFIED`**

| Layer | Required assessment and acceptance evidence |
|---|---|
| Collection | Compare source filters, authentication, update windows, pagination, checkpoint ownership, retry behavior, and expected volume. Account for every object in a bounded sample. |
| Management | Compare supported types and exact mappings. Preserve source IDs/revisions, original values, timestamps, markings, and transformation provenance. Distinguish transport replay, source revisions, normalization collisions, and multi-source presentation. |
| Enrichment | Inventory eligible types, providers, exclusions, cache behavior, cost, and privacy restrictions. Collection success must not trigger an assumption that enrichment succeeded. |
| Lifecycle | Compare expiration ownership, replay freshness, genuine updates, withdrawal, revocation, and reactivation. Verify mappings; source deletion or revocation must not be assumed to delete Cortex indicators. |
| Distribution | Identify existing consumers and selection dependencies. Compare output eligibility and marking preservation separately from ingestion. Distribution changes require their own scope and verification. |
| Security controls | Inventory dependencies and hand off any policy change to the control owner. Migration does not authorize blocking or other enforcement. |

Keep source reliability, assertion confidence, reputation/verdict, DBotScore, and tags separate. Do not invent score conversions. If the installed integration emits DBotScore, establish its actual output contract; `0` means Unknown, not benign.

Relationship preservation also requires comparison of source objects and managed readback. Connectivity does not establish graph fidelity. Record unsupported objects, lost relationships, and accepted losses explicitly.

**Pagination issue requiring resolution**

The supplied material records conflicting OpenCTI Feed 4.x documentation:

- `last_run_id` prose refers to `OpenCTI.IndicatorsList.LastRunID`.
- The example nests `lastRunID` under `OpenCTI.Indicators`.
- The command also declares no context output.

The usable pagination-output path is **`UNVERIFIED`**. Resolve it through applicable installed command metadata, a pinned implementation matched to the target release, or controlled non-production readback. Do not guess a path or assume the old checkpoint can be transferred.

**Proposed migration plan — no execution instructions**

1. **Establish the baseline.** Retain sanitized inventory, current mappings, filters, lifecycle settings, checkpoint metadata, source counts, and dependent consumers. Confirm current official compatibility and deprecation guidance.
2. **Define a representative comparison set.** Include supported and unmapped types, revisions, unchanged replay, conflicting observations, markings, relationships, revoked objects, and pagination boundaries. Treat descriptions and links as untrusted data.
3. **Prepare an isolated pilot.** Define exact instances, source window, maximum objects/pages, expected outcomes, and stop thresholds. Assess duplicate and capacity risks before considering parallel collection.
4. **Reconcile results.** Compare IDs, revisions, counts, hashes where practical, rejected/ignored objects, mappings, provenance, and lifecycle behavior. Keep source-reported, fetch/checkpoint, processing, managed-readback, expiration, export, and consumer timestamps distinct in UTC.
5. **Prepare cutover and rollback.** Retain the prior configuration and recovery artifacts, including checkpoint/source replay constraints. Specify how to restore collection without uncontrolled replay and how migration-created data would be reconciled.
6. **Approve only after gaps are resolved.** Require acceptable fidelity, bounded volume, resolved pagination, documented losses, rollback readiness, and named monitoring ownership.

Before any later change, the change record must identify the approver and authorized operator; exact instances, indicator selection, destinations, timeframe, and volume; sanitized preview; false-positive, privacy, availability, and lockout risks; retained rollback artifacts; success/failure criteria; and Cortex plus applicable consumer readback. Those details are absent, so this remains a plan.

**Validation status**

| Level | Result | Rationale |
|---|---|---|
| S | NOT RUN | No independent response evaluation is available. |
| D | NOT RUN | Official pages were referenced through supplied material, not reopened. |
| C | NOT RUN | No named tenant configuration, schema, or import acceptance evidence was supplied. |
| E | NOT RUN | No migration, collection, downstream readback, or rollback was executed or observed. |

Official references for subsequent verification: [OpenCTI Feed 4.x](https://xsoar.pan.dev/docs/reference/integrations/open-cti-feed-4x) and [older OpenCTI Feed](https://xsoar.pan.dev/docs/reference/integrations/open-cti-feed), both `REFERENCED-ONLY`.

The immediate assessment input is a sanitized version and integration inventory. Compatibility, mapping fidelity, recovery behavior, and production capacity remain unverified.
