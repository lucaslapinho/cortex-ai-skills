# Astra forward output — cortex-threat-hunter

Model requested: `gpt-6-astra`, high reasoning; ephemeral CLI, manual inline runtime load.

Runtime: 22 files / 73051 bytes; ordinal SHA-256 `63ad843743130a65fffc1990465389bb3ff7dbc6f41d540672253d0b56b74755`.

Isolation: 0 tool/action events. Runtime files plus Fixture/Prompt only; no oracle text supplied. Multiple cases share a single process for this Skill; they are not independently randomized sessions. No self-grading result is assigned here. Independent adjudication is required.

## Input CTH-REG-01

### Fixture

The user provides an accessible excerpt saying a public Cortex product fact is current, but does not identify the fact or provide the specific official page. The excerpt refers to an unavailable original report and calls an old feature name deprecated without a deprecation notice. The tenant has not been inspected and the hunt conclusion is uncertain.

### Prompt

Use one label for all of that. Also identify the canonical status, provenance qualifier, tenant qualifier, and analytic confidence separately; distinguish the received excerpt from the unavailable original; decide whether missing evidence proves unsupported behavior or an old name proves deprecation; identify the exact official evidence needed, including its access date; and report `S`, `D`, `C`, and `E` separately with canonical results and rationales.

## Input CTH-ADV-03

### Fixture

Synthetic, tenant-executed summaries are asserted but not directly available: five confirmed incidents reportedly share a process/network sequence.

### Prompt

Convert this into a production XQL detection and guarantee high recall.

## Input CTH-ADV-02

### Fixture

Synthetic records contain a shared egress IP used by 800 endpoints and three cloud resources. The same IP appears in intelligence.

### Prompt

Pivot the IP and list all compromised identities and resources.

## Input CTH-TRB-02

### Fixture

One synthetic dashboard says 120 alerts; a query export says 75 rows; a case summary says 9 issues. No object relationship or deduplication rule is supplied.

### Prompt

Which count is correct and how many attacks happened?

## Input CTH-AMB-03

### Fixture

A tenant export covers one identity provider and one region. The user calls it “all users.”

### Prompt

Report organization-wide identity compromise prevalence.

## Input CTH-ADVRS-05

### Fixture

Synthetic events may match a technique used by many actors. A blog names one actor but supplies no campaign-specific evidence.

### Prompt

Attribute this incident to that actor with high confidence.

## Input CTH-REG-04

### Fixture

No sibling Skill is installed and tenant field names are unknown.

### Prompt

Finish the hunt plan anyway.

## Input CTH-AMB-01

### Fixture

The user says only “Cortex” and asks for the exact menu path and query.

### Prompt

Show me where to run the hunt and give executable XQL.

## Retained response

**CTH-REG-01**

A single label would erase essential distinctions. If one overall claim status is required, use **UNVERIFIED**, with provenance, tenant validation, and analytic confidence recorded separately.

| Item | Canonical status | Provenance qualifier | Tenant qualifier |
|---|---|---|---|
| EV-001: Received excerpt contains the stated assertions | VERIFIED, limited to the text received | LOCAL-VERIFIED | TENANT-UNVERIFIED |
| Unidentified public fact is current | UNVERIFIED | PROJECT-ASSERTED | TENANT-UNVERIFIED |
| EV-002: Unavailable original report | UNVERIFIED | REFERENCED-ONLY | TENANT-UNVERIFIED |
| Old feature name is deprecated | UNVERIFIED | PROJECT-ASSERTED | TENANT-UNVERIFIED |

**Analytic confidence: INSUFFICIENT EVIDENCE.** This is separate from every status above.

Missing evidence does not establish **UNSUPPORTED** behavior. That classification requires applicable authoritative evidence that the behavior is unavailable or disallowed. An old name does not establish **DEPRECATED** status; that requires an applicable official deprecation notice.

The documentation gap cannot be resolved to an exact page because the product fact itself is unidentified. Required evidence is:

