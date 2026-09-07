# Cross-Skill review

**Repository version:** `0.1.0`  
**Evidence snapshot:** 2026-09-06 completion; 2026-09-04 historical baseline  
**Scope:** the seven standalone publication packages and their oracle-free runtime manifests  
**Reviewer boundary:** independent cross-role review; no Skill author self-approved a lane

## Verdict

`PASS` for repository publication within the stated evidence boundary. The required cross-role map is complete, all historical findings are closed, and the final ledger has zero unresolved `BLOCKER`, `CRITICAL`, `HIGH`, `MEDIUM`, or `LOW` findings. No Cortex tenant was available, so `C` and `E` remain `NOT RUN` throughout.

## Reviewed runtime identities

Hashes use ordinal relative-path ordering over records in the form `<lowercase file SHA-256><two spaces><relative POSIX path>`, joined by LF with no terminal LF.

| Skill | Runtime files / bytes | Ordinal SHA-256 |
|---|---:|---|
| `cortex-xql-query-engineer` | 22 / 202,475 | `d51eac19cdadd0852a4d2d7bf63dd894389aa621e972e1c09f39194f038af7f7` |
| `cortex-detection-engineer` | 22 / 123,904 | `b2c8a42b879b12df22b4efccc413d32d771cdbd119713021e7bdfc966349cb81` |
| `cortex-playbook-engineer` | 20 / 151,241 | `ee2624e64bbb650b98a9a7e7594bc8c3896d6f49bbc12fcf19801578f119ed4a` |
| `cortex-threat-hunter` | 22 / 73,435 | `af98de5883f06eea19adf89b9c6ce6cf1676830441f11f774d74a1b286f8f092` |
| `cortex-tim-engineer` | 21 / 126,788 | `e2e49820268e45ee8017ce67d397cb73d9d08cdfd80fc7dc9b16e1f58b2de0fb` |
| `cortex-platform-engineer` | 24 / 150,595 | `3960f33a98b7de1044d06ffac9f18adec15edce6b4e0425be362376642bebb8c` |
| `cortex-security-engineer` | 22 / 124,841 | `e5742a5500c39a874b5d68f5ac83679ab74a56efd86e088c6a48cf8110355a8d` |

## Historical required role map — 2026-09-04

| Skill -> independent reviewer role | Selected case or evidence | `S` | `D` | `C` | `E` | Verdict |
|---|---|---|---|---|---|---|
| XQL -> Detection Specialist + Technical Accuracy | `XQL-BAS-01`, `XQL-INT-01`, `XQL-ADV-01`, plus the current Golden chain | `PASS` - 3/3 current taxonomy-delta cases and 41/41 cumulative | `PASS` - 38 applicable; `N/A` - 3 | `NOT RUN` - 41/41; no tenant compiler | `NOT RUN` - 41/41; no tenant execution | `PASS` |
| Detection -> Threat Hunting Specialist + Technical Accuracy | `DET-INT-03` plus the technical subset | `PASS` - promotion is gated by corpus, baseline, telemetry and benign alternatives | `PASS` - 23/23-source register; 4/4 selected BIOC/correlation pages rechecked | `NOT RUN` - no tenant editor/compiler | `NOT RUN` - no rule execution or result | `PASS` |
| Playbook -> Platform Specialist + Technical Accuracy | `PB-TRB-02` plus `PB-BAS-03` | `PASS` - command states and parent/child contracts remain distinct | `PASS` - 35/35-source register; 2/2 selected permission/dependency pages rechecked | `NOT RUN` - no SDK/import target | `NOT RUN` - no playbook or action executed | `PASS` |
| Threat Hunter -> XQL Specialist | `CTH-ADV-03` | `PASS` - semantic tokens are used without fabricated XQL or schema | `N/A` - deliberately product-neutral conceptual response | `NOT RUN` - no tenant compiler | `NOT RUN` - no hunt executed | `PASS` |
| Threat Hunter -> Detection Specialist | `CTH-ADV-03` | `PASS` - complete detection handoff without a recall guarantee | `N/A` - no concrete surface claim in the selected response | `NOT RUN` | `NOT RUN` | `PASS` |
| TIM -> Platform Specialist + Technical Accuracy | Rerun `TIM-T03` plus the technical subset | `PASS` - the oracle-isolated response on the exact final runtime separates hosting, engine, network/TLS/auth, product-scoped selection/content, consumer retrieval and enforcement; it explicitly keeps collection/query wording XSOAR-scoped and XSIAM selection semantics `UNVERIFIED` | `PASS` - 32/32-source register; corrected X02/X16 and I02-I04/I10 scopes plus 6/6 selected Platform pages rechecked | `NOT RUN` - no integration/configuration target | `NOT RUN` - no fetch, distribution or enforcement | `PASS` |
| Platform -> Architecture Researcher + Technical Accuracy | `PLAT-BAS-02` plus the technical subset | `PASS` - agent, Broker VM, XDR Collector and Cortex Engine stay distinct | `PASS` - 45/45 current sources; 2/2 historical pointers correctly bounded; 47/47 URLs reachable | `NOT RUN` - no parser/editor/import/API target | `NOT RUN` - no event traversed a live path | `PASS` |
| Security -> Skill Architecture Reviewer | `SEC-BAS-01`, `SEC-INT-01`, `SEC-ADV-02` | `PASS` - 3/3, including explicit revision-impact for `SEC-BAS-01` | `N/A` - selected architecture responses are conceptual | `NOT RUN` | `NOT RUN` | `PASS` |
| Security -> Platform Specialist | `SEC-INT-01` | `PASS` - complete telemetry and data-readiness contract | `N/A` - conceptual cross-domain packet | `NOT RUN` | `NOT RUN` | `PASS` |
| Security -> Threat Hunting Specialist | `SEC-ADV-02` | `PASS` - hypothesis, coverage, benign explanations, duplication, enrichment and action gate are explicit | `N/A` - conceptual cross-domain packet | `NOT RUN` | `NOT RUN` | `PASS` |

