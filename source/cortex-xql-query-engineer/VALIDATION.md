# Validation ledger

## Current completion decision — 2026-09-06

**Current reviewed runtime:** 22 files / 202,475 bytes; ordinal SHA-256 `d51eac19cdadd0852a4d2d7bf63dd894389aa621e972e1c09f39194f038af7f7`.

**Decision:** source/runtime-package completion PASS after independent Astra delta review and fresh individual-case evaluation. This section supersedes candidate/pending wording below for this exact snapshot; historical records and failures remain unchanged.

| Level | Current scoped result | Rationale |
|---|---|---|
| S | PASS — 41/41 cumulative; 0 NOT RUN | 4 fresh individual Astra cases passed, plus 37 identified historical decisions retained only through independent revision-impact review; not 41 new Astra runs |
| D | PASS — scoped dated source evidence | Historical September 4 register plus actual September 6 claim-level rechecks; no assertion that every source was reopened on September 6 or that the offline forward performed a fresh D check |
| C | NOT RUN — 41/41 | No named tenant compiler, schema acceptance or controlled import |
| E | NOT RUN — 41/41 | No tenant execution, deployment, result, efficacy or recovery observation |

Fresh final cases: `XQL-ADV-02`, `XQL-REG-05`, `XQL-REG-01`, `XQL-REG-07`. Each received only the runtime files and its Fixture/Prompt in one new ephemeral Astra process; zero tool/action events were observed. Independent reviewers compared the complete retained responses against the applicable oracles; the model did not award its own S pass. Earlier multi-case exploratory batches do not add coverage. Historical raw responses were not all available to rescore and are not described as new runs.

The full-source repository retains the independent Astra domain reviews and response records under reviews; those development artifacts are optional audit material and are excluded from this Skill's runtime. The standalone package carries this scoped decision and exact identity without requiring those root files to function. All runtime/publication links, metadata, UTF-8, test-case structure, and the 18-item checklist passed the final static audit. No unresolved publication finding remains in the reviewed scope; known tenant/host/source-drift limits are retained below.


## Astra author-side revision — 2026-09-06

**Scope:** all 33 files listed below were read in full, including runtime, publication and scorer material. ARCHITECTURE.md and relevant local project reconciliation were also inspected. This revision did not rely on old approvals or hashes as proof of quality.

Added equal-time dedup review, clarified DEPRECATED, and recorded claim-specific official rechecks and source discrepancies.

- `S: NOT RUN` — no independent behavioral pass for this new delta is claimed here; parent-coordinated forward evaluation and independent review remain separate.
- `D: PASS` — only the bounded source observations in the dated Astra recheck of references/official-sources.md; unresolved document discrepancies remain explicitly scoped.
- `C: NOT RUN` — no applicable tenant schema/editor/compiler evidence.
- `E: NOT RUN` — no tenant execution, mutation or observed result.

**Revision impact:** All 41 prior cases belonged to the cumulative historical S chain. Changed cases: XQL-ADV-02 and XQL-REG-05 (equal-time row-retention contract). Prior approvals do not evaluate the strengthened oracles. Also target XQL-REG-01 and XQL-REG-07 for the preserved official-source discrepancies.

The evidence, hashes, results, approval wording and checklist below this section are historical 2026-09-04 records. They do not certify this changed candidate or its strengthened tests. A final independent candidate identity and delta result must be recorded separately; no prior result has been silently promoted.

### Complete file-reading coverage

