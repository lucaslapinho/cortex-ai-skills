# Product and Surface Map

## Contents

- [Use this map](#use-this-map)
- [Product boundaries](#product-boundaries)
- [Surface boundaries](#surface-boundaries)
- [Permission and entitlement chain](#permission-and-entitlement-chain)
- [Common ambiguous terms](#common-ambiguous-terms)
- [Selection record](#selection-record)

## Use this map

Choose the exact product and working surface before giving concrete syntax, navigation, permission, API, or deployment advice. When the target is unknown, ask for the material choice or offer clearly labeled alternatives.

This map routes work; it is not a feature-availability guarantee.

## Product boundaries

| Product/capability | Product-level purpose | Typical surfaces | Reverify before use |
|---|---|---|---|
| Cortex XSIAM | converged security operations across data, detection, investigation, automation, and licensed capabilities | Query Center, Cases/Issues, Detection Rules, Automation, TIM, Data Sources & Integrations, APIs | release, license, rollout, tenant configuration, RBAC/SBAC, data |
| Cortex XDR | extended detection and response with endpoint and other supported data sources | investigations, endpoint/response, XQL, rules, APIs, automation where available | XDR release/license; never import XSIAM-only guidance |
| Cortex XSOAR | orchestration, automation, case/incident management, collaboration, and threat intelligence | playbook editor, integrations, incident/case surfaces, APIs | XSOAR major version and deployment model |
| XSIAM TIM | licensed threat-intelligence management capability | Indicators, feeds, issue/IOC rules, enrichment/export workflows | Premium/TIM entitlement, source, scoring, object and action permissions |
| Cortex Cloud | cloud application/posture/runtime security with asset, case, detection, automation, and data features | inventories, graphs, findings/issues/cases, cloud rules, XQL, playbooks | Cortex Cloud module/license, release/rollout, identity scope |

Do not infer that identical menu names have identical behavior across products.

## Surface boundaries

| Surface | Primary purpose | Minimum evidence before concrete advice | Not established by access/use |
|---|---|---|---|
| Query Center | write, run, manage, schedule, and inspect XQL in its documented product context | product/release, query permission, data scope, dataset/schema, timeframe | rule compatibility, full data coverage, tenant-wide visibility |
| Saved query / Query Library | retain/share query objects | object access plus query/data scope | ability to execute or see the same rows |
| BIOC editor | behavior-based detection rule design | exact product/release, documented source/stage/function limits, rule permissions, query dependency, tenant editor test | scheduled/real-time compatibility or production efficacy |
| Scheduled correlation | evaluate eligible logic on a schedule/window | current restrictions, time anchor, schedule/action, rule limits, volume, tenant validation | real-time compatibility |
| Real-time correlation | evaluate an eligible restricted real-time rule | documented source/stage/function/action limits and independent editor test | scheduled action choices or full interactive XQL |
| XQLp / parsing rules | parse and map ingested data using its own subset/structure | parser grammar and tenant parser validation | ordinary XQL compatibility |
| Cases and Issues | triage, investigation, context, and workflow | Cases/Issues plus prerequisite/dependent permissions and scope | authorization for every playbook/integration/response action |
| Graph Search | visual cloud relationship/finding exploration | required license, Graph Search and dependent data/query permissions | Query Center or Action Center rights beyond assigned permissions |
| Detection Rules | manage IOC/BIOC/analytic/correlation/indicator rules | rule permission and dependent Query Center/other relevant visibility | prevention or response authorization |
| Playbooks/Scripts | author and use automation objects | role-level capability, object-level visibility/ownership, dependencies, integration permissions | all task execution rights or action safety |
| Jobs | scheduled/event-driven automation workflow | exact job type, playbook/input/error policy, Jobs permissions | correlation-rule schedule behavior |
| TIM / Indicators | aggregate, score, manage, share, and operationalize intelligence | entitlement, indicator/feed permission, source/confidence/lifecycle, consumer policy | maliciousness, attribution, or block authorization |
| Data Sources & Integrations | onboard/manage sources and automation/feed integrations | product-specific permissions, entitlement, connector/collector design, credentials governance | healthy ingestion, complete parsing, or query visibility |
| Integration Permissions | restrict commands by role at the integration-instance level | exact integration, instance, command, role, execution identity | playbook object access or endpoint-response policy |
| Action Center / response | initiate or monitor consequential actions | exact action permission, target scope, policy/approval, rollback/recovery, audit | correctness of the trigger |
| API | programmatic product function | current product API guide, tenant FQDN, auth, role/SBAC, endpoint schema, bounded errors/retries | endpoint existence in another product or production readiness |

### Interactive XQL is not a universal rule language

Never reuse a Query Center pipeline unchanged in BIOC, scheduled correlation, real-time correlation, or XQLp simply because it compiled interactively. Each target needs its own current documentation and editor/compiler evidence. Route mechanics to the XQL and detection owners.

### State-changing surfaces

Treat these as writes even if initiated from a query or analysis workflow:

- XQL `target` persistence;
- saved-object create/edit/delete/share/import;
- rule creation, enablement, disablement, exceptions, and prevention;
- playbook, script, Job, or integration-command execution;
- indicator creation, reputation override, block/allow list, EDL, feed export, or endpoint prevention;
- data-source/collector/integration configuration;
- role, scope, credential, license, or policy changes;
- endpoint or cloud response.

Read-only review does not authorize any of them.

## Permission and entitlement chain

Model permissions as a dependency graph, not a role-name shortcut:

1. product tenant and license/edition;
2. feature/component role permission;
3. dataset or object access;
4. RBAC and SBAC/data scope;
5. dependent component permissions;
6. integration-instance and command permission;
7. target/action permission;
8. organizational policy and human approval.

Examples from current XSIAM documentation:

- Query Center `View` does not permit running new queries; `View/Edit` provides broader query operations, while SBAC can still restrict results.
- In XSIAM, **Datasets Rows** filters apply to raw datasets and do not support XDM queries. Current guidance, rechecked on 2026-09-06, says XDM returns rows only when **All rows are accessible** is selected and no filter is defined in that scoping area. Raw results and empty XDM results can therefore be an access-model issue; inspect the effective identity and scope before blaming ingestion/mapping. Do not remove filters or broaden access as a diagnostic shortcut.
- BIOC and correlation editing depends on Query Center access.
- playbook/script visibility combines role-level permissions with object ownership/sharing; parent access does not imply editable visibility into every dependency.
- integration commands can be restricted per role and instance, independently of playbook visibility.
- TIM needs an applicable license as well as permissions.
- Graph Search has its own license and permission dependencies.

These are documentation statements, not observations of a particular tenant.

The XDM/scoping statement is `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED`:
[Manage user access — XSIAM](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/onboard-cortex-xsiam/post-deployment/manage-user-roles-and-access-management/manage-user-access.md).
For a filtered identity, route exact query/access design to the platform and data
owners and retain an authorized raw-dataset workflow where suitable.

## Common ambiguous terms

| User term | Clarify |
|---|---|
| “Cortex” | exact product, release, tenant, and surface |
| “application” | installed endpoint software, DLP application definition, Business Application, API application, or integration |
| “rule” | IOC, BIOC, analytic, scheduled correlation, real-time correlation, cloud posture/runtime rule, issue rule, or policy |
| “query” | Query Center, saved/scheduled query, rule predicate, API-run XQL, graph query, or XQLp parser |
| “incident” | XSOAR incident, XDR incident, XSIAM Case/Issue, or external ticket |
| “automation” | playbook, script, Quick Action, Job, response action, Agentic action, or third-party workflow |
| “block” | indicator list, endpoint prevention, network enforcement, integration command, or a policy decision |
| “owner” | business risk owner, technical artifact owner, operator, approver, data owner, or recovery owner |

## Selection record

Record:

| Field | Value |
|---|---|
| Product/release | `<value or unknown>` |
| License/rollout | `<observed or requires validation>` |
| Surface/object type | `<exact value>` |
| Environment | `<design/dev/non-production/production>` |
| Identity and scope | `<safe alias; RBAC/SBAC/object/data scope>` |
| Intended operation | `<read/design/validate/write/respond>` |
| Current evidence | `<class / qualifiers / date>` |
| Material alternative | `<alternative if ambiguity remains>` |
| Discriminating check | `<smallest check>` |
