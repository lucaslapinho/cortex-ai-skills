# Hunt-to-detection promotion

## Objective

Assess whether a hunt observation—multiple failed authentications followed by a success for the same identity—should become a durable detection.

## Product and evidence

- Product: Cortex XSIAM 3.x, tenant/version/license not supplied
- Candidate: scheduled correlation; real-time compatibility not assumed
- Evidence: `CONCEPTUAL / TENANT-UNVERIFIED`
- `S: NOT RUN` — no independent evaluation of this example revision.
- `D: PASS` — cited product boundaries were documented at the stated source snapshot; reported hunt observations remain unverified.
- `C: NOT RUN` — no exact tenant schema or rule-editor acceptance.
- `E: NOT RUN` — no tenant execution or observed detection outcome.

## Hunt evidence received

The hunt author reports several examples. No raw events, schema, query revision, benign controls, coverage record, or analyst dispositions were attached. The report is a lead, not proof of repeatability or detection readiness.

## Promotion questions

1. Is the behavior falsifiable and materially risky for the protected identity population?
2. Are failure and success events collected, parsed, timestamped, and attributable to the same stable identity/source context?
3. Does the query preserve one output row per intended sequence rather than multiply events?
4. Are event order, late arrival, duplicates, clock skew, and window boundaries defined?
5. Is a success actually authentication success, not a parser label or unrelated session?
6. What benign mechanisms—user error, password rotation, SSO retries, scanners—look similar?
7. Is the pattern repeatable on held-out data?
8. Which rule surface supports the required sequence/aggregation?

## Conceptual signal contract

```text
For each normalized identity and relevant source/application:
  count qualifying failures in a measured window
  require a qualifying later success tied to the intended context
  emit one signal with failure count, first/last times, success evidence,
  identity/source context, contributing event IDs, and rule revision
```

This is pseudologic. It does not supply field names, functions, or a threshold.

## Baseline and threshold plan

Segment identities by human/service/admin role and source application. Measure distributions across business cycles, password-expiry periods, maintenance, and known attack simulations. Hold out a later validation window. Choose a threshold that meets both sensitivity and analyst capacity; document inclusivity at the boundary.

## Required fixtures

- confirmed attack simulation with failures then success;
- failures without success;
- success preceding failures;
- common user-typo sequence;
- password rotation and service-account retry;
- duplicate and delayed events;
- same username in different domains/tenants;
- event exactly at the window boundary;
- missing source or success field;
- high-cardinality spray across many users.

## Decision

`NOT READY`. The smallest next step is to attach the exact hunt query/hash, schema/types, sample positive and benign records, source coverage, and distributions. Then verify scheduled-correlation compatibility in the current product editor.

Real-time correlation is not automatically preferred: current XSIAM real-time rules have a narrow XQL subset and mandatory `filter`, so the required sequence/aggregation may be incompatible. Do not redesign away the security semantics merely to fit the surface.

## FP/FN and lifecycle

Potential FPs: user mistakes, credential synchronization, health checks, stale services. Potential FNs: distributed spray, alternate identity formats, missing successes, adversary timing outside window. Monitoring must include distinct users/sources, Issues, analyst dispositions, source health, null rates, errors, and Case fragmentation.

No response automation is authorized. Any account disablement requires separate verification, approval, identity scope, recovery, and post-action evidence.

## Official references

- Local rule-lifecycle guidance: [detection lifecycle](../../references/detection-lifecycle.md) and [validation and governance](../../references/validation-monitoring-and-governance.md).
- [What are detection rules?](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/threat-management/detection-rules/what-are-detection-rules.md)
- [Create a correlation rule](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/threat-management/detection-rules/what-are-detection-rules/whats-a-correlation-rule/create-a-correlation-rule.md)
