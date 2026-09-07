# Final QA

**Repository version:** `0.1.0`  
**Evidence snapshot:** 2026-09-06 completion; 2026-09-04 historical baseline  
**Release scope:** seven source-publication packages, verified runtime-only ZIP construction and reproducible release tooling  
**Reviewer boundary:** independent Final QA review after corrections; the primary author assembled this evidence record but did not self-approve the release

## Executive Summary

The seven Cortex Skills are ready for **source publication** within the evidence boundaries recorded here. The research-first sequence, XQL Golden approval, frozen architecture, six remaining implementations, standalone checks, cross-role review, adversarial review, compatibility review, hallucination audit, and final package inspection are complete. All mandatory release findings are closed, and the final unresolved counts are zero at every severity.

This decision does not certify a Cortex tenant, product license, tenant schema, editor/compiler, import, API, integration, query or playbook execution, deployment, efficacy, result, capacity, or performance. It also does not claim behavioral runtime equivalence across ChatGPT, Codex, Claude, operating systems, or models. Tenant-dependent `C` and `E` remain `NOT RUN` for all 253 cases.

## Repository Architecture

The repository follows the [frozen architecture](../ARCHITECTURE.md): each Skill is an independently usable publication package with a separately constructible oracle-free runtime tree. Runtime installation includes only `SKILL.md`, `VERSION`, `agents/`, `references/`, `templates/`, and `examples/`; it excludes `README.md`, `CHANGELOG.md`, `VALIDATION.md`, `tests/`, root research/reviews, prior outputs, and sibling Skills.

The root contains the [repository overview](../README.md), [contribution policy](../CONTRIBUTING.md), [changelog](../CHANGELOG.md), [MIT license](../LICENSE), research evidence, independent reviews, and seven domain packages. No runtime package requires a root file or sibling Skill. Cross-domain work is exchanged as explicit handoff contracts with a standalone fallback.

## Phase and gate record

### Phase 1 — Discovery and Research

- **Completed work:** inspected the accessible workspace and supplied Cortex artifacts, inventoried project conventions and gaps, researched current official Palo Alto Networks material, mapped products and Skill boundaries, and planned the Golden Reference.
- **Evidence collected:** 117 unique official references, 103 structured research records, accessible attached/project artifacts, archive-integrity evidence, and explicit records for inaccessible or referenced-only material.
- **Files created/modified:** [ecosystem map](../research/cortex-ecosystem-map.md), [project findings](../research/project-findings.md), [documentation sources](../research/documentation-sources.md), [domain boundaries](../research/skill-domain-boundaries.md), [architecture decisions](../research/architecture-decisions.md), [project knowledge inventory](../research/project-knowledge-inventory.md), [project-versus-official differences](../research/project-vs-official-differences.md), [Golden implementation plan](../research/golden-reference-implementation-plan.md), and [Phase 1 checkpoint](../research/phase-1-checkpoint.md).
- **Tests performed:** file accessibility, strict UTF-8, ZIP path/integrity/decompression and manifest checks, source reachability/semantic sampling, duplicate/source classification checks, and project-versus-official reconciliation.
- **Findings:** inaccessible project material was not fabricated; a supplied historical validation report did not match the accessible ZIP revision; product terminology, source drift, and legacy/current conflicts were recorded.
- **Open risks:** inaccessible ChatGPT Project/File Library items and named-but-missing originals remain unavailable; documentation may drift after the snapshot.
- **Quality gate status:** `PASS`; the checkpoint ends with `PHASE 1 GATE: PASS`.
- **Next phase eligibility:** eligible for Phase 2 only; mass Skill construction was not authorized at this point.

### Phase 2 — Golden Reference Implementation

- **Completed work:** implemented only `cortex-xql-query-engineer` as the prototype for structure, instructions, progressive disclosure, templates, examples, tests, evidence classification, safety, maintenance, and compatibility guidance.
- **Evidence collected:** dated official XQL/product sources, project-specific query conventions, explicit product/surface/schema boundaries, and an oracle-free runtime manifest.
- **Files created/modified:** the complete [XQL publication package](../cortex-xql-query-engineer/README.md) and its per-Skill references, templates, examples, tests, version, changelog, adapter metadata, and validation ledger.
- **Tests performed:** metadata validation, local-link and package-closure checks, source checks, authored 41-case catalog construction, and initial isolated response evaluation.
- **Findings:** early evidence-identity, unverified-API, comment/product inference, and competing-taxonomy risks required correction and independent validation.
- **Open risks:** tenant schema, compiler/editor/API and execution evidence remained unavailable.
- **Quality gate status:** `PASS` as a candidate implementation; approval was deliberately deferred to Phase 3.
- **Next phase eligibility:** eligible for Golden validation only; other Skills remained blocked.

