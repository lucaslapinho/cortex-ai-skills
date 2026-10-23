# Official source register

**Review date:** 2026-09-04  
**Scope:** current official Palo Alto Networks documentation and one pinned official example repository  
**Tenant status:** no tenant was accessed; product documentation does not prove tenant availability, compilation, execution, or outcomes

## Focused refresh — 2026-10-23

The [dated semantic refresh](2026-10-23-refresh.md) records actual XSIAM/XDR BIOC and correlation rechecks, prevention conversion restrictions and Case-grouping qualification. The real-time action discrepancy remains unresolved. Only those inspected claims have fresh `D: PASS`; new-runtime `S/C/E: NOT RUN`. All other source dates below remain historical.

## Targeted Astra semantic recheck — 2026-09-06

S06/S07 were reopened: product-specific BIOC pages still document source restrictions, required `event_type`, non-aggregate filter/alter logic, case-insensitive evaluation, the initial historical-match bound and automatic PROCESS-SHA256 exception. S06 also reconfirmed the hit-disable safeguard. S08/S09 were reopened for the documented scheduled-correlation timing and safeguard boundaries; this does not imply identical product surfaces.

S08's migrated Markdown retains restricted real-time stages/functions and required filter, but **omits** the prior Generate-issue-only action note. The [legacy official indexed page](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Create-a-correlation-rule?contentId=bVMQUHW0PR_zPWqYqM4sWA) still contains that restriction. Preserve this documentation discrepancy and the earlier boundary as VERSION-DEPENDENT pending current target clarification. A search-index snapshot is not a fresh tenant fact, and omission does not establish support for real-time dataset/lookup writes.

`D: PASS` is limited to the inspected claims and this observed document discrepancy, not a blanket refresh of all 23 sources. `C/E: NOT RUN` — no tenant/editor/execution evidence. Original register dates and broader limitations remain below.

## Contents