The models under evaluation reported their own validation rows as `NOT RUN` when appropriate. The `S: PASS` decisions above are independent adjudications, not model self-attestation. Selected-case coverage outside XQL is not a claim that every authored case was run.

## Domain ownership and handoffs

| Domain | Primary ownership | Permitted cross-domain interface |
|---|---|---|
| XQL | Query mechanics, schema-safe construction, explanation, optimization and troubleshooting | Typed query requirements or non-executable semantic tokens |
| Detection | Rule lifecycle, readiness, validation, tuning and monitoring | Hunt-promotion packet, query requirement and playbook action contract |
| Playbook | Automation graph, data/context contracts, approvals, failures, recovery and readback | Product-bound command requirements and action-gate packet |
| Threat Hunter | Hypotheses, coverage, baselines, pivots, competing explanations and conclusions | XQL request and detection-opportunity handoff |
| TIM | Intelligence collection, normalization, scoring, enrichment, lifecycle and distribution | Consumer and enforcement contracts without assuming downstream state |
| Platform | Collection, ingestion, parsing, mapping, access, integration and end-to-end data path | Telemetry/data-readiness and component capability evidence |
| Security | Cross-domain intake, sequencing, ownership, risk, decision records and standalone fallback | Optional specialist handoffs that never become mandatory runtime dependencies |

Telemetry, schema, evidence and safety appear in multiple Skills as interface contracts. This is controlled duplication, not competing domain ownership. In the September 4 review of 1,625 runtime paragraphs, the only material literal cross-Skill duplication was the canonical qualifier list in four Skills, which is required for interoperability.

The runtime boundary contains 252 relative path links (508 including same-file anchors): zero broken targets, zero package escapes, zero absolute-path dependencies and zero reparse-point dependencies. No runtime file contains a `$cortex-*` selector. Security mentions sibling capabilities only as optional handoffs and supplies a standalone fallback.

## Findings and closure

