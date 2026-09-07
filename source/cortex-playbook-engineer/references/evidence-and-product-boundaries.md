# Evidence and Product Boundaries

**Documentation review cut:** 2026-09-04  
**Tenant status:** no tenant, installed-content inventory, command schema, playbook export, validator result, import, or execution evidence was available.  
**Document role:** standalone reference guidance; not an importable playbook artifact.
**Official evidence index:** [source register](official-sources.md); applicability remains limited to each source's named product and release.

## Contents

- [Source precedence](#source-precedence)
- [Canonical claim status](#canonical-claim-status)
- [Provenance and validation qualifiers](#provenance-and-validation-qualifiers)
- [Artifact classification](#artifact-classification)
- [Validation ladder](#validation-ladder)
- [Product and terminology boundaries](#product-and-terminology-boundaries)
- [Project-specific knowledge](#project-specific-knowledge)
- [Fail-closed decision rule](#fail-closed-decision-rule)
- [Handoff boundary](#handoff-boundary)

## Source precedence

Use this order for factual product behavior:

1. current official Palo Alto Networks documentation;
2. official Palo Alto examples, repositories, API references, and guides;
3. directly inspected, verified project-specific knowledge;
4. secondary sources only when necessary.

An official example demonstrates one revision; it does not prove tenant installation or universal support. A local artifact establishes what its bytes contain; it does not override current product documentation. Preserve conflicts and classify them as legacy, customized, version-specific, incorrect, or unresolved.

## Canonical claim status

Give each material claim exactly one primary status.

| Status | Meaning |
|---|---|
| `VERIFIED` | Directly supported by cited evidence applicable to the named product/surface |
| `VERSION-DEPENDENT` | Support changes with product, release, deployment, license, or surface |
| `INFERRED` | Bounded conclusion derived from evidence but not directly documented |
| `CONCEPTUAL` | Design or pseudoflow, not a product artifact or syntax claim |
| `UNSUPPORTED` | Applicable evidence establishes that behavior is not supported |
| `DEPRECATED` | Current official evidence labels the surface obsolete or replaced |
| `UNVERIFIED` | Available evidence cannot establish the claim |

Do not combine statuses such as “verified but unverified.” Instead, apply one status to each distinct claim and record its qualifier.

## Provenance and validation qualifiers

Qualifiers never replace the primary status.

| Qualifier | Meaning |
|---|---|
| `OFFICIAL-CURRENT` | Current first-party documentation was reviewed |
| `OFFICIAL-EXAMPLE` | A first-party example/repository revision was reviewed |
| `LOCAL-VERIFIED` | Local bytes or structure were inspected |
| `PROJECT-ASSERTED` | Project material makes the claim without underlying runtime evidence |
| `DERIVATIVE` | The material summarizes another source |
| `REFERENCED-ONLY` | A source is named/hashed but its bytes are absent |
| `TENANT-UNVERIFIED` | Target tenant content, schema, permissions, or behavior was not checked |
| `TENANT-SCHEMA-VERIFIED` | Required data/command/context schema was observed in the named tenant |
| `TENANT-COMPILED` | The named validator/editor accepted the exact artifact |
| `TENANT-EXECUTED` | The exact artifact ran under recorded scope and produced retained evidence |

Examples:

- XSIAM sub-playbook separation documented generally, tenant not inspected: `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED`.
- XSOAR 8.14 behavior proposed for an unknown XSOAR release: `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED`.
- Unsafe branch described by a summary whose YAML is missing: `UNVERIFIED / PROJECT-ASSERTED / REFERENCED-ONLY`.
- A compensating-action pattern with no native implementation selected: `CONCEPTUAL / DERIVATIVE`.

## Artifact classification

Classification applies to every proposed playbook deliverable, independently of claim status.

### `CONCEPTUAL`

Use for an architecture, graph sketch, state machine, decision table, or pseudoflow. Avoid executable-looking YAML/JSON and exact command/path placeholders that resemble validated product content. State what must be selected and verified.

### `CONFIGURATION GUIDANCE`

Use when current official product documentation establishes the relevant native concept, but the target tenant or deployment is not fully validated. Identify product/release, installed-content requirements, exact items still unknown, validation steps, and safety controls. Configuration guidance is not import-ready.

### `VERIFIED IMPORTABLE ARTIFACT`

Use only when retained evidence includes all of:

1. exact exported artifact and SHA-256;
2. target product, deployment, build/release, and tenant alias;
3. export/import schema or official content format applicable to that target;
4. installed pack, script, integration, and sub-playbook dependencies with versions;
5. exact command arguments and output schemas;
6. static validator/SDK name, version, environment, command, and passing output;
7. controlled import with successful readback;
8. functional test with representative fixtures and protected actions safely stubbed or authorized;
9. error, timeout, retry, loop, permission, approval, idempotency, and partial-failure results; and
10. reviewer independent of authorship.

If one required item is absent, downgrade the artifact. Do not guess the missing YAML/JSON, task UUID, command, context path, close reason, or dependency metadata.

## Validation ladder

| Level | Establishes | Does not establish |
|---|---|---|
| `S` | Static structure or controlled response behavior | Product support, tenant schema, import, or execution |
| `D` | Current official documentation for the stated behavior | Tenant content, permissions, or execution |
| `C` | Named validator/schema acceptance or controlled import | Correct business behavior or safe external side effects |
| `E` | Bounded execution/readback in a recorded environment | Universal or future product support |

Record `PASS`, `FAIL`, `NOT RUN`, or `N/A` at each level. A successful import is not a safe-run claim. A successful dry path is not evidence for an action path. A debugger session is execution evidence only for what actually ran and may still cause real side effects.

## Product and terminology boundaries

| Dimension | Cortex XSIAM | Cortex XSOAR |
|---|---|---|
| Current primary automation object language | Current documentation uses Case and Issue | Version-scoped XSOAR documentation can use incident terminology |
| Context | Current XSIAM documents Issue and parent Case context with some legacy implementation literals | XSOAR context behavior must be taken from the named XSOAR deployment/release |
| Trigger | XSIAM playbooks can be associated with automation rules, run manually, used as sub-playbooks, or scheduled/event-driven through documented Jobs | Use the named XSOAR release's incident/job/playbook guidance |
| Access | Object access, Case/Issue permissions, effective identity, and per-instance command restrictions are separate checks | Use the named XSOAR role/integration-permission model |
| Artifact format | Obtain an export from the target surface or current supported developer schema | Obtain an export/schema for the exact XSOAR deployment/release |

Guardrails:

- Never rename a literal technical key merely to modernize prose.
- Never infer that a matching label has the same schema across products.
- Never treat Case, Issue, incident, alert, Insight, Finding, context, and field objects as interchangeable.
- Never treat “private” sub-playbook context as a security boundary.
- Never infer a supported close reason, command, argument, or output from screenshots or prior content.

## Project-specific knowledge

Readable project material contributes useful patterns:

- explicit parent/child inputs and outputs;
- namespaced context;
- deterministic decisions with advisory AI;
- degraded failure paths;
- shadow-mode concepts;
- idempotency/no-overlap goals;
- approval before containment;
- secret and prompt-injection controls.

However, original playbook YAML/Python/PDF files referenced by the project summaries were unavailable. Reported flaws—including unsafe DBotScore handling, literal containment inputs, mixed context namespaces, fabricated observables, missing pagination/deduplication, and possible secret exposure—remain `UNVERIFIED / PROJECT-ASSERTED / REFERENCED-ONLY`. Use them as adversarial fixtures, not current product facts.

The official DBotScore convention is `0 Unknown`, `1 Good`, `2 Suspicious`, and `3 Bad`. That documented semantic does not prove a summarized playbook actually contains the alleged branch, and no score alone authorizes destructive action.

## Fail-closed decision rule

Before showing exact executable/import-like content:

1. identify the product, deployment, version, and surface;
2. inventory every command, path, task type, field, input/output, setting, and dependency;
3. verify each construct against a current official source or exact target export;
4. verify tenant installation, schema, permissions, and identity when claiming target compatibility;
5. obtain controlled import and execution evidence before claiming importability or behavior;
6. downgrade unknown portions to visible conceptual placeholders; and
7. state the smallest next validation step.

When in doubt, omit syntax. A complete conceptual control design is safer and more useful than plausible but false YAML.

## Handoff boundary

- Detection engineering supplies trigger semantics, quality, and false-positive controls.
- Platform engineering validates content deployment, engines, integrations, credentials, network path, and RBAC.
- Threat-intelligence engineering owns indicator lifecycle and reputation policy.
- Security engineering owns organization-level policy and risk acceptance.

This Skill still produces the complete playbook design, context contract, failure model, and validation plan without requiring any sibling package.