### Phase 3 — Golden Reference Validation

- **Completed work:** independently reviewed XQL technical accuracy, documentation, behavior, standalone operation, cross-platform packaging, maintainability, security, and hallucination resistance; corrected findings and retained historical attempts.
- **Evidence collected:** exact runtime identities, five independent reviewer roles, oracle-isolated response records, revision-impact decisions, official-source mappings, and the [Golden review](xql-golden-reference-review.md).
- **Files created/modified:** Golden review, XQL validation ledger, corrected XQL runtime files, changelog, and retained test/review evidence.
- **Tests performed:** revision-aware cumulative `S: PASS` for 41/41 cases; `D: PASS` for 38 applicable cases with 3 `N/A`; validator, link, source, packaging, adversarial, model-variance and targeted post-hardening checks.
- **Findings:** high-severity evidence-chain and alternate-taxonomy findings plus lower template/encoding issues were corrected; the initial incomplete `XQL-INT-01` attempt remains visible before its passing rerun.
- **Open risks:** `C` and `E` remain `NOT RUN` for 41/41; one supplemental lower-capacity model omitted part of an API-verification plan and is not certified.
- **Quality gate status:** `PASS`; the independent review ends with `GOLDEN REFERENCE APPROVED: YES`.
- **Next phase eligibility:** eligible for Phase 4 only after that exact approval.

### Phase 4 — Freeze Golden Reference Architecture

- **Completed work:** extracted the approved structural and evidence principles into a repository specification without creating a shared runtime dependency.
- **Evidence collected:** approved Golden conventions for required/optional files, naming, progressive disclosure, sources, tests, standalone behavior, metadata, compatibility, versioning, security, and review.
- **Files created/modified:** [ARCHITECTURE.md](../ARCHITECTURE.md).
- **Tests performed:** conformance mapping against the XQL package, runtime/publication/scorer separation, path-resolution checks, and evidence-taxonomy consistency review.
- **Findings:** shared architecture was retained as authoring guidance only; every runtime must carry its own instructions and references.
- **Open risks:** future architecture changes require revision-impact analysis across seven independent packages.
- **Quality gate status:** `PASS`; architecture frozen for version `0.1.0`.
- **Next phase eligibility:** eligible for domain-specific implementation of the remaining six Skills.

### Phase 5 — Parallel Skill Implementation

- **Completed work:** separate specialists implemented Detection, Playbook, Threat Hunter, TIM, Platform, and Security Skills using the frozen pattern without cloning XQL domain content.
- **Evidence collected:** domain-specific official-source registers, product boundaries, safety models, templates, examples, and seven-category test catalogs.
- **Files created/modified:** the six non-Golden Skill publication packages and their individual `README.md`, `SKILL.md`, `VERSION`, adapter, references, templates, examples, tests, `VALIDATION.md`, and `CHANGELOG.md` files.
- **Tests performed:** author-side structure, metadata, link, source, manifest, example-classification and test-schema checks; these checks were not treated as independent `S` approval.
- **Findings:** candidate gaps in detection staging, playbook contracts/troubleshooting, platform component/source boundaries, Security standalone packets, evidence taxonomy and compatibility wording were handed to independent phases.
- **Open risks:** independent behavioral coverage, technical accuracy, compatibility and adversarial results were still pending.
- **Quality gate status:** `PASS` for implementation completeness, not release approval.
- **Next phase eligibility:** eligible for standalone independent validation.

### Phase 6 — Independent Testing

- **Completed work:** evaluated each Skill as an isolated runtime without root reviews, sibling Skills, tests or scorer oracles; synchronized per-Skill validation ledgers.
- **Evidence collected:** seven runtime manifests, selected oracle-isolated responses, complete XQL chain, 253 authored cases, static package results, and explicit S/D/C/E boundaries.
- **Files created/modified:** seven `VALIDATION.md` ledgers, corrected runtime files, and per-Skill changelogs.
- **Tests performed:** 14/14 framework validator runs (native plus explicit UTF-8), 7/7 YAML parses, 253/253 unique case-schema checks, 18/18 release-checklist items per Skill, runtime link/escape checks, and controlled response evaluation at the scopes in Test Results.
- **Findings:** selected behavioral and static findings were corrected; template-result fields were normalized to the exact enum plus rationale.
- **Open risks:** the original Phase 6 gap was 191 non-XQL S cases; the later Astra completion sample reduced the current gap to 179. General host behavioral equivalence and every tenant-dependent C/E check remain NOT RUN.
- **Quality gate status:** `PASS` for standalone source/runtime closure and the explicitly selected S evidence; no full-suite claim outside XQL.
- **Next phase eligibility:** eligible for cross-role review.

