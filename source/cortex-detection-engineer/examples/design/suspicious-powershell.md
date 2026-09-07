# Suspicious PowerShell detection design

## Objective and decision

Design a candidate detection for encoded or otherwise obfuscated PowerShell activity with suspicious process relationships. Do not deploy it or attach containment.

## Applicable product and surface

- Product: Cortex XSIAM 3.x or Cortex XDR 5.x, exact tenant/version unknown
- Candidate surface: compare BIOC with scheduled correlation after schema discovery
- Evidence: `CONCEPTUAL / TENANT-UNVERIFIED`
- `S: NOT RUN` — no independent evaluation of this example revision.
- `D: PASS` — cited product boundaries were documented at the stated source snapshot; this does not verify the illustrative signal.
- `C: NOT RUN` — no exact tenant schema or rule-editor acceptance.
- `E: NOT RUN` — no tenant execution or observed detection outcome.

Current official BIOC documentation establishes a constrained behavior-rule surface, but no tenant schema or rule editor was available. Exact field names and query syntax are intentionally not guessed.

## Threat behavior and model

Observable behavior:

1. a process-start event represents PowerShell or a supported equivalent interpreter;
2. arguments show an encoded/obfuscated execution characteristic;
3. parent/causality context or execution location makes the behavior less consistent with an approved administration workflow;
4. the event occurs on an in-scope endpoint and is not a known controlled test.

Threat hypothesis: an adversary may use PowerShell to execute encoded content after initial access. Benign alternatives include software deployment, administrative automation, security tooling, and controlled red-team activity.

ATT&CK mapping is an interpretation to be selected from the current ATT&CK version after confirming the behavior. It does not establish compromise.

## Telemetry contract

| Need | Required evidence |
|---|---|
| Process start | Exact event category plus start subtype; category alone is insufficient |
| Interpreter identity | Tenant field/type and path/name normalization |
| Command arguments | Tenant field presence, truncation, privacy, and null rate |
| Parent/causality | Supported fields, lineage completeness, and entity keys |
| Endpoint/user | Stable identifiers, scope, and normalization |
| Time | Source/insert times, timezone, latency, and retention |
| Access | Query/rule identity and SBAC/RBAC scope |

Known gap: no schema or representative records were supplied. Therefore no concrete XQL field is shown.

## Conceptual logic

```text
SOURCE <VERIFIED_PROCESS_TELEMETRY>
WHERE event category is Process
  AND event subtype is verified Process Start
  AND normalized interpreter identifies PowerShell
  AND command arguments satisfy a reviewed obfuscation predicate
  AND at least one contextual risk clause is true
RETURN timestamp, stable endpoint, user, process, parent/causality,
       command evidence, source event ID, and rule provenance
```

This is pseudologic, not XQL. Before BIOC conversion, verify the target BIOC dataset, `event_type` predicate, fields/types, stage/function restrictions, case behavior, and historical volume in the current [BIOC source](../../references/official-sources.md#s06--create-a-bioc-rule-in-cortex-xsiam).

## Expected signal

One match is expected to mean: admitted process-start telemetry meets the encoded/obfuscated PowerShell predicate and a contextual risk clause. It does not mean the command is malicious, executed successfully, or caused impact.

Triage fields must let an analyst inspect raw arguments, interpreter path, parent/causality, user, endpoint, time, source event, and rule revision. Sensitive command content should be access-controlled and minimized in reports.

## Baseline and threshold

No numeric threshold is proposed. First measure by endpoint role, user/service-account class, parent process, signer/path, management tool, and change window. A per-event BIOC might fit only if the combined behavior is sufficiently selective; a scheduled correlation may fit if repeat count or related events are essential.

## Validation fixtures

| Fixture | Expected behavior |
|---|---|
| Encoded PowerShell under suspicious parent | Match candidate |
| Approved deployment script using encoded content | Identified as benign lookalike; not blindly allowlisted |
| Plain interactive PowerShell without risk clause | No match |
| Process-category event with non-start subtype | No match |
| Null/truncated command line | Safe non-match or explicit degraded path; no false assertion |
| Renamed interpreter or alternate host | Documented false-negative/evasion test |
| Duplicate/replayed start event | Duplicate handling verified |
| High-volume approved rollout | Capacity/safeguard test and rollback trigger |

## FP/FN and tuning

False positives: administrative automation, deployment tools, security scans, or controlled simulation. Prefer narrow verified context and expiring owner-approved exceptions. Do not allowlist by filename alone.

False negatives: alternate interpreters, remote execution, missing/truncated arguments, subtype/parser gaps, and obfuscation variants. Add compensating coverage or accept explicit residual risk.

## Rule readiness and safety

The candidate is not ready for deployment. Required next step: inspect tenant schema and representative positive/benign events, then compile the exact candidate in the selected non-production rule editor and run historical/shadow validation.

No automatic isolation, process termination, account disablement, or blocking is authorized by this signal.

## Official references

- [Create a BIOC rule — Cortex XSIAM](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/threat-management/detection-rules/what-are-detection-rules/whats-a-bioc/create-a-bioc-rule.md)
- [Create a correlation rule — Cortex XSIAM](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/threat-management/detection-rules/what-are-detection-rules/whats-a-correlation-rule/create-a-correlation-rule.md)
