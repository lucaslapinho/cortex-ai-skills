# Cortex Control Operational Handoff

Complete before a control becomes an operational dependency. This record does not itself authorize promotion.

## Artifact and ownership

| Field | Value |
|---|---|
| Handoff ID/date | `{{OPS-###}}` / `{{YYYY-MM-DD}}` |
| Control/artifact/version/hash | `{{VALUES}}` |
| Product/release/surface | `{{VALUES}}` |
| Environment | `{{NON-PRODUCTION / PRODUCTION}}` |
| Requirement/risk/decision | `{{REQ/RSK/DEC IDS}}` |
| Accountable control owner | `{{ROLE}}` |
| Operator/on-call | `{{ROLE}}` |
| Platform/data owner | `{{ROLE}}` |
| Approver | `{{ROLE}}` |
| Recovery owner | `{{ROLE}}` |

## Current evidence

| Property | Result | Evidence class/level | Record | Scope limit |
|---|---|---|---|---|
| Product support | `{{RESULT}}` | `{{CLASS / D}}` | `{{EV/VAL}}` | `{{LIMIT}}` |
| Schema/editor/execution | `{{RESULT}}` | `{{QUALIFIER / C/E}}` | `{{EV/VAL}}` | `{{LIMIT}}` |
| Signal quality | `{{RESULT}}` | `{{LEVEL}}` | `{{EV/VAL}}` | `{{LIMIT}}` |
| Safety/recovery | `{{RESULT}}` | `{{LEVEL}}` | `{{EV/VAL}}` | `{{LIMIT}}` |
| Integrated path | `{{RESULT}}` | `{{LEVEL}}` | `{{EV/VAL}}` | `{{LIMIT}}` |

Any required `NOT RUN` item blocks a production-readiness claim.

## Control behavior

- Trigger/input contract: `{{DESCRIPTION}}`
- Output/signal/action and grain: `{{DESCRIPTION}}`
- Expected normal volume/timing: `{{MEASURED BASELINE / UNKNOWN}}`
- Known benign paths: `{{LIST}}`
- Known misses/coverage gaps: `{{LIST}}`
- Dependencies: `{{SOURCE, QUERY, RULE, TIM, PLAYBOOK, INTEGRATION, IDENTITY}}`
- Degraded/manual path: `{{PLAN}}`

## Health monitoring

| Health signal | Source | Expected/threshold owner | Alert/escalation | Evidence retained |
|---|---|---|---|---|
| entitlement/feature | `{{SOURCE}}` | `{{OWNER-APPROVED VALUE}}` | `{{PATH}}` | `{{LOCATION}}` |
| ingestion/freshness/schema | `{{SOURCE}}` | `{{VALUE}}` | `{{PATH}}` | `{{LOCATION}}` |
| permission/object/command | `{{SOURCE}}` | `{{VALUE}}` | `{{PATH}}` | `{{LOCATION}}` |
| rule/job/playbook/feed/action | `{{SOURCE}}` | `{{VALUE}}` | `{{PATH}}` | `{{LOCATION}}` |
| errors/backlog/capacity | `{{SOURCE}}` | `{{VALUE}}` | `{{PATH}}` | `{{LOCATION}}` |

## Outcome monitoring

| Outcome | Measurement | Review owner/cadence | Decision triggered |
|---|---|---|---|
| signal/case disposition | `{{METHOD}}` | `{{ROLE/CADENCE}}` | `{{TUNE/ESCALATE}}` |
| false-positive causes | `{{METHOD}}` | `{{ROLE/CADENCE}}` | `{{ACTION}}` |
| known-positive/negative fixtures | `{{METHOD}}` | `{{ROLE/CADENCE}}` | `{{ACTION}}` |
| misses/incidents/hunt findings | `{{METHOD}}` | `{{ROLE/CADENCE}}` | `{{ACTION}}` |
| enrichment/action/recovery | `{{METHOD}}` | `{{ROLE/CADENCE}}` | `{{ACTION}}` |

Numeric targets require owner approval and measured context.

## Exception and tuning ledger

| Exception/change | Rationale/evidence | Scope | Coverage impact/test | Owner/approver | Expiry/review | Rollback |
|---|---|---|---|---|---|---|
| `{{ITEM}}` | `{{VALUE}}` | `{{VALUE}}` | `{{VALUE}}` | `{{ROLES}}` | `{{DATE}}` | `{{PLAN}}` |

## Failure, response, and recovery

| Failure | Detection | Immediate safe state | Escalation | Recovery/verification |
|---|---|---|---|---|
| data unavailable | `{{SIGNAL}}` | `{{FAIL CLOSED/DEGRADED}}` | `{{OWNER}}` | `{{PLAN}}` |
| permission/dependency denied | `{{SIGNAL}}` | `{{STATE}}` | `{{OWNER}}` | `{{PLAN}}` |
| timeout/partial action | `{{SIGNAL}}` | `{{STATE}}` | `{{OWNER}}` | `{{RECONCILE/COMPENSATE}}` |
| noise or suspected miss | `{{SIGNAL}}` | `{{STATE}}` | `{{OWNER}}` | `{{VALIDATE BEFORE TUNE}}` |

- Last recovery test/result: `{{DATE / PASS/FAIL/NOT RUN/N/A / RATIONALE / EVIDENCE}}`
- Manual containment/investigation path: `{{RUNBOOK}}`
- Evidence/privacy controls: `{{LOCATION, ACCESS, RETENTION, REDACTION}}`

## Change and retirement

- Promotion/change record: `{{ID / PENDING}}`
- Prior state and recovery artifact: `{{REFERENCE}}`
- Stop/rollback triggers: `{{OBJECTIVE CONDITIONS}}`
- Material-change revalidation: `{{PRODUCT, LICENSE, SCHEMA, SOURCE, ROLE, THREAT, POLICY}}`
- Review cadence: `{{OWNER-APPROVED VALUE}}`
- Retirement trigger and approver: `{{VALUE}}`
- Cleanup/dependency check: `{{SCHEDULES, CREDENTIALS, EXCEPTIONS, DATASETS, INTEGRATIONS, CONSUMERS}}`

## Handoff decision

- Operations acceptance: `{{ACCEPTED / REVISE / HOLD / PENDING}}`
- Evidence: `{{RECORD}}`
- Blocking gaps: `{{LIST / NONE}}`
- Residual limitations: `{{LIST}}`
- Explicit non-claims: `{{LIST}}`
