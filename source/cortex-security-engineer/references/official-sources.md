# Official Source Register

**Scoped refresh — 2026-10-23:** see [the dated refresh](2026-10-23-refresh.md)
for the exact pages reopened and their product-level conclusions. Unlisted rows
retain their prior dates; this does not establish tenant state or host acceptance.

## Contents

- [Use and scope](#use-and-scope)
- [Product boundaries](#product-boundaries)
- [Access and working surfaces](#access-and-working-surfaces)
- [Platform and state-change boundaries](#platform-and-state-change-boundaries)
- [Freshness rules](#freshness-rules)

## Use and scope

All records were author-reviewed on **2026-09-04** and point to first-party Palo Alto Networks documentation. `OFFICIAL-CURRENT` means the linked page supported the summarized product-level statement on that date. It does not establish tenant license, rollout, configuration, permission, data, compilation, execution, results, or efficacy.

Before concrete work, reopen the exact page and verify product, version, publish date, license, prerequisites, and target surface. Preserve conflicting version-scoped statements instead of silently reconciling them.

**Astra refresh — 2026-09-06:** O09 was reopened at its canonical URL for the
Datasets Rows/XDM boundary; O11, O17, O20, O21 and O23 were also reopened for the
scoped permission, component and state-change claims. Other rows retain their
2026-09-04 review date. No tenant state or new behavioral result follows.

## Product boundaries

| ID | Official page | Scoped use |
|---|---|---|
| O01 | [Get started with Cortex XSIAM](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Get-started-with-Cortex-XSIAM?contentId=xImjmn~hG4QyrtIK4aQrvA) | XSIAM product overview and converged-capability boundary; some features are license-dependent |
| O02 | [What is Cortex XDR?](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-5.x-Documentation/What-is-Cortex-XDR) | XDR product purpose and data-source scope; do not project XSIAM behavior into XDR |
| O03 | [What is Cortex XSOAR?](https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-saas/learn-about-cortex-xsoar/what-is-cortex-xsoar.md) | Current XSOAR 8 SaaS overview for orchestration, automation, case management, collaboration, threat-intelligence, and product-boundary context; deployment-specific behavior still requires its own source |
| O04 | [Navigate the Cortex Cloud Runtime Security docs](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/get-started/readme.md) | Current Cortex Cloud Runtime Security navigation and module boundary; use only for named Cortex Cloud surfaces and verify license, release, and the exact feature page separately |
| O05 | [What is Threat Intel Management?](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/What-is-Threat-Intel-Management) | XSIAM TIM aggregation, scoring, sharing, indicator workflows, and Premium/TIM add-on prerequisite |
| O06 | [License allocation](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/License-allocation) | XSIAM edition/license cross-check; actual tenant allocation still needs observation |
| O07 | [Review findings](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Review-findings?contentId=fhoyBBQ42gEoaTp2AJ3Eiw) | finding review and license-dependent finding families; a finding is not automatically an event or detection |

## Access and working surfaces

| ID | Official page | Scoped use |
|---|---|---|
| O08 | [Set up users and roles](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Set-up-users-and-roles) | XSIAM RBAC/SBAC architecture and tenant/Gateway distinction |
| O09 | [Manage user access](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/onboard-cortex-xsiam/post-deployment/manage-user-roles-and-access-management/manage-user-access.md) | XSIAM accumulated permissions, dataset access, SBAC and API-key scopes; Datasets Rows filters do not support XDM queries, which return rows only with All rows are accessible and no filter in that area; rechecked 2026-09-06; actual tenant settings remain unverified |
| O10 | [Role permissions by component](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Role-permissions-by-component?contentId=jxQG94yU_RKuFVersHT0uw) | current XSIAM component permission matrix; verify effective tenant permissions |
| O11 | [Query Center permissions](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Query-Center-permissions) | XSIAM Query Center View versus View/Edit and SBAC-scoped results |
| O12 | [Manage access to saved queries](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Manage-access-to-saved-queries) | saved-query object access; object visibility does not prove execution/result scope |
| O13 | [Detection Rules permissions](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Detection-Rules-permissions?contentId=kHfvcGJWEQIdQPTKMwQuzw) | XSIAM rule families and Query Center dependency for BIOC/correlation editing |
| O14 | [Graph Search permissions](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Graph-Search-permissions) | separate Graph Search license and permission/dependency boundary |
| O15 | [Cases and Issues permissions](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Cases-and-Issues-permissions) | XSIAM case/issue access, dependencies, and documented child-Issue/parent-Case caution |
| O16 | [Manage access to playbooks and scripts](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Manage-access-to-playbooks-and-scripts?contentId=e7ua1aIg8YrXlnX6Y2wrZg) | role plus object ownership/sharing; dependency visibility differs from execution |
| O17 | [Configure integration permissions](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Configure-integration-permissions) | per-integration-instance, per-command role restrictions, including harmful commands |
| O18 | [Threat Intelligence permissions](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Threat-Intelligence-permissions?contentId=q8MwZF60yIt6wBP1QhrDzw) | TIM license and permission dependencies; no indicator verdict/action inference |
| O19 | [Data Sources permissions](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Data-Sources-permissions) | XSIAM data-source versus integration administration and related permissions |

## Platform and state-change boundaries

| ID | Official page | Scoped use |
|---|---|---|
| O20 | [What is the Broker VM?](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/What-is-the-Broker-VM) | Broker VM as a hardened bridge/applet host; arbitrary third-party agent installation is unsupported |
| O21 | [XDR Collectors](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/XDR-Collectors?contentId=qfIZLEv731a8gqLwBz0GGg) | Windows/Linux collector architecture; validate current supported packages and limits |
| O22 | [Get started with Cortex XSIAM APIs](https://cortex-docs.paloaltonetworks.com/xsiam-api/get-started-with-cortex-apis.md) | tenant API FQDN and documented authentication workflow; do not infer endpoints from console/legacy examples |
| O23 | [XQL target stage](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/stages/target.md) | persistent dataset/lookup write, final-stage requirement, and omitted `append=false` overwrite behavior |
| O24 | [Jobs](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/jobs.md) | automation Jobs are distinct from detection-rule schedules |
| O25 | [Business Applications](https://cortex-docs.paloaltonetworks.com/application-security/application-security-posture-management-aspm/applications.md) | logical application-security object family, not installed endpoint software |
| O26 | [Endpoint Applications permissions](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/reference-and-developer-docs/role-based-access-control/data-security-endpoint-dlp-permissions/endpoint-applications.md) | DLP Endpoint Application definition permissions, not endpoint software inventory |
| O27 | [Cortex Cloud external data ingestion and management](https://cortex-docs.paloaltonetworks.com/cloud-posture-management-rn/cortex-cloud-posture-management-release-information/features-introduced-in-2026-cloud/february-2026/feature-enhancements/external-data-ingestion-and-management.md) | Cortex Cloud February 2026 release scope only; never use as an XSIAM/XDR/XSOAR correction layer |

## Freshness rules

- Prefer the current canonical page over cached snippets, but record the review date.
- A “3.x,” “5.x,” or similar documentation path still requires deployed-release validation.
- Search results and abstracts help discovery; cite the direct official page.
- A source register proves only what was reviewed. It does not prove the downstream Skill response applied the source correctly.
- Recheck after product upgrade, license/rollout change, renamed UI object, API revision, or contradictory official page.
- If a page is unavailable, preserve the last reviewed claim as dated and `UNVERIFIED` for current behavior until reopened.
