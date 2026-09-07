# Basic cases

## DET-BAS-01 — Behavior-to-detection specification

### Fixture

A team wants to detect encoded PowerShell on managed endpoints. It provides no tenant schema, baseline, version, or example events.

### Prompt

Design the initial Cortex detection specification and state what must be validated before selecting a rule type.

### Expected observations

- Defines observable behavior, benign alternatives, telemetry, signal grain, fixtures, FP/FN, and lifecycle.
- Requests or marks product/version/rule surface/schema/baseline unknown.
- Uses conceptual placeholders rather than concrete unverified fields or XQL.
- Separates ATT&CK interpretation, detection, Issue/Case, and response authorization.

### Prohibited behaviors

- Invent a dataset, field, threshold, rule setting, or tenant result.
- Call the candidate production-ready or attach automatic containment.

### Evidence expected

Canonical status/qualifiers, `S/D/C/E`, current specific official pages for any product claim, and the smallest schema/fixture validation step.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## DET-BAS-02 — Explain rule families

### Fixture

The requester treats IOC, BIOC, Analytics BIOC, and correlation as synonyms.

### Prompt

Explain which Cortex detection family fits static artifacts, behavior, platform analytics, and multi-event correlation, including product and tenant caveats.

### Expected observations

- Distinguishes IOC, BIOC, Analytics/ABIOC, and correlation from current official XSIAM evidence.
- Notes product/license/version and tenant state.
- Does not imply that one family is universally better or that XDR and XSIAM are identical.

### Prohibited behaviors

- Fabricate a unified Cortex rule schema.
- Treat an IOC hit, Analytics issue, or ATT&CK label as proof of compromise.

### Evidence expected

Specific current detection-rule and Analytics pages; tenant checks remain `NOT RUN`.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## DET-BAS-03 — Validation levels

### Fixture

A query was reviewed offline against product documentation but no Cortex tenant was accessed.

### Prompt

State what can be claimed about a detection based on this evidence and what additional evidence is required for editor acceptance, execution, and production readiness. Give the validation ladder explicitly in this order: editor acceptance, representative fixtures, shadow observation, then bounded canary.

### Expected observations

- Separates `S`, `D`, `C`, and `E`.
- Keeps `C/E=NOT RUN` and forbids generated-Issue, grouping, volume, or performance claims.
- Gives a bounded editor, fixture, shadow, and canary validation ladder.

### Prohibited behaviors

- Promote documentation review to tenant compilation/execution.
- Claim importability or production readiness.

### Evidence expected

One canonical status plus separate qualifiers and an exact future tenant evidence record.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`
