# Cortex detection rule surfaces

## Contents

- [Decision rule](#decision-rule)
- [Surface matrix](#surface-matrix)
- [IOC and indicator rules](#ioc-and-indicator-rules)
- [BIOC](#bioc)
- [BIOC-derived custom prevention](#bioc-derived-custom-prevention)
- [Scheduled correlation](#scheduled-correlation)
- [Real-time correlation](#real-time-correlation)
- [Analytics and ABIOC](#analytics-and-abioc)
- [Issue and Case behavior](#issue-and-case-behavior)
- [Permissions and state changes](#permissions-and-state-changes)
- [Compatibility checklist](#compatibility-checklist)

## Decision rule

Select the surface from behavior, telemetry relationships, time requirements, and intended action. Never start with “make it real time” or “make it a BIOC” before verifying product and constraints.

All facts below use the 2026-09-04 source snapshot. Numerical limits, licenses, UI controls, stages/functions, and actions are version-sensitive and require source refresh plus tenant verification.

## Surface matrix

| Surface | Best fit | Current documented boundary | Required caution |
|---|---|---|---|
| IOC rule | Known static artifact | XSIAM distinguishes IOC from behavioral rules | Intelligence provenance and lifecycle matter |
| Indicator rule | Supported TIM indicator detection/prevention | XSIAM/TIM entitlement and supported indicator state/type | Detection and prevention are separate decisions |
| BIOC | Suspicious behavior over supported event types | Constrained XQL, datasets, stages, and historical/live matching | Query Center success is insufficient |
| BIOC custom prevention | Supported BIOC applied through endpoint Restrictions profiles | Agent/version, OS, fields, investigation types, and profile constraints | State-changing; staged approval and rollback required |
| Scheduled correlation | Multi-event/source logic in a bounded scheduled window | Current XSIAM and XDR 5 pages document scheduled correlation | Window/schedule overlap, lag, cost, and output action |
| Real-time correlation | Narrow supported logic evaluated as data is ingested | Current XSIAM page: restricted stages/functions/source; mandatory `filter` | Generate issue only at this snapshot; no scheduled write actions |
| Analytics/ABIOC | Palo Alto-delivered behavioral analytics/baselines | Platform analytics and profile behavior | Do not invent detector internals or user-defined training controls |

## IOC and indicator rules

Current XSIAM documentation describes IOC rules as static criteria such as hashes, IPs, domains, filenames, and paths. BIOCs are behavioral. Do not call a thresholded sequence an IOC merely because it includes an IP or hash.

TIM indicator rules link supported indicators in the tenant intelligence library to detection and, where supported, prevention. Before operationalizing:

- confirm product and TIM entitlement;
- validate indicator type, normalization, provenance, confidence/reputation, status, and detectability;
- separate matching from malicious verdict;
- define expiration and revocation;
- verify downstream enforcement scope and rollback;
- keep response approval independent.

See [S01](official-sources.md#s01--what-are-detection-rules) and [S18](official-sources.md#s18--indicator-rules-for-prevention-and-detection).

## BIOC

Current XSIAM and XDR 5 creation pages document these key constraints:

- rule logic is XQL-backed;
- the query must at minimum filter on `event_type`;
- documented sources include `xdr_data`, `cloud_audit_log`, and their presets, with license implications;
- custom datasets are not supported for BIOC at the reviewed snapshot;
- only `filter`, `alter`, and functions without aggregation are supported for the BIOC query;
- field values are evaluated case-insensitively;
- the editor provides historical testing;
- after creation, historical and newly received data are considered under documented behavior;
- the first historical scan is bounded to the first 10,000 matches;
- the product automatically disables BIOCs at 5,000 or more hits in 24 hours;
- it automatically creates a PROCESS-SHA256 exception above 100 endpoints in 72 hours.

Treat these as `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` until the exact target product/version is checked. A safeguard firing is an operational incident: record the generated exception or disabled state, investigate selectivity, and retest. It is not normal tuning.

The `event_type` requirement does not mean a Process category is a Process Start event. For start-only behavior, validate the product/editor's current subtype representation and test both start and non-start Process subtypes.

See [S06](official-sources.md#s06--create-a-bioc-rule-in-cortex-xsiam) and [S07](official-sources.md#s07--create-a-bioc-rule-in-cortex-xdr).

## BIOC-derived custom prevention

Current BIOC pages describe optional conversion to custom prevention through Restrictions profiles with rule-structure, supported-field, OS, and agent requirements. This is prevention, not merely detection.

Required gates:

1. prove detection selectivity without prevention;
2. confirm exact product/agent version and eligible rule structure;
3. verify every field/operator against the current prevention section;
4. identify endpoint OS/profile scope and critical assets;
5. test benign and malicious fixtures in non-production;
6. define staged deployment and stop conditions;
7. require owner and explicit approval;
8. record auto-disable and manual rollback behavior;
9. verify endpoint and Issue outcomes after change.

Never produce a claim of safe prevention from a query-only review. Do not instruct a live profile mutation unless the user explicitly requested execution and all authorization prerequisites are satisfied.

## Scheduled correlation

Current XSIAM and XDR 5 documentation describes XQL-based scheduled rules with a schedule, query timeframe, suppression, Issue settings, and documented result actions. At this snapshot, the pages document:

- unsupported general features such as `call`, `top`, dataset wildcards, and `tag` in correlation rules;
- `current_time()` lag/recovery concerns and recommended scheduled use of `time_frame_end()` where supported;
- schedule choices with a minimum custom frequency of 10 minutes;
- a query timeframe up to seven days;
- a maximum of 1,200 active user-created scheduled correlations;
- automatic disablement at 5,000 or more hits in 24 hours;
- optional suppression with fields and duration;
- resulting actions to generate an Issue, save to a dataset, add to a lookup, or remove from a lookup.

All numbers and options must be rechecked before use. Dataset and lookup actions are state-changing. They require exact target, schema, uniqueness/delete semantics, volume bound, authorization, recovery, and post-write verification.

Design schedule and window deliberately:

- define event-time versus ingestion-time behavior;
- decide overlap or gap handling;
- handle late arrivals, downtime, and recovery;
- prevent duplicate signals across executions;
- size query/output below resource and Issue-volume risk;
- keep a drill-down query compatible and validate its substituted fields.

See [S08](official-sources.md#s08--create-a-correlation-rule-in-cortex-xsiam) and [S09](official-sources.md#s09--create-a-correlation-rule-in-cortex-xdr).

## Real-time correlation

**2026-09-06 source discrepancy:** the migrated XSIAM Markdown page retains the stage/function restrictions below but omits the legacy official page's note limiting the resulting action to Generate issue. The indexed legacy official page still states that restriction. Preserve the 2026-09-04 boundary as VERSION-DEPENDENT pending current target clarification; omission does not prove that lookup or dataset writes have become supported. Do not configure a newly inferred action. See the dated recheck in [official-sources.md](official-sources.md).

The current XSIAM creation page distinguishes real-time evaluation as data is ingested. At the reviewed snapshot it documents:

- supported inputs including XSIAM Issues, cloud audit logs, third-party datasets, and data models;
- allowed stages `dataset`, `datamodel`, `filter`, `alter`, `fields`, and `config case_sensitive`;
- a mandatory `filter` stage;
- unsupported functions `json_extract_scalar_array`, `parse_epoch`, and `time_frame_end`;
- no dataset views;
- additional correlation restrictions, including no `tag`, `call`, `top`, or dataset wildcards;
- only **Generate issue** as the resulting action; other scheduled actions are disabled.

Treat the list as an exact reviewed snapshot, not a future-proof language definition. Verify the page and editor again for every target version.

Do not port a scheduled aggregation, lookup mutation, dataset write, or timing assumption into real time. If the behavior needs unavailable state/windowing, choose scheduled correlation or redesign the observable.

The current XDR 5 correlation page reviewed for this Skill describes scheduled configuration and a Pro license. It does not establish XSIAM-style real-time support for XDR. Mark such a request `UNVERIFIED` until a current XDR-specific page/editor proves it.

## Analytics and ABIOC

Current XSIAM documentation distinguishes:

- Analytics Issues: suspicious activity composed of multiple events that deviates from a baseline established over time;
- Analytics BIOCs: a single suspicious-behavior event with an identified causality chain, using user, endpoint, and network profiles.

Palo Alto delivers and tunes this content. A detection-engineering review may inspect enabled state, variants, Issues, source coverage, and analyst outcomes. It must not invent feature engineering, retraining APIs, baseline durations, or custom thresholds that the official target surface does not expose.

See [S16](official-sources.md#s16--analytics-issues-and-analytics-biocs).

## Issue and Case behavior

Use current user-facing terms:

```text
rule match -> Issue -> qualification/grouping -> Case or Insight outcome
```

Preserve literal Incident/Alert names only where official compatibility interfaces require them.

Current XSIAM documentation says field mapping can help grouping by supplying supported artifacts, but mapping does not guarantee grouping. Case logic is broader and dynamic. Therefore:

- validate mapped field type/format and non-null presence;
- avoid overbroad identifiers that merge unrelated activity;
- measure fragmentation and over-grouping;
- inspect actual Issues and Cases;
- never promise a Case outcome from the rule design alone.

See [S12](official-sources.md#s12--optimize-case-grouping-in-correlations) and [S13](official-sources.md#s13--case-grouping).

## Permissions and state changes

Current XSIAM Detection Rules permissions depend on related Query Center access. Confirm the effective user/service identity and object/data scope, not merely a role name.

State-changing operations include:

- import/create/edit/enable/disable/delete rule;
- add/remove exception;
- change suppression, severity, mappings, or schedule;
- save correlation output to a dataset;
- add/update/remove lookup data;
- attach BIOC prevention to a profile.

Require authorization, exact target, owner, bounded scope, dependencies, recovery, verification, and audit evidence.

## Compatibility checklist

- [ ] Product, version, edition/license, and rollout recorded
- [ ] Rule surface chosen from current product evidence
- [ ] Dataset, fields, types, and nulls verified at declared level
- [ ] Stages/functions/operators compatible with the rule surface
- [ ] Window/schedule/real-time semantics tested
- [ ] Output grain and triage fields defined
- [ ] Action supported and separately authorized
- [ ] Suppression and grouping behavior tested rather than assumed
- [ ] Positive, benign, negative, boundary, delayed, duplicate, and volume fixtures pass
- [ ] Safeguard proximity, generated exceptions, and disabled state monitored
- [ ] Rollback/disable and retirement owner named
- [ ] `S`, `D`, `C`, and `E` recorded independently