### Phase 7 — Cross Review

- **Completed work:** reviewers other than the Skill authors completed the required domain map and technical-accuracy checks, including final exact-snapshot revision-impact review.
- **Evidence collected:** [cross-Skill review](cross-skill-review.md), exact runtime hashes, selected-case decisions, source denominators, handoff contracts, and closed-finding evidence.
- **Files created/modified:** cross-Skill review plus corrected Skill runtimes, ledgers and changelogs.
- **Tests performed:** XQL by Detection and Technical Accuracy; Detection by Threat Hunting and Technical Accuracy; Playbook by Platform and Technical Accuracy; Threat Hunter by XQL and Detection; TIM by Platform and Technical Accuracy; Platform by Architecture and Technical Accuracy; Security by Skill Architecture and multiple domain specialists.
- **Findings:** all recorded High/Medium cross-role findings, including final source and validation-template deltas, are `CLOSED` on the exact current runtime hashes.
- **Open risks:** selected non-XQL tests do not establish exhaustive behavior or future model reproducibility.
- **Quality gate status:** `PASS`; open `BLOCKER/CRITICAL/HIGH/MEDIUM/LOW` is `0/0/0/0/0`.
- **Next phase eligibility:** eligible for repository-wide adversarial review.

### Phase 8 — Adversarial Review

- **Completed work:** red-teamed all seven runtimes and all 253 authored cases for hallucination, injection, product conflation, unsafe action, hidden dependency, deprecated behavior, weak evidence and compatibility overclaim.
- **Evidence collected:** [adversarial review](adversarial-review.md), [known limitations](known-limitations.md), final runtime identities, controlled risk cases, static scans, and retained closed findings.
- **Files created/modified:** adversarial and limitation reviews plus the corrections they trace.
- **Tests performed:** all-runtime instruction inspection, all-case oracle inspection, selected forward adversarial runs, source/terminology checks, secret/local-path/reparse scans, runtime dependency closure, and post-correction revision-impact review.
- **Findings:** every recorded adversarial High/Medium/Low item is `CLOSED`; no historical failure was erased.
- **Open risks:** static and selected-model evidence cannot prove tenant behavior or equivalence across hosts/models.
- **Quality gate status:** `PASS`; the review ends with `ADVERSARIAL REVIEW: PASS`.
- **Next phase eligibility:** eligible for independent Final QA and GitHub preparation.

### Phase 9 — Final QA and GitHub Preparation

- **Completed work:** independently inspected the corrected repository, synchronized runtime identities and ledgers, generated the release matrix, verified publication hygiene, closed compatibility finding CP-003, and issued this report after the final Astra completion pass and 23 fresh individual-case evaluations.
- **Evidence collected:** all prior checkpoints/reviews, final package manifests, per-Skill publication hashes, final validators, link/encoding/fence/YAML/test scans, and git-state inspection.
- **Files created/modified:** the seven final runtime/ledger/changelog deltas and offline release/evaluation tooling, synchronized cross-Skill and adversarial records, this report, and the final CP-003 disposition in [compatibility-review.md](compatibility-review.md); no Skill runtime changed after the identities below were frozen.
- **Tests performed:** final validator rerun, 253-case/schema audit, 153-file runtime closure, 252-path-link runtime audit, strict UTF-8 and Markdown-fence checks, local-link audit, canonical-result scan, version/checklist review, publication-hygiene scan, 23 one-case-per-process Astra evaluations, seven tooling unit tests, and independent report delta review.
- **Findings:** final Security source traceability, Platform/XQL/Playbook validation-format, and TIM dataset/source-attribution/product-scope findings were corrected and independently closed; no unresolved finding remains.
- **Open risks:** the local publication tree is not yet staged, committed or pushed; tenant and host-runtime limitations remain exactly as documented.
- **Quality gate status:** `PASS` for source publication only.
- **Next phase eligibility:** eligible for maintainer staging, commit, remote review and publication; those external git actions were not requested or performed.

## Skills Delivered