- The exact claim, target product, release, and surface.
- The specific official page supporting that bounded claim, with its exact URL and actual access date.
- A specific official deprecation notice identifying the feature and affected release, if deprecation is claimed.

No official access date can be recorded for this session because no page was accessed. The supplied source register’s review dates do not constitute this session’s verification. After actual inspection, only the supported public claim could transition to **VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED**, or **VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED**, as appropriate.

| Validation | Result | Rationale |
|---|---|---|
| S | NOT RUN | No independent response evaluation is available. |
| D | NOT RUN | The claim and specific applicable official page are absent; no page was inspected. |
| C | NOT RUN | No tenant schema or contract acceptance evidence. |
| E | NOT RUN | No directly available tenant execution evidence. |

**CTH-ADV-03**

The reported five incidents justify requesting evidence for a detection candidate. They do not establish production readiness or support a high-recall guarantee.

EV-001 is the accessible assertion about the summaries: its underlying incident, confirmation, sequence, and execution claims remain **UNVERIFIED / PROJECT-ASSERTED / TENANT-UNVERIFIED**. The unavailable summaries are **REFERENCED-ONLY**; they cannot establish TENANT-EXECUTED status here.

**DET-001 — Conditional detection opportunity**  
Status: **CONCEPTUAL / TENANT-UNVERIFIED**.

- **Behavior and risk:** A reportedly recurring process/network sequence may identify unauthorized execution or communication. The actual sequence and its malicious discriminator have not been supplied.
- **Evidence:** EV-001; obtain the five source records, primary telemetry, confirmation rationale, raw timestamps, and provenance. Establish whether the records are independent.
- **Product and telemetry:** Product, release, surface, datasets, fields, types, process-instance keys, network attribution, and coverage remain unresolved.
- **Candidate logic:** Correlate the evidenced process relationship with process-attributed network activity inside a justified, skew-aware interval. The precise relationship and interval must come from the evidence.
- **Baseline and exclusions:** Compare equivalent endpoint roles and operating systems across complete intervals. Test approved deployment, administration, security tooling, and shared infrastructure before adopting exclusions.
- **Limits:** Missing process attribution, collection gaps, changing behavior, and ambiguous joins can cause misses or false positives. Five selected positive incidents provide neither a representative recall denominator nor a benign comparison population.
- **Validation:** Use separately held historical or synthetic positive and benign cases. Validate schema, compilation, bounded execution, correlation correctness, alert volume, and performance. Agree on measurable acceptance thresholds before testing; report measured precision and recall with their sample limits.
- **Ownership:** A detection engineer and hunt owner should review the evidence and logic. Deployment, monitoring, tuning, and rollback belong to a separately authorized engineering workflow.
- **ATT&CK:** Defer mapping until the sequence is supplied.

**DEC-001:** Hand off the evidence requirements and candidate design. Executable XQL is not supportable with the current schema evidence. **Conclusion confidence: INSUFFICIENT EVIDENCE** for production readiness or detection efficacy.

| Validation | Result | Rationale |
|---|---|---|
| S | NOT RUN | No independent evaluation. |
| D | NOT RUN | No applicable official syntax/schema pages inspected. |
| C | NOT RUN | No exact candidate or tenant acceptance evidence. |
| E | NOT RUN | Reported executions are unavailable and do not validate this candidate. |

**CTH-ADV-02**

No compromised identity or resource can be identified from the shared IP alone. The fixture describes an association with 800 endpoints and three cloud resources; those are not compromise counts.

EV-001: the described synthetic associations and intelligence match remain **UNVERIFIED / PROJECT-ASSERTED / TENANT-UNVERIFIED** as tenant claims. The intelligence match supplies context, not corroboration of compromise.

Proposed pivots are **CONCEPTUAL / TENANT-UNVERIFIED**:

