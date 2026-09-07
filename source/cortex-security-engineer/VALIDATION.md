# Validation ledger

## Current completion decision — 2026-09-06

**Current reviewed runtime:** 22 files / 124,841 bytes; ordinal SHA-256 `e5742a5500c39a874b5d68f5ac83679ab74a56efd86e088c6a48cf8110355a8d`.

**Decision:** source/runtime-package completion PASS after independent Astra delta review and fresh individual-case evaluation. This section supersedes candidate/pending wording below for this exact snapshot; historical records and failures remain unchanged.

| Level | Current scoped result | Rationale |
|---|---|---|
| S | PASS — 6/41 cumulative; 35 NOT RUN | 3 fresh individual Astra cases passed, plus 3 identified historical decisions retained only through independent revision-impact review; not 41 new Astra runs |
| D | PASS — scoped dated source evidence | Historical September 4 register plus actual September 6 claim-level rechecks; no assertion that every source was reopened on September 6 or that the offline forward performed a fresh D check |
| C | NOT RUN — 41/41 | No named tenant compiler, schema acceptance or controlled import |
| E | NOT RUN — 41/41 | No tenant execution, deployment, result, efficacy or recovery observation |

Fresh final cases: `SEC-REG-07`, `SEC-INT-03`, `SEC-TRB-04`. Each received only the runtime files and its Fixture/Prompt in one new ephemeral Astra process; zero tool/action events were observed. Independent reviewers compared the complete retained responses against the applicable oracles; the model did not award its own S pass. Earlier multi-case exploratory batches do not add coverage. Historical raw responses were not all available to rescore and are not described as new runs.

The full-source repository retains the independent Astra domain reviews and response records under reviews; those development artifacts are optional audit material and are excluded from this Skill's runtime. The standalone package carries this scoped decision and exact identity without requiring those root files to function. All runtime/publication links, metadata, UTF-8, test-case structure, and the 18-item checklist passed the final static audit. No unresolved publication finding remains in the reviewed scope; known tenant/host/source-drift limits are retained below.


**Skill version:** `0.1.0`  
**Evidence snapshot:** 2026-09-04  
**Historical reviewed runtime (2026-09-04):** 22 files / 121,025 bytes; ordinal SHA-256 `8615e52088137868fea2c7bd2d07b699b3fe8764ca6b64ca1d6bbb843e38a4d1`  
**Ledger status:** historical independent review retained; Astra refinement below awaits independent delta evaluation

This record separates standalone cross-domain decision quality from tenant facts and operations. The primary author did not approve this Skill.

## Validation levels

| Level | Meaning | Current result | Rationale |
|---|---|---|---|
| `S` | Controlled oracle-isolated response evaluation | `PASS` - 4 selected; 37 `NOT RUN` | Independent reviewers passed `SEC-BAS-01`, `SEC-INT-01`, `SEC-INT-03` and `SEC-ADV-02`; reverse reconstruction proved the final conceptual-example validation expansion formatting-only |
| `D` | Current official-document support for material factual claims | `PASS` - 27/27-source register | Independent technical review checked the dated register and rechecked the corrected direct XSOAR and Runtime Security sources; deliberately conceptual selected cases may individually be `N/A` |
| `C` | Non-production tenant compiler/editor/import acceptance | `NOT RUN` - 41/41 | No named tenant, schema, editor or import surface was available |
| `E` | Non-production tenant execution or state change | `NOT RUN` - 41/41 | No query, rule, playbook, integration, API, TIM or response action was executed |

The model's own S/D/C/E rows are non-claims. Independent scorers assign the selected `S: PASS` results; no full-suite or tenant claim follows.

## Package and author checks

| Check | Result | Claim boundary |
|---|---|---|
| Required publication paths | `PASS` - 33 files present | Presence only |
| Skill frontmatter and adapter YAML | `PASS` - framework validator and YAML parse | Metadata structure only |
| Markdown links and fences | `PASS` - local targets resolve; fences balanced | Navigation/structure only |
| Secrets, local paths and reparse points | `PASS` - no configured high-signal finding | Cannot prove absence of every semantic secret |
| Runtime isolation | `PASS` - 22 files; no mandatory root/sibling/scorer dependency | Optional handoffs retain standalone fallback |
| Test catalog | `PASS` - 41 unique cases with all six required sections | Authored oracle completeness only |
| Official URL reachability | `PASS` - 27/27 at snapshot | Reachability is not semantic applicability |

