# Hunt methodology

## Contents

1. Hunt lifecycle
2. Hypothesis design
3. Context and ATT&CK
4. Query-plan contract
5. Iteration log
6. Evidence-to-conclusion rules
7. Stopping conditions

## 1. Hunt lifecycle

Use:

Preserve → Acquire → Validate → Examine → Correlate → Hypothesize → Test → Conclude → Document.

For a proactive hunt, early hypotheses may guide acquisition, but never skip preservation, validation, or provenance. Maintain a decision log whenever the window, population, exclusions, baseline, or hypothesis changes.

## 2. Hypothesis design

A useful hypothesis contains:

- behavior, not merely a threat name;
- bounded actor/process/entity population;
- time and environment context;
- expected observables;
- telemetry preconditions;
- falsification criteria;
- at least one materially plausible alternative.

Poor:

> Hunt for T1059.

Better:

> If a process outside the approved administration population launched an interpreter to fetch or execute remote content on managed Windows endpoints during the last seven complete days, endpoint process and network telemetry should show a time-correlated parent/child and destination pattern, subject to endpoint collection, clock, retention, and network-visibility limits.

The ATT&CK technique can be added after the behavior is described. It does not prove the event.

## 3. Context and ATT&CK

Context questions:

- What initiated the hunt: IOC, behavior, anomaly, issue/case, external report, or campaign?
- Which asset, identity, cloud resource, application, and network zones matter?
- What approved administrative or service activity resembles the behavior?
- What clock, retention, scope, and collection limits apply?

For ATT&CK:

- map only behaviors supported by evidence or explicitly planned observables;
- record the ATT&CK version/date when the exact mapping matters;
- explain consistency and inconsistency;
- allow multiple candidate mappings;
- avoid actor attribution from technique overlap.

## 4. Query-plan contract

Each QP-nnn record contains:

| Field | Requirement |
|---|---|
| Question | One analytic question |
| Product/surface | XSIAM Query Center, XDR XQL surface, another verified surface, or product-neutral |
| Schema evidence | Applicable official dataset/field documentation, tenant-observed schema, or unresolved placeholders; identify which and retain tenant gaps |
| Time basis | Event/source/ingestion choice and timezone |
| Population | Entities and exclusions |
| Logic | Filter, projection, aggregation, sequence, or join intent |
| Baseline | Comparison population and statistic |
| Signal | Pattern that supports the hypothesis |
| Falsifier | Pattern that weakens it |
| Coverage | Retention, access, parser, collection, and sampling constraints |
| Pivot | Next query or corroborating source |
| Validation | Schema, compile, bounded execution, and result checks |

If schema evidence is missing, write semantic tokens such as DATASET_ENDPOINT_PROCESS and FIELD_EVENT_TIME. Mark the plan CONCEPTUAL / TENANT-UNVERIFIED and route the tokens to tenant schema discovery or an XQL specialist. Do not wrap unresolved tokens in a code block that appears executable.

Applicable official schema can support a documentation-grounded XQL candidate; it cannot establish tenant availability, compilation, or results. If schema is supplied or documented, validate:

1. dataset and field existence;
2. types and nullability;
3. event-time semantics;
4. value shapes;
5. product/release applicability;
6. permissions and scope;
7. bounded time/window and row sample;
8. compile and execution separately.

## 5. Iteration log

Change one major dimension at a time where practical:

| Iteration | Change | Reason | Expected effect | Observed effect | Decision |
|---|---|---|---|---|---|
| I-01 | Initial bounded plan | Establish signal | Unknown | Not run | Await tenant validation |

Record broadened windows, removed filters, alternate time fields, schema substitutions, deduplication changes, and added data sources. This prevents query drift from becoming an undocumented new hypothesis.

## 6. Evidence-to-conclusion rules

- One source is a lead; seek an independent discriminator for high-impact conclusions.
- Absence is interpretable only inside verified coverage.
- Repeated events do not automatically represent repeated entities.
- Correlation is not causation; shared values and time proximity need explanation.
- Enrichment is contextual unless corroborated by primary telemetry.
- A benign alternative is not eliminated until its discriminator is tested.
- Confidence applies only to the stated population and period.

## 7. Stopping conditions

Stop or hand off when:

- the decision is supported to the agreed confidence;
- necessary telemetry is absent or inaccessible;
- continued iteration would only restate the same evidence;
- the problem becomes query engineering, detection engineering, incident response, malware analysis, or platform administration;
- the next step is destructive or requires new authorization;
- the evidence contains sensitive material that should not be further reproduced.

Record why the hunt stopped and what evidence would reopen it.
