# Rule readiness review template

**Default result:** `NOT READY` until every required gate has evidence. This is a review scaffold, not deployment approval.

## Target

- Rule ID/revision/hash: `<...>`
- Product/version/license/tenant alias: `<...>`
- Proposed surface: `<...>`
- Current state: `<research|draft|editor-tested|shadow|canary|production>`
- Reviewer/date: `<...>`

## Evidence summary

- Canonical status/qualifiers: `<...>`
- `S`: `<PASS|FAIL|NOT RUN|N/A + rationale>`
- `D`: `<PASS|FAIL|NOT RUN|N/A + rationale and dated official-source evidence>`
- `C`: `<PASS|FAIL|NOT RUN|N/A + rationale and exact tenant/editor evidence>`
- `E`: `<PASS|FAIL|NOT RUN|N/A + rationale and exact tenant execution evidence>`

## Gate review

| Gate | Evidence | Result | Finding/remediation |
|---|---|---|---|
| Behavior/threat model is falsifiable | `<...>` | `<...>` | `<...>` |
| ATT&CK is interpretation, dated | `<...>` | `<...>` | `<...>` |
| Required telemetry and coverage verified | `<...>` | `<...>` | `<...>` |
| Dataset/fields/types/nulls verified | `<...>` | `<...>` | `<...>` |
| Logic row grain/cardinality/time correct | `<...>` | `<...>` | `<...>` |
| Exact rule surface supports constructs | `<...>` | `<...>` | `<...>` |
| Baseline/threshold evidence sufficient | `<...>` | `<...>` | `<...>` |
| Positive/benign/negative/edge fixtures pass | `<...>` | `<...>` | `<...>` |
| FP/FN/evasion analysis complete | `<...>` | `<...>` | `<...>` |
| Issue fields and grouping expectations tested | `<...>` | `<...>` | `<...>` |
| Volume/capacity/safeguard margin acceptable | `<...>` | `<...>` | `<...>` |
| Permission and change authorization ready | `<...>` | `<...>` | `<...>` |
| Monitoring, rollback, retirement assigned | `<...>` | `<...>` | `<...>` |

## Surface-specific checks

- BIOC: `event_type`, sources, stages/functions, aggregation, case behavior, historical-test behavior, first-scan bound, exact current hit-disable threshold, automatic exception scope/trigger, and tenant/version revalidation: `<...>`
- Scheduled correlation: XQL restrictions, schedule/window, lag/recovery, suppression, action, output, audit: `<...>`
- Real-time correlation: supported product/source/stage/function, mandatory `filter`, Generate issue only: `<...>`
- BIOC prevention: compatible rule/agent/OS/profile, separate prevention approval, canary/rollback: `<...>`
- Analytics/ABIOC: documented controls only; no invented model settings: `<...>`

## Findings

| ID | Severity | Evidence | Required correction | Owner | Disposition |
|---|---|---|---|---|---|
| `<F-01>` | `<BLOCKER|CRITICAL|HIGH|MEDIUM|LOW>` | `<...>` | `<...>` | `<...>` | `OPEN` |

## Decision

- Readiness: `<NOT READY|READY FOR EDITOR TEST|READY FOR SHADOW|READY FOR CANARY|READY FOR APPROVED PRODUCTION SCOPE>`
- Authorized scope: `<none unless explicitly evidenced>`
- Blocking evidence: `<...>`
- Next step: `<...>`
- Safe failure: `No state change when target, permission, tests, owner, or rollback is missing.`
