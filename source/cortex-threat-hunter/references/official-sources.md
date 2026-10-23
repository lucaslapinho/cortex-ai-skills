# Official sources

## Focused refresh — 2026-10-23

Read the [dated semantic refresh](2026-10-23-refresh.md) for newly inspected query/graph permissions, XDR issue-dataset exclusions, iterative investigation and grouping-population claims. Those bounded observations have `D: PASS`; new-runtime `S/C/E: NOT RUN`. The remaining register and evaluation dates are historical.

## Targeted Astra semantic recheck — 2026-09-06

Only the following bounded claims were refreshed; this does not redate the whole register or establish tenant behavior.

| Source | Claim actually inspected |
|---|---|
| [Query Center permissions](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/reference-and-developer-docs/role-based-access-control/investigation-and-response-permissions/search-permissions/query-center-permissions.md) | View versus View/Edit activities differ; scope controls affect the visible population. A returned population is not automatically organization-wide. |
| [Graph Search permissions](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/reference-and-developer-docs/role-based-access-control/investigation-and-response-permissions/search-permissions/graph-search-permissions.md) | Separate cloud-license prerequisites and permission dependencies; Graph Search is not assumed available from XQL access alone. |
| [XDR 5 query case and issue data](https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/detect-investigate-and-respond-to-threats/investigate-and-respond-to-cases/investigate-issues/issue-investigation-actions/query-case-and-issue-data.md) | Product-specific cases/issues datasets and limited API-aligned field exposure; informational issues are excluded from the documented issue query scope. A dataset query is not the entire issue population. |
| [XSIAM research a known threat](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/investigation-and-response/research-a-known-threat.md) | Lead-driven iterative XQL investigation, causality/timeline review and tested/tuned detection handoff; no claim that this example hunt ran. |

`D: PASS` for these bounded source observations; `C/E: NOT RUN` — tenant permissions, licenses, schemas, visibility and execution were not accessed.

## Contents

1. Source policy
2. Query and data sources
3. Investigation and object sources
4. Detection and intelligence sources
5. Source-use limits

## 1. Source policy

Reviewed 2026-09-04. Palo Alto Networks product documentation and official repositories are authoritative for public product behavior. The applicable tenant remains the authority for enabled licenses, schemas, values, retention, permissions, and actual execution.

Use the most specific current page for a claim. Recheck a page before making a time-sensitive external claim. A documentation URL does not prove tenant support.

## 2. Query and data sources

| ID | Product | Official source | Claim supported |
|---|---|---|---|
| Q01 | XSIAM 3.x | [How to build XQL queries](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/How-to-build-XQL-queries) | XQL-building workflow; product/version scoped |
| Q02 | XSIAM 3.x | [Datasets and presets](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Datasets-and-presets) | Dataset/preset concepts; tenant availability still unverified |
| Q03 | XQL | [XQL command reference](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme.md) | Current public XQL command reference |
| Q04 | XSIAM | [XSIAM data model schema](https://cortex-docs.paloaltonetworks.com/xsiam-data-model-schema/readme.md) | Public XDM schema reference; population is tenant-sensitive |
| Q05 | XSIAM 3.x | [XQL query best practices](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/XQL-Query-best-practices) | Current query-planning/performance guidance |
| Q06 | XSIAM 3.x | [Query Center permissions](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Query-Center-permissions) | Query Center access and scope controls |
| Q07 | XSIAM 3.x | [Data retention](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Data-retention) | Retention is configured/product-sensitive |
| Q08 | XSIAM 3.x | [Graph Search permissions](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Graph-Search-permissions) | Graph Search permissions, scope, and license prerequisites |
| Q09 | XSIAM 3.x | [Create Graph Search query](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Create-Graph-Search-query) | Cloud asset/finding relationship exploration and prerequisites |
| Q10 | XDR 5.x | [Create XQL query](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-5.x-Documentation/Create-XQL-query?contentId=9Gvfbx_VJQzkKWUZVHy1AQ) | XDR-specific XQL workflow |
| Q11 | XDR 5.x | [Query case and issue data](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-5.x-Documentation/Query-case-and-issue-data) | XDR 5 case/issue query context |
| Q12 | XDR 5.x | [Legacy Query Builder](https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/reference-and-developer-docs/cortex-xdr-xql/build-xql-queries/legacy-query-builder.md) | Versioned legacy surface/entity guidance |
| Q13 | Official examples | [Cortex XQL Queries repository, pinned commit](https://github.com/PaloAltoNetworks/cortex-xql-queries/tree/a3a2c0c49e3006a95053a0a4855b043e5d2b5196) | Official examples only; not tenant execution proof |

## 3. Investigation and object sources

| ID | Product | Official source | Claim supported |
|---|---|---|---|
| I01 | XSIAM | [Research a known threat](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/investigation-and-response/research-a-known-threat.md) | Lead-driven iterative threat research using applicable investigation surfaces |
| I02 | XDR 5.x | [Research a known threat](https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/detect-investigate-and-respond-to-threats/investigate-and-respond-to-cases/research-a-known-threat.md) | XDR-specific known-threat investigation guidance |
| I03 | XSIAM 3.x | [Investigate issues](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Investigate-issues) | Issue investigation context |
| I04 | XSIAM 3.x | [What are cases](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/What-are-cases) | Case object context |
| I05 | XSIAM 3.x | [Review findings](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Review-findings?contentId=fhoyBBQ42gEoaTp2AJ3Eiw) | Finding-review context |

## 4. Detection and intelligence sources

| ID | Product | Official source | Claim supported |
|---|---|---|---|
| D01 | XSIAM 3.x | [What are detection rules](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/What-are-detection-rules) | Detection-rule categories and product boundary |
| D02 | XSIAM 3.x | [View generating BIOC or IOC rule](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/View-generating-BIOC-or-IOC-rule?contentId=EpAfS2pyZ375crfcS~_fdA) | Provenance path from issue/detection to generating rule |
| T01 | XSIAM 3.x | [What is Threat Intel Management](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/What-is-Threat-Intel-Management) | Threat-intelligence management context; indicator data remains contextual |

## 5. Source-use limits

- OFFICIAL-CURRENT supports the documented product behavior on the reviewed page, not a specific tenant outcome.
- OFFICIAL-EXAMPLE is a design clue, not a supported-schema or performance guarantee.
- Version paths such as 3.x and 5.x must remain in the claim.
- UI text and licensing can change; reverify before operational use.
- Tenant dataset/field existence requires TENANT-SCHEMA-VERIFIED.
- Compilation requires TENANT-COMPILED.
- Results require TENANT-EXECUTED and an evidence record.
- No source authorizes destructive action or converts ATT&CK/IOC context into a verdict.