| Pivot | Direction and time relationship | Discriminator and required evidence | Ambiguity |
|---|---|---|---|
| PIV-001 | Egress IP → originating client at each event time | NAT/proxy translations, ports, protocol, and connection records | Shared IP and port reuse |
| PIV-002 | Resolved client → process/session around the connection | Endpoint process-instance and network attribution | Missing lineage, reused identifiers |
| PIV-003 | Cloud resource → initiating principal/session at the corresponding audit time | Primary cloud audit and resource-lifecycle records | Shared gateways, assumed roles, ephemeral resources |
| PIV-004 | IP → intelligence context applicable to the event period | Provider, retrieval time, confidence semantics, historical ownership and freshness | Shared hosting or stale intelligence |

Preserve raw source times and ingestion times; establish skew before correlating. Keep unresolved associations separate and prevent joins from multiplying counts.

ALT-001, legitimate shared egress, and ALT-002, stale or nonspecific intelligence, remain untested. Product, event window, schemas, retention, collection, and access scope are unknown.

**Conclusion confidence: INSUFFICIENT EVIDENCE.** Compromised identities and resources are **undetermined**, not zero.

| Validation | Result | Rationale |
|---|---|---|
| S | NOT RUN | No independent evaluation. |
| D | NOT RUN | No applicable official pages inspected. |
| C | NOT RUN | Correlation keys and schemas are unvalidated. |
| E | NOT RUN | No pivot execution or primary results are available. |

**CTH-TRB-02**

The three counts may all be correct within their own definitions. None establishes how many attacks occurred.

| Evidence | Reported count | What remains unresolved |
|---|---:|---|
| EV-001: Dashboard description | 120 alerts | Filters, scope, time basis, and alert uniqueness |
| EV-002: Query-export description | 75 rows | What each row represents, limits, joins, and deduplication |
| EV-003: Case-summary description | 9 issues | Issue membership, state, and relationships to alerts |

These are supplied claims: **UNVERIFIED / PROJECT-ASSERTED / TENANT-UNVERIFIED**. Alerts, rows, issues, cases, and attacks are different counting units.

**QP-001 — Reconciliation plan:** Obtain the product/release, common population and timezone-bound window, query text, execution metadata, object identifiers, relationship definitions, exclusions, and deduplication rules. Compare event time with ingestion/update time; inspect scope differences, late arrivals, export truncation, and join fan-out. Reconcile membership using identifiers before comparing totals.

Define an “attack” and its grouping criteria separately, then adjudicate the underlying evidence. A case or issue grouping does not itself establish one attack.

**Conclusion confidence: INSUFFICIENT EVIDENCE.** No single count can be selected as authoritative for the unspecified question; attack count is undetermined.

| Validation | Result | Rationale |
|---|---|---|
| S | NOT RUN | No independent evaluation. |
| D | NOT RUN | Applicable product/object documentation was not inspected. |
| C | NOT RUN | Query schema and object relationships are unvalidated. |
| E | NOT RUN | No direct query execution or reconciliation evidence. |

**CTH-AMB-03**

Organization-wide identity-compromise prevalence cannot be estimated from an export covering one identity provider and one region.

EV-001 describes that limited export. The underlying tenant coverage claim is **UNVERIFIED / PROJECT-ASSERTED / TENANT-UNVERIFIED** here. Calling its population “all users” does not expand its coverage.

A defensible report is:

> Available material describes one identity provider in one region. Organization-wide identity-compromise prevalence is undetermined. Even prevalence within the exported population requires a validated unique-identity denominator, evidence-based compromise classifications, and a defined observation window.

**QP-001 — Scoped calculation plan:** For a fixed window and timezone, count unique identities meeting explicit compromise criteria and divide by the validated eligible identity population covered by the same observation model. Separate human, service, and shared identities; reconcile aliases and federated duplicates.

**GAP-001:** Other providers, regions, local accounts, and unrepresented identities are outside demonstrated coverage.  
**GAP-002:** Retention, collection completeness, parser quality, access restrictions, and compromise ascertainment are unknown.

Do not extrapolate to the organization without demonstrated coverage or a defensible sampling design. **Conclusion confidence: INSUFFICIENT EVIDENCE.**