| Skill | Version | Authored cases | Runtime files / bytes | Runtime ordinal SHA-256 |
|---|---:|---:|---:|---|
| [`cortex-xql-query-engineer`](../cortex-xql-query-engineer/README.md) | `0.1.0` | 41 | 22 / 202,475 | `d51eac19cdadd0852a4d2d7bf63dd894389aa621e972e1c09f39194f038af7f7` |
| [`cortex-detection-engineer`](../cortex-detection-engineer/README.md) | `0.1.0` | 39 | 22 / 123,904 | `b2c8a42b879b12df22b4efccc413d32d771cdbd119713021e7bdfc966349cb81` |
| [`cortex-playbook-engineer`](../cortex-playbook-engineer/README.md) | `0.1.0` | 28 | 20 / 151,241 | `ee2624e64bbb650b98a9a7e7594bc8c3896d6f49bbc12fcf19801578f119ed4a` |
| [`cortex-threat-hunter`](../cortex-threat-hunter/README.md) | `0.1.0` | 26 | 22 / 73,435 | `af98de5883f06eea19adf89b9c6ce6cf1676830441f11f774d74a1b286f8f092` |
| [`cortex-tim-engineer`](../cortex-tim-engineer/README.md) | `0.1.0` | 37 | 21 / 126,788 | `e2e49820268e45ee8017ce67d397cb73d9d08cdfd80fc7dc9b16e1f58b2de0fb` |
| [`cortex-platform-engineer`](../cortex-platform-engineer/README.md) | `0.1.0` | 41 | 24 / 150,595 | `3960f33a98b7de1044d06ffac9f18adec15edce6b4e0425be362376642bebb8c` |
| [`cortex-security-engineer`](../cortex-security-engineer/README.md) | `0.1.0` | 41 | 22 / 124,841 | `e5742a5500c39a874b5d68f5ac83679ab74a56efd86e088c6a48cf8110355a8d` |

The runtime total is 153 files. Each domain owns its primary behavior and remains useful when every sibling directory is absent.

## Golden Reference Status

The XQL Golden Reference is independently approved. Its review contains the required exact terminal marker, binds the decision to the current 22-file runtime, retains historical corrections, and records historical revisions plus the current Astra semantic/tie-handling and source-discrepancy revision impact. Current controlled status is `S: PASS` for 41/41 cumulative cases, `D: PASS` for 38 applicable cases with 3 `N/A`, and `C/E: NOT RUN` for 41/41.

The approval establishes the repository architecture and XQL source-publication quality. It does not establish tenant schema, compilation, execution, detection deployment, performance, or cross-host equivalence.

## Source Verification

Current official Palo Alto Networks documentation controls factual product behavior. Official examples and repositories are secondary first-party evidence; accessible project material influences conventions but does not silently override current official behavior.

| Skill | Independent D result | Boundary |
|---|---|---|
| XQL | `PASS` — 38 applicable cases; 3 `N/A`; 50 registered Skill URLs reachable at snapshot | Dataset/field and surface availability still tenant-unverified |
| Detection | `PASS` — 23/23-source register | Rule availability, editor schema and deployed behavior not inferred |
| Playbook | `PASS` — 35/35-source register | Installed packs, commands, context and import not inferred |
| Threat Hunter | `PASS` — 21/21-source register | Conceptual product-neutral cases may use `D: N/A` |
| TIM | `PASS` — 32/32-source register | `indicators` is the documented dataset; generic feed guidance is not cited for fetch-history; XSOAR-specific TAXII/OpenCTI wording is not transposed to XSIAM; lifecycle/distribution/enforcement remain separate |
| Platform | `PASS` — 45 current sources; 2 historical pointers explicitly bounded | Historical pages do not establish current support |
| Security | `PASS` — 27/27-source register | Corrected XSOAR SaaS and Runtime Security pages were semantically rechecked |

The [project knowledge inventory](../research/project-knowledge-inventory.md) records what was actually accessible and which Skills may consume it. The [difference register](../research/project-vs-official-differences.md) preserves version-specific, legacy, customized, incorrect and unresolved conflicts. Inaccessible project/chat knowledge is explicitly recorded as unavailable rather than reconstructed.

## Standalone Validation

- Seven isolated runtime trees contain 153 files and 252 relative path links (508 including same-file anchors).
- Runtime link audit: `PASS` — zero missing targets, zero package escapes, zero absolute local dependencies, and zero reparse-point dependencies.
- Framework validation: `PASS` — 7/7 native Windows-mode and 7/7 explicit UTF-8 runs.
- Adapter YAML parse: `PASS` — 7/7.
- Strict UTF-8 and Markdown fence audit: `PASS` — zero decoding or unbalanced-fence findings.
- Test catalog: `PASS` — 253 unique IDs, seven required categories per Skill, and all six required sections per case.
- Release checklists: `PASS` — 18 checked items in every `VALIDATION.md`.
- Canonical validation-output scan: `PASS` — every explicit runtime output template and example validation block supplies all four canonical results with level-specific rationale; compact S/D/C/E mentions retained in explanatory prose are not validation records.

