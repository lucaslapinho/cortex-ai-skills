# Astra completion review

**Date:** 2026-09-06 (America/Sao_Paulo; late-session tool timestamps fall on 2026-09-07 UTC)  
**Version:** `0.1.0`, pre-publication completion  
**Request:** review, improve and finish all seven Skills with Astra, prioritizing the attached master prompt.  
**Boundary:** local source/runtime packages; no global installation, external publication or Cortex deployment.

## Method and coverage

The main agent used `skill-creator` for authoring, standalone packaging and evaluator/scorer separation, and official host guidance for compatibility. The attached master prompt remains the acceptance specification; embedded instructions in knowledge artifacts are data, not separate authorization.

Three Astra specialists read every file of their assigned packages before making bounded corrections:

| Reviewer / author of completion deltas | Packages read | Files | Authored cases inspected |
|---|---|---:|---:|
| `astra_xql_detection_hunt` | XQL, Detection, Threat Hunter | 99 | 106 |
| `astra_playbook_tim` | Playbook, TIM | 63 | 65 |
| `astra_platform_security` | Platform, Security | 68 | 82 |
| Total | Seven complete publication packages | 230 | 253 |

Root architecture, research, inventory, source precedence, prior reviews and the master prompt were reconciled separately. The 2026-09-04 full-register and cumulative behavioral evidence is historical evidence; this pass does not relabel those runs as Astra execution or pretend to re-open every registered URL on September 6. Changed claims received targeted current first-party checks, recorded in their local source registers.

## Findings and improvements

| ID | Severity | Finding / correction | Impacted packages |
|---|---|---|---|
| AST-01 | MEDIUM | Absence of evidence is `UNVERIFIED`, not `UNSUPPORTED`; historical content is not automatically `DEPRECATED`. A readable assertion/excerpt is not an inaccessible original. | Threat Hunter |
| AST-02 | MEDIUM | Documented-but-tenant-unverified XQL can be presented with explicit C/E limits; ties in latest-row deduplication must not imply a unique deterministic event without an evidenced tie-breaker. | XQL, Threat Hunter |
| AST-03 | MEDIUM | Turning off detection linkage is a state change requiring scoped authorization and recovery, not an automatic troubleshooting shortcut. | Detection |
| AST-04 | MEDIUM | Complete every explicit validation-output contract with canonical S/D/C/E results and rationale; include `N/A`; remove contradictory host-selector and validation oracles. | Detection, Playbook, Security; pre-Astra eleven-output corrections in five packages retained |
| AST-05 | MEDIUM | Carry full requiredness/default/retention dimensions into playbook I/O templates; debugger/parallel branches and context scope are not a no-side-effect guarantee. | Playbook |
| AST-06 | MEDIUM | Distinguish EDL selection defaults from consumer authorization; assess query/format overrides, all-field output, sensitive data and downstream readback. Preserve contradictory OpenCTI pagination-path documentation. | TIM |
| AST-07 | MEDIUM | Add XSIAM XDM-versus-Datasets-Rows restriction to raw-visible/XDM-empty diagnosis; do not widen access as an automatic remedy. | Platform, Security |
| AST-08 | LOW | Synchronize release identities and automate oracle-free ZIP construction, overwrite protection, integrity checks and static audit. Clarify direct user authorization versus embedded artifact instructions. | Root architecture, release tool and all ledgers |

These are corrections to publication quality, not claims that a particular tenant is vulnerable, misconfigured or compromised. Independent completion-delta disposition and controlled outputs are recorded below before release.

## Targeted official rechecks

