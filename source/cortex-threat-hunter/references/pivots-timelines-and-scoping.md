# Pivots, timelines, baselines, and scoping

## Contents

1. Pivot contract
2. Enrichment contract
3. Timeline contract
4. Baseline design
5. Scope and counting
6. Competing explanations

## 1. Pivot contract

For every PIV-nnn:

- source evidence ID;
- from-entity and to-entity;
- pivot relationship;
- direction and time window;
- expected discriminator;
- source required;
- ambiguity/collision risks;
- result status;
- next decision.

Common pivot entities include endpoint, process, file/hash, identity/session, IP, domain, URL, cloud resource, application, case/issue, and finding. Entity availability is product- and tenant-sensitive.

Avoid “pivot sprawl.” A pivot is justified only if it can support, weaken, scope, or distinguish the hypothesis.

## 2. Enrichment contract

Record:

- provider/source;
- retrieved time;
- subject;
- type of context;
- freshness/expiry;
- provider confidence or score semantics;
- conflicts with other sources;
- effect on the hunt.

An indicator match or reputation result remains context until primary telemetry connects it to an in-scope behavior. A common service, proxy, resolver, CDN, or shared hosting IP can create misleading relationships.

## 3. Timeline contract

Each timeline event contains:

- event ID;
- raw timestamp and timezone;
- normalized analysis time;
- time type: source/event, ingestion, detection, update, or analyst action;
- source and entity;
- observation;
- clock/skew note;
- certainty;
- related evidence and hypothesis.

Never silently replace the raw timestamp. If ordering depends on uncertain clock skew, describe the ordering as approximate or unknown.

## 4. Baseline design

Specify:

- target population;
- peer population and why it is comparable;
- baseline period and exclusion windows;
- timezone and complete intervals;
- segmentation such as role, OS, location, workload, or service;
- statistic and unit of counting;
- minimum sample and sparsity concerns;
- seasonality, maintenance, onboarding, and drift;
- data-coverage equivalence between target and baseline.

Do not call a difference anomalous until denominator, population, coverage, and normal variability are understood. An anomaly is a prioritization signal, not maliciousness.

## 5. Scope and counting

State the unit:

- raw events;
- deduplicated events;
- process instances;
- sessions;
- unique identities;
- endpoints;
- network destinations;
- cloud resources;
- alerts;
- issues;
- cases;
- findings.

Do not compare units as though they were interchangeable. Record deduplication keys and collision/fan-out risks.

Scope must include:

- included and excluded entity groups;
- management/collection population;
- time and retention boundary;
- known blind spots;
- unresolved identity/entity mappings;
- whether the result reflects all data or only the analyst's role scope.

## 6. Competing explanations

Create an ALT-nnn record:

| Field | Meaning |
|---|---|
| Explanation | The benign or different malicious interpretation |
| Supporting facts | Evidence consistent with it |
| Contradicting facts | Evidence inconsistent with it |
| Discriminator | Observation that separates it from the primary hypothesis |
| Coverage need | Source/population/time needed |
| Result | Supported, weakened, unresolved, or untested |

Frequent alternatives:

- approved software deployment or patching;
- administrator or help-desk activity;
- service/shared accounts;
- security scanners and test infrastructure;
- proxy, NAT, resolver, or load-balancer artifacts;
- backup, monitoring, orchestration, or CI/CD activity;
- parser/schema changes;
- late or duplicate ingestion;
- asset rename/reimage or ephemeral cloud reuse.
