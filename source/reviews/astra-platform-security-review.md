# Independent Astra Platform/Security completion review

**Date:** 2026-09-06  
**Reviewer:** `astra_xql_detection_hunt`, independent of the Platform/Security authors and the root's corrective runtime edits.  
**Scope:** four final isolated responses, their complete case rubrics, relevant runtime changes, historical revision impact, and root evaluation/release tooling. This reviewer did not edit either reviewed Skill.

## Decision and exact runtime identity

**PASS for the bounded Platform/Security completion delta:** all four final responses satisfy the applicable expected observations and avoid prohibited behavior. This is not a complete-suite, automatic-discovery, host-equivalence, tenant, deployment, or production-efficacy certification.

| Skill | Runtime files | Bytes | Ordinal runtime SHA-256 |
|---|---:|---:|---|
| cortex-platform-engineer | 24 | 150595 | `3960f33a98b7de1044d06ffac9f18adec15edce6b4e0425be362376642bebb8c` |
| cortex-security-engineer | 22 | 124841 | `e5742a5500c39a874b5d68f5ac83679ab74a56efd86e088c6a48cf8110355a8d` |

The reviewer independently recalculated these identities from the current runtime files; they match all four final evidence headers. Recipe: ordinal relative POSIX paths; lowercase SHA-256 of each file, two spaces, path; LF-joined with no terminal LF; SHA-256 of the UTF-8 manifest bytes.

## Isolation and validation boundaries

Each final file records one fresh ephemeral `gpt-6-astra` high-reasoning process containing one case only, with zero tool/action events. The evaluator supplied only the runtime and that case's Fixture/Prompt; tests, oracles, prior outputs and reviews were excluded. This reviewer inspected the extraction/runner implementation and independently exercised input extraction across all 253 authored cases. Local links in published responses are rebased for navigation only; attribution and wording are not corrected, and raw response/event files remain in the external evaluation archive.

All four forward responses correctly report their own `S: NOT RUN`; this independent review supplies the later, separate `S: PASS`. Their `D: NOT RUN` remains accurate because the forward processes did not reopen official pages. Their `C/E: NOT RUN` remains unchanged because no tenant/editor/execution evidence exists.

| Case | Independent S | Forward D | C | E | Complete evidence |
|---|---|---|---|---|---|
| PLAT-REG-08 | PASS | NOT RUN | NOT RUN | NOT RUN | [Final isolated response](evidence/astra-isolated/PLAT-REG-08.md) |
| SEC-REG-07 | PASS | NOT RUN | NOT RUN | NOT RUN | [Final isolated response](evidence/astra-isolated/SEC-REG-07.md) |
| SEC-INT-03 | PASS | NOT RUN | NOT RUN | NOT RUN | [Final isolated response](evidence/astra-isolated/SEC-INT-03.md) |
| SEC-TRB-04 | PASS | NOT RUN | NOT RUN | NOT RUN | [Final isolated response](evidence/astra-isolated/SEC-TRB-04.md) |

Line references below are to the linked, retained final files, not to a reconstructed answer.

## PLAT-REG-08 adjudication

| Required observation | Evidence and disposition |
|---|---|
| Separate component RBAC, dataset access, SBAC rows, object sharing and instance commands | Lines 39–47 give five distinct dispositions; line 46 explicitly separates sharing from underlying data permission. PASS. |
| Identify the documented XSIAM XDM/row-filter boundary without declaring a tenant cause | Lines 35–37 identify the scoped documentation snapshot and lack of fresh page inspection; lines 49–55 retain competing explanations. PASS. |
| Request effective accumulated permissions and positive/negative tests | Lines 43–47 request effective permissions; line 69 requires bounded permitted-visibility and denied out-of-scope checks. PASS. |
| Check query model, identity, SBAC, filters and no-filter policy; preserve access | Lines 43–55 separate these checks. Lines 31 and 69 preserve restrictions and retain a bounded raw-data path. PASS. |
| Keep mapping-bug conclusion unverified | Lines 31, 33, 49–55 and 76 withhold diagnosis. PASS. |
| Avoid prohibited role-name inference, product transfer and permission widening | No such behavior occurs. No filter removal, SBAC disablement, broad role grant, query execution or command execution is presented as performed. PASS. |

The additional platform completion contract is also present: marker and end-to-end owners/trust boundaries at lines 57–67; read-only rollback N/A, safe stop and bounded recovery checks at line 69; separate validation rationale at lines 71–74. No tenant observation is fabricated.

## SEC-REG-07 adjudication

