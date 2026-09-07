# XSIAM and XSOAR Playbook Concepts

**Documentation review cut:** 2026-09-04  
**Default status:** `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED` for named XSIAM behavior; XSOAR statements are `VERSION-DEPENDENT` for 8.14 On-prem.  
**Artifact class:** `CONFIGURATION GUIDANCE`; this document is not a playbook export.
**Primary official evidence:** [source register](official-sources.md), PB01-PB17 for XSIAM and XS01-XS10 for XSOAR 8.14 On-premises.

## Contents

- [Product selection](#product-selection)
- [XSIAM playbook surface](#xsiam-playbook-surface)
- [Triggers and Jobs](#triggers-and-jobs)
- [Tasks, commands, and scripts](#tasks-commands-and-scripts)
- [Sub-playbooks](#sub-playbooks)
- [Conditions, loops, and transforms](#conditions-loops-and-transforms)
- [Context and fields](#context-and-fields)
- [Manual interaction and approvals](#manual-interaction-and-approvals)
- [War Room, evidence, and Quiet Mode](#war-room-evidence-and-quiet-mode)
- [XSOAR 8.14 On-prem boundary](#xsoar-814-on-prem-boundary)
- [Adaptation checklist](#adaptation-checklist)

## Product selection

Do not begin with a generic “Cortex playbook.” Record:

| Dimension | Required value |
|---|---|
| Product | XSIAM or XSOAR |
| Deployment | SaaS/on-premises as applicable |
| Release/build | Exact or unknown |
| Primary object | XSIAM Issue/Case, XSOAR incident, Job, manual/sub-playbook, or other documented object |
| Content source | Custom, system/content-pack, Org repository, Marketplace, export, or conceptual design |
| Edit/update relationship | Attached, detached, duplicated, custom, or unknown |
| Execution identity | Named role/service identity and data scope |
| Dependencies | Installed packs, integrations, scripts, sub-playbooks, credentials, engines/workers |

Matching task names do not establish matching behavior across products or pack versions.

## XSIAM playbook surface

Current XSIAM documentation describes playbooks as visual workflows for investigation, response, and operational automation. The Task Library can expose commands/scripts, sub-playbooks, manual/blank tasks, section headers, and other documented task types. What appears in a particular tenant depends on content and permissions.

Treat the playbook editor as a configuration surface, not an import schema. A narrative design should identify nodes and edges without inventing internal task IDs or YAML properties.

System/content-pack playbooks can have update/attachment behavior and permission restrictions. Duplicating, detaching, editing, or reattaching can change upgrade behavior; current official guidance warns that reattachment can overwrite customizations. Record the content relationship before proposing changes.

## Triggers and Jobs

For XSIAM, current settings guidance distinguishes:

- automation rules that trigger a playbook for matching Issues;
- a playbook with no trigger configuration, suitable for use as a sub-playbook or manual run; and
- Jobs that run playbooks on documented time or event conditions.

Do not treat a Job schedule as a detection-rule schedule. For any trigger, record:

- trigger object/type and product terminology;
- exact condition source and evidence;
- evaluation ordering or competing rules when relevant;
- enablement state;
- replay/duplicate behavior;
- data freshness and expected arrival window;
- maximum concurrent/overlapping executions;
- a stable idempotency key design; and
- a safe no-match/unknown path.

No-overlap and deduplication are engineering requirements unless a cited product feature implements them. Label such controls `CONCEPTUAL` until the exact implementation is selected and tested.

## Tasks, commands, and scripts

Separate task type from task implementation:

- a playbook task may invoke a script or integration command;
- the exact inputs and outputs belong to the installed script/integration version;
- an integration instance and effective command permission can determine whether the task runs;
- selecting a command in documentation or Marketplace content does not prove a tenant exposes it; and
- a task can write context, mutate a Case/Issue, contact an external system, or execute a disruptive action.

Before naming an exact command or argument, collect the target tenant's current command help or a pinned official content definition. Record:

| Item | Evidence required |
|---|---|
| Command/script name | Installed pack/version or pinned official definition |
| Argument | Exact help/schema, type, requiredness, accepted values, secret flag |
| Output | Exact context schema, type, cardinality, empty/error behavior |
| Instance | Enabled target instance, routing/engine, test status |
| Permission | Effective role for the exact command on that instance |
| Side effect | Read/write class, external target, reversibility, evidence/readback |
| Runtime control | Timeout, retries, rate limit, cancellation/reconciliation |

If unavailable, name the required capability rather than inventing a command. Example: “invoke the tenant-verified endpoint-isolation command” is safe conceptual guidance; a guessed command is not.

## Sub-playbooks

Current XSIAM guidance describes a sub-playbook as a playbook nested as a task in a parent playbook. A sub-playbook can itself be a parent elsewhere. Reusable sub-playbooks should use generic, explicit inputs and return explicit outputs.

For each sub-playbook, define:

- one responsibility and owning team;
- version and update relationship;
- input/output groups and contract;
- whether context remains separate or is shared;
- empty and error behavior;
- loop behavior, if any;
- required integrations/scripts/packs;
- protected side effects;
- observability/evidence; and
- compatibility tests for every caller.

Private/default context separation is not RBAC. Global sharing increases coupling and collision risk. Prefer explicit outputs when that preserves the intended data flow.

## Conditions, loops, and transforms

Conditions must enumerate at least true, false, empty/unknown, error, and type-mismatch behavior. Use deterministic conditions before protected actions.

Current XSIAM documentation supports sub-playbook loops with built-in exit behavior, per-input iteration, or selected automation control. It also documents an implementation default/maximum that can change by release. For a safe design, choose and verify an explicit maximum, sleep/interval, exit condition, and total deadline rather than relying on a default.

A loop contract includes:

- input collection type and cardinality;
- pairing behavior for multiple collections;
- item identity and duplicate semantics;
- exit success, terminal error, and timeout conditions;
- maximum iterations and total work bound;
- rate limiting and external service capacity;
- per-item result/error ledger; and
- partial-completion and restart behavior.

Filters and transforms operate on context-selected data. Verify the actual source, type, and cardinality. Do not assume two parallel arrays remain correctly paired without an explicit tested relationship.

## Context and fields

Current XSIAM guidance distinguishes:

- Issue context accessed through documented Issue-context selectors;
- parent Case context through a different legacy-named implementation selector;
- writes to parent Case context through a documented script; and
- parent Case fields as a separate concept from parent Case context.

Do not normalize literal names. For example, `${issue.status}`, `${parentIncidentContext.hostname}`, and `setParentIncidentContext` appear in current XSIAM documentation, but they remain product/version-scoped examples. They do not prove that `hostname` or another custom path exists in the target tenant.

Sub-playbook context is separate by default in current XSIAM guidance unless sharing is configured. Main and sub-playbook tasks do not directly see each other's separate context. Shared/global context changes visibility but does not grant authorization.

See [data contracts and context](data-contracts-and-context.md) for the validation process.

## Manual interaction and approvals

Manual or communication tasks can pause work for human input. A safe approval design identifies:

- the protected action;
- accountable approver role and separation of duties;
- evidence presented to the approver;
- allowed decisions and typed result;
- authentication requirement for external recipients when applicable;
- deadline/SLA, reminder, no-response result, and escalation;
- whether another role can complete the task;
- duplicate/late response handling; and
- immutable audit reference.

Do not equate “manual task exists” with policy approval. Verify who can actually complete it and what happens when the SLA expires.

## War Room, evidence, and Quiet Mode

War Room/task results can support investigation and debugging, but visibility, indexing, and evidence behavior depend on task/playbook settings.

Current XSIAM guidance states that Quiet Mode suppresses saved task inputs/outputs and indicator extraction from task presentation/indexing while context remains available and errors/warnings are written to the War Room. Therefore:

- Quiet Mode is an operational/performance setting, not a confidentiality boundary;
- a design must still minimize secrets and sensitive data in context;
- evidence-required tasks need an intentional record outside suppressed details; and
- troubleshooting must distinguish missing presentation from missing context/output.

Current XSIAM task configuration can register task results as Case timeline records and mark results as evidence where supported. Treat exact options as version-sensitive and verify the target UI. Record source time and effective time deliberately; do not hard-code a fixed time that would be repeated on every execution.

## XSOAR 8.14 On-prem boundary

The bundled XSOAR evidence is explicitly scoped to Cortex XSOAR 8.14 On-prem. It documents playbooks, incidents, integrations, context, error handling, debugging, War Room, Jobs, and engines for that release.

When adapting an XSIAM design to XSOAR or the reverse:

1. relabel the product and object model;
2. re-discover triggers, fields, context, tasks, and close semantics;
3. validate every command against installed packs/instances;
4. re-evaluate roles, engines/workers, credentials, and network path;
5. obtain an export/schema from the target product;
6. rerun error, debugger, loop, and side-effect tests; and
7. keep the result `CONFIGURATION GUIDANCE` until controlled import evidence exists.

Never claim another XSOAR release or SaaS surface matches 8.14 On-prem without an applicable source.

## Adaptation checklist

- [ ] Product, deployment, and release identified
- [ ] Case/Issue versus incident terminology mapped without changing literals
- [ ] Trigger and enablement model revalidated
- [ ] Every input/output/context path revalidated
- [ ] Every command/script and pack version revalidated
- [ ] Sub-playbook context and loop behavior revalidated
- [ ] Object, data, and integration-command permissions tested
- [ ] Error, timeout, retry, and partial-failure behavior tested
- [ ] War Room/evidence/Quiet Mode behavior revalidated
- [ ] Protected actions stubbed until explicit authorization and readback exist
- [ ] Export/import schema and dependencies validated in the target
- [ ] Artifact classification remains honest
