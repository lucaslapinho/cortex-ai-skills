# Cortex Ecosystem Map

**Research cut:** 2026-09-04  
**Scope:** Cortex XDR, Cortex XSIAM, Cortex XSOAR, Threat Intelligence Management (TIM), shared ingestion/content-development surfaces, and Cortex Cloud as an explicit boundary-only contrast  
**Authority:** Current Palo Alto Networks documentation takes precedence over project material for product behavior.

## Purpose

This map defines the product and engineering surfaces that the seven standalone Skills must reason about. It is a development artifact, not a runtime dependency. Exact tenant datasets, fields, licenses, enabled modules, integrations, permissions, retention, and UI behavior must still be verified in the target environment.

## Evidence classes

Use a canonical claim class plus separate provenance/validation qualifiers. For example, `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED` means the general syntax or behavior is documented but its availability or data population was not checked in a tenant. `LOCAL-VERIFIED` and `PROJECT-ASSERTED` describe evidence provenance; they never promote a product claim by themselves.

| Class | Use in this repository |
|---|---|
| `VERIFIED` | Supported by current official Palo Alto Networks documentation or an official repository/reference reviewed at this research cut. |
| `VERSION-DEPENDENT` | Official behavior exists, but product version, edition, license, deployment model, or migration state changes applicability. |
| `INFERRED` | A bounded conclusion follows from verified evidence but is not stated directly by the source; identify the inference and alternatives. |
| `CONCEPTUAL` | An engineering pattern rather than an executable product artifact. |
| `UNSUPPORTED` | Current official material says the behavior is unsupported or unavailable. |
| `DEPRECATED` | Official material identifies the capability, interface, or documentation as deprecated/legacy. |
| `UNVERIFIED` | Evidence is insufficient; the Skill must not fill the gap by guessing. |

The seven canonical classes above are mandatory in Skill outputs. Apply separate provenance/validation qualifiers without treating them as claim classes:

| Qualifier | Use in this repository |
|---|---|
| `OFFICIAL-CURRENT` | Current first-party documentation was reviewed. |
| `OFFICIAL-EXAMPLE` | A first-party example or repository was reviewed; pin a revision before reuse. |
| `LOCAL-VERIFIED` | The local bytes or structure were directly inspected. |
| `PROJECT-ASSERTED` | Project material makes the claim, but the underlying implementation/runtime evidence is absent. |
| `DERIVATIVE` | The material summarizes another source and is not independent corroboration. |
| `REFERENCED-ONLY` | A source is named or hashed, but its bytes are unavailable. |
| `TENANT-UNVERIFIED` | Tenant schema, configuration, permission, installed content, or runtime behavior was not checked. |
| `TENANT-SCHEMA-VERIFIED` | Dataset, field, and type availability was observed in the named tenant and review date. |
| `TENANT-COMPILED` | The named tenant accepted the query or artifact syntax. |
| `TENANT-EXECUTED` | The query or artifact executed under recorded scope and timeframe. |

Research shorthand such as `CURRENT-OFFICIAL` maps to this two-dimensional model as defined in `architecture-decisions.md`.

## Product map

