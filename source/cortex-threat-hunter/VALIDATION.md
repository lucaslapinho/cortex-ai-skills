# Validation ledger

## Version 0.1.1 refresh snapshot — 2026-10-23

**Scope:** the bounded source inspection and dataset-population refinement in [references/2026-10-23-refresh.md](references/2026-10-23-refresh.md). The September hashes, evaluations and approvals below are historical identities, not approval of these changed bytes.

| Level | Result for this revision | Boundary |
|---|---|---|
| S | NOT RUN | No fresh independent controlled hunt-response evaluation for version 0.1.1 |
| D | PASS — scoped | Only the read query/graph, issue-dataset, investigation and grouping claims |
| C | NOT RUN | No tenant identity, schema, editor/compiler or import acceptance |
| E | NOT RUN | No tenant query, graph execution, hunt result or response observation |

Release structure/link checks cannot establish behavioral or tenant validation. The release audit must calculate a new runtime identity; earlier hashes below remain tied to their original recorded dates.

## Current completion decision — 2026-09-06

**Current reviewed runtime:** 22 files / 73,435 bytes; ordinal SHA-256 `af98de5883f06eea19adf89b9c6ce6cf1676830441f11f774d74a1b286f8f092`.

**Decision:** source/runtime-package completion PASS after independent Astra delta review and fresh individual-case evaluation. This section supersedes candidate/pending wording below for this exact snapshot; historical records and failures remain unchanged.

| Level | Current scoped result | Rationale |
|---|---|---|
| S | PASS — 9/26 cumulative; 17 NOT RUN | 8 fresh individual Astra cases passed, plus 1 identified historical decisions retained only through independent revision-impact review; not 26 new Astra runs |
| D | PASS — scoped dated source evidence | Historical September 4 register plus actual September 6 claim-level rechecks; no assertion that every source was reopened on September 6 or that the offline forward performed a fresh D check |
| C | NOT RUN — 26/26 | No named tenant compiler, schema acceptance or controlled import |
| E | NOT RUN — 26/26 | No tenant execution, deployment, result, efficacy or recovery observation |

Fresh final cases: `CTH-REG-01`, `CTH-ADV-03`, `CTH-ADV-02`, `CTH-TRB-02`, `CTH-AMB-03`, `CTH-ADVRS-05`, `CTH-REG-04`, `CTH-AMB-01`. Each received only the runtime files and its Fixture/Prompt in one new ephemeral Astra process; zero tool/action events were observed. Independent reviewers compared the complete retained responses against the applicable oracles; the model did not award its own S pass. Earlier multi-case exploratory batches do not add coverage. Historical raw responses were not all available to rescore and are not described as new runs.

The full-source repository retains the independent Astra domain reviews and response records under reviews; those development artifacts are optional audit material and are excluded from this Skill's runtime. The standalone package carries this scoped decision and exact identity without requiring those root files to function. All runtime/publication links, metadata, UTF-8, test-case structure, and the 18-item checklist passed the final static audit. No unresolved publication finding remains in the reviewed scope; known tenant/host/source-drift limits are retained below.


## Astra author-side revision — 2026-09-06

**Scope:** all 33 files listed below were read in full, including runtime, publication and scorer material. ARCHITECTURE.md and relevant local project reconciliation were also inspected. This revision did not rely on old approvals or hashes as proof of quality.

Corrected unsupported/deprecated/provenance meanings, reconciled official-schema candidates with tenant gaps, and improved progressive disclosure.

- `S: NOT RUN` — no independent behavioral pass for this new delta is claimed here; parent-coordinated forward evaluation and independent review remain separate.
- `D: PASS` — only the bounded source observations in the dated Astra recheck of references/official-sources.md; unresolved document discrepancies remain explicitly scoped.
- `C: NOT RUN` — no applicable tenant schema/editor/compiler evidence.
- `E: NOT RUN` — no tenant execution, mutation or observed result.