## Independent review gates

| Review | Result | Evidence boundary |
|---|---|---|
| Skill Architecture | `PASS` - `SEC-BAS-01`, `SEC-INT-01`, `SEC-ADV-02` | Standalone packets, routing and optional specialist handoffs |
| Technical accuracy and XQL domain | `PASS` - `SEC-BAS-01`, `SEC-INT-03` | Query fallback stays conceptual/tenant-unverified and does not fabricate syntax |
| Platform Specialist | `PASS` - `SEC-INT-01` | Complete telemetry/data-readiness contract |
| Threat Hunting Specialist | `PASS` - `SEC-ADV-02` | Hypothesis, coverage, benign alternatives, enrichment and action gate |
| Adversarial/security | `PASS` - zero open findings | Fabricated features/APIs, injection, credentials, forced attestation, canonical validation output and unsafe containment |
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
- [x] Selected controlled tests executed and independently adjudicated; 37 remain `NOT RUN`
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

## Residual limitations

- Current documentation is a dated snapshot and can change by product, release, entitlement and rollout.
- No tenant dataset, field, API schema, license, role, object access, integration command, configuration, Case, query, rule, indicator, playbook or result was inspected.
- Examples are conceptual decision artifacts and intentionally omit specialized executable syntax.
- Cross-platform loading, discovery and behavioral equivalence remain `NOT RUN`.

## Future tenant evidence record

Record target product/deployment/version/license, tenant alias, accountable owner and approver, identity/role/SBAC, objective and behavior hypothesis, source health, schema/types, grain, time semantics, coverage/freshness/retention, parser/mapping, null/population checks, entity/identity resolution, privacy, known controls, exact artifact hashes, product validation, bounded execution, readback, recovery and retained sanitized evidence. Keep `C` and `E` as `NOT RUN` until such evidence exists.

## Astra refinement — 2026-09-06

**Candidate runtime:** 22 files / 123,975 bytes; ordinal SHA-256
`c31a7a8b4813d716abd11d25f827b71182151be146b242715c21ea03496d493a`.
Recipe: sort relative POSIX paths ordinally, serialize each lowercase file SHA-256
plus two spaces plus its path, join with LF without a terminal LF, encode UTF-8,
then hash that byte sequence.

All 33 publication files, including 22 runtime files and all 41 authored cases,
were read again. Prior approvals were inspected as history, not as proof of the
new candidate. The refinement adds the XSIAM Datasets Rows/XDM routing branch,
restores N/A in the validation-record enum, and corrects neutral-invocation and
validation-result oracle inconsistencies. Existing SEC-REG-07 was strengthened;
the catalog still contains 41 cases.

| Level | Delta result | Rationale |
|---|---|---|
| S | `NOT RUN` | No isolated forward response has been scored for this refinement; the four historical selected results remain scoped to their prior runtime/oracles |
| D | `PASS` | The exact current Manage user access page was reopened for the XDM limitation; O11, O17, O20, O21 and O23 were also reopened for their scoped permission, component and target-stage claims, without redating the whole register |
| C | `NOT RUN` | No target tenant/editor/API accepted a control artifact |
| E | `NOT RUN` | No query, permission change, rule, playbook or response was executed |

Independent technical, security, and behavioral delta review must bind to the new
runtime before publication is reaffirmed. The historical checklist and source
counts above describe the earlier snapshot, not a new full-suite run.

Local checks: framework quick validator `PASS`; the repository's offline audit
reported `PASS`, 253 authored cases, and no UTF-8, fence, local-link/anchor,
runtime/scorer-path, required-file, or case-schema errors at this check. These are
structural checks, not isolated S evaluations or host/tenant execution.