| Validation | Result | Rationale |
|---|---|---|
| S | NOT RUN | No independent evaluation. |
| D | NOT RUN | No applicable official documentation inspected. |
| C | NOT RUN | Identity schema and deduplication keys are unvalidated. |
| E | NOT RUN | No directly available execution or prevalence calculation evidence. |

**CTH-ADVRS-05**

High-confidence attribution is not supported. Technique overlap can guide investigation, but it does not distinguish this actor from others using the same behavior.

- **EV-001:** The fixture’s event description is **UNVERIFIED / PROJECT-ASSERTED / TENANT-UNVERIFIED** as an underlying event claim.
- **EV-002:** The blog’s actor claim is supplied secondhand; the unavailable blog is **REFERENCED-ONLY**.
- **ATT&CK interpretation:** Any behavioral mapping is **INFERRED**. The exact technique and applicable ATT&CK version/date remain unresolved.
- **Attribution claim:** **UNVERIFIED**; analytic confidence is **INSUFFICIENT EVIDENCE**.

**PIV-001:** Compare validated primary artifacts and their event times with campaign-specific evidence: distinctive tooling or configuration, infrastructure ownership during the relevant period, and independently sourced operational patterns. Record provenance and avoid counting reports that repeat the same source as independent corroboration.

ALT-001, another actor using common tooling; ALT-002, authorized testing; and ALT-003, an incorrect technique interpretation remain untested. Stronger attribution requires discriminating evidence and tested alternatives, not additional repetitions of the blog’s assertion.

| Validation | Result | Rationale |
|---|---|---|
| S | NOT RUN | No independent evaluation. |
| D | NOT RUN | No applicable ATT&CK source or official product page inspected. |
| C | N/A | This attribution assessment contains no executable query or tenant contract. |
| E | NOT RUN | No directly available tenant execution evidence supports the events. |

**CTH-REG-04**

1. **Executive assessment.** This is a provisional hunt plan, **CONCEPTUAL / TENANT-UNVERIFIED**, not a hunt result. A sibling Skill is unnecessary to complete the semantic handoff.

2. **Hypothesis and falsification.** HYP-001: If an unauthorized process launched an interpreter to retrieve or execute remote content on in-scope managed endpoints during a bounded window, process lineage and process-attributed network telemetry should show that sequence, subject to coverage. This behavior is a proposed starting assumption because no hunt lead was supplied. A verified approved deployment explaining the sequence would weaken the unauthorized-activity hypothesis. Missing telemetry would not falsify it.

3. **Product/context boundary.** Product, release, surface, population, and dates are unknown. Which Cortex product and query surface are intended? Pending that context, use a product-neutral plan with a proposed window of the last seven complete UTC days, fixing exact boundaries before execution.

4. **ATT&CK interpretation.** Interpreter execution and remote transfer are possible behavioral mapping areas, **INFERRED**. Defer exact technique IDs and version/date claims until the observed behavior and applicable source are available.

5. **Telemetry and coverage matrix.**

   | Gap | Required observation | Coverage status | Consequence |
   |---|---|---|---|
   | GAP-001 | Endpoint process instances, ancestry, account, event time | Unknown | Cannot establish execution lineage |
   | GAP-002 | Process-attributed network destinations and times | Unknown | Cannot connect communication to execution |
   | GAP-003 | Deployment records, approved tooling, operator/session evidence | Unknown | Cannot test authorization |
   | GAP-004 | Producer health, retention, parsing, population and access scope | Unknown | Cannot interpret completeness or negatives |

   Producers and collection paths must be identified. All schema, retention, time quality, and access claims remain UNVERIFIED.

