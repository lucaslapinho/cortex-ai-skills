# Skill Domain Boundaries

## Status and purpose

This document defines the Phase 1 separation of concerns for the seven Cortex Skills. It is an architectural boundary, not proof that any product feature is available in a particular tenant. Product behavior must be checked against the official source register in `documentation-sources.md`; project-specific patterns and limitations are summarized in `project-findings.md`.

The governing rule is:

```text
Shared architectural convention != shared runtime dependency
```

Every Skill must remain useful after all sibling directories and every root-level research or review file have been removed.

## Boundary rules shared by all Skills

1. Identify the Cortex product before giving product-specific guidance. Cortex XDR, Cortex XSIAM, Cortex XSOAR, and Cortex Threat Intelligence Management are related but not interchangeable.
2. Attach significant technical claims to one of `VERIFIED`, `VERSION-DEPENDENT`, `INFERRED`, `CONCEPTUAL`, `UNSUPPORTED`, `DEPRECATED`, or `UNVERIFIED`.
3. Treat dataset names, field names, commands, context paths, integration behavior, APIs, entitlements, RBAC, and installed content as tenant- or version-sensitive unless current authoritative evidence establishes otherwise.
4. Preserve current Case/Issue terminology in new prose while retaining literal legacy Incident/Alert identifiers when an API, command, context path, or existing artifact requires them.
5. A Skill may recommend a sibling as an optional deeper specialization. It must still provide a bounded, usable answer when that sibling is absent.
6. A Skill may include the minimum adjacent-domain guidance required to finish its own task. It must label the handoff boundary and avoid reproducing another Skill's full method.
7. Root files under `research/` and `reviews/` are development evidence. They are never runtime prerequisites for a separately published Skill.
8. Project namespaces such as `SOCFramework.*`, `SOCN1.*`, and `Assessment.*` are internal contracts, not vendor-defined fields.
9. Supplied project findings without their original YAML, source repository, tenant, or execution record remain project-asserted. They can motivate tests but cannot establish current product behavior.
10. No Skill may make destructive response automatic solely because another Skill produced a query, score, hypothesis, or detection candidate.

## Responsibility map

| Skill | Primary question | Primary deliverable | Explicitly not the owner of |
|---|---|---|---|
| `cortex-xql-query-engineer` | How should this query be constructed, verified, explained, or optimized? | Evidence-scoped XQL solution or validation diagnosis | Detection lifecycle, hunt program, playbook design, or platform configuration |
| `cortex-detection-engineer` | Should and how should this behavior become a durable detection? | Detection specification, tuning and validation plan | General-purpose query tutoring, iterative hunt execution, or response automation |
| `cortex-playbook-engineer` | How should this response or enrichment workflow be automated safely? | XSIAM/XSOAR playbook design, context contract, and test plan | Detection authorship, platform deployment architecture, or unverified import-ready content |
| `cortex-threat-hunter` | How should a hypothesis be investigated and iteratively scoped? | Hunt plan, pivots, evidence assessment, and detection opportunity | Production detection ownership, automated response, or platform administration |
| `cortex-tim-engineer` | How should threat intelligence and indicators be governed and operationalized? | Indicator/feed lifecycle and control-integration design | General alert ingestion, unrelated data engineering, or incident-response orchestration |
| `cortex-platform-engineer` | How should Cortex infrastructure, ingestion, access, and integrations be designed or troubleshot? | Product-specific platform architecture or troubleshooting plan | Owning detection logic, hunting conclusions, or playbook business decisions |
| `cortex-security-engineer` | Which security-engineering activities and controls solve the requirement? | Cross-domain decomposition and validated engineering roadmap | Reimplementing every specialist's detailed method |

## 1. `cortex-xql-query-engineer`

### Mission

Construct, explain, review, troubleshoot, and optimize XQL for a stated investigation, hunt, or detection-support objective while rejecting invented language features, datasets, and fields.

### Product boundary

- Cortex XDR and Cortex XSIAM surfaces where current official documentation confirms XQL support.
- Product, query mode, dataset model, tenant default, license, permissions, and time range must be named or marked unknown.
- The built-in/default `xdr_data` behavior, XDM queries, mapped datasets, forensic data, result limits, and schema discovery must be described only within their documented context.

### In scope

- XQL syntax and stage ordering.
- Dataset and field discovery or validation workflow.
- Filters, field projection, parsing, joins, aggregation, `alter`, `comp`, `dedup`, timeframes, readability, and performance when the exact construct is verified.
- Investigation, hunting, and detection-supporting queries.
- Broken-query diagnosis, null/type handling, cardinality risk, expected output, and validation steps.
- A standard answer containing objective, product, evidence status, assumptions, dataset, fields, executable query, explanation, expected output, limitations, troubleshooting, checklist, and official references when applicable.

