# Changelog

All notable changes to this Skill are documented here. Versions follow Semantic Versioning.

## Astra completion delta — 2026-09-06 (0.1.0 candidate)

- Read all 33 package files afresh and reopened applicable BIOC/correlation source content.
- Removed troubleshooting advice to disable existing linkage without authorization; strengthened `DET-ADR-05` for design-only scope.
- Completed canonical S/D/C/E result-and-rationale fields in templates and all five examples; removed the competing XQL readiness shorthand.
- Preserved the migrated real-time action-note discrepancy instead of inferring new write support. Independent delta evaluation and tenant `C/E` remain `NOT RUN` until separately recorded.

## 0.1.0 — 2026-09-04

### Added

- Standalone detection-engineering workflow from threat behavior through retirement.
- Product and rule-surface boundaries for Cortex XSIAM and Cortex XDR.
- Current official-source register for BIOC, correlation, Analytics, permissions, Case/Issue, grouping, XQL, and monitoring behavior.
- Separate evidence statuses, provenance qualifiers, and S/D/C/E validation levels.
- Templates for a detection specification, readiness review, tuning, validation, and lifecycle monitoring.
- Worked examples covering PowerShell, hunt promotion, overbroad correlation, missing telemetry, and scheduled-versus-real-time choice.
- Basic, intermediate, advanced, troubleshooting, ambiguity, adversarial, and regression test catalogs.
- Explicit safeguards for rule mutation, correlation dataset/lookup actions, custom prevention, and downstream response.

### Known limitations

- No live Cortex tenant, schema export, editor/compiler response, rule import, rule execution, generated Issue/Case, or production quality metric was available.
- ChatGPT, Codex, and Claude runtime behavior has not yet been independently tested.
- Independent technical, domain, security, adversarial, and static compatibility reviews completed for the publication candidate; host runtime and tenant-dependent C/E validation remain `NOT RUN`.
- Expanded the reusable evidence record into four typed canonical S/D/C/E results, each requiring level-specific rationale and retained evidence or an explicit reason not run.

This release remains `0.x` because material tenant and supported-host runtime validation remains incomplete.