| Product or surface | Current role | Principal engineering objects | Important boundaries | Primary Skills |
|---|---|---|---|---|
| Cortex XDR | Endpoint detection, investigation, response, and analytics, with capabilities varying by edition and license. | Endpoints, Cases and Issues in Cortex XDR 5, legacy-compatible Incident/Alert identifiers where documented, endpoint telemetry, datasets, XQL, response actions, APIs. | Cortex XDR 5 changed user-facing terms from Incidents/Alerts to Cases/Issues while compatible technical surfaces can retain old identifiers. Do not assume every XSIAM automation, TIM, ingestion, or RBAC feature exists identically in XDR. | XQL, detection, threat hunter, platform, security |
| Cortex XSIAM | Converged security operations platform integrating data, analytics, Case/Issue management, automation, and licensed modules. | Cases, Issues, Insights, Findings, correlation rules, XQL, datasets, playbooks, scripts, integrations, jobs, assets, indicators. | XSIAM 3 uses Cases and Issues in user-facing terminology, while compatible technical identifiers and APIs can retain legacy Incident/Alert names. Edition, add-ons, and RBAC matter. | all seven |
| Cortex XSOAR | Security orchestration, automation, and response platform, with cloud/on-premises and version distinctions. | Incidents or product-version equivalents, playbooks, sub-playbooks, automations/scripts, integrations, commands, context data, War Room, jobs, content packs. | Never transpose XSIAM Case/Issue context paths or XSIAM-only collection helpers into XSOAR without official, version-specific evidence. | playbook, TIM, platform, security |
| Cortex Cloud (boundary-only) | Separately documented cloud security platform whose release notes can reuse labels also seen elsewhere. | Only the currently evidenced surfaces: Data Sources/Integrations management and RBAC/SBAC permissions. | A08/C15 are retained only to prevent cross-product leakage. They do not establish Cortex Cloud Case/Issue, posture/runtime, or XQL object mappings, and their changes do not supersede XSIAM, XDR, or XSOAR documentation. | platform and security boundary checks; no dedicated Skill in this release |
| Threat Intelligence Management | Licensed intelligence lifecycle capability available in relevant Cortex deployments. | Indicators, feeds, source reliability, reputation, confidence, tags, deduplication, enrichment, expiration, TAXII/STIX/MISP integrations, EDL distribution. | Generic protocol support does not prove identical product behavior. TIM licensing, RBAC, integration versions, scoring, expiration, and downstream enforcement must be verified. | TIM, playbook, threat hunter, detection, platform, security |
| Cortex data ingestion | Telemetry and alert collection through supported agents, collectors, Broker VM applets/integrations, APIs, and vendor-specific mechanisms. | Sources, transport, collectors, parsing/mapping, datasets, schemas, health/status, authentication. | Architecture guidance is not configuration proof. Do not invent ports, sizing, applet compatibility, API parameters, or dataset names. | platform, XQL, detection, threat hunter, security |
| Cortex content development | Development and validation of integrations, scripts, playbooks, lists, layouts, and other supported pack entities. | `Packs/<PackName>/...`, metadata, YAML/JSON/Python content, tests, release notes, `demisto-sdk`. | Current contribution layout differs from historical/custom exports. Native Windows is not a supported `demisto-sdk` development environment; use an officially supported environment such as WSL2/container when applicable. | playbook, platform, security |

## Shared operational model

The ecosystem is best treated as connected but non-identical engineering layers:

```text
Security requirement
  -> product and license boundary
  -> telemetry/source prerequisites
  -> ingestion, parsing, mapping, and dataset visibility
  -> XQL investigation or hunt
  -> detection/correlation decision
  -> Case/Issue or product-specific investigation object
  -> enrichment and intelligence lifecycle
  -> playbook decision and approval gates
  -> response action
  -> post-action verification and evidence
```

Each arrow is a validation boundary. A downstream Skill must not silently treat the output of an earlier layer as proven.

## Object and terminology boundaries

| Concept | Verified interpretation | Guardrail |
|---|---|---|
| Case / Incident | Cortex XDR 5 explicitly documents **Case** as the current user-facing term formerly called **Incident**. Current XSIAM documentation uses Case, and XSIAM API migration notes map legacy Incident workflows to the Cases service. Compatible APIs, fields, context commands, and exports may retain `incident` identifiers. | Preserve a working legacy technical identifier when required; label its product/version. Do not mechanically rename executable content. |
| Issue / Alert | Cortex XDR 5 explicitly documents **Issue** as the current user-facing term formerly called **Alert**. Current XSIAM documentation uses Issue, and XSIAM API migration notes map legacy Alert workflows to the Issues service. | Identify product/version and object type before selecting fields, API endpoints, datasets, or playbook context. |
| Insight | In current XSIAM documentation, an Insight is an Issue that did not meet Case-promotion criteria. | Do not define Insight solely as output from Analytics/BIOC or from a detector type. |
| Finding | A Finding describes current asset state, posture, behavior, exposure, or vulnerability; policy/rule logic can generate a related Issue. | Do not model a Finding as a nested subtype of Issue or imply identity-preserving promotion. |
| XQL dataset | A query source whose existence and schema depend on product, integrations, configuration, and permissions. Dataset queries can use the tenant's built-in/default dataset, commonly `xdr_data`; XDM queries require mapped data. | Never fabricate a dataset or field. Validate in current official docs and, for execution, in tenant schema/autocomplete or a bounded probe. |
| Playbook context | Product/version-specific key-value data accessed through documented paths. In current XSIAM guidance, Issue context and parent Case context/fields use distinct namespaces. | Separate sub-playbook context is data scope, not an authorization or confidentiality boundary. Define explicit inputs/outputs and do not rely on global sharing as a shortcut. |
| Indicator score | A source- and integration-dependent intelligence assessment. DBotScore officially distinguishes `0 Unknown`, `1 Good`, `2 Suspicious`, and `3 Bad`. | Never collapse `0` into benign or use one score alone for destructive action. |