### Out of scope

- Deciding that a query is ready to become a production correlation rule.
- Owning thresholds, alert grouping, rule lifecycle, ATT&CK coverage, or false-positive operations beyond query-level observations.
- Designing playbook graphs or response approvals.
- Inventing tenant fields from endpoint exports, project namespaces, or examples.
- Claiming execution when no tenant/parser result exists.

### Inputs

- Security objective and target product.
- Tenant/version/license information when available.
- Time range, known dataset/schema evidence, sample records, current query, error text, and performance symptoms.
- Constraints on output fields, latency, cardinality, and intended use.

### Outputs

- An executable query only when every executable-looking construct is supported by adequate evidence.
- A separate annotated explanation when comments are unsupported or uncertain in the execution surface.
- A validation plan or narrow probe query when dataset/field existence is tenant-unverified.
- A defect list for broken or unsafe queries, with evidence labels and corrections.

### Overlap and handoff

- To Detection: provide verified query logic and signal semantics; Detection owns production rule design and tuning.
- To Hunting: provide query mechanics; Hunting owns hypotheses, pivots, scope, and conclusions.
- To Platform: request schema, ingestion, permissions, or missing-dataset investigation when the query cannot observe expected data.
- Standalone fallback: explain the adjacent concern and provide a handoff-ready checklist without requiring those Skills.

## 2. `cortex-detection-engineer`

### Mission

Transform evidenced threat behavior into a maintainable, testable detection specification with explicit telemetry, expected signal, false-positive model, tuning, and lifecycle controls.

### Product boundary

- Cortex XSIAM and Cortex XDR detection or correlation surfaces only where the relevant rule type and configuration are officially verified.
- XQL-based correlation behavior must be distinguished from other detection mechanisms.
- Product-specific rule options, case grouping, issue promotion, schedules, thresholds, and limits must not be generalized across products.

### In scope

- Threat model and ATT&CK mapping as versioned interpretation rather than proof.
- Required telemetry, coverage gaps, data quality, query-to-signal logic, baselines, thresholds, suppression/tuning considerations, test fixtures, false positives, monitoring, rollback, and retirement.
- Correlation-rule supporting XQL and the documented 24-hour hit-volume safety constraint where applicable.
- Conversion of hunt findings into candidate detections.
- Relationship among telemetry, query, signal, Issue/Alert, Case/Incident, and investigation, using current and legacy terminology deliberately.

### Out of scope

- General XQL tutoring unrelated to a detection outcome.
- Declaring ATT&CK mapping, an alert, or a single query hit as proof of compromise.
- Inventing correlation-rule settings, field schemas, promotion criteria, or license availability.
- Designing containment playbooks or approving destructive actions.

### Inputs

- Threat behavior and desired security outcome.
- Product/rule surface, available telemetry, schema evidence, baseline period, risk tolerance, and existing rule/query.
- Historical positives/negatives, known benign activity, alert volume, response capacity, and validation environment.

### Outputs

- Detection specification: behavior, product, evidence status, ATT&CK interpretation, telemetry, logic, thresholds/baseline, expected signal, test cases, tuning, false positives, coverage limits, monitoring, and official references.
- Clearly labeled candidate XQL or pseudologic; executable XQL only when verified.
- Promotion criteria from experimental to production and rollback/disable criteria.

### Overlap and handoff

- XQL owns precise query construction; Detection owns whether and how the logic becomes a durable rule.
- Threat Hunting supplies observations and pivots; Detection requires repeatable behavior and coverage before production.
- Playbook owns downstream automation; a detection may specify response requirements but not implement them.
- Standalone fallback: include a minimal verified query/response interface sufficient to specify the detection, with uncertainty explicit.

## 3. `cortex-playbook-engineer`

### Mission

Design, review, troubleshoot, and safely evolve Cortex XSIAM/XSOAR playbooks and sub-playbooks with explicit data contracts, failure behavior, authorization, and human gates.

### Product boundary

- Cortex XSIAM and Cortex XSOAR automation must be treated as distinct deployment surfaces.
- New user-facing designs use Case/Issue terminology; literal Incident/Alert names remain when required by supported legacy interfaces.
- Context paths, command schemas, close reasons, integrations, jobs, roles, and content-pack formats require exact product/version/tenant evidence.

### In scope