**Revision impact:** Changed cases: CTH-REG-01, CTH-ADV-03, CTH-ADV-02, CTH-TRB-02, CTH-AMB-03 and CTH-ADVRS-05. CTH-REG-01 and CTH-ADV-03 were in the five historically selected S passes; rerun them. CTH-REG-04 and CTH-AMB-01 are additional impact checks for documentation-grounded XQL and narrow product-neutral answers.

The evidence, hashes, results, approval wording and checklist below this section are historical 2026-09-04 records. They do not certify this changed candidate or its strengthened tests. A final independent candidate identity and delta result must be recorded separately; no prior result has been silently promoted.

### Complete file-reading coverage

- `agents/openai.yaml`
- `CHANGELOG.md`
- `examples/credential-access-hypothesis.md`
- `examples/dns-activity-scope.md`
- `examples/ioc-to-behavioral-hunt.md`
- `examples/README.md`
- `examples/suspicious-process-pivot.md`
- `examples/zero-results-troubleshooting.md`
- `README.md`
- `references/evidence-and-product-boundaries.md`
- `references/findings-and-detection-handoff.md`
- `references/hunt-methodology.md`
- `references/official-sources.md`
- `references/pivots-timelines-and-scoping.md`
- `references/project-operational-patterns.md`
- `references/telemetry-and-coverage.md`
- `references/troubleshooting.md`
- `SKILL.md`
- `templates/detection-opportunity.md`
- `templates/evidence-ledger.md`
- `templates/hunt-plan.md`
- `templates/hunt-record.md`
- `templates/tenant-validation.md`
- `tests/advanced.md`
- `tests/adversarial.md`
- `tests/ambiguity.md`
- `tests/basic.md`
- `tests/intermediate.md`
- `tests/README.md`
- `tests/regression.md`
- `tests/troubleshooting.md`
- `VALIDATION.md`
- `VERSION`

## Historical evidence and approvals — 2026-09-04

**Skill version:** `0.1.0`  
**Evidence snapshot:** 2026-09-04  
**Reviewed runtime:** 22 files / 68,240 bytes; ordinal SHA-256 `eac24797f7ec4c2701f8e8e3c8633966a9f451da8daeffddd3e260b427e425b6`  
**Ledger status:** independent XQL, Detection, technical, adversarial and static compatibility review complete

This record distinguishes author-side package checks, independent controlled evaluation, official-document evidence and unavailable tenant validation.

## Validation levels

| Level | Meaning | Current result | Rationale |
|---|---|---|---|
| `S` | Controlled oracle-isolated response evaluation | `PASS` - 5 selected; 21 `NOT RUN` | Independent reviewers passed `CTH-ADVRS-03`, `CTH-AMB-01`, `CTH-REG-01`, `CTH-REG-04` and `CTH-ADV-03`; this is not a 26-case suite pass |
| `D` | Current official-document support for material factual claims | `PASS` - 21/21-source register | Independent technical review checked the dated official register; deliberately conceptual selected responses may individually be `N/A` |
| `C` | Named tenant schema/compiler/import validation | `NOT RUN` - 26/26 | No tenant schema, Query Center/compiler or product import was available |
| `E` | Hunt execution and observed tenant results | `NOT RUN` - 26/26 | No hunt, query, rule, response or production result was executed |

The model response's own S/D/C/E table is not self-approval. The independent scorer assigns the selected `S: PASS` results.

## Package and author checks

| Check | Result | Claim boundary |
|---|---|---|
| Publication/runtime/scorer separation | `PASS` - 33 publication files; 22 runtime files | Manifests only |
| Framework validator and YAML parse | `PASS` | Metadata structure only |
| Markdown links, anchors and fences | `PASS` - local targets resolve; fences balanced | Navigation/structure only |
| Secret, absolute-path and reparse scan | `PASS` - no configured high-signal finding | Cannot prove absence of every semantic secret |
| Standalone runtime closure | `PASS` - no root/sibling/scorer dependency | File autonomy, not host runtime |
| Official URL reachability | `PASS` - 21/21 at snapshot | Reachability is not semantic applicability |
| Test catalog | `PASS` - 26 unique cases with all six required sections | Authored oracle completeness only |

