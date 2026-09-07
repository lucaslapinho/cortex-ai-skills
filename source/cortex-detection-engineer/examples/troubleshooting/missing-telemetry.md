# Missing telemetry in a quiet detection

## Symptom

A candidate endpoint detection returned zero matches during a controlled test, and the user wants to conclude the behavior did not occur.

## Product and evidence

- Product: Cortex XSIAM 3.x documentation baseline; tenant version, edition, rule surface, and identity scope unknown
- Query/rule and controlled event: not supplied
- Status: `UNVERIFIED / TENANT-UNVERIFIED`
- `S: NOT RUN` — no independent evaluation of this example revision.
- `D: PASS` — cited product boundaries were documented at the stated source snapshot; tenant coverage is not established.
- `C: NOT RUN` — no exact tenant schema or rule-editor acceptance.
- `E: NOT RUN` — no tenant execution or observed detection outcome.

## Why zero is inconclusive

Zero rows may reflect:

- the source did not generate or collect the event;
- category/subtype mismatch;
- parser/mapping or field-null behavior;
- event-time/insert-time, timezone, schedule, or retention mismatch;
- license or rule-surface restriction;
- RBAC/SBAC/data scope;
- rule disabled, exception, or suppression;
- query logic error;
- the behavior truly did not occur.

## Smallest discriminating sequence

1. Preserve the exact controlled-test timestamp, endpoint alias, expected raw event, rule/query revision, product/version, and execution identity.
2. Confirm source generation at the endpoint/system.
3. Confirm collection/ingestion around both event and insert times.
4. Inspect tenant schema/types and a known-positive record using the same identity.
5. Verify event category and exact subtype; do not infer a start event from Process category or process-named fields.
6. Run the smallest read-only Query Center probe over a bounded window.
7. Verify the candidate in the exact BIOC/correlation editor and inspect rule state/audit evidence.
8. Only then interpret a no-match within documented coverage.

## Detection consequence

Until the controlled event is observable, mark the detection's coverage and recall `UNVERIFIED`. Do not compensate by removing behavioral predicates or inventing fields. Escalate concrete collector/parser/access configuration to platform ownership while preserving the detection telemetry contract.

## Expected result

Expected, not observed: the sequence identifies whether failure is at source generation, transport/ingestion, schema/access, rule compatibility, or detection logic. If coverage remains unknown, no absence conclusion is permitted.

## Official references

- Local diagnostic guidance: [telemetry and signal](../../references/telemetry-signal-and-query-handoff.md) and [troubleshooting](../../references/troubleshooting.md).
- [Datasets and presets](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Datasets-and-presets)
- [Query Center permissions](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Query-Center-permissions)
