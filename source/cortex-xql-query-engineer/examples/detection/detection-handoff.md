# Detection Handoff: PowerShell Process Visibility

This example hands a documented interactive query to a detection specialist without representing it as a production rule.

## Handoff summary

| Item | Value |
|---|---|
| Behavior candidate | Process-category telemetry matching selected Windows-style image filenames (`powershell.exe` or `pwsh.exe`) |
| Product | Cortex XSIAM 3.x |
| Validated surface | None; query is documented for interactive Query Center only |
| Canonical classes | Syntax/schema definitions: `VERIFIED`; detection effectiveness: `UNVERIFIED` |
| Qualifiers | `OFFICIAL-CURRENT`, `TENANT-UNVERIFIED` |
| S validation | `NOT RUN` — no independent response evaluation was performed for this example. |
| D validation | `PASS` — the cited current official references support the interactive query and documented rule-surface restrictions for the stated scope. |
| C validation | `NOT RUN` — no target-tenant schema, Query Center compilation, or rule-editor validation was inspected. |
| E validation | `NOT RUN` — no query, rule, Issue generation, or response action was executed or observed. |
| Production status | Not ready; no tenant schema, compilation, execution, baseline, fixtures, volume, grouping, or rule-editor validation |
| Response authority | None |

## Interactive query artifact

**VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED**  
**Product/context: Cortex XSIAM 3.x interactive Query Center, not a rule definition**

- `S: NOT RUN` — no independent response evaluation was performed for this example.
- `D: PASS` — the cited current official references support the interactive query and documented rule-surface restrictions for the stated scope.
- `C: NOT RUN` — no target-tenant schema, Query Center compilation, or rule-editor validation was inspected.
- `E: NOT RUN` — no query, rule, Issue generation, or response action was executed or observed.

```xql
config timeframe = 1d
| dataset = xdr_data
| filter event_type = 1 and action_process_image_name != null
| filter (lowercase(action_process_image_name) contains "powershell.exe" or lowercase(action_process_image_name) contains "pwsh.exe")
| fields _time, agent_hostname, agent_id, actor_effective_username, action_process_username, action_process_image_name, action_process_image_command_line
| sort desc _time
| limit 200
```

The candidate finds rows matching two literal Windows-style image filenames. It can miss other PowerShell hosts, filename forms, or platforms and does not distinguish administrative use from malicious use, establish a threshold, or define how matches become Issues/Cases.

`event_type = 1` selects the Process category, which can include more than process-start events. This candidate is not an execution-only signal. A process-start-only design must verify the current `event_sub_type` value in the target product/editor and test both included and excluded subtypes rather than inserting an unverified enum here.

## Target compatibility and rule-conversion decision

| Target | Decision | Evidence-based reason |
|---|---|---|
| Interactive Query Center | `UNVERIFIED IN TENANT` | Constructs and fields are documented, but compilation/execution, permissions, and population were not observed. |
| BIOC | `UNSUPPORTED` as written | Current BIOC guidance requires an `event_type` filter and permits `filter`, `alter`, and non-aggregate functions; this query additionally uses `fields`, `sort`, and `limit`. |
| Scheduled correlation | `UNVERIFIED` | No target action, schedule, query window, field mapping, volume test, or rule-editor validation exists. Recheck the current schedule, window, count, and hit safeguards in the [compatibility matrix](../../references/xql-language.md#execution-context-compatibility) and deployed rule editor. Interactive validity is insufficient. |
| Real-time correlation | `UNSUPPORTED` as written | Current real-time guidance limits stages to `dataset`, `datamodel`, `filter`, `alter`, `fields`, and `config case_sensitive`, requires `filter`, and allows only Generate issue as the resulting action; this query uses `config timeframe`, `sort`, and `limit`. |
| XQLp | `UNSUPPORTED` in this context | XQLp is a modified parsing-rule language, not an ordinary dataset-query conversion target. |

A detection author could design a separate BIOC or correlation candidate around the behavior, but must not paste this query unchanged or describe a stripped query as validated merely because its stages look allowable.

## Expected signal semantics

- **Input grain:** one visible process event.
- **Interactive output:** up to 200 newest matching visible events with endpoint, user, image, and command-line context.
- **Positive result:** visible telemetry contains one of the selected filename substrings.
- **Does not prove:** malicious intent, encoded payload, credential access, lateral movement, compromise, or attribution.
- **Zero rows:** inconclusive without collection, retention, parser, clock, permission, field-population, and known-fixture evidence.

## False positives

Authorized administration, device management, deployment tooling, login scripts, troubleshooting, build systems, and security operations can generate the same filename match. Candidate tuning should begin with representative benign fixtures and governed context such as signed script origin, parent chain, user/endpoint role, command behavior, and change window using only tenant-verified fields.

Do not hard-code an allowlist from this example. Every exception needs owner, reason, scope, expiry, and regression tests.

## False negatives

The query can miss renamed/copied binaries, alternate interpreters, activity outside retention/timeframe, endpoints without collection, events hidden by RBAC/SBAC, delayed or dropped telemetry, null/truncated fields, and fileless behavior not represented by the selected image-name field. More behavioral logic may improve coverage but requires schema and fixture evidence.

## Optimization and volume plan

1. Validate the interactive query with known benign and controlled positive fixtures.
2. Measure hit volume by relevant entity and time bucket before selecting a rule type or threshold.
3. Preserve the behavior invariant while considering a narrower window or more selective, tenant-verified conditions.
4. Compare candidate and baseline outputs; a smaller result count is not proof of equivalent detection.
5. Inspect null rates and coverage by endpoint/user population.
6. Recheck the compatibility matrix's current BIOC/correlation hit safeguards. Design selectivity and monitoring so automatic disablement is an emergency safeguard, not normal tuning.
7. For BIOC, inspect and regression-test any automatic `PROCESS SHA256` exception after broad endpoint coverage so it does not silently reduce detection.
8. Record rule-editor validation, historical test output, grouping, suppression, time-anchor behavior, action eligibility, rollback/disable criteria, and post-deployment monitoring.

No performance or volume result exists for this example.

## Detection-owner decisions still required

- threat model and behavior definition;
- rule type and product/release eligibility;
- target-specific XQL representation;
- dataset/field/type/population evidence;
- baseline, threshold, grouping, suppression, and severity;
- positive, benign, edge, null, and negative fixtures;
- ATT&CK mapping as an interpretation, not evidence;
- expected analyst context and Case/Issue behavior;
- monitoring, tuning, rollback, retirement, and ownership;
- any response linkage with authorization, least scope, rollback/recovery, and post-action verification.

## Official references

- [BIOC creation and XQL restrictions](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/threat-management/detection-rules/what-are-detection-rules/whats-a-bioc/create-a-bioc-rule.md)
- [Correlation-rule creation and XQL restrictions](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/threat-management/detection-rules/what-are-detection-rules/whats-a-correlation-rule/create-a-correlation-rule.md)
- [`xdr_data` schema reference](https://cortex-docs.paloaltonetworks.com/xql-schema-reference/xdr-data-fields.md)
- [`lowercase()`](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/functions/lowercase.md)
- [`fields`](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/stages/fields.md)
- [`sort`](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/stages/sort.md)
- [`limit`](https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/stages/limit.md)

Use [the detection handoff template](../../templates/detection-query.md) for a new candidate and [the tenant validation record](../../templates/tenant-validation.md) for every actual test.