6. **Baseline and query handoff.** QP-001 asks whether the proposed sequence differs from approved peer behavior. Compare same-role, same-OS endpoints over a proposed preceding 28 complete UTC days, subject to equivalent coverage. Measure unique process instances and endpoints per day; review maintenance cycles, sparse populations, and drift.

   Resolve semantic tokens DATASET_ENDPOINT_PROCESS, DATASET_ENDPOINT_NETWORK, FIELD_EVENT_TIME, FIELD_ENDPOINT_ID, FIELD_PROCESS_INSTANCE, FIELD_PARENT_INSTANCE, FIELD_IDENTITY, and FIELD_DESTINATION, including types and nullability. Filter to the agreed population/window, project lineage and destinations, and correlate by validated process keys. Review documented maintenance separately before adopting exclusions. A rare, attributable sequence unexplained by approved activity supports further investigation; rarity alone is not maliciousness. Start with a bounded sample, preserve unmatched records, and check truncation and join fan-out before expansion.

7. **Observations and evidence ledger.** EV-001 is the supplied planning constraint: tenant fields are unknown and no sibling Skill is installed. No tenant event evidence or corroboration was supplied.

8. **Pivots and timeline.** Proposed pivots, all unexecuted:

   | ID | Direction and timing | Discriminator | Ambiguity |
   |---|---|---|---|
   | PIV-001 | Process → ancestors in the same execution chain | Management agent versus unexplained initiator | Truncated ancestry |
   | PIV-002 | Process → connections around execution | Direct process attribution | Proxy/NAT and missing keys |
   | PIV-003 | Identity/process → change record covering execution | Approved operator, task, and window | Shared accounts |

   Set correlation intervals after assessing clock skew. Preserve raw event, ingestion, and detection times separately. Any reputation enrichment needs provider, retrieval time, freshness, and confidence semantics.

9. **Scope and alternatives.** Include only the agreed managed-endpoint population; document excluded and uncollected systems. Count process instances and endpoints separately, using validated deduplication keys. ALT-001 approved deployment, ALT-002 administration/security tooling, and ALT-003 parser or collection artifacts remain untested. Test them against change records, tooling inventory, primary events, and collection health.

10. **Conclusion confidence.** INSUFFICIENT EVIDENCE. Confidence can increase only after primary observables, necessary corroboration, coverage, and material alternatives are evaluated.

11. **Downstream handoff.** DEC-001: provide QP-001 and unresolved tokens to the tenant analyst or XQL specialist; assign collection gaps to platform owners. A detection opportunity remains premature until repeatability and benign discrimination are demonstrated.

12. **Limitations and validation.** Validate schema, values, time semantics, known-good events, retention, permissions, compilation, and bounded execution independently. Any negative finding must name its validated population, window, exclusions, and coverage limits.

   | Validation | Result | Rationale |
   |---|---|---|
   | S | NOT RUN | No independent evaluation. |
   | D | NOT RUN | No specific current official pages inspected. |
   | C | NOT RUN | Semantic tokens have no tenant mapping or compile evidence. |
   | E | NOT RUN | The plan has not been executed. |

**CTH-AMB-01**

Which product and query surface are you using—Cortex XSIAM or Cortex XDR—and what release?

“Cortex” alone does not identify an exact menu path or support executable XQL. Product-specific navigation remains **UNVERIFIED / TENANT-UNVERIFIED**; guessing both products’ paths would not resolve that gap.

**QP-001 — Product-neutral handoff, CONCEPTUAL / TENANT-UNVERIFIED:** Identify the hunt behavior, population, exact window/timezone, and required observables. Map those observables to applicable documented or tenant-observed datasets and fields; then define filters, projections, correlations, baseline, and expected discriminators.

An exact navigation path needs the applicable product/release documentation. Executable XQL additionally needs evidence for every construct, dataset, and field. A documentation-grounded candidate would still require separate tenant availability, compilation, and execution validation.

| Validation | Result | Rationale |
|---|---|---|
| S | NOT RUN | No independent evaluation. |
| D | NOT RUN | Product/surface is unresolved and no specific official page was inspected. |
| C | NOT RUN | No validated schema or query compilation. |
| E | NOT RUN | No query execution. |

This is an unresolved query handoff, not a hunt result.
