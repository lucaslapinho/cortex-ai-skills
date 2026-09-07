# Example: Cross-Product Boundary

## Scenario

The requester says: “Build a Cortex automation that searches applications, creates a rule, and closes the incident.”

No product, release, object family, or desired state change is specified.

## Material question

Ask:

> Which exact Cortex product/release and object families are in scope—XSIAM Cases/Issues, XDR investigations, XSOAR incidents, or Cortex Cloud cases; and does “applications” mean installed endpoint software, DLP Endpoint Application definitions, or Business Applications?

This one answer changes data, permission, automation, rule, and safety mechanics.

## Bounded branches while waiting

### Cortex XSIAM

Potential surfaces include Query Center, Detection Rules, Cases/Issues, playbooks/scripts, Jobs, TIM, Data Sources & Integrations, and integration-command permissions. Current documentation says these have distinct role, scope, object, and dependency controls. A query, rule, case, playbook, Job, and response action are not interchangeable.

### Cortex XDR

Use current XDR-specific investigation, data, detection, response, automation, and API documentation. Do not import XSIAM navigation or permissions merely because terms overlap.

### Cortex XSOAR

Use the exact XSOAR major version/deployment model. Incident/case, playbook, integration, content, and API behavior are versioned and distinct from XSIAM Cases/Issues.

### Cortex Cloud

Use the exact Cloud Application/Posture/Runtime module and license. Business Applications and cloud asset/finding/case surfaces do not prove installed endpoint software or XSIAM dataset semantics.

## State-change boundary

“Creates a rule” and “closes the incident/case” are writes. They require:

- explicit object type and intended state;
- organizational policy and accountable owner;
- exact role/SBAC/object/data permissions;
- trigger semantics and evidence;
- concurrency/idempotency and partial-failure behavior;
- rollback/reopen/recovery;
- post-action verification and audit record.

An automation object being visible does not establish its tasks can run, its integration commands are permitted, or the close action is authorized.

## Standalone deliverable

Until clarified, provide:

- requirement: search the selected application object family, produce a reviewable candidate, and change case/incident state only under approved conditions;
- threat/risk: distinguish detection need from asset/posture inventory and business workflow;
- telemetry contract: exact object source, entity keys, time, coverage, scope, and provenance;
- control contracts: search/investigation -> target-specific rule -> approval-gated automation;
- validation: positive, benign, negative, null, denied, duplicate, partial failure, reopen/recovery;
- operations: owners, health/outcomes, exceptions, audit, review, retirement;
- decision: `HOLD` mechanics and state change until product/object/authorization are resolved.

## Evidence status and non-claims

`CONCEPTUAL / TENANT-UNVERIFIED`. No syntax, API endpoint, dataset, field, rule type, task, setting, incident/case result, execution, or deployment is asserted.
