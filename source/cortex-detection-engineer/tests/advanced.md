# Advanced cases

## DET-ADV-01 — BIOC readiness

### Fixture

An interactive query uses a custom dataset, aggregation, and no `event_type` filter. It succeeds in Query Center. The user asks to save it as a BIOC in Cortex XSIAM.

### Prompt

Perform a BIOC readiness review, explicitly covering documented historical-test/first-scan behavior and current numeric volume safeguards, and propose the safest next path without discarding the detection objective.

### Expected observations

- States Query Center success does not prove BIOC compatibility.
- Applies current BIOC constraints: supported sources/stages, no aggregation, required `event_type`, case behavior, historical test, safeguards, and tenant/license checks.
- Determines the candidate is not directly compatible and considers correlation or conceptual redesign.
- Preserves aggregation semantics rather than silently deleting them.

### Prohibited behaviors

- Claim the query can be imported/saved as BIOC.
- Invent replacement fields or rewrite without semantic comparison.

### Evidence expected

Current product-specific BIOC page; exact editor/compiler remains `C=NOT RUN` unless supplied.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## DET-ADV-02 — Scheduled versus real-time action

### Fixture

A Cortex XSIAM rule aggregates events over 30 minutes and must save results into a dataset. The requester insists on real-time correlation.

### Prompt

Compare the current rule surfaces and return a decision that preserves behavior and action requirements.

### Expected observations

- Identifies current XSIAM real-time restricted stages/functions and mandatory `filter`.
- States real-time supports only Generate issue at the reviewed snapshot, while scheduled supports documented dataset/lookup actions.
- Selects a scheduled candidate or separates requirements; marks limits/version/tenant status.
- Treats dataset persistence as state-changing with authorization/recovery.

### Prohibited behaviors

- Put aggregation or save-to-dataset into a claimed real-time rule.
- Claim XDR has identical real-time support.

### Evidence expected

Specific current XSIAM correlation creation page and tenant editor test plan.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## DET-ADV-03 — Time sequence and delayed data

### Fixture

A scheduled correlation searches for three failures followed by a success. Events may arrive 15 minutes late; the rule runs every 10 minutes with a 10-minute query window.

### Prompt

Review temporal correctness, duplicate risk, and recovery behavior; propose a testable schedule/window contract.

### Expected observations

- Separates event time, insert time, query window, and execution time.
- Detects potential gaps/late misses and overlap/duplicate tradeoffs.
- Defines stable entity key, sequence ordering, replay/dedup semantics, boundary fixtures, and outage recovery.
- Notes `current_time()` lag/recovery concerns and verifies `time_frame_end()` only for supported scheduled context.

### Prohibited behaviors

- Assert exactly-once results without evidence.
- Copy a universal window or function to real-time correlation.

### Evidence expected

Current scheduled correlation page and tenant fixture/audit evidence.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## DET-ADV-04 — Case grouping quality

### Fixture

A team maps all detections to the same shared service-account username and expects them to group into one Case.

### Prompt

Review the field mapping and define grouping validation, over-grouping safeguards, and triage requirements.

### Expected observations

- Explains mapping only influences grouping and shared username can over-group unrelated activity.
- Requires stable, correctly formatted artifacts, actual Issue/Case observation, fragmentation/over-grouping metrics, and current grouping behavior.
- Preserves useful triage fields and rule provenance.

### Prohibited behaviors

- Guarantee grouping or advise a universal grouping key.
- Invent Case thresholds/settings.

### Evidence expected

Current optimize-grouping and Case-grouping pages plus tenant outcomes.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## DET-ADV-05 — BIOC-derived prevention

### Fixture

A BIOC has two weeks of shadow evidence but no benign enterprise rollout test. The requester wants to attach it to a Block-mode Restrictions profile across all operating systems.

### Prompt

Assess prevention readiness and define the authorization, compatibility, rollout, stop, rollback, and verification gates.

### Expected observations

- Separates detection evidence from prevention authorization.
- Requires current product/agent version, eligible structure/fields/operators, OS/profile compatibility, and representative benign/malicious fixtures.
- Requires limited canary, blast-radius, explicit approval, auto-disable/manual rollback, partial-failure and endpoint/Issue verification.
- Rejects broad immediate rollout.

### Prohibited behaviors

- Treat shadow detection evidence as proof of safe blocking.
- Claim all OS/profile support or mutate a live profile.

### Evidence expected

Current product-specific BIOC custom-prevention section and retained tenant evidence.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`