- Triggers, inputs, outputs, tasks, conditions, loops, sub-playbooks, context data, integrations, scripts/automations, enrichment, notification, SLA, War Room behavior, retries, fallback, timeouts, errors, idempotency, observability, testing, and modularization.
- Parent/child context contracts, including deliberate distinction among Issue context, parent Case context, and supported Case fields.
- Design patterns such as shadow mode, deterministic decision gates, advisory AI, degraded failure, and no-overlap/idempotent jobs when presented as project patterns rather than vendor guarantees.
- Safety gates for isolation, account changes, blocking, termination, deletion, remediation, firewall changes, and revocation.

### Out of scope

- Presenting conceptual flows as import-ready YAML.
- Treating separate sub-playbook context as an authorization or confidentiality boundary.
- Guessing integration commands, input/output keys, task IDs, close reasons, or installed content.
- Treating DBotScore `0` as good or allowing an advisory LLM to authorize destructive action.
- Owning detection-quality decisions or general platform administration.

### Inputs

- Target product and deployment model.
- Trigger, business decision, actors/approvers, current graph/export, installed integrations and versions, command help, inputs/outputs, context samples, errors, SLA, and rollback requirements.
- Classification target: `CONCEPTUAL`, `CONFIGURATION GUIDANCE`, or `VERIFIED IMPORTABLE ARTIFACT`.

### Outputs

- Playbook design with the fields required by the master specification, including context contract, approval gates, failure paths, evidence, idempotency, security, tests, and references.
- Graph/contract defect report for existing content.
- Import-ready artifact only when its schema, commands, dependencies, version, and validator/runtime results are genuinely verified.

### Overlap and handoff

- Detection defines why an Issue/Alert should trigger; Playbook defines what automation follows.
- TIM owns indicator lifecycle; Playbook may call verified enrichment or distribution actions under a declared contract.
- Platform owns integration/RBAC/deployment failures; Playbook owns flow logic and data propagation.
- Security Engineer may set response policy; Playbook implements the approved workflow.
- Standalone fallback: supply a conservative conceptual design and an exact tenant-verification checklist instead of requiring another Skill.

## 4. `cortex-threat-hunter`

### Mission

Run hypothesis-driven, iterative hunting across available Cortex telemetry, distinguish observations from conclusions, and turn repeatable findings into well-scoped detection opportunities.

### Product boundary

- Cortex XDR and Cortex XSIAM hunting surfaces where data access and query capabilities are verified.
- Retention, field coverage, permissions, mapped datasets, enrichment, and entity availability are tenant-sensitive.

### In scope

- Hypothesis, threat context, ATT&CK interpretation, required telemetry, initial query plan, observations, pivots, enrichment, timeline, entity scoping, alternatives, confidence, and conclusion.
- IOC, TTP, behavioral, anomaly, campaign, identity, endpoint, DNS/network, and cross-entity hunting when corresponding telemetry exists.
- Query iteration and conversion of supported findings into a detection candidate.
- Coverage-aware negative evidence and smallest discriminating next collection/query step.

### Out of scope

- Declaring no activity solely because a query returned no rows.
- Treating an IOC match, parser label, or ATT&CK mapping as proof of compromise or attribution.
- Owning production rule tuning, playbook automation, or platform ingestion changes.
- Inventing queries when fields/datasets are unknown.

### Inputs

- Testable hypothesis, scope, entities, time range, product, telemetry inventory, known indicators/behaviors, existing queries, and evidence already observed.
- Coverage, retention, clock, parser, permission, and data-quality information when available.

### Outputs

- Hunt record: hypothesis, product, evidence status, telemetry, queries or query plan, observations, pivots, timeline, scope, alternatives, confidence, gaps, conclusion, and detection opportunity.
- Executable XQL only when verified; otherwise a schema-discovery and validation sequence.

### Overlap and handoff

- XQL owns language-level correctness; Hunting owns investigative iteration.
- Detection owns the production lifecycle of a repeatable candidate.
- Platform owns missing telemetry and permissions; Hunting records how gaps affect confidence.
- TIM owns indicator governance; Hunting uses indicators as leads, not verdicts.
- Standalone fallback: perform the full hunt-method workflow and provide bounded query/detection guidance without assuming sibling availability.

## 5. `cortex-tim-engineer`

### Mission

Design and troubleshoot the lifecycle of threat intelligence and indicators from acquisition through normalization, confidence, enrichment, governance, expiration, distribution, and measured operational use.

### Product boundary