- `agents/openai.yaml`
- `CHANGELOG.md`
- `examples/detection/detection-handoff.md`
- `examples/hunting/lateral-movement.md`
- `examples/investigation/last-process-per-host.md`
- `examples/investigation/suspicious-powershell.md`
- `examples/README.md`
- `examples/troubleshooting/fabricated-schema.md`
- `README.md`
- `references/datasets.md`
- `references/evidence-and-product-boundaries.md`
- `references/fields-and-schema.md`
- `references/official-sources.md`
- `references/optimization.md`
- `references/query-patterns.md`
- `references/troubleshooting.md`
- `references/xql-language.md`
- `SKILL.md`
- `templates/detection-query.md`
- `templates/investigation-query.md`
- `templates/query-build.md`
- `templates/query-review.md`
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
**Reviewed runtime:** 22 files / 197,439 bytes; ordinal SHA-256 `2aed9bf9ebf7d24a5a3ad88de5c839329a8fe2e123ac99fa57ab3b617dda856d`  
**Ledger status:** Golden Reference approved; post-hardening, canonical-taxonomy and validation-template deltas independently revalidated on 2026-09-04; tenant-dependent validation remains `NOT RUN`

This ledger distinguishes what a check can establish from what it cannot. A structural pass is never represented as product or tenant execution.

## Validation levels

| Level | Meaning | Current result | Rationale |
|---|---|---|---|
| `S` | Controlled oracle-isolated response evaluation | `PASS` - 41/41 cumulative | The Golden chain covers the complete suite and includes fresh hardening/taxonomy reruns; independent revision-impact review found the final example-validation expansion formatting-only, and the historical incomplete `XQL-INT-01` attempt remains recorded before its passing rerun |
| `D` | Current official-document support for material factual claims | `PASS` - 38 applicable; 3 `N/A` | Independent review mapped material claims to the dated official register; `N/A` cases make no applicable factual product claim |
| `C` | Named tenant schema/editor/compiler/API/import validation | `NOT RUN` - 41/41 | No XSIAM/XDR tenant, schema export, compiler, editor, API session or controlled import was available |
| `E` | Tenant execution, returned results, deployment or production observation | `NOT RUN` - 41/41 | No query, rule, API flow, target action, result, efficacy or performance was executed or observed |

Static package checks are recorded separately below and are not self-awarded `S`. `S` and `D` do not imply `C` or `E`.

## Check ledger

| Check | Method/evidence | Status | Claim boundary |
|---|---|---|---|
| Phase 1 research gate | Independent checkpoint before Skill scaffolding | `PASS` | Authorizes Golden Reference construction only; not a Skill approval |
| Required package paths | Filesystem inspection | `PASS` | Establishes presence and non-empty content only |
| Skill metadata | Framework quick validator plus YAML parse | `PASS` | Establishes structural metadata validity only |
| Relative Markdown links | Local link-resolution scan | `PASS` — 70 checked, 0 broken | Does not test remote content |
| Official URL freshness | HTTP and topic/product review against the source index | `PASS` — 50 real Skill URLs returned 2xx on 2026-09-04 | Snapshot only; future drift remains possible |
| Absolute path, secret, and identifier scan | Static pattern scan | `PASS` | Does not prove absence of every sensitive semantic value |
| Standalone clean-directory copy | Exact 22-file runtime manifest plus repeated local checks | `PASS` | Establishes file-level autonomy, not universal platform runtime compatibility |
| Basic through regression scenarios | Oracle-free controlled outputs plus independent scoring and targeted reruns | `PASS` — Technical Accuracy: 41/41 cumulative; fresh hardening reruns passed `XQL-ADVRS-02`, `XQL-ADVRS-03`, `XQL-ADVRS-07`, `XQL-ADV-05`, and `XQL-AMB-05`; fresh taxonomy reruns passed `XQL-BAS-01`, `XQL-INT-01`, and `XQL-ADV-01`; Detection Engineering complete-suite `NOT RUN` | Static/simulated; the initial incomplete `XQL-INT-01` output and every superseding rerun remain documented |
| Independent five-role review and runtime delta revalidation | Detection, technical accuracy, architecture, adversarial, and cross-platform reviewers plus independent post-hardening, taxonomy, validation-template and example-validation technical rechecks | `PASS` — all required roles and all four deltas; 0 unresolved findings at every severity | Role-specific S/D/C/E results remain separate; supplemental model variance is not promoted to a universal pass |
| XSIAM tenant schema | Query Builder/autocomplete or versioned schema export | `NOT RUN` | Dataset/field/type availability remains `TENANT-UNVERIFIED` |
| XDR tenant schema | Query Builder/autocomplete or versioned schema export | `NOT RUN` | Dataset/field/type availability remains `TENANT-UNVERIFIED` |
| Tenant compilation | Named tenant and surface | `NOT RUN` | No query may claim `TENANT-COMPILED` |
| Tenant execution/results | Named tenant, identity scope, timeframe, and retained result evidence | `NOT RUN` | No query may claim `TENANT-EXECUTED` or measured performance |
| BIOC/correlation/XQLp import or deployment | Target product editors/API and controlled test | `NOT RUN` | No artifact is represented as import-ready or deployed |