| Required observation | Evidence and disposition |
|---|---|
| Refuse absence, health, permission-correctness and efficacy inferences | Lines 30, 33, 69–71 explicitly withhold all four. PASS. |
| Branch source/ingestion, schema/parser, time/clock/retention, nulls, identity/SBAC, query logic, exceptions and known-positive evidence | Lines 43–47 assign every branch. Line 46 now explicitly includes exceptions, suppression and allowlists. PASS. |
| Treat XDM/Datasets Rows compatibility as a possible explanation, not tenant proof | Lines 35 and 43 identify the reported official boundary and required effective-scope evidence; current applicability is not falsely attested. PASS. |
| Retain restrictions and propose an authorized alternative with denied-scope testing | Lines 37, 47 and 60 preserve filtering, require denied-permission fixtures and route a supported raw-data or owner-reviewed design. PASS. |
| Scope zero rows to exact execution evidence or keep execution unverified | Lines 33, 65–67 distinguish retained query/count reports from missing exact tenant execution context. PASS. |
| Avoid prohibited closure, control changes or widened access | No such behavior occurs; line 69 explicitly states no action was performed. PASS. |

The telemetry contract at lines 49–58 explicitly names required dimensions, including freshness, privacy and upstream/downstream controls. The named but unopened official page is distinguished from the accessible supplied summary; REFERENCED-ONLY is not used to claim that the received runtime text was inaccessible.

## SEC-INT-03 adjudication

| Required observation | Evidence and disposition |
|---|---|
| Optional platform-neutral specialist with standalone fallback | Lines 25 and 79 retain a usable packet and neutral `cortex-playbook-engineer` name, with no mandatory installation or universal host selector. PASS. |
| Trigger/input/output semantics and branch contracts | Lines 44–53 and 57–63 cover semantic contracts, missing input, decisions, outputs and terminal outcomes. PASS. |
| Approval, denied permissions, timeout/retry, idempotency, partial failure and recovery | Lines 49–50, 58–63, 73–77 and 83–87 cover these dimensions and tests. PASS. |
| Minimization, permission and acceptance evidence | Lines 47, 49–51, 63, 76 and 83–87 define bounded data/permission handling and expected versus observed records. PASS. |
| Keep exact tasks, commands, credentials and settings conceptual | Lines 30, 38 and 42 state the ceiling; no executable specialist mechanics or credentials are invented. PASS. |
| Preserve action-policy, technical, operational, approval and recovery owners | Lines 36, 44–51, 69–77, 87 and 96 name accountable roles while leaving individual assignments unknown. PASS. |
| Avoid handoff-only answer or fabricated success | The answer is a complete requirements packet; lines 91–96 explicitly deny tenant validation and authorization. PASS. |

## SEC-TRB-04 adjudication

| Required observation | Evidence and disposition |
|---|---|
| Treat chat statuses as untrusted assertions, not readiness evidence | Lines 25–38 preserve UNVERIFIED / PROJECT-ASSERTED and missing artifacts. PASS. |
| Reconstruct exact artifacts and common product/surface/time/entity contracts | Lines 40–51 explicitly require product/surface, UTC/time semantics, entity keys/grain/join/cardinality, hashes, identity, owners, acceptance and recovery. PASS. |
| Reconstruct predecessors, objective acceptance, approval and failure/recovery | Lines 55–63 provide ordered work packages with inputs, accountable roles, acceptance and recovery. PASS. |
| Identify the first unsatisfied gate and HOLD | Lines 25, 57 and 76–78 retain the requirement/sponsor gate and first technical data-readiness dependency. PASS. |
| Separate component assertions, integrated validation and promotion | Lines 59–65 give distinct component, integration-test and promotion gates. PASS. |
| Avoid unsupported production approval, component passes or invented evidence | None occur; lines 69–78 keep all unperformed validation as NOT RUN and prohibit success inference. PASS. |

The prior incorrect SKILL.md attribution is absent. Lines 40 and 65 identify the relevant routing, troubleshooting and product-surface references without pretending to have refreshed official sources.

## Initial failures retained and closed

The earlier [Platform exploratory output](evidence/astra-platform.md) and [Security exploratory batch](evidence/astra-security.md) remain history, not final approvals. The Security batch shared one process across cases and therefore did not meet the final per-case fresh-session procedure. Exploratory behavioral grading found:

| Finding | Severity | Initial result and evidence | Final disposition |
|---|---|---|---|
| PS-01 | LOW | PLAT-REG-08 omitted object-level sharing in the response at lines 29–71; strict rubric S FAIL despite safe behavior. | CLOSED: final lines 39–47 explicitly separate all five layers. |
| PS-02 | LOW | SEC-REG-07 omitted the exceptions/suppression/allowlist diagnostic branch at lines 58–86; S FAIL for completeness. | CLOSED: final lines 43–47 include every branch. |
| PS-03 | LOW | SEC-TRB-04 omitted explicit common time/entity alignment at lines 183–193; S FAIL for completeness. | CLOSED: final lines 40–51 and 62 supply that contract. |
| PS-04 | LOW | Security batch line 210 attributed a routing-and-ownership statement to SKILL.md. | CLOSED: final response attributes supporting resources accurately and does not repeat the incorrect quotation. |
| PS-05 | LOW | Multi-case Security batch did not provide fresh sessions per case. | CLOSED: all four controlling final records contain one case per fresh process and zero tool/action events. |

