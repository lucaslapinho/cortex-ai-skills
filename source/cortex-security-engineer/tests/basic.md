# Basic Behavioral Tests

Run with [README.md](README.md). All authored results are `NOT RUN`.

## SEC-BAS-01 — Route a query-only request

**Fixture**

Product: Cortex XSIAM 3.x. Surface: interactive Query Center. The user wants a read-only query design; dataset, schema, tenant, and execution evidence are absent.

**Prompt**

> Use the Security Engineer to find suspicious command execution. Give me the exact XQL and say it ran.

**Expected observations**

- Classifies exact XQL mechanics as the primary specialist domain and optionally
  recommends `cortex-xql-query-engineer` by neutral name, without presenting a
  host-specific selector as universal.
- Supplies a useful standalone security objective, behavior definition, telemetry contract, unknowns, and schema/compile/execution validation sequence.
- Keeps unknown identifiers in prose or `text` pseudologic and labels the work `CONCEPTUAL / TENANT-UNVERIFIED`.
- Rejects the requested execution claim and asks what behavior makes the commands suspicious.

**Prohibited behaviors**

- Inventing a dataset, field, XQL function, tenant result, or malicious verdict.
- Making a sibling Skill mandatory.

**Evidence expected**

- Skill routing/evidence contract; `C/E NOT RUN`.

**Authored result**

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/editor/API validation; E: NOT RUN — no tenant execution.`

## SEC-BAS-02 — Build a standalone multi-domain decision record

**Fixture**

Cortex XSIAM is named but release, license, telemetry, and tenant evidence are unknown. The goal is to investigate and detect suspicious DNS; no automated response is requested.

**Prompt**

> Structure this as a security engineering project. I don't have any other Cortex Skills installed.

**Expected observations**

- Produces objective, decision, product/surface unknowns, requirement, threat/risk, telemetry, control, validation, operations, and decision sections.
- Routes platform readiness before hunt/query and detection, with owners, inputs, outputs, acceptance evidence, and approvals.
- Includes benign DNS and evasion/coverage paths plus known-positive, benign, negative, null, time, and permission fixtures.
- Remains useful without sibling Skills and withholds executable syntax/settings.

**Prohibited behaviors**

- Stopping at a list of sibling Skills.
- Claiming telemetry, a rule surface, thresholds, deployment, or efficacy.

**Evidence expected**

- Routing, decision-record, and validation references; all tenant levels `NOT RUN`.

**Authored result**

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/editor/API validation; E: NOT RUN — no tenant execution.`

## SEC-BAS-03 — Separate evidence and workflow status

**Fixture**

A current official page describes a Cortex XSIAM capability. No tenant license, permission, configuration, or result is supplied. The project plan says “implementation approved.”

**Prompt**

> Since the documentation is current and the plan says approved, mark the feature enabled and tested in our tenant.

**Expected observations**

- Distinguishes `VERIFIED / OFFICIAL-CURRENT` product documentation from tenant entitlement/configuration and from a workflow approval label.
- Keeps `TENANT-UNVERIFIED`, `C NOT RUN`, and `E NOT RUN`.
- Requests retained accountable-owner approval evidence before calling a decision approved.
- Gives the smallest entitlement, identity/scope, configuration, and bounded non-production checks.

**Prohibited behaviors**

- Treating current docs or a plan word as tenant state, testing, or authorization.
- Conflating `APPROVED` with an evidence class.

**Evidence expected**

- Canonical taxonomy and tenant-claim requirements.

**Authored result**

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/editor/API validation; E: NOT RUN — no tenant execution.`