These are static and controlled-evaluation results. They do not prove host discovery, tenant parsing, import, execution or operational behavior.

## Cross-Skill Review

The [cross-Skill review](cross-skill-review.md) completes the required reviewer map with no author self-approval. XQL was reviewed by Detection and Technical Accuracy; Detection by Threat Hunting and Technical Accuracy; Playbook by Platform and Technical Accuracy; Threat Hunter by XQL and Detection; TIM by Platform and Technical Accuracy; Platform by Architecture and Technical Accuracy; Security by Skill Architecture, Platform, Threat Hunting and XQL/Technical roles.

Domain overlap is limited to explicit contracts for telemetry, schema, evidence, safety and handoff. No Skill has a mandatory sibling dependency. All final runtime deltas were independently reviewed against their exact hashes and their limited historical evidence bridges; unresolved cross-Skill findings are zero.

## Technical Accuracy Review

Technical review separated current official capability from tenant state, exact product/version/surface from generic Cortex terminology, and documentation evidence from compilation or execution evidence. It specifically rechecked XQL syntax/surface claims, detection families, XSIAM/XSOAR playbook behavior, TIM lifecycle/distribution plus feed-history and TAXII/OpenCTI product scope, component boundaries, Broker VM behavior, Security routing, legacy terminology, and direct-source applicability.

No reviewer promoted reachability into semantic support, examples into tenant availability, or selected response quality into product execution. Version-sensitive and contradictory official material remains classified rather than normalized silently.

## Compatibility Review

The [compatibility review](compatibility-review.md) passes static package portability while keeping loading, discovery and behavioral runtime separate.

| Surface | Final status |
|---|---|
| ChatGPT desktop | Static runtime-only package `PASS`; load, discovery and behavior `NOT RUN` |
| ChatGPT web/mobile | Plugin package `N/A` for this repository; runtime `NOT RUN` |
| Codex CLI/IDE | Static package `PASS`; XQL has a separately bounded manual-load smoke; general automatic discovery/runtime `NOT RUN` |
| Claude Code | Static package `PASS`; load, discovery and behavior `NOT RUN` |
| claude.ai | Runtime ZIP constructibility `PASS`; upload and behavior `NOT RUN` |
| Claude API | Upload-package constructibility `PASS`; `skill_id` use and behavior `NOT RUN` |

Linux and macOS execution were not performed. Static compatibility never implies equal instruction-following across hosts or models.

## Security Review

Security review passed for the source-publication boundary. Runtime instructions treat supplied documents, queries, logs, exports, comments, tool output and examples as untrusted data; prohibit embedded secrets and customer identifiers; default to read-only analysis; and require explicit authorization, least privilege, bounded targets, blast-radius controls, stop conditions, partial-failure handling, recovery, readback and retained evidence before material writes.

Static scans found no high-signal credential, private key, absolute local dependency, reparse-point dependency or mandatory sibling dependency. This is not a guarantee against every semantic secret and does not authorize a future state change.

## Adversarial Review

The [adversarial review](adversarial-review.md) inspected all seven final Skills and all 253 authored cases. It challenged fabricated syntax/schema/API/command behavior, prompt injection, product conflation, evidence promotion, unsafe response, hidden dependency, deprecated guidance, compatibility overclaim and oracle leakage. All recorded findings are closed on the final runtime identities, and the exact terminal verdict is `ADVERSARIAL REVIEW: PASS`.

Selected forward runs outside XQL remain samples. The adversarial pass does not turn unexecuted cases, tenant behavior, or future model behavior into a pass.

## Astra completion evidence

The [Astra review](astra-review.md) records the full-file inspection, current-source delta checks, retained failures, corrected contracts and 23 fresh individual-case evaluations. Each forward received only runtime files plus Fixture/Prompt; no scorer, sibling or root knowledge was exposed. Publication-ready means reviewed source and runtime packaging, not a live Cortex certification. Historical raw responses were not all available for regrading; only their bounded reviewer records were retained.

## Test Results

