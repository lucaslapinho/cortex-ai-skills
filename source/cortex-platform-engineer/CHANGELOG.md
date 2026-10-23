# Changelog

## [0.1.1] — 2026-10-23

- Added a bounded documentation refresh for API authentication/migration, effective
  dataset access, Broker VM, XSIAM Engines, event collectors, and command permissions.
- Preserved the API release notes' conflicting Case artifacts HTTP methods as an
  unresolved source discrepancy; no endpoint method or payload was substituted.
- Recorded the 3.6 API documentation changes without asserting tenant availability.
- Preserved the operating contract, examples, templates, and historical evaluations.
  New behavioral evaluation, tenant acceptance, and execution remain `NOT RUN`.

### Astra forward-evaluation correction — 2026-09-06

- Required explicit disposition of every access layer, including object-level sharing, after PLAT-REG-08 omitted that layer. Historical attempt retained; rerun required.

All notable changes to this standalone Skill are recorded here.

## 0.1.0 candidate refinement — 2026-09-06 (Astra)

- Added the current XSIAM Datasets Rows/XDM restriction to access design and
  raw-versus-normalized troubleshooting, including an access-preserving alternative
  and the disabled dataset-access-management display distinction.
- Updated the source register, API/troubleshooting templates, missing-telemetry
  example, and existing PLAT-REG-08 oracle without increasing the 41-case catalog.
- Aligned the example index with the examples' unverified reported causes.
- Reopened selected official component, ingestion, API, and permission sources.
  This is an author/reviewer refinement awaiting independent delta evaluation;
  no new S, tenant C/E, or host-runtime pass is asserted.

## [0.1.0] — 2026-09-04

### Added

- Evidence-scoped architecture and troubleshooting workflow for Cortex XSIAM, XDR, and XSOAR.
- Required end-to-end path from expected data through query visibility, with ownership, trust boundaries, and layer-specific failure checks.
- Product-bound controls for agents, Broker VM, XDR Collectors, XSOAR Engines, integrations, ingestion, parsing, mapping, datasets, forwarding, APIs, RBAC, and SBAC.
- Safety gates for credentials, configuration changes, replay, destructive operations, and tenant-state claims.
- Standalone references, templates, examples, platform matrix, source register, manifests, and 41 behavior-focused tests across all seven required categories.

### Known limitations

- No live Cortex tenant, configuration export, tenant schema, API session, collector, agent, Broker VM, XSOAR Engine, parser compiler, or production observation was available.
- No configuration was imported, applied, deployed, or rolled back.
- Product features, licenses, configuration fields, limits, ports, roles, datasets, and UI paths can change after the 2026-09-04 documentation review.
- Independent Architecture, technical, adversarial, security, and static compatibility review completed for the publication candidate; selected behavior passed on the current runtime.
- Normalized the end-to-end syslog example's S/D/C/E rows to canonical results with rationale; independent revision-impact review preserved the selected Architecture case and current-source decision.
- Expanded the API access-review verdict into four typed canonical S/D/C/E results with level-specific rationale and evidence requirements.
- Static review does not establish cross-platform runtime behavior or tenant product compatibility.

The release remains pre-1.0 because tenant-dependent and supported-host runtime validation remain unavailable.
