# Usage examples

[Home](../README.md) · [Installation](instalacao.md) · [Limitations](validacao.md)

The prompts below are example requests, not executed queries, enabled rules, or importable playbooks. Before using them, make the Skill available through your application's supported mechanism. Do not assume that mentioning a name loads a package that is not present.

## Context that improves any response

Provide only what you actually know:

```text
Product: [XSIAM, XDR, or XSOAR; do not treat them as interchangeable].
Version, license, and surface: [available information].
Objective: [the outcome I need].
Data: [schema, query, error, anonymized events, or configuration].
Analysis window and time zone: [specify].
Constraints: [retention, privacy, available integrations].
Authorization: analysis only; no tenant actions.
Deliverable: [proposed query, diagnosis, design, or checklist].
```

Do not include credentials, keys, tokens, real customer names, or unnecessary personal data. Bracketed fields are inputs to complete, not assumed facts.

## 1. Review an XQL query

Skill: [cortex-xql-query-engineer](../source/cortex-xql-query-engineer/README.md).

```text
Use cortex-xql-query-engineer.

Product: Cortex XSIAM.
Objective: review my PowerShell investigation query.
Current query: [paste].
Schema and field types: [attach whatever is available].
Observed error: [paste the exact message or state that there is no error].
Window: [specify dates and time zone].

Preserve the original intent. Explain corrections and their potential
effects on the results. Do not invent datasets, fields, or functions.
If the schema is missing, provide the required checks first.
Consult the applicable official documentation and propose tests.
Do not claim compilation, execution, or performance gains without evidence.
```

**Expected deliverable:** review, schema-dependent proposal, explanation, and verification plan. This is not an actual tenant result.

## 2. Propose a detection

Skill: [cortex-detection-engineer](../source/cortex-detection-engineer/README.md).

```text
Use cortex-detection-engineer.

I want to assess a detection for repeated authentication failures
followed by a success for the same identity.
Product: [specify].
Available telemetry and schema: [attach].
Known legitimate behaviors: [describe].

Define the hypothesis, prerequisites, correlation logic, window,
grouping, entities, and potential false positives.
Do not present a threshold as validated without a baseline.
Include positive, negative, and ambiguous cases, a tuning plan,
and promotion criteria.
Do not create or enable rules in the tenant.
```

**Expected deliverable:** detection specification, gaps, and tests; efficacy and thresholds still require validation.

## 3. Design a phishing playbook

Skill: [cortex-playbook-engineer](../source/cortex-playbook-engineer/README.md).

```text
Use cortex-playbook-engineer.

Design, without executing, a phishing investigation playbook.
Product and version: [specify].
Confirmed integrations and commands: [attach the inventory].
Incident inputs: [list].

Define the main workflow, subplaybooks, input/output contracts,
deterministic decisions, and handling of inconclusive evidence.
Include timeouts, safe retries, partial failures, and recovery.
Require human approval before containment or message removal.
If a command is not verified, mark it as pending.
Do not present the design as importable YAML without validating the format.
```

**Expected deliverable:** operational design, contracts, and a test plan; no containment or import is authorized.

## 4. Conduct threat hunting

Skill: [cortex-threat-hunter](../source/cortex-threat-hunter/README.md).

```text
Use cortex-threat-hunter.

Hypothesis: a compromised identity may have been used to access
multiple endpoints through remote administration.
Product, period, and time zone: [specify].
Available telemetry and gaps: [attach].

Create a hunting plan with questions, pivots, temporal correlation,
entities, and required sources.
Consider legitimate administrative explanations.
Distinguish an absence of events from an absence of coverage.
Do not conclude that a compromise occurred based on one indicator alone.
Provide criteria to confirm, refute, or leave the hypothesis open,
and propose a handoff to detection engineering.
```

**Expected deliverable:** investigation plan with competing hypotheses and coverage limitations.

## 5. Review Threat Intelligence Management

Skill: [cortex-tim-engineer](../source/cortex-tim-engineer/README.md).

```text
Use cortex-tim-engineer.

I want to review the lifecycle of indicators received from feeds.
Product, version, integrations, and formats: [specify].
Current confidence and expiration rules: [describe].
Export consumers: [list without credentials].

Analyze ingestion, normalization, deduplication, enrichment,
classification conflicts, expiration, revocation, and distribution.
Separate intelligence management from blocking actions performed
by downstream consumers.
Document feed failures and recovery from an incorrect distribution.
Do not publish indicators or change policies.
```

**Expected deliverable:** governance assessment and lifecycle design; exporting indicators does not imply blocking.

## 6. Troubleshoot ingestion and mapping

Skill: [cortex-platform-engineer](../source/cortex-platform-engineer/README.md).

```text
Use cortex-platform-engineer.

Symptom: I can see events in the raw dataset, but cannot find them
in the query that uses the expected mapping.
Product and version: [specify].
Source, anonymized configuration, schema, query, and examples: [attach].

Build a sequence of read-only checks.
Consider ingestion, parsing, mapping, types, time, query logic,
and permissions as separate hypotheses.
Request evidence before attributing a cause.
Do not change RBAC, collectors, or parsing rules.
Provide a differential diagnosis and information for escalation.
```

**Expected deliverable:** ordered checks and evidence-supported hypotheses, not an invented cause.

## 7. Coordinate a case across specialties

Skill: [cortex-security-engineer](../source/cortex-security-engineer/README.md).

```text
Use cortex-security-engineer.

I have an identity alert, a query with an error, and a playbook
that stopped during enrichment.
Product and version: [specify].
Anonymized evidence and errors: [attach].

Separate investigation, query, detection, and automation workstreams.
Define priorities, dependencies, inputs, and outputs for each.
Identify the recommended Skill for each area.
Do not assume other Skills or subagents are available;
if they are not, provide a standalone plan and contracts
for manual continuation.
Do not execute any actions in the environment.
```

**Expected deliverable:** integrated triage and a handoff plan between specialties, without assuming automatic delegation.

## How to check the response

A useful response should:

- use only data and references that are actually accessible;
- identify the relevant product, surface, version, and assumptions;
- cite specific official sources for technical claims;
- distinguish facts, inferences, and concepts;
- state exactly which checks were not performed;
- request specific authorization before proposing to execute a change.

When an essential input is missing, explaining the gap is better than delivering an apparently ready-made solution. To evaluate a Skill, use your own anonymized cases; do not provide the repository's answer keys to the assistant.