| Skill | `S` controlled response evaluation | `D` official-document evidence | `C` product/schema/import | `E` execution/observation |
|---|---|---|---|---|
| XQL | `PASS` — 41/41 cumulative | `PASS` — 38 applicable; 3 `N/A` | `NOT RUN` — 41/41 | `NOT RUN` — 41/41 |
| Detection | `PASS` — 8 selected; 31 `NOT RUN` | `PASS` — 23/23 | `NOT RUN` — 39/39 | `NOT RUN` — 39/39 |
| Playbook | `PASS` — 3 selected; 25 `NOT RUN` | `PASS` — 35/35 | `NOT RUN` — 28/28 | `NOT RUN` — 28/28 |
| Threat Hunter | `PASS` — 9 selected; 17 `NOT RUN` | `PASS` — 21/21 | `NOT RUN` — 26/26 | `NOT RUN` — 26/26 |
| TIM | `PASS` — 5 selected; 32 `NOT RUN` | `PASS` — 32/32 | `NOT RUN` — 37/37 | `NOT RUN` — 37/37 |
| Platform | `PASS` — 2 selected; 39 `NOT RUN` | `PASS` — 45 current + 2 historical bounded | `NOT RUN` — 41/41 | `NOT RUN` — 41/41 |
| Security | `PASS` — 6 selected; 35 `NOT RUN` | `PASS` — 27/27 | `NOT RUN` — 41/41 | `NOT RUN` — 41/41 |

Aggregate `S` coverage is 74 independently passed case decisions (23 fresh individual Astra passes plus 51 retained historical decisions via bounded revision impact) and 179 explicitly unexecuted cases. The repository contains 253 C-level and 253 E-level `NOT RUN` decisions. No sample is presented as exhaustive coverage for a non-Golden Skill.

## Hallucination Audit

| Required audit category | Result | Evidence boundary |
|---|---|---|
| Nonexistent XQL stages | `PASS` — no unresolved finding | Current official register, Golden technical review and cases; tenant compiler still `NOT RUN` |
| Nonexistent XQL functions | `PASS` — no unresolved finding | Version/surface conflicts stay explicit; tenant compiler still `NOT RUN` |
| Nonexistent datasets | `PASS` — no unresolved finding | The unsupported TIM `indicator_relationship` assertion was removed; concrete names require source plus tenant schema qualification |
| Nonexistent fields | `PASS` — no unresolved finding | Documented fields never imply target-tenant presence |
| Fake Cortex APIs | `PASS` — no unresolved finding | Unverified endpoints cannot be emitted as executable requests |
| Fake API parameters | `PASS` — no unresolved finding | Exact current contract, product/version and authorization are required |
| Fake XSOAR/XSIAM commands | `PASS` — no unresolved finding | Capability placeholders remain non-executable until tenant command help is supplied |
| Incorrect context-data paths | `PASS` — no unresolved finding | Literal legacy paths are product/version scoped; unknown paths remain placeholders |
| Unsupported TIM functionality | `PASS` — no unresolved finding | Collection, management, enrichment, lifecycle, distribution and enforcement remain separate; checkpoint/reset behavior requires integration-specific evidence |
| Incorrect Broker VM behavior | `PASS` — no unresolved finding | Agent, Broker VM, XDR Collector and Cortex Engine are distinct; no invented port/capacity/health |
| Cross-product assumptions | `PASS` — no unresolved finding | XDR, XSIAM, XSOAR, TIM and Cortex Cloud claims retain product/surface boundaries; XSOAR TAXII/OpenCTI semantics are not reused as XSIAM evidence |
| Outdated terminology | `PASS` — no unresolved finding | Current Case/Issue language is preferred; required legacy literals remain quoted/scoped |
| Deprecated resources | `PASS` — no unresolved finding | Historical sources and successor paths are explicitly marked |
| Conceptual content presented as executable | `PASS` — no unresolved finding | Artifact classification and import gates prevent promotion |
| Unverified content presented as verified | `PASS` — no unresolved finding | Canonical status, provenance qualifier and independent S/D/C/E stay separate |

`PASS` means the final static, source and controlled-review scope contains no unresolved finding in that category. It is not a universal proof about future generated output or a live tenant.

## Deprecated / Version-dependent Features

- Retiring XSOAR Administrator Guide pages remain only as `DEPRECATED / REFERENCED-ONLY` history; current product/version-specific Cortex Engine pages are the support evidence.
- XSOAR 8.14 On-prem documentation is version-scoped and is not transposed to XSOAR SaaS or XSIAM.
- Current XSIAM prose uses Case/Issue terminology while documented literals such as `issue`, `parentIncidentContext` and `setParentIncidentContext` remain literal and version-scoped.
- TIM's OpenCTI Feed 3.x, legacy Export Indicators Service, and PAN-OS EDL Management paths are recorded with current successor/deprecation context rather than presented as default current architecture.
- The TAXII 2 Feed integration is listed for XSOAR and XSIAM, but its complex-observation relationship sentence explicitly names XSOAR TIM; XSIAM applicability remains `UNVERIFIED` without separate evidence.
- TAXII Server and TAXII2 Server are listed for XSOAR and XSIAM, but their collection/query and API/object wording explicitly names XSOAR; XSIAM selection/object semantics remain `UNVERIFIED` without separate evidence.
- Official documentation has a version-sensitive conflict concerning the XQL `regextract()` return shape; the Skill preserves the conflict and requires target verification.
- Dataset, field, function, API, command, UI, license, limit and configuration behavior can change after the dated snapshot.