## XQL and analytics surface

`cortex-xql-query-engineer` owns executable query construction and validation. `cortex-detection-engineer` owns whether query logic should become a production signal and how it is tuned. `cortex-threat-hunter` owns iterative hypothesis testing and pivots.

Verified guardrails for all three:

- XQL is stage-oriented and uses pipe-delimited processing.
- Dataset and XDM query forms have different source-selection expectations.
- Dataset names, fields, presets, parsing, mappings, and permissions are tenant-sensitive.
- Small timeframes, early selective filters, early field reduction, and explicit limits are recommended.
- Result limits vary by execution context; a Skill must cite the applicable context instead of universalizing one limit.
- Correlation-rule logic must be selective; current official guidance states automatic disablement at 5,000 or more hits in 24 hours.
- Forensic-storage data requires explicit consideration and is not silently included in every query.

No accessible project artifact contains a saved XQL query or tenant schema. All concrete query fields beyond officially documented examples remain `TENANT-UNVERIFIED` until probed.

## Automation surface

`cortex-playbook-engineer` owns design of playbooks, tasks, sub-playbooks, context contracts, integrations, retries, fallback, idempotency, approval, and evidence. It must classify every deliverable as one of:

- `CONCEPTUAL`
- `CONFIGURATION GUIDANCE`
- `VERIFIED IMPORTABLE ARTIFACT`

The last classification requires the exact exported artifact, target product/version, dependencies, command schemas, formatting/validation evidence, and an appropriate tenant test. None of the accessible project summaries alone meets that bar.

Actions such as endpoint isolation, account disablement, IOC blocking, process termination, network changes, file deletion, or user revocation require confidence, scope, permission, blast-radius, approval/policy, rollback or recovery, and post-action verification controls.

## Ingestion and platform surface

`cortex-platform-engineer` traces missing telemetry through:

```text
Expected data
  -> source generation
  -> agent / collector / integration / Broker VM path
  -> transport and authentication
  -> ingestion health
  -> parsing and mapping
  -> dataset/schema visibility
  -> RBAC and query access
```

The Skill may propose a validation plan without inventing exact settings. Broker VM applets, collector support matrices, ports, sizing, authentication, datasets, and integration parameters require current official evidence for the stated product/version.

Two ingestion cautions from the accessible material and official reconciliation are mandatory:

1. `send_events_to_xsiam()` is documented for XSIAM system integrations and fails from custom integrations; it is not a generic public-ingestion shortcut.
2. `POST /public_api/v1/alerts/insert_parsed_alerts` remains referenced by current administration guidance, but current API release notes classify it as a legacy XSIAM 2.x API without an identified Platform successor. A former XDR REST page supplied historical schema, license, and limit details, but its URL now redirects to the generic portal and no specific current canonical page was identified. Those historical details must not be represented as maintained XSIAM schema, licensing guidance, or current limits.

## Project-specific operational knowledge

Accessible material contributes useful but bounded context:

