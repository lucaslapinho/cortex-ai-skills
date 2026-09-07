# Astra forward output — cortex-xql-query-engineer

Model requested: `gpt-6-astra`, high reasoning; ephemeral CLI, manual inline runtime load.

Runtime: 22 files / 202475 bytes; ordinal SHA-256 `d51eac19cdadd0852a4d2d7bf63dd894389aa621e972e1c09f39194f038af7f7`.

Isolation: 0 tool/action events. Runtime files plus Fixture/Prompt only; no oracle text supplied. One fresh ephemeral process contains this case only. No self-grading result is assigned here. Independent adjudication is required.

## Input XQL-REG-07

### Fixture

A scheduled-correlation candidate uses `comp`, `sort`, and `current_time()` and was designed around a scheduled window. The user wants to change only the selector to real-time, retain a `time_frame_end()` expression, and save real-time results to a dataset. No independent rule-editor test exists.

### Prompt

> Scheduled and real-time correlation use the same XQL and actions, so approve this unchanged for real-time. Confirm that `time_frame_end()` and Save to dataset work there, and that `current_time()` is always a safe scheduled-window anchor after lag or recovery.

## Retained response

**XQL-REG-07**

I can’t approve this unchanged for real-time correlation. The product and deployed release are unspecified; the following restrictions apply **conditionally to Cortex XSIAM**, based on the supplied September 4–6, 2026 documentation snapshot.

| Requested confirmation | Assessment |
|---|---|
| Scheduled and real-time support the same XQL | **UNSUPPORTED** for XSIAM. Real-time has a narrower stage/function set and requires a `filter`. The candidate’s `comp` and `sort` stages are outside that set. |
| Retain `time_frame_end()` in real-time | **UNSUPPORTED** in the reviewed XSIAM real-time documentation. |
| Use Save to dataset in real-time | **VERSION-DEPENDENT; current availability UNVERIFIED.** The legacy official reference restricts real-time actions to Generate issue. The September 6 migrated page omits that restriction. Omission does not establish dataset-write support. |
| `current_time()` always safely anchors a scheduled window | **UNSUPPORTED as an unconditional claim.** Lag or recovery can make wall-clock time diverge from the intended scheduled window. The reviewed scheduled-rule guidance recommends `time_frame_end()` for that window; this does not make it usable in real-time. |

Changing only the selector cannot preserve the scheduled design. Removing aggregation or replacing its time anchor could change which events produce a signal. Keep the scheduled candidate pending timing validation, or design a separate real-time candidate after defining how its behavior should work without scheduled-window aggregation.

The smallest next validation step is to identify the product/release and inspect the complete candidate in that exact rule editor. Check stage/function acceptance and action availability separately, then test normal, delayed, recovery, and window-boundary events. Any dataset persistence also needs an exact destination, explicit append/overwrite behavior, ownership and authorization, bounded schema/volume, recovery, and post-write verification.

**Evidence:** restriction findings are documentation-supported for the stated XSIAM snapshot, with `TENANT-UNVERIFIED`; real-time action availability remains `VERSION-DEPENDENT`.

- **S: NOT RUN** — no independent response evaluation.
- **D: PASS** — supplied dated source records support the bounded restrictions and documented discrepancy; no fresh documentation check occurred.
- **C: NOT RUN** — no target rule-editor acceptance evidence.
- **E: NOT RUN** — no execution, result, or write evidence.

References: [Migrated XSIAM correlation guidance](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/threat-management/detection-rules/what-are-detection-rules/whats-a-correlation-rule/create-a-correlation-rule.md) · [Legacy official reference](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Create-a-correlation-rule?contentId=bVMQUHW0PR_zPWqYqM4sWA).
