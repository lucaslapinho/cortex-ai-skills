# Example: repeated indicator from several feeds

## Objective

Explain why one IP appears repeatedly with conflicting assessments without deleting data or resetting collection state.

## Evidence status

- Product: reported as XSIAM; version, license, integration versions, and tenant evidence absent.
- Observed claim: “the IP appears many times” is `UNVERIFIED / PROJECT-ASSERTED / TENANT-UNVERIFIED` until a readback is supplied.
- Official facts about multi-feed expiration are `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED`.

## Competing hypotheses

| Hypothesis | Least-invasive check | What would support it |
|---|---|---|
| A page/checkpoint replayed | Compare sanitized page/checkpoint IDs and source native IDs across runs | Same source revision fetched in repeated pages/runs |
| The source published revisions | Compare native ID and modification time | New revisions with stable source identity |
| Different values normalized together | Compare original and normalized values and transform version | Distinct originals share one governed identity |
| Several sources contribute to one managed indicator | Inspect source-level provenance in indicator readback | One indicator with several source observations |
| UI/report grouping is misunderstood | Export/read one bounded sample with stable identifiers | Presentation count differs from stored identity count |

## Assessment conflict

Build a source table before resolving anything:

| Source | Native observation time | Reliability | Native assessment | Cortex readback | Expiration owner |
|---|---|---|---|---|---|
| Feed A | `{{UTC}}` | `{{UNKNOWN}}` | `{{VALUE}}` | `{{NOT_PROVIDED}}` | `{{UNKNOWN}}` |
| Feed B | `{{UTC}}` | `{{UNKNOWN}}` | `{{VALUE}}` | `{{NOT_PROVIDED}}` | `{{UNKNOWN}}` |

Do not average the scores or claim “highest wins.” Current XSIAM documentation describes a reliability/recency rule for expiration in a multi-feed case; it does not establish a universal verdict/confidence merge formula. A separate XSOAR 8.9 on-premises verdict page has its own scope and cannot be projected here.

## Safe next steps

1. Confirm product/version, feed instances, integration versions, and effective permissions.
2. Select one sanitized indicator and a narrow UTC window.
3. Collect native IDs/revisions, page/checkpoint metadata, original/normalized values, and source-level readback.
4. Locate the first stage where the count diverges.
5. Only then propose an approved mapping or checkpoint change with bounded replay and rollback.

## Prohibited shortcut

Do not delete the indicator, reset fetch history, disable exclusions, or widen feed scope “to test.” Those actions can destroy evidence, replay large volumes, or change downstream behavior.

## Limitations

No root cause is established, no tenant operation was run, and no performance or duplicate rate was measured.

## Local references

- [Feeds and source quality](../../references/feeds-and-source-quality.md)
- [Scoring, enrichment, and relationships](../../references/scoring-enrichment-and-relationships.md)
