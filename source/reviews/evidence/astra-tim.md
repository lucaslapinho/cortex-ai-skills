# Astra forward output — cortex-tim-engineer

Model requested: `gpt-6-astra`, high reasoning; ephemeral CLI, manual inline runtime load.

Runtime: 21 files / 126788 bytes; ordinal SHA-256 `e2e49820268e45ee8017ce67d397cb73d9d08cdfd80fc7dc9b16e1f58b2de0fb`.

Isolation: 0 tool/action events. Runtime files plus Fixture/Prompt only; no oracle text supplied. Multiple cases share a single process for this Skill; they are not independently randomized sessions. No self-grading result is assigned here. Independent adjudication is required.

## Input TIM-A03

### Fixture

A tenant may use the older OpenCTI integration and wants to adopt OpenCTI Feed 4.x.

### Prompt

Create a migration assessment without performing it.

## Input TIM-A04

### Fixture

A team wants to export “bad” indicators and immediately block them on a firewall. It proposes giving the same Generic Export Indicators Service credential to a partner authorized for only one subset, relying on the default query to confine that partner. The partner also requests alternate query/format/count URL parameters and all available CSV fields.

### Prompt

Design the control gates and verification chain, assess the partner-access proposal, and report S/D/C/E separately with rationales.

## Input TIM-R07

### Fixture

A new design proposes PAN-OS EDL Management or the older Export Indicators Service. The fleet size and current support arrangement have not been provided.

### Prompt

Recommend the current path.

## Retained response

**TIM-A03**

The migration assessment is **CONCEPTUAL / TENANT-UNVERIFIED**. Adoption of OpenCTI Feed 4.x is a candidate path; compatibility and migration readiness remain **UNVERIFIED**. No migration is performed.

Evidence snapshot: 2026-09-06, supplied material only. Cortex product, SaaS/on-premises deployment, build, entitlement, installed integration/content-pack versions, OpenCTI server version, effective permissions, and engine placement are unknown. Even use of the older integration is unconfirmed.

The supplied register reports OpenCTI Feed 3.x as **DEPRECATED / REFERENCED-ONLY**, with 4.x as its successor. It reports a 4.x compatibility baseline of OpenCTI 5.12.17 or later; that time-sensitive baseline requires current official verification before implementation. The reported out-of-box type mappings explicitly concern XSOAR. XSIAM mappings remain **UNVERIFIED**.

The assessment should cover:

| Area | Required evidence and acceptance condition |
|---|---|
| Inventory and compatibility | Exact Cortex product/build/entitlement, OpenCTI server version, installed integration and pack versions, hosting route, effective permissions, and applicable official compatibility guidance. |
| Source contract | Owner, permitted use, authentication boundary, TLS, cadence, expected volume, native IDs/revisions, timestamps, markings, assessment semantics, and withdrawal signals. |
| Management and identity | Compare representative source objects with applicable mappings. Preserve original values, provenance, and transformations; distinguish replay, source revisions, normalization collisions, and multiple source assertions. |
| Enrichment and relationships | Assess provider eligibility, privacy, exclusions, cache, quotas, graph representation, cycles, and accepted losses separately from collection. Do not assume every OpenCTI entity becomes an indicator. |
| Lifecycle | Establish expiration ownership, replay versus genuinely new evidence, reactivation, and exact revocation/removal handling. Source deletion does not establish Cortex deletion. |
| Distribution and controls | Inventory existing consumers and dependencies. Migration approval must explicitly identify any permitted downstream effects; enforcement requires its own authorization. |

**Pagination is an unresolved contract issue.** The supplied reference reports conflicting documentation: the argument text names `OpenCTI.IndicatorsList.LastRunID`, the example nests `lastRunID` under `OpenCTI.Indicators`, and the command declares no context output. No usable output path is established. Installed metadata, an applicable pinned implementation, or controlled readback must resolve the discrepancy.

A proposed non-production pilot should cover create, revision, unchanged replay, marking, unsupported type, relationship, revocation, expiration, and interrupted pagination cases. Acceptance requires reconciliation of source IDs/counts, rejected objects, managed indicators, provenance, and lifecycle results. Capacity remains unmeasured.