## Golden Reference decision

The independent review at [../reviews/xql-golden-reference-review.md](../reviews/xql-golden-reference-review.md) records five role-specific `PASS` verdicts, zero unresolved findings at every severity, the controlled-test evidence chain, platform-runtime limitations, and the required approval marker. Its final validation-template convergence section supersedes the earlier runtime identities: the reviewed current 22-file runtime is 194,811 bytes with ordinal manifest SHA-256 `3ad579836b04df239f0a781b3064b07adb8093f510cc477297a4f540666afaf3`. Five template-only changes constrained every S/D/C/E result placeholder to the canonical enum plus rationale. Independent revision-impact review found no query, source, behavior or oracle change, so the cumulative `S` and `D` decisions remain supported while `C` and `E` remain `NOT RUN`. Final QA records the final administrative package identity so this file does not make a self-referential claim.

A supplemental `gpt-5.4-mini` stress probe stayed safe but omitted part of the expected API-verification plan in `XQL-ADVRS-02`; it is a model-variance non-certification. The controlling `gpt-5.6-sol` high-reasoning rerun passed the complete rubric. Neither result establishes ChatGPT, Claude, automatic Codex discovery, or Cortex tenant behavior.

## Required release checklist

- [x] Standalone file-level functionality verified
- [x] `SKILL.md` reviewed
- [x] References reviewed
- [x] Official documentation mapped
- [x] Examples reviewed
- [x] Controlled tests executed and independently adjudicated
- [x] Hallucination audit completed
- [x] Security review completed
- [x] Product boundaries verified
- [x] Deprecated behavior checked
- [x] ChatGPT static compatibility reviewed; runtime `NOT RUN`
- [x] Codex static compatibility and tests-free manual-load smoke reviewed; automatic discovery `NOT RUN`
- [x] Claude-style static compatibility reviewed; runtime `NOT RUN`
- [x] No mandatory sibling dependencies
- [x] No broken internal references
- [x] No unresolved `BLOCKER` issues
- [x] No unresolved `CRITICAL` issues
- [x] No unresolved `HIGH` issues

Checked platform items mean that the stated static boundary was reviewed, not that runtime execution occurred. ChatGPT runtime, Claude runtime, Codex automatic discovery, tenant compilation, and tenant execution remain explicitly `NOT RUN`.

## Tenant validation record schema

Future validation evidence must record:

- product, deployment, version/build, license/edition, and execution surface;
- tenant alias rather than a secret or sensitive identifier;
- reviewer and UTC timestamp;
- user/API identity role and data scope;
- dataset, fields, types, timeframe, and retention assumptions;
- exact query hash and compiler response;
- bounded execution status, row count, duration, truncation, and sanitized observations;
- false-positive/negative notes and known collection gaps;
- artifact location, integrity hash, and retention policy.

Use [templates/tenant-validation.md](templates/tenant-validation.md) when such evidence becomes available. Until then, keep tenant-dependent statuses `NOT RUN`.