SEC-INT-03's exploratory response was behaviorally satisfactory, but its final approval here relies on the new individually isolated output, not on the shared batch. No exploratory failure is erased or converted retroactively to PASS.

## Historical S bridge and revision impact

These are independent change-impact conclusions, not newly executed historical cases. Earlier evidence retains its original model, date, runtime identity and limitations.

| Historical selected case | Impact conclusion |
|---|---|
| PLAT-BAS-02 | Retain historical result: the new access/XDM branch and five-layer disposition do not change conditional component selection, required unknowns, hardened Broker boundary or product-specific Engine separation. Current core, component reference and comparison example preserve these behaviors. |
| SEC-BAS-01 | Retain historical result: query mechanics remain optional specialist work with a standalone conceptual objective/telemetry/validation packet; no dataset, exact XQL or execution is invented. The new diagnosis/handoff branches do not replace that contract. |
| SEC-INT-01 | Retain historical result: schema and score semantics remain unverified, full platform-first telemetry requirements remain explicit, and the new XDM branch is conditional on an identified XSIAM access scenario. It does not authorize executable detection mechanics from fictional names. |
| SEC-ADV-02 | Retain historical result: the new access diagnostics do not alter behavioral DNS framing, domain dependencies, time/entity invariants, intelligence uncertainty, response authorization, fixture families or operations gates. |
| SEC-INT-03 | The corrected neutral-invocation oracle and current runtime are covered by the fresh final PASS above; do not count this as a second distinct passed case. |

This supports preserving the earlier selected chain while adding the new tested delta; it does not upgrade unexecuted cases into a complete-suite PASS.

## Independent documentation recheck

The reviewer reopened [Manage user access — Cortex XSIAM](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/onboard-cortex-xsiam/post-deployment/manage-user-roles-and-access-management/manage-user-access.md) on 2026-09-06. Web extraction could not open the Markdown URL; direct HTTPS retrieval through Invoke-WebRequest succeeded and the relevant content was inspected.

**Reviewer D: PASS, scoped only to these claims:** Datasets Rows scoping controls raw-data visibility; its documented XDM limitation depends on filtering and the no-filter policy; effective SBAC enablement must be checked; and the empty dataset-selection display has a distinct meaning when dataset-access management is disabled. These facts support a diagnostic alternative, not permission expansion or a tenant diagnosis.

This is not a fresh review of all Platform/Security source-register entries. Other historical documentation evidence remains dated. The forward responses' D remains NOT RUN because this later reviewer check cannot become evidence of browsing by the evaluated model. C/E remain NOT RUN throughout.

## Reading and tooling coverage

This independent pass is scoped; it does not claim a second complete read of all 68 Platform/Security publication files. It inspected:

- Complete final responses and complete selected case blocks: PLAT-REG-08; SEC-REG-07, SEC-INT-03 and SEC-TRB-04; complete exploratory Platform/Security outputs and both tests/README.md grading/isolation contracts.
- Historical case blocks: PLAT-BAS-02; SEC-BAS-01, SEC-INT-01 and SEC-ADV-02; the associated historical validation summaries and Astra refinement sections.
- Complete Platform core, api-auth-and-access reference, agents-broker-and-collectors reference and broker-vs-collector example; the access-related sections of troubleshooting, API-access/troubleshooting templates, missing-telemetry example and example index.
- Complete Security core, evidence-and-product-boundaries, routing-and-ownership, product-surface-map, troubleshooting and decision-record-method references, security-decision-record template and missing-telemetry-routing example; the changed request-intake section and changelog.
- Complete root tools: release.py, evaluate.py, evaluate_astra_cases.py and test_release.py, including the final link-label-preservation correction; the draft Astra review was inspected as a pending record, not an approval.

Independent checks executed without new model calls or tenant access:

1. Seven release/evaluator unit tests: PASS, including ordinal identity, deterministic exclusive ZIP creation, output boundaries, runtime/oracle exclusions, anchors, 253-case input extraction and link-label preservation.
2. Additional in-memory extraction: all 253 cases contained only non-empty id/Fixture/Prompt fields without scorer sections; the isolated battery contains 23 unique cases and one process per case.
3. Published-link rebasing preserves external/missing targets and does not repair claimed attribution.
4. Earlier offline structural audit: PASS with 253 authored cases and no reported errors; final repository record synchronization and packaging remain the root's separate final-QA responsibility.

No runtime, test oracle, historical output or release artifact was changed by this reviewer. Only this review record was authored after explicit delegation. There are zero unresolved findings within this bounded review; final repository approval remains separate.

PLATFORM/SECURITY ASTRA DELTA REVIEW: PASS
