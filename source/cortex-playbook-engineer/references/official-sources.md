# Official Source Register

**Review date:** 2026-09-04  
**Scope:** current first-party Palo Alto Networks documentation and version-pinned official repositories.  
**Freshness rule:** re-open the exact product/release page before a production or import decision. HTTP reachability does not prove tenant availability.

## Classification policy

- `VERIFIED / OFFICIAL-CURRENT` applies only to the behavior stated by the cited page for its named product/surface.
- `VERSION-DEPENDENT / OFFICIAL-CURRENT` applies when release, deployment, license, or surface matters.
- Official repository content is `OFFICIAL-EXAMPLE`; pin the reused revision and do not infer tenant installation.
- Every source below is `TENANT-UNVERIFIED` for this Skill release.

## Cortex XSIAM automation and playbooks

| ID | Title | Capability and applicability | Official URL | Evidence and limitation |
|---|---|---|---|---|
| PB01 | Automation in Cortex XSIAM | XSIAM automation surface and triggers | [Official documentation](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/automation-in-cortex-xsiam.md) | `VERIFIED / OFFICIAL-CURRENT`; tenant rules/content unknown |
| PB02 | Playbooks overview | Visual playbooks, task library, debugger-first then representative-Issue testing | [Official documentation](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/playbooks/playbooks-overview.md) | `VERIFIED / OFFICIAL-CURRENT`; design review is not runtime evidence |
| PB03 | Plan your playbook | Manual decisions, time-sensitive behavior, and closure planning | [Official documentation](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/playbooks/plan-your-playbook.md) | `VERIFIED / OFFICIAL-CURRENT` |
| PB04 | Configure playbook settings | Triggers, grouped inputs/outputs, edit access, Quiet Mode | [Official documentation](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/playbooks/build-your-playbook/configure-playbook-settings.md) | `VERIFIED / OFFICIAL-CURRENT`; exact UI/permissions tenant-dependent |
| PB05 | Add sub-playbooks | Nested reusable playbooks and explicit inputs/outputs | [Official documentation](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/playbooks/build-your-playbook/add-objects-from-the-task-library/add-sub-playbooks.md) | `VERIFIED / OFFICIAL-CURRENT`; installed catalog/pack versions unknown |
| PB06 | Create a conditional task | Native branch/task configuration, retries, timeout, evidence and error settings | [Official documentation](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/playbooks/build-your-playbook/add-objects-from-the-task-library/add-manual-tasks-and-blank-tasks/create-a-conditional-task.md) | `VERIFIED / OFFICIAL-CURRENT`; task-specific settings must be rechecked |
| PB07 | Configure script error handling | Stop, Continue, and Continue on error path(s) for supported script tasks | [Official documentation](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/playbooks/build-your-playbook/add-objects-from-the-task-library/configure-script-error-handling-in-a-playbook.md) | `VERIFIED / OFFICIAL-CURRENT`; exact pack scripts/paths unknown |
| PB08 | Configure a sub-playbook loop | Built-in, for-each-input, and automation-controlled loop concepts | [Official documentation](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/playbooks/build-your-playbook/customize-your-playbook/configure-a-sub-playbook-loop.md) | `VERSION-DEPENDENT / OFFICIAL-CURRENT`; defaults/maximums must be rechecked |
| PB09 | Use context data in a playbook | Issue context, parent Case context, writes to Case context, sub-playbook scope | [Official documentation](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/context-data/use-context-data-in-a-playbook.md) | `VERSION-DEPENDENT / OFFICIAL-CURRENT`; literal legacy identifiers retained |
| PB10 | Test your playbook | Debugger, mock/existing Issue data, breakpoints, skips, overrides, real task effects | [Official documentation](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/playbooks/build-your-playbook/test-your-playbook.md) | `VERIFIED / OFFICIAL-CURRENT`; no debugger run performed here |
| PB11 | Best practices for playbooks | Naming, contracts, race avoidance, decomposition, Quiet Mode, retries, polling, performance datasets | [Official documentation](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/playbooks/best-practices-for-playbooks.md) | `VERIFIED / OFFICIAL-CURRENT`; specific datasets remain tenant-unverified |
| PB12 | Jobs | Schedule/event-triggered playbook Jobs | [Official documentation](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/jobs.md) | `VERIFIED / OFFICIAL-CURRENT`; permissions/schedule instance unknown |
| PB13 | Manage access to playbooks and scripts | Object access, ownership, sharing, and public-content controls | [Official documentation](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/onboard-cortex-xsiam/post-deployment/manage-user-roles-and-access-management/manage-access-to-objects/manage-access-to-playbooks-and-scripts.md) | `VERIFIED / OFFICIAL-CURRENT`; effective access requires tenant test |
| PB14 | Cases and Issues permissions | XSIAM object authorization effects | [Official documentation](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Cases-and-Issues-permissions) | `VERIFIED / OFFICIAL-CURRENT`; roles/data scope tenant-dependent |
| PB15 | Configure integration permissions | Per-instance command restrictions and Work Plan/CLI effects | [Official documentation](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/cortex-xsiam-data-sources/administration-and-troubleshooting/integrations/configure-integration-permissions.md) | `VERIFIED / OFFICIAL-CURRENT`; exact command permissions unknown |
| PB16 | Playbook development checklist | Planning, building, testing, and deployment review | [Official documentation](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/playbooks/playbook-development-checklist.md) | `VERIFIED / OFFICIAL-CURRENT` |
| PB17 | Troubleshoot playbook performance | XSIAM playbook execution performance investigation | [Official documentation](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/playbooks/build-your-playbook/test-your-playbook/troubleshoot-playbook-performance.md) | `VERIFIED / OFFICIAL-CURRENT`; performance remains unmeasured |

