# Example: zero-results troubleshooting

Status: CONCEPTUAL / DERIVATIVE / TENANT-UNVERIFIED

## Supplied statement

“The query returned zero rows, so the campaign did not affect us.”

## Assessment

The campaign-absence claim remains UNVERIFIED. The inference from zero rows alone is not justified: zero rows describe a query outcome only after execution is verified; they do not establish absence outside the query's observable model and coverage.

## Validation sequence

1. Confirm Cortex product/release and query surface.
2. Verify the dataset/fields exist in the applicable tenant.
3. Confirm event-time semantics, timezone, and exact window.
4. Confirm retention covers the entire window.
5. Prove collection with a known-good expected event for the same population.
6. Confirm parser/value shapes, permissions, and data scope.
7. Capture compile and execution outcomes.
8. Review filters, exclusions, limits, sampling, and cancellation.
9. Seek an independent telemetry source.

## Evidence ledger

- EV-001: accessible user report of zero rows; underlying execution claim is UNVERIFIED / PROJECT-ASSERTED / TENANT-UNVERIFIED. Missing original execution evidence is a separate gap, not proof that the received report is inaccessible.
- GAP-001: query text and execution metadata absent.
- GAP-002: population, retention, and collection absent.
- GAP-003: permission/scope and schema validation absent.

## Defensible conclusion

No conclusion about campaign presence or absence can be made from the supplied statement. Confidence: INSUFFICIENT EVIDENCE.

If all prerequisites later pass, use:

> No matching records were observed within the validated queried population and window. Activity outside verified collection, retention, parsing, permissions, scope, or the query's observable model remains unresolved.

## Local references

- [Troubleshooting](../references/troubleshooting.md)
- [Telemetry and coverage](../references/telemetry-and-coverage.md)
