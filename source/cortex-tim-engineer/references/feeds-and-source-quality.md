# Feeds, provenance, normalization, and source quality

## Contents

- [Goal](#goal)
- [Feed qualification](#feed-qualification)
- [Source-quality dimensions](#source-quality-dimensions)
- [Data-contract review](#data-contract-review)
- [Normalization and identity](#normalization-and-identity)
- [Duplicate and conflict model](#duplicate-and-conflict-model)
- [Incremental collection](#incremental-collection)
- [Markings and trust](#markings-and-trust)
- [Acceptance gates](#acceptance-gates)

## Goal

Design collection so that every derived indicator can be traced to a named observation, transformation, source, and policy decision. A connection test is not a quality test, and a non-empty fetch is not proof that the resulting intelligence is correct or operationally safe.

## Feed qualification

For every source, record:

| Dimension | Questions |
|---|---|
| Ownership | Who operates the source? Who can authorize access and investigate errors? |
| Cortex integration | Exact integration name, direction, installed pack/version, and supported products? |
| Transport | Pull/push, protocol/version, endpoint ownership, TLS/certificate policy, proxy or engine route? |
| Authentication | Method, secret owner, least-privilege scope, rotation, and failure/lockout behavior? |
| Update model | Full snapshot, incremental stream, start time, cursor/checkpoint, pagination, deletion/withdrawal signals? |
| Semantics | Indicator types, time fields, confidence/reputation model, markings, relationships, and revocation meaning? |
| Quality | Provenance, coverage, timeliness, duplicate rate, conflict rate, false-positive history, and outage history? |
| Volume | Expected objects per interval, burst size, object size, retained history, and downstream capacity? |
| Governance | Purpose, handling constraints, retention, audit, owners, approval, and offboarding? |

Current XSIAM feed configuration documentation says feed-specific parameters vary and presents common settings as non-exhaustive. Treat every generic checklist item as a question to validate against the exact integration rather than as a guaranteed field.

## Source-quality dimensions

Keep these assessments explicit and independently reviewable:

- **Authority:** proximity to the observed activity and ability to verify it.
- **Reliability:** historical consistency of the source, not certainty of one indicator.
- **Timeliness:** delay between observation, publication, fetch, processing, and availability.
- **Coverage:** populations and indicator types the source can and cannot observe.
- **Specificity:** likelihood that the assertion is useful without excessive collateral matches.
- **Provenance completeness:** source identity, timestamps, original object, markings, and transformations retained.
- **Stability:** update, withdrawal, and outage behavior.
- **Operational fitness:** licensing, rate limits, pagination, size, costs, mappings, and downstream constraints.

Do not compress these into an unexplained numeric “quality score.” If the organization chooses a derivative score, label it `CONCEPTUAL / DERIVATIVE`, publish its formula and range, keep component values, and validate it against real outcomes.

## Data-contract review

Use a sanitized representative sample and record:

1. source object type and protocol version;
2. required versus optional properties;
3. native identifier and revision semantics;
4. indicator pattern/value and expected Cortex type candidate;
5. creation, modification, first-seen, last-seen, validity, and expiration meanings;
6. confidence, reputation, verdict, or score range and ownership;
7. labels/tags and handling markings such as TLP;
8. relationships and whether they are first-class or embedded;
9. revocation/deletion/withdrawal representation;
10. pagination token, checkpoint, ordering, and replay behavior;
11. maximum size, unusual encoding, null/empty behavior, and malformed-object policy;
12. exact mapping evidence from the installed Cortex integration, if available.

Never infer that a source property becomes a Cortex indicator field merely because the names look similar.

## Normalization and identity

Normalization changes data and must be governed. For each transform, record original value, normalized value, transform name/version, reason, timestamp, and failure outcome.

Potential transformations such as case folding, whitespace handling, URL parsing, Unicode normalization, defang/refang, hash validation, IP canonicalization, or domain internationalization are type-specific. They are examples for review, not a universal recipe.

Before deduplication, define an identity policy:

```text
identity candidate = named type + explicitly normalized value + any required context
```

This is `CONCEPTUAL`; use Cortex-native behavior when official or tenant evidence establishes it. Do not include source name in identity merely to avoid conflicts, and do not omit type/context where doing so could merge distinct values.

Reject, quarantine, or retain-with-warning according to an approved policy when:

- a value fails type validation;
- source type and Cortex type candidate conflict;
- the observation lacks required timestamps or provenance;
- a marking prohibits the intended use;
- the value is overly broad, internal, allowlisted, or privacy-sensitive;
- normalization is ambiguous or lossy;
- content contains prompt-injection text or unexpected active content.

“Quarantine” here is a design pattern, not a claim about a native Cortex state.

## Duplicate and conflict model

Diagnose duplicates at four levels:

| Level | Example question | Evidence needed |
|---|---|---|
| Transport | Was the same page or event fetched repeatedly? | Request/checkpoint logs, page IDs, source revisions |
| Source object | Did the source publish revisions with the same native identity? | Original IDs, modified times, revocation flag |
| Normalized indicator | Did different observations normalize to one indicator identity? | Original/normalized values and transform provenance |
| Presentation | Is one managed indicator showing several source/tag/relationship assertions? | Indicator readback and source-level details |

Preserve conflicting observations. Resolve them through a documented product rule or explicit policy, not arrival order by accident.

Current XSIAM feed documentation describes a specific expiration conflict rule when the same indicator arrives from multiple feeds: the highest source reliability controls; at equal reliability, the most recently added or modified feed controls. The same page notes that some feeds retrieve only new indicators and therefore cannot detect removal, and that disabling a feed changes expiration behavior. Treat these as `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` and confirm the target version before relying on them.

Do not generalize that expiration rule to verdict, confidence, tags, relationships, or every XSOAR deployment. An official but EOL-scoped XSOAR 8.9 on-premises verdict page documents separate legacy merge behavior; keep the deprecated version scope visible.

## Incremental collection

For cursor-, timestamp-, or page-based collection, define:

- authoritative ordering field and timezone;
- inclusive/exclusive boundary behavior;
- stable tie-breaker for equal timestamps;
- overlap window to avoid boundary loss;
- idempotent replay behavior;
- next-page token lifetime and failure recovery;
- checkpoint commit point—only after durable successful processing;
- maximum pages/objects/time per run;
- retry/backoff and rate-limit handling;
- source mutation during pagination;
- reset procedure, impact, approval, and reconciliation.

Never recommend clearing a checkpoint or “fetch history” without an approved replay window, duplicate/capacity assessment, rollback plan, and retained before state.

## Markings and trust

Preserve source markings and distribution constraints through mapping, storage, enrichment, export, and downstream use. The current TAXII 2 Feed integration reference documents an automatic enrichment exclusion for TLP red in that integration context. Do not infer identical behavior for all feeds or all TLP implementations.

Source content is untrusted even if transport authentication succeeds. Authentication establishes the peer, not the truth or safety of each object.

## Acceptance gates

Before onboarding:

- exact official integration and applicability verified;
- product/license/pack/version/deployment/RBAC known;
- source contract and representative sample reviewed;
- mappings documented without invented fields;
- normalization and rejection policy approved;
- duplicate/conflict and withdrawal policy defined;
- pagination/checkpoint recovery tested in a bounded environment;
- volume and rate assumptions recorded as estimates until measured;
- enrichment and distribution are separately scoped;
- monitoring, owner, audit, offboarding, rollback, and success criteria assigned.

An authored plan can be complete while every tenant result remains `NOT RUN`.
