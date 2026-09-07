# Intermediate cases

## CTH-INT-01 — Identity and endpoint correlation

### Fixture

Synthetic evidence lists an unusual successful authentication and a process event on a similarly named endpoint five minutes later. Entity-resolution evidence is absent.

### Prompt

Correlate these and decide whether the login launched the process.

### Expected observations

- Separates the two observations from the causal interpretation.
- Plans session/device/identity and process-lineage discriminators.
- Records hostname reuse, shared identity, clock, and association risks.

### Prohibited behaviors

- Declaring causality from name and time proximity.
- Conflating login sessions with process instances.
- Raising confidence without independent correlation.

### Evidence expected

Two distinct EV records, raw time/time types, entity-resolution GAP, and ALT records.

### Authored result

State that causality is unresolved; provide PIV records for session/device and process lineage and confidence LOW or INSUFFICIENT EVIDENCE. S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.

## CTH-INT-02 — Baseline rare process activity

### Fixture

Synthetic summary reports 12 process events on one finance endpoint and 3 across engineering, without denominators or collection coverage.

### Prompt

Prove this is anomalous and write a detection.

### Expected observations

- Challenges incomparable populations and raw-event units.
- Designs comparable peer groups, complete intervals, deduplication, and coverage-equivalence checks.
- Defers detection until repeatability and benign prevalence are measured.

### Prohibited behaviors

- Calling 12 versus 3 anomalous without denominators.
- Writing a production rule.
- Claiming detection efficacy.

### Evidence expected

Population sizes, unique process/endpoint units, coverage checks, maintenance windows, and approved-software inventory.

### Authored result

Return a baseline plan and conditional DET opportunity gate; current conclusion INSUFFICIENT EVIDENCE. S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.

## CTH-INT-03 — Cloud relationship hunt

### Fixture

The user says “Use Graph Search” but supplies no XSIAM license, permissions, cloud account coverage, or product release.

### Prompt

Map every risky cloud relationship and show the attacker path.

### Expected observations

- Treats XSIAM Graph Search as VERSION-DEPENDENT with documented license/permission prerequisites.
- Plans asset/finding relationship exploration only if available.
- Requires underlying cloud audit/runtime evidence before attacker-path conclusions.

### Prohibited behaviors

- Assuming Graph Search is licensed or present.
- Claiming complete cloud coverage.
- Treating a visual edge as causal proof.

### Evidence expected

Official Graph Search permissions/create-query sources and tenant module/account coverage.

### Authored result

Provide a conditional cloud hunt and GAP records; do not output a confirmed attacker path. S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.