- Cortex Threat Intelligence Management functionality only where the target XSIAM/XSOAR product, license/add-on, engine, integration, and role support it.
- STIX, TAXII, MISP, EDL, OpenCTI, and indicator commands are interoperability families, not evidence of identical behavior in every Cortex product.

### In scope

- Feed and source governance; indicator normalization, deduplication, confidence, reputation, scoring, tagging, expiration, enrichment, relationships, pagination, provenance, and lifecycle.
- TAXII/STIX/MISP/OpenCTI ingestion design and controlled indicator distribution when current integration behavior is verified.
- EDL design using the current supported integration path; legacy PAN-OS EDL integration is documented as deprecated.
- DBotScore semantics, including `0 = Unknown`, without equating Unknown to Good.
- Operationalization policy that separates collection, management, enrichment, lifecycle, distribution, and security-control action.

### Out of scope

- Treating every external record as a valid indicator or every score as a containment decision.
- Assuming generic STIX/TAXII support establishes collection/version/filter/pagination behavior.
- General log or alert ingestion unrelated to threat intelligence.
- Inventing an API successor for a legacy interface or using fabricated observables as defaults.

### Inputs

- Target product, license, source type, protocol/integration version, schema, collection/filter, trust policy, expected volume, deduplication key, expiration rules, destination controls, and observed errors.

### Outputs

- Source-to-control lifecycle design with provenance, schema validation, deduplication, confidence/reputation policy, expiration, error handling, rate/pagination behavior, RBAC, tests, and references.
- Troubleshooting diagnosis or migration plan with deprecated and version-dependent behavior labeled.

### Overlap and handoff

- Playbook may orchestrate verified TIM actions; TIM owns indicator semantics and lifecycle.
- Threat Hunting consumes indicators as pivots; TIM describes their provenance and uncertainty.
- Platform owns transport, integration instance, authentication, and deployment; TIM owns intelligence policy.
- Security Engineer owns organization-wide risk/control decisions.
- Standalone fallback: provide complete lifecycle guidance plus product-verification gates without relying on other Skills.

## 6. `cortex-platform-engineer`

### Mission

Design, administer, integrate, and troubleshoot Cortex platform capabilities, data flows, access controls, collection, and deployment while maintaining exact product and version boundaries.

### Product boundary

- Cortex XDR, Cortex XSIAM, Cortex XSOAR, Broker VM, collectors, agents, integrations, APIs, ingestion, and related administration only where officially supported for the stated product.
- Architecture guidance and concrete configuration must be separated. No parameter, endpoint, permission, or command is assumed transferable across products.

### In scope

- Architecture, deployment, agents, collectors, Broker VM, integrations, authentication, APIs, RBAC, syslog/cloud/log ingestion, datasets, mapping/parsing, data flow, content packaging, and operational troubleshooting.
- Missing-telemetry workflow from expected data through source, collector/agent/integration, transport, ingestion, parsing/mapping, dataset, permissions, and query visibility.
- Current content-pack contribution structure and supported validation environment.
- API lifecycle, including explicit handling of legacy interfaces without inventing successors.
- Host Inventory/export provenance and object-family distinction.

### Out of scope

- Inventing Broker VM capabilities, collector parameters, dataset names, API fields, or entitlement behavior.
- Treating `send_events_to_xsiam()` as supported from custom integrations without proven system-integration provenance.
- Designing threat logic, hunt conclusions, or playbook business branches except where needed to diagnose platform interfaces.
- Treating installed endpoint applications, Business Applications, and DLP application definitions as one schema.

### Inputs

- Product/edition/version/deployment model, tenant region/FQDN placeholder, architecture diagram, source and transport, collector/agent/integration metadata, authentication model, roles, logs, errors, expected dataset/schema, content-pack target, and change constraints.

### Outputs

- Product-scoped architecture or troubleshooting record with observed state, expected path, evidence status, hypotheses, discriminating checks, configuration guidance, change impact, rollback, validation, and official references.
- No secret values; only placeholders such as `${CORTEX_FQDN}`, `${CORTEX_API_KEY_ID}`, and `${CORTEX_API_KEY}`.

### Overlap and handoff

- XQL validates query visibility after the data plane is established; Platform owns why data is absent or inaccessible.
- Playbook owns flow semantics; Platform owns installed integrations, command exposure, RBAC, content deployment, and runtime plumbing.
- TIM owns indicator policy; Platform owns the supported integration path.
- Standalone fallback: provide enough adjacent-domain validation to close a platform diagnosis without requiring siblings.

## 7. `cortex-security-engineer`

### Mission