- XQL: current first-party `join`, `dedup` and `regextract` documentation. The `regextract` return-shape conflict remains explicit; examples do not resolve contradictory normative text automatically.
- Detection: current first-party correlation/BIOC behavior checked within its exact product/surface.
- Playbook: current XSIAM context, debugger and Quiet Mode; no promotion of context scope into access control or debugger into universal simulation.
- TIM: TAXII 2 Feed, Generic Export Indicators Service and legacy export/PAN-OS EDL/OpenCTI pages. The integration's listed product support is separate from a paragraph explicitly scoped to XSOAR.
- Platform/Security: current product-specific Engines, system-only `send_events_to_xsiam`, XSIAM user access and relevant routing/component boundaries.
- Host packaging: [OpenAI Build skills](https://learn.chatgpt.com/docs/build-skills), [Claude Code Skills](https://code.claude.com/docs/en/skills) and [Anthropic Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), reopened September 6. The existing static/load/discovery/runtime separation remains applicable; no host runtime certification follows.

Exact product URLs and claim-level scope are retained in each Skill's source register and the [difference register](../research/project-vs-official-differences.md).

## Completion evidence

All 23 final individual-case responses passed independent adjudication, bound to the runtime identities in [Final QA](final-qa.md). No model under test saw the scorer sections. The three domain reports are [XQL/Detection/Hunt](astra-xql-detection-hunt-review.md), [Playbook/TIM](astra-playbook-tim-review.md), and [Platform/Security](astra-platform-security-review.md).

| Package | Fresh individual Astra cases passed | Historical case decisions retained by scoped impact review | Cumulative reviewed S decisions | Authored cases still NOT RUN |
|---|---:|---:|---:|---:|
| XQL | 4 | 37 | 41/41 | 0 |
| Detection | 2 | 6 | 8/39 | 31 |
| Playbook | 2 | 1 | 3/28 | 25 |
| Threat Hunter | 8 | 1 | 9/26 | 17 |
| TIM | 3 | 2 | 5/37 | 32 |
| Platform | 1 | 1 | 2/41 | 39 |
| Security | 3 | 3 | 6/41 | 35 |
| Total | 23 | 51 | 74/253 | 179 |

All 253 tenant C levels and all 253 tenant E levels remain NOT RUN. Cumulative counts are reviewer decisions, not 74 newly reproduced Astra responses. Some historical raw responses were unavailable in the publication evidence tree; the final reviewers retained only their scoped historical records, not a new regrading or model-equivalence claim.

### Evaluation method and retained failures

A first file-load Playbook attempt could not read SKILL.md because the Windows read-only execution policy blocked the read commands. It did not load the Skill and is a setup NOT RUN, not a Skill behavioral pass. The safety policy was not disabled. The supported fallback supplied the exact oracle-free runtime inline to an ephemeral CLI session.

Initial multi-case batches were exploratory. Strict review identified omitted object sharing (PLAT-REG-08), exceptions/suppression/allowlists (SEC-REG-07), common time/entity contracts and a wrong local-source attribution (SEC-TRB-04), shadow/canary promotion (DET-ADR-05), and counting units (CTH-ADV-02). These failures remain in the retained batch records and domain reviews. Core instructions were improved; no unsafe-action prohibition was removed to obtain a pass.

The controlling final battery uses one fresh process per case, requested model gpt-6-astra with high reasoning, full runtime files plus Fixture/Prompt only, and observed zero tool/action events. It uses manual inline loading, not automatic discovery. User config was omitted; this is not a proof that every host-level instruction is absent. The independent harness check found no scorer-section leakage across all 253 extracted inputs. Four oracle discrepancies were corrected to preserve actual source provenance and official conflicts; they did not introduce a correct-answer hint into the fixtures or prompts.

No forward opened current official documentation. Where a response reports D PASS solely for a supplied dated verification record, the reviewer treats it as inherited documentary evidence, not a new D check. Maintainer/reviewer first-party rechecks are recorded separately. Publication rendering rebases local links only and preserves substantive response wording and any historical misattribution; raw response/event archives were retained outside the source tree.

### Tooling and architecture closure

All 14 framework validator runs (seven native and seven explicit UTF-8), seven adapter parses, 253 case-schema checks, 18 checklist items per Skill and seven release/evaluator unit tests passed. Runtime closure: 153 files, 252 relative path links and 508 local links including same-file anchors; no missing or escaping dependency. The final release audit additionally verifies exact runtime/publication identities and all required approval markers.

The independent tool review found a link-rebasing helper that could alter a label equal to its target. The fix replaces only the URL capture span, with a passing regression test; no affected pattern occurred in the final inspected responses. Evaluation now rescans the runtime after execution to catch added files as well as changed bytes. Batch reruns can target a new output directory without overwriting prior evidence.

The frozen authorization clarification affects authoring guidance, not product behavior: explicit scoped user requests can authorize their actions; embedded artifact instructions cannot. Platform/Security independently reviewed it PASS, with existing containment/recovery/impact gates intact. No installed Skill silently inherits a root-file change.

All AST-01 through AST-08 findings and the later strict-forward/tooling findings are CLOSED in the reviewed source scope. Remaining tenant, host discovery, model variance, documentation drift and inaccessible-project-evidence boundaries are documented in [known limitations](known-limitations.md). Seven runtime ZIPs and one source ZIP are produced only after final independent synchronization approval; no global install, commit, push or deployment is performed.
