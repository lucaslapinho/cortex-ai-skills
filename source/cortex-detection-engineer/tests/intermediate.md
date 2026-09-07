# Intermediate cases

## DET-INT-01 — Tune noisy PowerShell logic

### Fixture

A PowerShell detection is noisy during software deployment. The only suggestion is to allowlist `powershell.exe` when launched by a deployment tool.

### Prompt

Create a tuning plan that reduces benign noise while protecting known-positive coverage and governs any exception.

### Expected observations

- Requests rule/query samples, distributions, positive/benign fixtures, and deployment scope.
- Challenges filename/parent-only allowlisting as attacker-mimickable.
- Designs a controlled before/after experiment, FP/FN comparison, shadow/canary, owner, expiry, and rollback.
- Does not equate suppression with improved selectivity.

### Prohibited behaviors

- Apply a permanent global exception or threshold with no evidence.
- Claim lower volume is proof of better quality.

### Evidence expected

Tenant data required for thresholds; product settings cited only if used.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## DET-INT-02 — ATT&CK and telemetry

### Fixture

A proposal says “Mapped to Credential Access; therefore the tenant covers it.” No telemetry inventory or active-rule evidence is supplied.

### Prompt

Review the ATT&CK claim and produce a coverage validation plan.

### Expected observations

- Treats ATT&CK as dated interpretation, not occurrence or coverage proof.
- Notes active contributing source status does not prove all detectors/rules are active/applicable.
- Requires behavior-to-technique rationale, telemetry, rule state, schema, fixtures, and outcomes.

### Prohibited behaviors

- Accept coverage solely from a mapping/dashboard tile.
- Invent data-source connectivity or rule activation.

### Evidence expected

Current XSIAM MITRE coverage page plus tenant rule/source/fixture evidence plan.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## DET-INT-03 — Hunt-to-detection promotion

### Fixture

A hunter observed failed logins followed by success in three examples, but supplies no query, raw events, control group, or baseline.

### Prompt

Determine whether the observation is ready for a production rule and define the promotion gates.

### Expected observations

- Treats hunt observations as leads and returns `NOT READY` or equivalent.
- Defines repeatability, schema, time/order, entity key, benign alternatives, held-out fixtures, threshold/capacity, rule-context, and owner gates.
- Compares scheduled versus real-time only after semantics are defined.

### Prohibited behaviors

- Invent a numeric threshold or concrete XQL.
- Claim compromise or production readiness from three examples.

### Evidence expected

Conceptual status and exact missing evidence/next step.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## DET-INT-04 — Expected signal and investigation

### Fixture

A candidate returns one row per user after aggregation, but the design does not say which contributing events or triage fields remain.

### Prompt

Review the signal contract, its relationship to Issues/Cases, and the fields needed for investigation and grouping.

### Expected observations

- Defines pre/post aggregation grain and preserves contributing-event/rule provenance.
- Identifies triage fields, null/type/privacy checks, and drill-down expectations.
- Treats Issue generation and Case grouping as separate observed outcomes.
- Says mapping can influence but not guarantee grouping.

### Prohibited behaviors

- Promise Case grouping from one mapped username.
- Treat the aggregate row as proof of maliciousness.

### Evidence expected

Current Case/Issue and grouping pages plus tenant output tests.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`
