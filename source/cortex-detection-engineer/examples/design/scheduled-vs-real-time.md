# Scheduled versus real-time correlation decision

## Objective

Choose a Cortex XSIAM rule surface for a design that correlates multiple events, aggregates by user, and asks to save the result into a dataset for later analysis.

## Evidence status

- Product: Cortex XSIAM 3.x, exact tenant/version/license unknown
- Status: `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED`
- `S: NOT RUN` — no independent evaluation of this example revision.
- `D: PASS` — the cited surface restrictions were documented at the 2026-09-04 snapshot; see the official register's 2026-09-06 action-note discrepancy before current configuration.
- `C: NOT RUN` — no exact tenant schema or rule-editor acceptance.
- `E: NOT RUN` — no tenant execution or observed action.

## Requirement analysis

The design requires:

- multiple-event aggregation;
- an evaluation window;
- persistence to a dataset rather than immediate Issue generation.

At the reviewed snapshot, current XSIAM documentation says real-time correlation:

- supports a narrow set of stages;
- requires `filter`;
- does not support several functions or dataset views;
- supports only **Generate issue** as the resulting action.

Therefore the requested aggregation and save-to-dataset action must not be presented as a real-time rule.

## Decision

Choose a **scheduled correlation candidate** if the exact XQL, schedule/window, dataset action, schema, license, permissions, and editor test support the use case. If immediate detection is required, separate that requirement and redesign a compatible real-time signal that only generates an Issue; do not silently remove aggregation or persistence semantics.

## Scheduled design gates

- Verify every XQL stage/function against current correlation restrictions.
- Define schedule, window, late-arrival recovery, overlap/gap, and duplicate behavior.
- Confirm target dataset name/schema/owner and whether multiple rules write to it.
- Treat saving data as state-changing: authorize, bound volume, preserve recovery, and verify writes.
- Define output grain and fields before aggregation.
- Test historical fixtures and expected volume.
- Monitor audit status, retries, errors, and hit safeguards.

## Expected outcome

Expected, not observed: a scheduled rule editor accepts the exact candidate in a non-production tenant; bounded executions persist rows with the designed grain; monitoring captures execution and errors. These remain `C/E=NOT RUN` until evidence exists.

## Limitations

The current page documents limits and options that can change. Recheck before implementation. Do not infer equivalent real-time support in Cortex XDR from the XSIAM page.

## Official reference

- Local compatibility guidance: [rule surfaces](../../references/rule-surfaces.md).
- [Create a correlation rule — Cortex XSIAM](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/threat-management/detection-rules/what-are-detection-rules/whats-a-correlation-rule/create-a-correlation-rule.md)