- evidence-first DFIR sequencing, source traceability, explicit uncertainty, negative-evidence coverage gates, privacy minimization, and adversarial validation;
- derivative summaries for historical/custom `soc-optimization` content and a separate identity/DNS/OpenCTI/N1/Continuous Assessment package;
- endpoint/application export batches with incomplete generating-query and application provenance;
- project-asserted high-risk playbook defects, including unsafe DBotScore handling, literal containment arguments, mixed context namespaces, fabricated placeholder observables, missing pagination/deduplication, and possible secret exposure;
- no accessible originals for the referenced playbooks, scripts, PDFs, content repository, or tenant exports needed to reproduce those claims.

These facts influence tests, failure modes, templates, and review criteria. They do not validate product syntax or tenant behavior.

## Skill ownership map

| Skill | Owns | Does not own | Standalone minimum |
|---|---|---|---|
| `cortex-xql-query-engineer` | Query construction, validation, optimization, debugging, query-focused investigation support | Detection lifecycle, full hunt methodology, playbook design, platform configuration | Must explain product/schema assumptions and produce a safe validation path without sibling Skills. |
| `cortex-detection-engineer` | Threat model to telemetry to signal, thresholds/baselines, correlation-rule design, false positives, tuning, lifecycle | General XQL language manual, exploratory campaign hunting, response implementation | Must provide enough query-shape guidance to specify logic while marking exact syntax for XQL validation. |
| `cortex-playbook-engineer` | Automation architecture, context contracts, safety gates, reliability, debugging, artifact classification | Detection quality decision, generic platform deployment, intelligence governance | Must produce a complete conceptual/configuration design even without other Skills. |
| `cortex-threat-hunter` | Hypothesis-driven investigation, iterative pivots, timelines, scoping, conversion to detection candidates | Production rule lifecycle, full XQL reference, response orchestration | Must provide safe query hypotheses and schema-validation steps without assuming sibling installation. |
| `cortex-tim-engineer` | Intelligence ingestion, normalization, scoring/confidence, deduplication, enrichment, expiration, distribution/governance | General telemetry ingestion, arbitrary playbook construction, firewall configuration | Must describe protocol/product uncertainty and operationalization safety independently. |
| `cortex-platform-engineer` | Product boundaries, architecture, ingestion, integrations, collectors/Broker VM, APIs, auth/RBAC, troubleshooting | Threat behavior design, complete XQL authoring, incident-response decision logic | Must trace end-to-end data flow and require exact configuration evidence. |
| `cortex-security-engineer` | Broad requirement decomposition and cross-domain engineering sequence | Duplicating the full manual of every specialist | Must solve the planning/orchestration problem even when no sibling Skill is installed. |

## Research limitations

- No live Cortex tenant, license inventory, role assignment, schema browser, Query Builder autocomplete, dataset list, integration instance, playbook debugger, or API credential was available.
- No wider ChatGPT Project knowledge or Project File Library material was assumed accessible.
- Referenced source files absent from the mounted artifacts remain `REFERENCED-ONLY` even when hashes or summaries exist.
- Official documentation changes over time. Every Skill must preserve a review date and revalidate version-sensitive facts during maintenance.
- Static repository and prompt tests can validate behavior contracts but cannot certify tenant execution.

## Phase 1 checkpoint

| Item | Status |
|---|---|
| Completed work | Workspace and supplied-artifact ingestion; product/object map; initial skill ownership and operational boundaries. |
| Evidence collected | Current official documentation, official developer references/repositories, readable local artifacts, archive inventories, and baseline DFIR conventions. |
| Files created/modified | This ecosystem map; companion Phase 1 records are maintained in this directory. |
| Tests performed | Structural archive review, provenance comparison, workspace search, source reconciliation, and terminology/behavior cross-checks. |
| Findings | Product convergence does not remove version/license boundaries; no tenant schema or executable Cortex artifact is available; multiple project claims are derivative or legacy. |
| Open risks | Tenant execution, exact schemas, license/RBAC, missing original content, and future documentation drift. |
| Quality gate | This workstream is complete. The consolidated Phase 1 decision is recorded only in `phase-1-checkpoint.md`; earlier per-file checkpoints are historical inputs. |
| Next phase eligibility | Refer to `phase-1-checkpoint.md`. Only the XQL Golden Reference can become eligible; the other six Skills remain gated. |
