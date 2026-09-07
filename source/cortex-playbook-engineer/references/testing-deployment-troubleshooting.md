# Testing, Deployment, and Troubleshooting

**Documentation review cut:** 2026-09-04  
**Artifact class:** `CONFIGURATION GUIDANCE`; no import or execution was performed for this Skill release.  
**Current level:** authored/static package work only; target validation levels `C` and `E` are `NOT RUN`.
**Primary official evidence:** [source register](official-sources.md), PB02, PB10-PB11, PB16-PB17, XS07-XS08, and CT02-CT06.

## Contents

- [Test strategy](#test-strategy)
- [Static and behavioral tests](#static-and-behavioral-tests)
- [XSIAM debugger safety](#xsiam-debugger-safety)
- [Import and content validation](#import-and-content-validation)
- [Functional test matrix](#functional-test-matrix)
- [Deployment stages](#deployment-stages)
- [Troubleshooting workflow](#troubleshooting-workflow)
- [Symptom matrix](#symptom-matrix)
- [Performance and observability](#performance-and-observability)
- [Evidence record](#evidence-record)

## Test strategy

Keep four levels independent:

| Level | Example | Passing claim |
|---|---|---|
| `S` | Independent oracle-isolated response evaluation | The retained response meets the stated case rubric; an author-side structure/link check does not establish this result |
| `D` | Current official source confirms a task/setting behavior | Product documentation supports the bounded claim |
| `C` | Exact export accepted by named validator or controlled import | Artifact/schema accepted in that target only |
| `E` | Bounded workflow executed and state read back | Observed behavior under recorded fixture/identity only |

Use `PASS`, `FAIL`, `NOT RUN`, or `N/A` with rationale. Never infer `C` or `E` from a Markdown design.

## Static and behavioral tests

Before any target import:

- inventory every task, edge, input, output, context path, script, command, argument, sub-playbook, pack, integration, credential, role, and external target;
- validate source/product/release applicability;
- check unreachable tasks, missing error branches, cycles/loops, concurrency, shared-key writes, and closure paths;
- scan for secrets, literal customer values, unsafe defaults, fabricated observables, task IDs, commands, and context paths;
- review action/approval/recovery controls;
- exercise decision tables with valid, benign, unknown, error, and conflicting evidence;
- run hallucination-resistance prompts and importability-attestation tests; and
- isolate the Skill/runtime under test from its scorer/oracles.

Record author-side structure/link/design checks separately. Only retained oracle-isolated responses with independent adjudication establish `S`; applicable current official-source verification establishes `D`. Neither establishes import evidence, and the model under evaluation must not self-award `S`.

## XSIAM debugger safety

Current official XSIAM documentation says the debugger can use an empty mock Issue or an existing Issue, inspect context/indicators/task data, set breakpoints, skip tasks, and temporarily override inputs/outputs.

Important boundaries:

- The debugger runs under the logged-in user's permissions.
- Tasks still execute normally. Platform or external writes can be real.
- Selecting an existing Issue does not alter that original Issue/context, but executed tasks can still change other state.
- Breakpoints pause before a task; already-running parallel tasks can continue.
- Manual tasks pause unless skipped.
- Overrides/skips are session-scoped and do not permanently change the playbook.
- Current documentation notes unsupported debugger behavior for a parent-Case field surface; recheck it for the target release.

Safe plan:

1. use a dedicated development tenant/test identity where available;
2. choose synthetic non-sensitive fixtures;
3. skip every destructive, mutating, or external-notification task;
4. override the required output with a typed synthetic result;
5. verify that the skipped branch cannot be reached in parallel;
6. run negative permissions and error paths;
7. retain sanitized screenshots/logs/context snapshots and artifact hash; and
8. conduct a separately authorized reversible action test only when required.

Do not call a debugger run a dry run unless all side effects were demonstrably stubbed.

## Import and content validation

To claim `VERIFIED IMPORTABLE ARTIFACT`, retain:

- target export/import schema and product/release;
- exact artifact hash;
- pack layout and dependency graph;
- script/integration/sub-playbook versions;
- validator/SDK version, supported OS/runtime, command, and output;
- controlled import and object readback;
- target tenant/deployment alias and effective role;
- functional fixtures and results; and
- independent review.

Official `demisto-sdk` tooling and developer documentation can support content formatting/validation, but tool flags and schemas evolve. Pin the installed SDK version. Official research says supported workflows include Linux, macOS, and WSL2 rather than native Windows; verify current prerequisites before running it.

An official `demisto/content` playbook is an example at a pinned revision, not evidence that the target tenant has the same pack or that custom dependencies are satisfied.

## Functional test matrix

At minimum test:

| Area | Required fixtures |
|---|---|
| Trigger | Matching, nonmatching, duplicate, replayed, stale, disabled, competing rule |
| Input | Valid, missing, null, wrong type, malformed, oversized, hostile content |
| Enrichment | Success, legitimate empty, not found, auth denial, rate limit, timeout, malformed output |
| Decision | True, false, unknown, conflicting, insufficient evidence, parser/model failure |
| Sub-playbook | Valid I/O, missing output, separate/shared context, version mismatch, unavailable dependency |
| Loop | Empty, one, many, duplicate, unequal list lengths, exit, maximum, timeout, partial failure |
| Error | Stop, continue-degraded, error branch, nested error, lost diagnostic |
| Retry | Transient success, exhausted budget, permanent failure, timeout-after-write reconciliation |
| Approval | Approve, reject, request evidence, expire/no response, unauthorized approver, late/duplicate reply |
| Action | Already in state, success/readback, denied, partial batch, unknown status, rollback success/failure |
| Notification | Success, duplicate suppression, wrong recipient rejected, delivery failure/escalation |
| Evidence | Quiet/non-quiet behavior, redaction, identity, timestamps, action/readback, retention |
| Closure | Complete, degraded, unresolved, notification pending, rollback pending, unsupported close reason |

## Deployment stages

```text
Design review
-> source/dependency/permission inventory
-> static validation
-> controlled import in exact target
-> debugger with protected tasks skipped or stubbed
-> isolated reversible integration tests
-> representative Issue/incident trigger test
-> shadow/observation-only rollout when applicable
-> limited authorized rollout
-> monitored production change
-> rollback or wider promotion decision
```

For each promotion, define owner, evidence, entry/exit criteria, target count, monitoring window, stop condition, rollback/recovery, and approval. “Shadow mode” is a project design pattern unless the chosen product feature is officially documented and tested; do not imply a universal switch.

## Troubleshooting workflow

1. Preserve the artifact version/hash, run/task ID, sanitized error, timestamp/timezone, product/release, and identity.
2. Identify whether the symptom is trigger, graph, context, content, permission, engine/worker/network, command, external service, evidence display, or side-effect state.
3. Compare expected versus observed state without editing the production artifact.
4. Reproduce with the smallest safe fixture and protected tasks skipped/stubbed.
5. Change one variable, retain output, and classify the result.
6. Reconcile external state before any retry.
7. Update contract, test, reference, and changelog if the correction changes behavior.

## Symptom matrix

| Symptom | Discriminating checks | Unsafe shortcut |
|---|---|---|
| Playbook did not start | Enablement, exact trigger rule/order, object type, matching fields, permissions, ingestion time | Recreate the playbook blindly |
| Task unavailable | Installed pack/version, detached/system state, dependency, content permission | Guess a replacement task ID |
| Command unavailable | Enabled instance, installed integration version, command help, permitted roles | Invent command/argument |
| Missing output | Producer status/error, output schema, ignored/extended output, filter/transform, context scope, Quiet Mode view | Substitute a similar context path |
| Wrong branch | Input type/cardinality, empty/unknown state, stale/shared context, transform, parallel write | Coerce unknown to false/benign |
| Loop runs once | Array passed whole versus configured sub-playbook loop, target release behavior | Duplicate tasks manually |
| Loop does not stop | Exit source, type/operator, max/interval/deadline, stale/shared context | Increase maximum without cause |
| Duplicate ticket/action | Trigger replay, stable key, prior-state read, concurrent runs, timeout reconciliation | Add unbounded retries |
| Task is stuck/pending | Manual/Ask completion identity, command permission, engine/instance, timeout, external wait | Have an administrator bypass approval silently |
| Error hidden | Error handling selection, error path, Quiet Mode/War Room, original task ID | Treat no visible output as success |
| Debugger succeeded but production fails | Test identity/data, skipped tasks, overrides, unavailable parent field, content/instance differences | Mark tenant execution verified |
| Action status success but state unchanged | Exact target, async behavior, readback source/freshness, partial result, permission | Close without verification |
| Performance degradation | Run/task metrics, loop/cardinality, extraction, context size, API calls, timeout/retry storm | Claim one static edit measured improvement |

## Performance and observability

Current XSIAM best-practices documentation identifies performance-oriented techniques including task decomposition, deliberate Quiet Mode, necessary-only indicator extraction, retries/polling, minimizing calls/resources, and XQL datasets for playbook/script metrics. Dataset presence and fields remain tenant-dependent.

Measure rather than assume:

- run count and concurrency;
- per-task duration and queue time;
- retry and timeout rate;
- input/output/context size;
- loop item/iteration counts;
- command/API count and rate-limit responses;
- error/degraded/partial rates;
- approval dwell time;
- notification delay/failure;
- action/readback latency; and
- end-to-end SLA.

A design improvement is not a measured performance gain without retained before/after evidence from the named environment.

## Evidence record

```text
Artifact classification:
Product / deployment / version:
Tenant alias and environment:
Artifact path/hash/version:
Installed dependencies and versions:
Validator/SDK and result:
Import identity, timestamp, result, and readback:
Test fixture and protected-task controls:
Execution identity and permissions:
Run/task IDs and timestamps:
Expected behavior:
Observed behavior:
External side effects and readback:
Errors/retries/timeouts/partial state:
Recovery/rollback:
Sanitized evidence locations and hashes:
S result: <PASS | FAIL | NOT RUN | N/A> — <independent response-evaluation rationale and retained record>
D result: <PASS | FAIL | NOT RUN | N/A> — <dated official-document rationale and sources, or reason not applicable/run>
C result: <PASS | FAIL | NOT RUN | N/A> — <named validation/import/debug rationale and retained record, or reason not run>
E result: <PASS | FAIL | NOT RUN | N/A> — <observed execution/side-effect rationale and retained record, or reason not run>
Limitations and reviewer:
```

Do not include secrets, private hosts, customer identifiers, or raw sensitive content in this record.