| ID | Discovery severity | Finding | Correction and independent retest | Final status |
|---|---|---|---|---|
| `CSR-HIGH-001` | `HIGH` | Cortex Engine guidance relied on a retiring XSOAR source and could make the component itself appear deprecated. | Product-scoped current XSIAM, XDR, XSOAR SaaS and XSOAR On-prem sources replaced it; the retiring page remains a historical pointer only; Platform architecture/D review passed. | `CLOSED` |
| `CSR-HIGH-002` | `HIGH` | `OFFICIAL-SYNTAX / NOT-TENANT-EXECUTED` acted as a competing evidence taxonomy. | The ladder was removed from active runtime content; current `XQL-BAS-01`, `XQL-INT-01` and `XQL-ADV-01` passed; the Golden chain remains revision-aware. | `CLOSED` |
| `CSR-MEDIUM-001` | `MEDIUM` | Security standalone packets omitted discriminating request and telemetry fields. | Objective, behavior placeholder, full telemetry/data-readiness contract and validation sequence were added; `SEC-BAS-01`, `SEC-INT-01` and `SEC-ADV-02` passed. | `CLOSED` |
| `CSR-MEDIUM-002` | `MEDIUM` | S/D/C/E enumeration and self-evaluation rules varied between Skills and templates. | The frozen architecture and every runtime core now use only `PASS`, `FAIL`, `NOT RUN` or `N/A` with rationale and prohibit self-awarding `S`. | `CLOSED` |
| `CSR-MEDIUM-003` | `MEDIUM` | Two Platform source entries redirected semantically and two historical entries could be mistaken for current support. | Current P01/D05 targets were recorded and C14/A09 were explicitly bounded as historical; independent D review passed. | `CLOSED` |
| `CSR-MEDIUM-004` | `MEDIUM` | Playbook missing-command troubleshooting omitted entitlement, availability/authorization separation and a complete evidence matrix. | The workflow now collects target evidence, distinguishes unavailable/disabled/incompatible/unauthorized and returns all four validation levels; `PB-TRB-02` passed. | `CLOSED` |
| `CSR-MEDIUM-005` | `MEDIUM` | Security source entries O03/O04 resolved through generic documentation targets, weakening claim-level traceability. | They now point directly to the current official XSOAR SaaS overview and Cortex Cloud Runtime Security landing page; all 27 source records returned HTTP 200 and the two corrected scopes passed semantic recheck. | `CLOSED` |
| `CSR-MEDIUM-006` | `MEDIUM` | The Platform syslog example used noncanonical or unexplained S/D/C/E results. | Its four rows now use the canonical enum with rationale; D cites the current official Broker VM Syslog Collector page, S/C/E remain `NOT RUN`, and `PLAT-BAS-02` was preserved by independent revision-impact review. | `CLOSED` |
| `CSR-MEDIUM-007` | `MEDIUM` | XQL and Playbook templates retained generic, compacted or rationale-free validation-result placeholders. | XQL's five affected templates and Playbook's design/context/tenant summaries now require four explicit canonical results with rationale. Independent revision-impact review preserved the stated S/D evidence and kept every C/E result `NOT RUN`. | `CLOSED` |
| `CSR-MEDIUM-008` | `MEDIUM` | TIM X16 asserted an undocumented `indicator_relationship` dataset/TIM-add-on tie, and TAXII 2 relationship wording could be transposed from XSOAR TIM to XSIAM. | X16 now states only the documented `indicators` dataset; I02 and all affected guidance preserve the source's explicit XSOAR wording and leave XSIAM applicability `UNVERIFIED`. All 32 URLs and the two corrected claims passed independent review; selected S cases were preserved only by scoped revision impact. | `CLOSED` |
| `CSR-MEDIUM-009` | `MEDIUM` | TIM residual source wording attributed common fetch-history behavior to a general XSIAM feed page and could transpose XSOAR-specific OpenCTI and outbound TAXII collection/query semantics to XSIAM. | X02 now requires integration-specific checkpoint/reset evidence; I03/I04 and I10 restrict the documented collection/query/API-object and out-of-box mapping wording to XSOAR while leaving XSIAM semantics `UNVERIFIED`. Independent exact-snapshot semantic review passed 32/32 sources with zero open findings, and oracle-isolated `TIM-T03` reran `PASS` without product transposition. | `CLOSED` |

No historical failure was erased. Closure applies only to the corrected runtime hash and the stated static, controlled-rerun or independent revision-impact evidence. The historical deltas above were checked against the exact current runtime identities; no behavioral reproducibility, tenant or host-runtime claim follows from revision-impact review.

## Consistency conclusions

- The canonical seven statuses, qualifiers and S/D/C/E result enum are consistent across the seven runtime packages.
- The same official URL may be reused for a different bounded claim; 44 reused URL families were inspected and no material classification conflict remained.
- `Case/Issue` is the preferred XSIAM terminology. `Alert/Incident` remains only in generic, quoted legacy or explicitly versioned contexts.
- Agent, Broker VM, XDR Collector and Cortex Engine are never treated as interchangeable.
- A natural phrase such as "not tenant executed" may describe a limitation, but it cannot return as a badge, status ladder or substitute for canonical status, qualifiers and S/D/C/E.

## Limitations

- No Cortex tenant, schema, compiler, import surface, integration instance or product execution was available.
- No configuration change, deployment, result, efficacy or performance observation was made.
- Outside XQL, forward tests were selected risk cases rather than complete-suite execution.
- Controlled runs used the declared reviewer model and tests-free runtime; equivalence across models and hosts is not established.
- These hashes identify an uncommitted local snapshot, not a Git commit.

## Astra completion delta — 2026-09-06

The current identities above supersede the historical runtime snapshots for publication. All 230 Skill files and 253 authored cases received a full Astra inspection. Independent reviewers other than each delta author then reviewed corrections and 23 fresh, one-case-per-process response evaluations. Results and revision-impact limits are retained in [Astra completion review](astra-review.md), [XQL/Detection/Hunt review](astra-xql-detection-hunt-review.md), [Playbook/TIM review](astra-playbook-tim-review.md), and [Platform/Security review](astra-platform-security-review.md).

Historical results are not relabeled as Astra runs. Initial batches exposed completeness and citation failures, which remain retained; the final individual outputs are the completion evidence. Four source/oracle discrepancies were reconciled without inferring new support or inventing tenant results. The residual eleven pre-Astra output placeholders and the later S-scope reference inconsistency are closed by explicit output contracts and independent revision-impact review. In particular, the old Threat claim qualifier in ADV-TH-01 is historical: a readable assertion is PROJECT-ASSERTED; only an unavailable original is REFERENCED-ONLY.

Current scoped cumulative S coverage is 74 case decisions: 23 fresh individual Astra passes and 51 retained historical decisions through bounded revision-impact review; 179 cases remain NOT RUN. Current-source rechecks are separately dated and do not turn an offline forward into a live D check. All 253 tenant C/E levels remain NOT RUN. No deployment or host discovery is certified.

CROSS-SKILL REVIEW: PASS