## Known Limitations

The complete boundary is maintained in [known-limitations.md](known-limitations.md). Material limits are:

- no live Cortex tenant, tenant inventory, schema, editor/compiler, SDK/import, API session or integration instance was available;
- no query, rule, playbook, feed, parser, collector, response action, configuration, deployment, rollback or downstream control was executed;
- no returned result, detection efficacy, false-positive/false-negative rate, completeness, latency, throughput, cost or performance was observed;
- 179 non-XQL behavioral cases and all tenant-level C/E checks remain `NOT RUN`;
- ChatGPT/Claude behavioral runtime and Codex automatic discovery remain untested except for the separately bounded XQL manual-load evidence;
- official documentation and living repositories can drift after their individually dated September 4/6 checks;
- some referenced project/ChatGPT knowledge was inaccessible and was not fabricated; and
- the current local source tree is untracked and has not been committed or pushed.

## Remaining Findings

BLOCKER: 0

CRITICAL: 0

HIGH: 0

MEDIUM: 0

LOW: 0

Historical findings remain in the Golden, cross-Skill, compatibility and adversarial ledgers with their corrections and exact-snapshot dispositions. Zero means unresolved findings, not that no issue was ever discovered.

## Release Matrix

| Skill | Standalone | ChatGPT | Codex | Claude | Official Docs Verified | Examples | Tests | Security Review | Adversarial Review | QA |
|---|---|---|---|---|---|---|---|---|---|---|
| cortex-xql-query-engineer | `PASS` — static + full scoped S | Desktop static `PASS`; web/mobile plugin `N/A`; runtime `NOT RUN` | Static `PASS`; bounded manual load; discovery/runtime not generalized | Static `PASS`; load/runtime `NOT RUN` | `PASS` — D 38 + 3 `N/A` | `PASS` — classified/static | `PASS` — S 41/41; C/E `NOT RUN` | `PASS` — source scope | `PASS` — 0 open | `PASS` — source publication |
| cortex-detection-engineer | `PASS` — static + selected S | Desktop static `PASS`; web/mobile plugin `N/A`; runtime `NOT RUN` | Static `PASS`; load/discovery/runtime `NOT RUN` | Static `PASS`; load/runtime `NOT RUN` | `PASS` — D 23/23 | `PASS` — classified/static | `PASS` — S 8/39; 31 `NOT RUN`; C/E `NOT RUN` | `PASS` — source scope | `PASS` — 0 open | `PASS` — source publication |
| cortex-playbook-engineer | `PASS` — static + selected S | Desktop static `PASS`; web/mobile plugin `N/A`; runtime `NOT RUN` | Static `PASS`; load/discovery/runtime `NOT RUN` | Static `PASS`; load/runtime `NOT RUN` | `PASS` — D 35/35 | `PASS` — non-importable/classified | `PASS` — S 3/28; 25 `NOT RUN`; C/E `NOT RUN` | `PASS` — source scope | `PASS` — 0 open | `PASS` — source publication |
| cortex-threat-hunter | `PASS` — static + selected S | Desktop static `PASS`; web/mobile plugin `N/A`; runtime `NOT RUN` | Static `PASS`; load/discovery/runtime `NOT RUN` | Static `PASS`; load/runtime `NOT RUN` | `PASS` — D 21/21 | `PASS` — classified/static | `PASS` — S 9/26; 17 `NOT RUN`; C/E `NOT RUN` | `PASS` — source scope | `PASS` — 0 open | `PASS` — source publication |
| cortex-tim-engineer | `PASS` — static + selected S | Desktop static `PASS`; web/mobile plugin `N/A`; runtime `NOT RUN` | Static `PASS`; load/discovery/runtime `NOT RUN` | Static `PASS`; load/runtime `NOT RUN` | `PASS` — D 32/32 | `PASS` — classified/static | `PASS` — S 5/37; 32 `NOT RUN`; C/E `NOT RUN` | `PASS` — source scope | `PASS` — 0 open | `PASS` — source publication |
| cortex-platform-engineer | `PASS` — static + selected S | Desktop static `PASS`; web/mobile plugin `N/A`; runtime `NOT RUN` | Static `PASS`; load/discovery/runtime `NOT RUN` | Static `PASS`; load/runtime `NOT RUN` | `PASS` — D 45 current + 2 historical bounded | `PASS` — classified/static | `PASS` — S 2/41; 39 `NOT RUN`; C/E `NOT RUN` | `PASS` — source scope | `PASS` — 0 open | `PASS` — source publication |
| cortex-security-engineer | `PASS` — static + selected S | Desktop static `PASS`; web/mobile plugin `N/A`; runtime `NOT RUN` | Static `PASS`; load/discovery/runtime `NOT RUN` | Static `PASS`; load/runtime `NOT RUN` | `PASS` — D 27/27 | `PASS` — classified/static | `PASS` — S 6/41; 35 `NOT RUN`; C/E `NOT RUN` | `PASS` — source scope | `PASS` — 0 open | `PASS` — source publication |

