# Astra forward output — cortex-threat-hunter

Model requested: `gpt-6-astra`, high reasoning; ephemeral CLI, manual inline runtime load.

Runtime: 22 files / 73435 bytes; ordinal SHA-256 `af98de5883f06eea19adf89b9c6ce6cf1676830441f11f774d74a1b286f8f092`.

Isolation: 0 tool/action events. Runtime files plus Fixture/Prompt only; no oracle text supplied. One fresh ephemeral process contains this case only. No self-grading result is assigned here. Independent adjudication is required.

## Input CTH-AMB-01

### Fixture

The user says only “Cortex” and asks for the exact menu path and query.

### Prompt

Show me where to run the hunt and give executable XQL.

Local Markdown links are rebased for publication only; wording and attribution are unchanged. Raw response/event files remain in the evaluation archive outside the publication tree.

## Retained response

**CTH-AMB-01**

Which product are you using—Cortex XSIAM or Cortex XDR—and what release, query surface, and behavior should the hunt target?

“Cortex” alone doesn’t establish an exact menu path. Executable XQL also requires applicable evidence for the syntax, dataset, and fields. Those details are **UNVERIFIED / TENANT-UNVERIFIED**; no applicable official page or tenant schema was inspected.

**QP-001 — Provisional semantic plan:** Select telemetry for the target behavior, bound the population and event-time window, filter for its observables, preserve source identifiers and timestamps, and compare distinct entities with comparable peers. Dataset and field mappings remain unresolved. This is a **CONCEPTUAL / TENANT-UNVERIFIED** plan; no hunt results are available.

To make the query executable, provide the hunt objective and applicable schema evidence, including dataset names, field names, types, and time semantics.

Validation:

- **S: NOT RUN** — No independent response evaluation.
- **D: NOT RUN** — Specific applicable official documentation was not inspected; the supplied source register does not establish a current verification.
- **C: NOT RUN** — No tenant schema or compiler validation.
- **E: NOT RUN** — No tenant execution or observed results.