- [Use and freshness](#use-and-freshness)
- [Product and object boundaries](#product-and-object-boundaries)
- [Detection and rule surfaces](#detection-and-rule-surfaces)
- [XQL, schema, permissions, and examples](#xql-schema-permissions-and-examples)
- [Source-to-claim rules](#source-to-claim-rules)
- [Maintenance checklist](#maintenance-checklist)

## Use and freshness

Use the most specific record that supports the material claim. Re-open it before relying on a numeric limit, license, stage/function restriction, action, schedule, grouping behavior, field mapping, or permission in production. A `200` response on the review date proves reachability only.

Source order is current product documentation, official API/reference material, and then pinned official examples. Each source below is `OFFICIAL-CURRENT` unless marked as an official living example. Tenant-dependent conclusions remain `TENANT-UNVERIFIED`.

## Product and object boundaries

### S01 — What are detection rules?

- Product: Cortex XSIAM 3.x
- Page: [What are detection rules?](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/threat-management/detection-rules/what-are-detection-rules.md)
- Supports: official distinction among IOC, BIOC, Analytics BIOC, and correlation rules.
- Boundary: does not establish license, enabled content, tenant configuration, or effectiveness.

### S02 — What is Cortex XDR?

- Product: Cortex XDR 5.x
- Page: [What is Cortex XDR?](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-5.x-Documentation/What-is-Cortex-XDR)
- Supports: XDR product boundary and edition-dependent capability model.
- Boundary: do not transfer XSIAM-only real-time correlation or Case behavior without an XDR-specific page.

### S03 — Cases and Issues terminology migration

- Product: Cortex XDR 5.x
- Page: [Improved incident management workflow with cases and issues](https://cortex-docs.paloaltonetworks.com/upgrade-to-cortex-xdr-5/improved-incident-management-workflow-with-cases-and-issues.md)
- Supports: current user-facing Case/Issue terms and compatibility with former Incident/Alert identifiers.
- Boundary: preserve literal legacy identifiers in supported APIs, fields, exports, or existing automation.

### S04 — What are cases?

- Product: Cortex XSIAM 3.x
- Page: [What are cases?](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/What-are-cases)
- Supports: a Case connects related Issues into an investigative problem.
- Boundary: one matching event or Issue is not itself proof of a complete Case or compromise.

### S05 — Investigate issues

- Product: Cortex XSIAM 3.x
- Page: [Investigate issues](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Investigate-issues)
- Supports: Issue sources and investigation model.
- Boundary: Issues, Insights, Findings, and Cases are distinct objects.

## Detection and rule surfaces

### S06 — Create a BIOC rule in Cortex XSIAM

- Product: Cortex XSIAM 3.x
- Page: [Create a BIOC rule](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/threat-management/detection-rules/what-are-detection-rules/whats-a-bioc/create-a-bioc-rule.md)
- Supports: BIOC datasets and XQL restrictions, historical testing, safeguards, import boundary, and custom-prevention prerequisites.
- Version-sensitive facts at this snapshot: first 10,000 historical matches; auto-disable at 5,000 or more hits in 24 hours; automatic PROCESS-SHA256 exception above 100 endpoints in 72 hours; `event_type` filter; supported stages without aggregation; case-insensitive evaluation.
- Boundary: recheck all limits, supported fields, licenses, OS/agent requirements, and import schema before use.

### S07 — Create a BIOC rule in Cortex XDR

- Product: Cortex XDR 5.x
- Page: [Create a BIOC rule](https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/detect-investigate-and-respond-to-threats/threat-management/detection-rules/whats-a-bioc/create-a-bioc-rule.md)
- Supports: XDR 5 BIOC license and rule-construction boundaries.
- Boundary: an XSIAM tenant and an XDR tenant can differ in license, schema, profile, UI, and supported behavior.

### S08 — Create a correlation rule in Cortex XSIAM

- Product: Cortex XSIAM 3.x
- Page: [Create a correlation rule](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/threat-management/detection-rules/what-are-detection-rules/whats-a-correlation-rule/create-a-correlation-rule.md)
- Supports: scheduled versus real-time selection, restricted real-time XQL, schedules/windows, suppression, resulting actions, field mapping, and volume safeguards.
- Snapshot boundary: current real-time rules support only Generate issue; scheduled rules can expose documented dataset/lookup actions. Recheck in the target product before configuration.

### S09 — Create a correlation rule in Cortex XDR

- Product: Cortex XDR 5.x
- Page: [Create a correlation rule](https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/detect-investigate-and-respond-to-threats/threat-management/detection-rules/whats-a-correlation-rule/create-a-correlation-rule.md)
- Supports: XDR Pro license boundary and scheduled-correlation configuration documented for XDR 5.
- Boundary: do not infer XSIAM real-time behavior from this page; verify the XDR target independently.

### S10 — Monitor correlation rules

- Product: Cortex XSIAM 3.x
- Page: [Monitor correlation rules](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/threat-management/detection-rules/what-are-detection-rules/whats-a-correlation-rule/monitor-correlation-rules.md)
- Supports: `correlations_auditing`, initiation/completion/error statuses, query versus execution times, retries, failure reasons, rule identity, suppression, XQL, and health issues.
- Boundary: audit fields and rows must be observed in the tenant before an operational claim.

### S11 — Troubleshoot scheduled correlation errors

- Product: Cortex XSIAM 3.x
- Page: [Troubleshoot server errors in scheduled correlation rules](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/threat-management/detection-rules/what-are-detection-rules/whats-a-correlation-rule/troubleshoot-server-errors-in-scheduled-correlation-rules.md)
- Supports: separate query-resource failures from Issue-generation/output failures and reduce query/output complexity deliberately.
- Boundary: do not copy an example function without verifying current syntax and target compatibility.

### S12 — Optimize Case grouping in correlations

- Product: Cortex XSIAM 3.x
- Page: [Optimize case grouping in correlations](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Optimize-case-grouping-in-correlations)
- Supports: correctly mapped fields can influence grouping and prioritization.
- Boundary: the page explicitly says field mapping does not guarantee grouping.

### S13 — Case grouping

- Product: Cortex XSIAM 3.x
- Page: [Case grouping](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Case-grouping)
- Supports: current promotion/grouping concepts and Insights boundary.
- Boundary: logic is dynamic and domain-dependent; recheck before encoding severity/grouping expectations.

### S14 — Detection Rules permissions

- Product: Cortex XSIAM 3.x
- Page: [Detection Rules permissions](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Detection-Rules-permissions?contentId=kHfvcGJWEQIdQPTKMwQuzw)
- Supports: detection-rule RBAC and Query Center permission dependencies.
- Boundary: role names do not prove effective permissions; test the named identity and scope.

### S15 — View the generating BIOC or IOC rule

- Product: Cortex XSIAM 3.x
- Page: [View the generating BIOC or IOC rule](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/View-generating-BIOC-or-IOC-rule?contentId=EpAfS2pyZ375crfcS~_fdA)
- Supports: Issue-to-rule provenance for BIOC/IOC-generated Issues.
- Boundary: retain rule/source identifiers in evidence and lifecycle records.

### S16 — Analytics Issues and Analytics BIOCs

- Product: Cortex XSIAM 3.x
- Page: [Analytics issues and Analytics BIOCs](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/threat-management/analytics/analytics-issues-and-analytics-biocs.md)
- Supports: standard Analytics Issues can represent multiple-event deviation from a learned baseline; ABIOCs describe a single suspicious event with causality context and use Analytics profiles.
- Boundary: do not invent detector internals, custom retraining, or universal threshold controls.

### S17 — MITRE ATT&CK framework coverage

- Product: Cortex XSIAM 3.x
- Page: [Review MITRE ATT&CK framework coverage](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Review-MITRE-ATT-CK-framework-coverage)
- Supports: dashboard coverage views and contributing data-source types.
- Boundary: active source status does not imply every related rule/detector is active or applicable.

### S18 — Indicator rules for prevention and detection

- Product: Cortex XSIAM 3.x / Threat Intelligence Management
- Page: [Generate issues from indicators using indicator rules](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Generate-issues-from-indicators-using-indicator-rules-for-prevention-and-detection)
- Supports: indicator-library-to-detection/prevention linkage for supported types.
- Boundary: entitlement, indicator lifecycle, active/detectable state, and enforcement scope require tenant verification.

## XQL, schema, permissions, and examples

### S19 — XQL command reference

- Product: Cortex XQL
- Page: [Cortex XQL Command Reference](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme.md)
- Supports: current general language syntax.
- Boundary: globally documented syntax may still be restricted in BIOC or correlation contexts.

### S20 — Datasets and presets

- Product: Cortex XSIAM 3.x
- Page: [Datasets and presets](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Datasets-and-presets)
- Supports: tenant dataset/preset discovery and integration dependence.
- Boundary: documentation does not prove population or the target tenant's schema.

### S21 — XQL query best practices

- Product: Cortex XSIAM 3.x
- Page: [XQL query best practices](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/XQL-Query-best-practices)
- Supports: bounded timeframes, early filtering, field reduction, limits, and context-sensitive result behavior.
- Boundary: no universal performance gain or result limit may be claimed.

### S22 — Query Center permissions

- Product: Cortex XSIAM 3.x
- Page: [Query Center permissions](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Query-Center-permissions)
- Supports: query execution and result scope depend on access.
- Boundary: zero rows can reflect RBAC/SBAC rather than absence.

### S23 — Official XQL examples

- Product: Cortex XDR / Cortex XSIAM
- Repository: [PaloAltoNetworks/cortex-xql-queries](https://github.com/PaloAltoNetworks/cortex-xql-queries)
- Reviewed revision: `a3a2c0c49e3006a95053a0a4855b043e5d2b5196`
- Evidence: `VERIFIED / OFFICIAL-EXAMPLE` only for the pinned revision.
- Boundary: examples do not prove tenant schema, current rule compatibility, or execution.

## Source-to-claim rules

| Claim | Minimum evidence |
|---|---|
| Product supports a rule family | Specific current product page and license scope |
| Query is rule-compatible | Current rule page plus exact editor/compiler acceptance for `C` |
| Dataset/field exists in a tenant | Schema/autocomplete or export with product/version/date/identity |
| Threshold or baseline is suitable | Representative tenant observations and documented method |
| Issue was generated | Sanitized tenant execution evidence with rule ID and timeframe |
| Issue grouped into a Case | Case/Issue evidence; field mapping alone is insufficient |
| Rule is production-effective | Outcome metrics, FP/FN review, coverage, drift, and owner evidence |
| Artifact can be imported | Exact schema/tool/target validation and controlled import evidence |

## Maintenance checklist

1. Re-open every source used by a changed claim.
2. Record product, version, page publication/update state, and review date.
3. Diff limits, licenses, actions, stages/functions, permissions, terminology, and object behavior.
4. Update the affected reference, example, and regression case together.
5. Rerun local links, URL reachability, secret scan, standalone copy, and behavioral tests.
6. Obtain independent technical, domain, security, adversarial, and compatibility review.
