# TIM troubleshooting guide

## Contents

- [Method](#method)
- [Evidence bundle](#evidence-bundle)
- [Symptom matrix](#symptom-matrix)
- [Duplicate and conflict investigation](#duplicate-and-conflict-investigation)
- [Lifecycle investigation](#lifecycle-investigation)
- [Distribution investigation](#distribution-investigation)
- [Safe mutation boundary](#safe-mutation-boundary)
- [Stop conditions](#stop-conditions)

## Method

Troubleshoot with competing hypotheses and the least-invasive observation first:

1. define the expected behavior and its official/tenant evidence;
2. establish product, version, license/add-on, integration/pack version, deployment, engine, and effective permissions;
3. bound the timeframe, source, run, indicator sample, and destination;
4. build hypotheses across the full chain;
5. collect sanitized read-only evidence;
6. eliminate hypotheses rather than changing several variables;
7. propose a state change only after scope, approval, rollback, and verification are ready;
8. retain the evidence and label remaining uncertainty.

“No indicators” and “no error” are observations, not root causes.

## Evidence bundle

Request only what is necessary:

- product/deployment/version/build and license/add-on;
- installed content pack and exact integration version;
- sanitized instance configuration and effective role permissions;
- integration health, start/end UTC, run identifier, status, and sanitized error/warning logs;
- source availability and a small, sanitized representative object set;
- request/page/checkpoint metadata without tokens or secrets;
- mapping/type-validation evidence and rejected-object counts;
- source and managed indicator timestamps, provenance, state, tags, and applicable assessment values;
- enrichment provider/status/cache/exclusion evidence;
- export/service selection and a sanitized served-output sample;
- consumer fetch/status and downstream policy state;
- previous known-good state and recent change record.

Do not ask for full credential-bearing configuration exports, unrestricted indicator dumps, or production-sensitive telemetry when a narrow sample suffices.

## Symptom matrix

| Symptom | Competing hypotheses | Least-invasive evidence | Do not conclude |
|---|---|---|---|
| Feed fetches zero objects | Empty source window; wrong collection/filter; checkpoint ahead; permissions; mapping rejects; source outage; license/integration issue | Source-side count, exact window, sanitized config, run logs, checkpoint metadata | “No threats exist.” |
| Objects fetched but no indicators visible | Unsupported type; validation/formatting failure; exclusions; wrong product surface; permissions; delayed processing | Type/mapping docs, rejection logs, exact sample, readback with same timeframe | “Ingestion is broken” before locating the stage. |
| Same indicator appears repeatedly | Page replay; checkpoint not committed; source revisions; normalization collision; multi-source presentation; UI interpretation | Native IDs/revisions, page/checkpoint logs, normalized identity, source list | Duplicate storage without readback. |
| Conflicting verdict or expiration | Different source reliability; recency; product-specific merge rule; manual override; custom script; stale view | Source-level observations, reliability, modification times, manual audit, exact product docs | A universal “highest score wins” rule. |
| Enrichment absent | Unsupported type; exclusion; missing integration; permissions; provider/rate failure; cached state; privacy policy | Applicable type/profile, exclusion, integration health, cache context, sanitized error | Ingestion failure. |
| Indicator expired unexpectedly | Feed/type/manual policy; multi-feed reliability; feed disabled; timestamp semantics; custom automation | Expiration source, feed states, reliability, audit, exact timestamps | Deletion or source revocation. |
| Removed source item stays active | Feed cannot detect removal; source windowing; checkpoint failure; another source; policy | Integration behavior, source observation set, per-source evidence, expiration owner | Cortex ignored a deletion. |
| TAXII relationship missing | Integration limitation; unsupported object/expression; mapping; source never sent link | Source bundle, integration docs, ignored-object evidence, readback | Lossless graph support. |
| EDL URL serves data but firewall does not block | Consumer cache; auth/TLS; parse rejection; policy not attached/committed; wrong device scope; allowlist | Served sample, consumer fetch logs, list status, policy/commit readback | Export equals enforcement. |
| Long-running service unreachable | Hosting/engine route; certificate; authentication; firewall/NAT; service health; wrong product-specific endpoint | Current integration docs, service health, network/TLS observations | The URL format from another deployment applies. |

## Duplicate and conflict investigation

For one sanitized indicator sample:

1. list every source observation, native ID, revision, source timestamps, fetch run, and marking;
2. record the original and normalized values plus transform version;
3. compare checkpoint/page evidence for replay;
4. determine whether the product shows one indicator with multiple source assertions or multiple records;
5. record source reliability, native assessment, managed assessment, expiration owner, and manual overrides;
6. find the exact documented or tenant-configured merge rule;
7. keep the root cause `UNVERIFIED` until evidence selects a hypothesis.

Do not delete duplicates as the first diagnostic step. It destroys evidence and may hide a pagination or identity defect.

## Lifecycle investigation

Build a UTC timeline:

```text
source created/modified/observed
-> fetch page and checkpoint
-> Cortex create/update
-> enrichment and relationship updates
-> expiration policy calculation or manual override
-> export eligibility and served-output changes
-> consumer refresh and control changes
```

For each transition, record observed time separately from source-reported time. A polling timestamp must not silently become “last seen.” Check feed disablement, multi-feed source reliability, manual expiration, exclusions, and custom scripts/playbooks only when applicable.

## Distribution investigation

Test the chain without jumping stages:

1. Does the narrow Cortex selection contain the expected indicator?
2. Does the export/service serialize it in the expected form?
3. Can the authorized consumer retrieve the current output?
4. Does the consumer accept the value and show a fresh list?
5. Is the list attached to the intended policy and scope?
6. Is the policy committed/active?
7. Is the observed control behavior consistent, and what safe test supports that?

Record each result independently. Never bypass authentication or widen a list to diagnose a consumer problem.

## Safe mutation boundary

The following are state-changing or risk-bearing and require approval, exact scope, before state, rollback, and readback:

- changing feed start time, filters, mappings, interval, reliability, verdict, or expiration;
- clearing/resetting a checkpoint or fetch history;
- enabling insecure certificate behavior or changing network exposure;
- disabling exclusions or privacy gates;
- manually enriching sensitive values;
- changing indicator verdict/state, expiring, excluding, or deleting indicators;
- altering an outbound query, starting a long-running service, or changing credentials;
- attaching an EDL to a security policy or committing a control change.

Provide a diagnostic plan when authorization or evidence is missing; do not execute or phrase the mutation as already completed.

## Stop conditions

Pause escalation and request the missing authority/context when:

- the exact tenant, product, integration, or consumer target is ambiguous;
- credentials, secrets, or personal data would be exposed;
- a requested reset/replay could create uncontrolled volume;
- a broad deletion or block lacks a reviewed item list;
- certificate validation or access control would be weakened;
- no rollback or downstream readback exists;
- the proposed action crosses from distribution into enforcement;
- evidence conflicts and a tenant-specific fact is required.

State what remains known, what was ruled out, and the smallest safe next observation.