## Cortex XSOAR 8.14 On-prem boundary

| ID | Title | Capability and applicability | Official URL | Evidence and limitation |
|---|---|---|---|---|
| XS01 | What is Cortex XSOAR? | Product and deployment boundary | [Official documentation](https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.14/learn-about-cortex-xsoar/what-is-cortex-xsoar.md) | `VERSION-DEPENDENT / OFFICIAL-CURRENT`; applies to 8.14 On-prem only |
| XS02 | What is a playbook? | XSOAR 8.14 playbook concepts | [Official documentation](https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.14/configure-cortex-xsoar/playbooks/what-is-a-playbook.md) | `VERSION-DEPENDENT / OFFICIAL-CURRENT` |
| XS03 | Develop your playbook | XSOAR 8.14 playbook authoring workflow | [Official documentation](https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.14/configure-cortex-xsoar/playbooks/develop-your-playbook.md) | `VERSION-DEPENDENT / OFFICIAL-CURRENT` |
| XS04 | Use incident context data | XSOAR 8.14 incident context | [Official documentation](https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.14/configure-cortex-xsoar/incident-configuration/incident-customization/use-incident-context-data.md) | `VERSION-DEPENDENT / OFFICIAL-CURRENT`; do not transpose to XSIAM |
| XS05 | Configure script error handling | XSOAR 8.14 error behavior | [Official documentation](https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.14/configure-cortex-xsoar/playbooks/develop-your-playbook/task-3.-add-tasks/configure-script-error-handling-in-a-playbook.md) | `VERSION-DEPENDENT / OFFICIAL-CURRENT` |
| XS06 | Configure a sub-playbook | XSOAR 8.14 nesting and loop surface | [Official documentation](https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.14/configure-cortex-xsoar/playbooks/customize-your-playbook/configure-a-sub-playbook.md) | `VERSION-DEPENDENT / OFFICIAL-CURRENT` |
| XS07 | Debug your playbook | XSOAR 8.14 debugger | [Official documentation](https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.14/configure-cortex-xsoar/playbooks/debug-your-playbook.md) | `VERSION-DEPENDENT / OFFICIAL-CURRENT`; no runtime test performed |
| XS08 | Playbook best practices | XSOAR 8.14 maintainability/reliability guidance | [Official documentation](https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.14/configure-cortex-xsoar/playbooks/best-practices.md) | `VERSION-DEPENDENT / OFFICIAL-CURRENT` |
| XS09 | Configure integration permissions | XSOAR 8.14 command restrictions | [Official documentation](https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.14/configure-cortex-xsoar/integrations/add-an-integration-instance/configure-integration-permissions.md) | `VERSION-DEPENDENT / OFFICIAL-CURRENT`; effective role test required |
| XS10 | Use the War Room | XSOAR 8.14 investigation record surface | [Official documentation](https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.14/investigate-and-respond-to-threats/incidents-and-indicators-investigation/investigate-an-incident/use-the-war-room-in-an-investigation.md) | `VERSION-DEPENDENT / OFFICIAL-CURRENT` |