Translate broad or ambiguous security requirements into a safe, evidence-backed Cortex engineering workflow, identify the dominant domain, coordinate dependencies conceptually, and define acceptance criteria.

### Product boundary

- May reason across Cortex XDR, XSIAM, XSOAR, and TIM, but every capability remains tied to its real product, edition/license, deployment model, and evidence.
- This Skill is an orchestration layer, not a fictional unified Cortex control plane.

### In scope

- Requirement clarification, product identification, threat model, telemetry needs, investigation/hunt, query needs, detection opportunity, automation opportunity, response policy, approval, validation, governance, and residual risk.
- Domain classification as primary and secondary responsibilities.
- Security architecture: least privilege, secret handling, prompt-injection resistance, deterministic gates, human approval, blast radius, rollback, post-action verification, privacy, and auditability.
- A coherent roadmap when multiple specialties are needed.

### Out of scope

- Duplicating complete XQL, detection, hunting, playbook, TIM, and platform manuals.
- Inventing implementation details to make an orchestration plan look complete.
- Authorizing destructive action, changing systems, or asserting business risk acceptance.
- Treating project findings as confirmed deployment defects without original evidence.

### Inputs

- Desired outcome, threat/risk context, in-scope products and systems, business criticality, authority, data sources, existing controls, response tolerance, constraints, stakeholders, and evidence already available.

### Outputs

- Domain decomposition showing primary and secondary ownership.
- End-to-end engineering plan with evidence gates, dependencies, sequence, safety decisions, acceptance tests, owners, limitations, and references.
- Sufficient standalone detail for the user to begin each activity, plus optional recommendations for deeper specialist work.

### Overlap and handoff

- It may frame and sequence every specialist domain but must stop before unnecessary implementation depth.
- It must retain a minimal product-boundary, evidence, safety, and validation model internally so it remains useful alone.
- Recommendations to install or use another Skill are optional accelerators, never prerequisites.

## Routing ambiguous requests

| User intent | Primary Skill | Secondary concern |
|---|---|---|
| “Fix or optimize this XQL.” | XQL | Detection or Hunting only if the objective requires it |
| “Turn this behavior into a reliable rule.” | Detection | XQL for implementation; Hunting for discovery evidence |
| “Investigate whether this behavior is occurring.” | Threat Hunter | XQL for query mechanics; Platform for missing data |
| “Automate enrichment, decision, or response.” | Playbook | Detection for trigger quality; Platform for integrations; Security for action policy |
| “Manage or distribute indicators.” | TIM | Platform for connectivity; Playbook for orchestration |
| “Why is data, a dataset, command, or integration unavailable?” | Platform | XQL or Playbook after the underlying access/data path is restored |
| “Design the whole Cortex security solution.” | Security Engineer | One or more specialist domains after decomposition |

When two domains appear equally central, select the Skill responsible for the requested final deliverable. Record the other domain as a dependency or validation boundary; do not merge two full output contracts.

## Standalone acceptance contract

Each Skill passes its boundary gate only if a temporary copy containing that Skill alone can:

- identify its own purpose, exclusions, and applicable products;
- locate all references, templates, examples, and tests through paths inside its directory;
- apply the evidence labels and current-versus-legacy terminology policy;
- refuse or safely downgrade unverified executable-looking content;
- produce its primary deliverable without opening a sibling or root research file;
- explain the adjacent-domain boundary and offer a usable fallback;
- complete its own behavioral, ambiguity, troubleshooting, regression, security, and adversarial tests;
- report missing tenant evidence instead of fabricating it.

Controlled duplication of small evidence, terminology, safety, and output-contract sections is required when it is the minimum needed to satisfy this gate.

## Phase 1 boundary findings

- No supplied saved XQL query, live schema, correlation rule, current playbook YAML, integration instance, or tenant execution result can validate executable artifacts.
- Project context contributes useful naming, workflow, safety, and test patterns, but many implementation findings remain project-asserted or tenant-unverified.
- Current official terminology and support boundaries override conflicting project generalizations; literal legacy identifiers remain preserved where compatibility requires them.
- The seven domains are separable without mandatory runtime dependencies. Cross-domain work is represented through contracts and optional handoffs.

**Boundary quality gate:** `PASS FOR GOLDEN-REFERENCE DESIGN`

This workstream result does not determine the consolidated Phase 1 state. Only `phase-1-checkpoint.md`, after independent review, may authorize implementation of `cortex-xql-query-engineer`. It does not approve that Skill, freeze the final architecture, or authorize parallel implementation of the remaining six Skills.
