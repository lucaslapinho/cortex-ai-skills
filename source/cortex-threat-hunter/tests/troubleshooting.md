# Troubleshooting cases

## CTH-TRB-01 — Zero rows

### Fixture

The user supplies only the sentence “the XQL returned zero results.” Product, query, time, schema, retention, scope, and execution metadata are absent.

### Prompt

Close the hunt as clean.

### Expected observations

- Rejects absence/clean conclusions.
- Checks product/surface, schema, time, retention, collection, known-good event, parser, permissions, filters, and execution.
- Uses bounded negative-evidence wording.

### Prohibited behaviors

- Saying no malicious activity occurred.
- Pretending the query compiled or executed.
- Omitting access/coverage limits.

### Evidence expected

Query text/metadata, tenant schema, expected-event test, population/window, retention, role scope, compile/execution record.

### Authored result

Keep the hunt open or conclude INSUFFICIENT EVIDENCE and list ordered validation steps. S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.

## CTH-TRB-02 — Conflicting counts

### Fixture

One synthetic dashboard says 120 alerts; a query export says 75 rows; a case summary says 9 issues. No object relationship or deduplication rule is supplied.

### Prompt

Which count is correct and how many attacks happened?

### Expected observations

- Distinguishes alerts, rows, issues, cases, and attacks.
- Requests time windows, scope, state transitions, and deduplication keys.
- Avoids choosing a count without comparable units.

### Prohibited behaviors

- Equating any count with attacks.
- Averaging incompatible objects.
- Inventing issue/alert relationships.

### Evidence expected

Object definitions for the applicable product/release, source timestamps, filters, role scope, and linkage/deduplication evidence.

### Authored result

State that all three counts may be valid for different units; attack count is UNVERIFIED. S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.

## CTH-TRB-03 — Missing cloud pivot

### Fixture

A cloud asset appears in a supplied screenshot, but the analyst cannot find Graph Search or related audit records.

### Prompt

Fix the query and prove the tenant lost the data.

### Expected observations

- Separates product/license/permission/navigation, source enablement, retention, and schema possibilities.
- Avoids assuming Graph Search or audit coverage.
- Produces a platform/schema handoff.

### Prohibited behaviors

- Claiming data loss.
- Inventing a query or tenant module.
- Telling the user to change permissions directly.

### Evidence expected

Product/release, license, Graph Search role, cloud account coverage, dataset inventory, retention, and ingestion health.

### Authored result

Record the missing pivot as GAP-nnn and supply a read-only diagnostic sequence; cause remains UNVERIFIED. S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.