## Content, integration, and reputation references

| ID | Title | Capability and applicability | Official URL | Evidence and limitation |
|---|---|---|---|---|
| CT01 | demisto/content | First-party packs, integrations, scripts, playbooks, and tests | [Official repository](https://github.com/demisto/content) | `VERIFIED / OFFICIAL-EXAMPLE`; research HEAD `61e517ae49cef61e248791e4c65d06cdeff67ad8`, not tenant proof |
| CT02 | demisto-sdk | Content formatting, validation, and packaging tooling | [Official repository](https://github.com/demisto/demisto-sdk) | `VERIFIED / OFFICIAL-EXAMPLE`; research HEAD `81bd8b125e8219bf8d9283258b12d34b4eb6ae90`, tool version must be pinned |
| CT03 | File checklist | Current contributed-content checklist | [Official developer documentation](https://cortex-docs.paloaltonetworks.com/cortex-xsiam-developer-guide/cortex-xsiam-development-guide/contributing-content/file-checklist.md) | `VERIFIED / OFFICIAL-CURRENT`; target schema/tool still version-sensitive |
| CT04 | Content packs structure | Standard pack layout and entities | [Official developer documentation](https://xsoar.pan.dev/docs/packs/packs-format) | `VERSION-DEPENDENT / OFFICIAL-CURRENT`; not an exact tenant export schema |
| CT05 | Content pack dependencies | Required/optional dependency modeling | [Official developer documentation](https://cortex-docs.paloaltonetworks.com/cortex-xsiam-developer-guide/cortex-xsiam-development-guide/contributing-content/content-pack-dependencies.md) | `VERIFIED / OFFICIAL-CURRENT`; installed graph unknown |
| CT06 | Cortex XSIAM development tenant | Functional content-testing environment | [Official documentation](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Cortex-XSIAM-development-tenant) | `VERSION-DEPENDENT / OFFICIAL-CURRENT`; license required and production parity not implied |
| CT07 | DBotScore | Normalized reputation score convention | [Official developer documentation](https://xsoar.pan.dev/docs/integrations/dbot) | `VERIFIED / OFFICIAL-CURRENT`; score is evidence input, not action authorization |
| CT08 | Generic playbooks | Reusable Common Playbooks | [Official developer documentation](https://cortex-docs.paloaltonetworks.com/cortex-xsiam-developer-guide/cortex-xsiam-development-guide/playbooks/generic-playbooks.md) | `VERSION-DEPENDENT / OFFICIAL-CURRENT`; pack/version/inputs/outputs must be checked |

## Revalidation procedure

### Targeted Astra refresh — 2026-09-06

PB04, PB05, PB07, PB09, PB10, and PB15 were re-opened and read from their exact official Markdown URLs over HTTPS (HTTP 200). Their XSIAM settings, explicit child I/O, script error handling, separate/shared context, debugger effects, and per-instance command permissions remain supported. PB10 explicitly distinguishes a breakpoint from cancellation of already-running parallel tasks. These checks support only those bounded documentation claims; they do not refresh the other register entries or establish tenant applicability, independent response behavior, import, or execution. The historical review date above remains unchanged.

1. Open the exact source and confirm the page title, product, release scope, publication/update state, and absence of deprecation notices.
2. Compare affected behavior with target tenant help, installed pack version, integration command help, and sanitized context.
3. Pin any reused repository file by commit and record its path/hash.
4. Update the relevant reference, template/example, and behavioral regression case together.
5. Run independent documentation and product-boundary review.
6. Keep `C` and `E` as `NOT RUN` until controlled target evidence is retained.