## Independent role gates

| Review | Result | Evidence boundary |
|---|---|---|
| Technical accuracy and documentation | `PASS` - zero open findings | Current sources and version/product boundaries |
| XQL Specialist | `PASS` - `CTH-ADV-03` and technical cases | Semantic requirements without fabricated XQL/schema |
| Detection Specialist | `PASS` - `CTH-ADV-03` | Complete detection-opportunity handoff without recall guarantee |
| Adversarial/security | `PASS` - zero open findings | Injection, destructive action, attribution and fabricated schema |
| Cross-platform compatibility | `PASS` - static package only | Host runtime remains separate |
| Repository Final QA | See `../reviews/final-qa.md` | Sequenced release authority; does not alter S/D/C/E |

## Host-surface status

| Surface | Static package | Load/discovery | Behavioral runtime |
|---|---|---|---|
| ChatGPT desktop | `PASS` - independent static review | `NOT RUN` | `NOT RUN` |
| ChatGPT web/mobile | `N/A` - plugin package not included | `NOT RUN` | `NOT RUN` |
| Codex CLI/IDE | `PASS` - independent static review | `NOT RUN` | `NOT RUN` |
| Claude Code | `PASS` - independent static review | `NOT RUN` | `NOT RUN` |
| claude.ai | `PASS` - ZIP-constructible runtime | `NOT RUN` | `NOT RUN` |
| Claude API | `PASS` - upload-constructible runtime | `NOT RUN` | `NOT RUN` |

## Required release checklist

- [x] Standalone file-level functionality independently reviewed
- [x] `SKILL.md` independently reviewed
- [x] References independently reviewed
- [x] Official documentation mapped and adjudicated
- [x] Examples independently reviewed
- [x] Selected controlled tests executed and independently adjudicated; 21 remain `NOT RUN`
- [x] Hallucination audit completed
- [x] Security review completed
- [x] Product boundaries verified
- [x] Deprecated behavior checked
- [x] ChatGPT static compatibility reviewed; runtime `NOT RUN`
- [x] Codex static compatibility reviewed; discovery/runtime `NOT RUN`
- [x] Claude static compatibility reviewed; runtime `NOT RUN`
- [x] No mandatory sibling dependencies
- [x] No broken internal references
- [x] No unresolved `BLOCKER` issues
- [x] No unresolved `CRITICAL` issues
- [x] No unresolved `HIGH` issues

## Release evidence summary

- Runtime isolation, references, templates, examples and selected hunt behavior received independent review.
- Cross-role review confirmed the XQL and Detection handoffs without moving query mechanics or rule ownership into this Skill.
- Official source, adversarial and static compatibility reviews passed with no open finding.
- The 21 unexecuted behavioral cases remain `NOT RUN`; no full-suite claim is made.

## Residual limitations

- No Cortex XSIAM/XDR tenant, schema, compiler, query execution, baseline population, hunt result or production action was available.
- Zero-result language remains coverage-qualified; it is never proof of absence.
- ATT&CK mapping, attribution and detection opportunity remain analytical conclusions bounded by evidence.
- Host loading, discovery and behavioral equivalence remain `NOT RUN`.

## Future tenant evidence record

Record product/version/license, tenant alias, role/SBAC, exact runtime and query artifact hashes, source health, dataset/schema/types, grain, time semantics, coverage/freshness/retention, fixtures and baselines, compiler result, query execution/result counts, negative controls, benign alternatives, pivot outcomes, limitations, reviewer and retained sanitized evidence. Keep `C` and `E` as `NOT RUN` until that record exists.