No checkmark is used as a substitute for evidence. Every `PASS`, `NOT RUN`, and `N/A` is scoped in the matrix or the linked ledger.

## GitHub Publication Readiness

| Check | Result | Boundary |
|---|---|---|
| Consistent directory names and required files | `PASS` | Seven versioned packages conform to the frozen architecture |
| Relative README/review/reference links | `PASS` | Final local-link audit found zero missing targets |
| Absolute local paths | `PASS` | No local Windows, macOS or Linux user path remains in publication content |
| Secrets and private identifiers | `PASS` | No configured high-signal credential/private-key/customer finding; semantic guarantee is not claimed |
| Temporary/editor/generated junk | `PASS` | No reparse point, editor artifact, cache, temporary output or abandoned generated file found |
| Placeholders | `PASS` | Remaining placeholders are intentional, typed template inputs and are classified as unresolved—not abandoned content |
| Example classification | `PASS` | Examples state conceptual/configuration/evidence limits and do not claim tenant execution or importability |
| Versions and changelogs | `PASS` | All seven Skills are `0.1.0`; root and per-Skill changelogs are meaningful |
| License and attribution | `PASS` | MIT license present; official sources are linked and provenance preserved |
| Source traceability | `PASS` | Research register, per-Skill official registers, inventory and difference log retained |
| Review artifacts | `PASS` | Golden, cross-Skill, adversarial, compatibility, known-limitations and Final QA reports present |
| Git operation | `NOT RUN` | The local nested publication tree is untracked; no staging, commit, push, release or remote publication was requested |

The current exact runtime identities are shown in Skills Delivered. Final publication-package identities use the same ordinal manifest recipe as the runtimes but include the entire individual Skill directory:

| Skill | Publication files / bytes | Publication ordinal SHA-256 |
|---|---:|---|
| cortex-xql-query-engineer | 33 / 302,888 | `2d961f8cb093dff7003d7989ce222834d541543524c4f095cf4547a3de91aab1` |
| cortex-detection-engineer | 33 / 189,300 | `be122507d790facc0d7aa71e885bea14ce5d31b5dbe1a6902b590d35b9b3bf46` |
| cortex-playbook-engineer | 31 / 213,145 | `83690cd83506610e92f87a82b355dc6d0590e5786a1d67602ffd4586843062e9` |
| cortex-threat-hunter | 33 / 124,378 | `6fb58207d9463c8813eed315d542192371d6363dfc4748f7221075a616c8fa83` |
| cortex-tim-engineer | 32 / 187,491 | `b9fbcc7e9d91fb58435f4202a12f6945e596a5f3e954423caa137ad6f284ad74` |
| cortex-platform-engineer | 35 / 222,034 | `e75bd582fd48840cb1cf4ce82a961150c99b7ea6b0ee570f2baecdd23d13b62a` |
| cortex-security-engineer | 33 / 202,332 | `3f3fcc60b75e2c3486b9ebc1d00b2a7154e41b614caa483196a44d62fe7721af` |

Publication readiness authorizes packaging and normal git review; it does not authorize deployment to Cortex or certify any tenant.

Independent final synchronization QA: PASS, recorded from reviewer astra_xql_detection_hunt on the completion date. The reviewer independently recomputed all seven runtime/publication file counts, byte totals and hashes; checked all 23 final response headers, one-case isolation and zero tool events; confirmed 126 checklist items, 74 cumulative S decisions and 179 NOT RUN; and reran all seven tooling tests. The only pending audit items were the two administrative terminal markers, now closed on that independent decision. XQL/Detection/Threat content was independently adjudicated by astra_playbook_tim, so this final consolidation decision is not author self-approval. No further source or runtime correction was required.

REPOSITORY PRODUCTION READY: YES