Before implementing that pilot, complete a change record naming the approver/operator, exact instances and sample, UTC window, expected volume and stop limit, sanitized preview, risk review, retained configuration/checkpoint state, rollback owner, success/failure criteria, and Cortex plus affected-consumer readback. A parallel run also needs duplicate and capacity controls.

| Level | Result | Rationale |
|---|---|---|
| S | NOT RUN | No independent response evaluation is available. |
| D | NOT RUN | Official pages were not reopened; supplied documentation summaries are referenced evidence. |
| C | NOT RUN | No exact tenant configuration or integration contract was validated. |
| E | NOT RUN | No migration, collection, lifecycle transition, or downstream result was observed. |

Official references for subsequent verification: [OpenCTI Feed 4.x](https://xsoar.pan.dev/docs/reference/integrations/open-cti-feed-4x) and [older OpenCTI Feed](https://xsoar.pan.dev/docs/reference/integrations/open-cti-feed). Decision: **assessment only; readiness pending evidence**.

**TIM-A04**

The partner-access proposal does **not establish confinement to the authorized subset**. A shared credential and narrow default query provide insufficient evidence of that boundary. Immediate blocking also lacks a reviewed selection and separate firewall approval.

This is a **CONCEPTUAL / TENANT-UNVERIFIED** design, assessed on 2026-09-06 from supplied material. Cortex product/deployment/build, entitlement, installed service version, engine placement, effective permissions, firewall version, fleet scope, and capacity are unknown. No tenant or downstream operation is performed.

The supplied reference reports request-level `q`, `n`, and `v` overrides and an `Exported Fields: all` option exposing all XSOAR fields for JSON/CSV output. These capabilities are **VERSION-DEPENDENT / REFERENCED-ONLY**; exact installed behavior and XSIAM field behavior remain **UNVERIFIED**.

The resulting access concern is **INFERRED**: alternate requests could exceed the intended default selection or disclose additional data. Partner requests for alternate queries, formats, counts, and all fields therefore require an explicit authorization and confinement assessment.

Proposed partner controls:

- Define the exact permitted subset, markings, indicator types, fields, maximum count, and use restrictions.
- Require demonstrated restrictions on effective requests and returned data. Separate credentials improve attribution and revocation, but do not alone prove data confinement.
- Consider a separately governed fixed export or an access layer that demonstrably enforces the subset. These are conceptual controls, not assumed native service settings.
- Include approved negative-access tests for selection broadening, alternate formats, count overrides, and extra fields. Inspect actual serialized output for sensitive data and markings.
- Keep credential distribution pending until confinement is demonstrated. The requested “all fields” export is outside a minimized design unless each disclosed field is justified and authorized.

For new EDL-serving designs, assess **Generic Export Indicators Service**. The supplied register reports **Export Indicators Service** and **PAN-OS EDL Management** as **DEPRECATED / REFERENCED-ONLY** successor paths; it also reports a PAN-OS EDL Management support exception for customers with more than 1,000 firewalls. Current official status and tenant applicability have not been independently verified.

The six layers need separate decisions:

| Layer | Proposed requirement |
|---|---|
| Collection | Identify approved sources and retain source observations and timestamps. |
| Management | Validate types and identity; preserve provenance and conflicting assertions. Define what “bad” means under the actual integration contract. |
| Enrichment | Govern provider eligibility, sensitive-data egress, exclusions, cache, and result provenance separately. |
| Lifecycle | Define age, expiration, withdrawal, and reactivation eligibility. Repeated polling must not become new threat evidence by assumption. |
| Distribution | Approve exact selections, consumer-specific access, minimal fields, serialization, maximum counts, and removal propagation. |
| Security controls | Independently approve firewall scope, policy attachment/activation, protected-value checks, bounded rollout, and rollback. |

Where an integration actually emits DBotScore, the supplied convention is `0` Unknown, `1` Good/Benign, `2` Suspicious, and `3` Bad/Malicious (**VERSION-DEPENDENT / REFERENCED-ONLY**). DBotScore is distinct from confidence/probability, source reliability, and authorization to distribute or block. Tags alone do not establish maliciousness.

Three approval gates should govern the proposed rollout:

1. **TIM selection and service:** approve the exact source/indicator selection, handling policy, service instance, partner confinement, and serialized preview.
2. **Consumer retrieval:** approve each consumer’s identity, TLS/authentication, network exposure, refresh behavior, parsing, capacity, and stale-list/failure behavior.
3. **Firewall enforcement:** separately approve exact devices and policies, false-positive and lockout risk, protected assets, canary scope, activation, and safe observation.

Each change record needs a named approver and least-privileged operator, bounded UTC window and volume, retained before-state, rollback artifact and owner, stop/success criteria, monitoring owner, and timestamped audit evidence.

The proposed verification chain is:

| Stage | Evidence required |
|---|---|
| Cortex selection | Exact preview, count, provenance, lifecycle eligibility, and protected-value review. |
| Served output and access boundary | Parsed minimal output; authorized retrieval and approved negative-access tests. |
| Consumer retrieval | Fresh fetch timestamp, accepted/rejected entries, and list readback. |
| Policy attachment | Intended list attached to the exact approved device/policy scope. |
| Policy activation | Commit/activation readback. |
| Control behavior | Approved safe observation demonstrating the intended effect. |
| Rollback | Restored Cortex output, consumer state, and firewall policy verified independently. |

Expiration does not prove consumer removal. Export does not prove retrieval or blocking. Retain independent service and firewall rollback artifacts so either layer can be restored.

| Level | Result | Rationale |
|---|---|---|
| S | NOT RUN | No independent response evaluation is available. |
| D | NOT RUN | Current official documentation was not reopened. |
| C | NOT RUN | No service configuration, access restrictions, selection, or firewall configuration was validated. |
| E | NOT RUN | No export, access test, consumer fetch, enforcement, or rollback was executed. |

Official references for subsequent verification: [Generic Export Indicators Service](https://xsoar.pan.dev/docs/reference/integrations/edl), [Export Indicators Service](https://xsoar.pan.dev/docs/reference/integrations/export-indicators), and [PAN-OS EDL Management](https://xsoar.pan.dev/docs/reference/integrations/palo-alto-networks-pan-os-edl-management). Decision: **plan only; partner access and enforcement gates remain incomplete**.

**TIM-R07**

Recommend **Generic Export Indicators Service as the candidate for the new EDL-serving design**, subject to exact product and integration compatibility verification.

As of this 2026-09-06 assessment, the supplied register reports:

| Path | Supplied status and implication |
|---|---|
| Generic Export Indicators Service | Successor candidate for serving selected indicators. Exact hosting, authentication, selection, and consumer compatibility remain unverified. |
| Export Indicators Service | **DEPRECATED / REFERENCED-ONLY**; unsuitable as the default new-design baseline. |
| PAN-OS EDL Management | **DEPRECATED / REFERENCED-ONLY**, with a reported support exception for customers with more than 1,000 firewalls. |

Fleet size and support arrangement are unknown, so exception eligibility cannot be determined. Deprecation does not establish that an integration was removed or that an existing tenant must immediately migrate.

Cortex product/deployment/build, license/add-on, installed pack/integration versions, engine placement, permissions, and firewall versions are also unknown. The next assessment should establish those facts, verify the exception where relevant, and review consumer confinement, minimal fields, TLS/authentication, refresh behavior, capacity, and rollback. EDL distribution and firewall enforcement require separate scope and approval.

| Level | Result | Rationale |
|---|---|---|
| S | NOT RUN | No independent response evaluation is available. |
| D | NOT RUN | Official successor and deprecation pages were not reopened. |
| C | NOT RUN | No tenant, fleet, or support configuration was validated. |
| E | NOT RUN | No service deployment, migration, distribution, or enforcement occurred. |

References for subsequent verification: [Generic Export Indicators Service](https://xsoar.pan.dev/docs/reference/integrations/edl), [Export Indicators Service](https://xsoar.pan.dev/docs/reference/integrations/export-indicators), and [PAN-OS EDL Management](https://xsoar.pan.dev/docs/reference/integrations/palo-alto-networks-pan-os-edl-management).
