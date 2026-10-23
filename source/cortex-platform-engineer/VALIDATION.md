# Validation ledger

## Current documentation refresh — 2026-10-23

**Skill version:** `0.1.1`. The [dated source review](references/2026-10-23-refresh.md)
identifies seven reopened pages and the bounded claims reviewed. The runtime gains
that reference and a source-register link; the operating contract, examples,
templates, and tests are unchanged. Earlier counts, hashes, approvals, and passes
below describe `0.1.0` only and are not current-runtime attestations.

| Level | Refresh result | Scope |
|---|---|---|
| S | `NOT RUN` | No new isolated controlled behavioral response was evaluated. |
| D | `PASS` | The dated reference records exact source checks and the unresolved Case artifacts HTTP-method discrepancy; other register rows retain their prior dates. |
| C | `NOT RUN` | No host import, tenant editor, schema, or API acceptance was exercised. |
| E | `NOT RUN` | No tenant execution, data-path test, deployment, or recovery was exercised. |

Local metadata and package checks are reported separately from these levels by the
distribution validation. Plugin import, skill discovery, and host behavior remain
unverified until the exact distribution is tested in the target account.

## Historical completion decision — 2026-09-06

**Current reviewed runtime:** 24 files / 150,595 bytes; ordinal SHA-256 `3960f33a98b7de1044d06ffac9f18adec15edce6b4e0425be362376642bebb8c`.

**Decision:** source/runtime-package completion PASS after independent Astra delta review and fresh individual-case evaluation. This section supersedes candidate/pending wording below for this exact snapshot; historical records and failures remain unchanged.

| Level | Current scoped result | Rationale |
|---|---|---|
| S | PASS — 2/41 cumulative; 39 NOT RUN | 1 fresh individual Astra cases passed, plus 1 identified historical decisions retained only through independent revision-impact review; not 41 new Astra runs |
| D | PASS — scoped dated source evidence | Historical September 4 register plus actual September 6 claim-level rechecks; no assertion that every source was reopened on September 6 or that the offline forward performed a fresh D check |
| C | NOT RUN — 41/41 | No named tenant compiler, schema acceptance or controlled import |
| E | NOT RUN — 41/41 | No tenant execution, deployment, result, efficacy or recovery observation |

Fresh final cases: `PLAT-REG-08`. Each received only the runtime files and its Fixture/Prompt in one new ephemeral Astra process; zero tool/action events were observed. Independent reviewers compared the complete retained responses against the applicable oracles; the model did not award its own S pass. Earlier multi-case exploratory batches do not add coverage. Historical raw responses were not all available to rescore and are not described as new runs.

The full-source repository retains the independent Astra domain reviews and response records under reviews; those development artifacts are optional audit material and are excluded from this Skill's runtime. The standalone package carries this scoped decision and exact identity without requiring those root files to function. All runtime/publication links, metadata, UTF-8, test-case structure, and the 18-item checklist passed the final static audit. No unresolved publication finding remains in the reviewed scope; known tenant/host/source-drift limits are retained below.


**Skill version:** `0.1.0`  
**Evidence snapshot:** 2026-09-04  
**Historical reviewed runtime (2026-09-04):** 24 files / 145,375 bytes; ordinal SHA-256 `17a3babdadf9c7e65497a0389efbda8d15e92be46b49a9946d74d7da29276cfc`  
**Ledger status:** historical independent review retained; Astra refinement below awaits independent delta evaluation

This ledger separates architecture quality and current documentation from tenant configuration, compilation/import and end-to-end execution.

## Validation levels

| Level | Meaning | Current result | Rationale |
|---|---|---|---|
| `S` | Controlled oracle-isolated response evaluation | `PASS` - 1 selected; 40 `NOT RUN` | Independent Architecture cross-review passed `PLAT-BAS-02`; reverse reconstruction proved the final API-verdict expansion formatting-only; author observations are not counted |
| `D` | Current official-document support for material factual claims | `PASS` - 45/45 current sources | Independent review also bounded 2/2 retiring pages as historical pointers; 47/47 registered URLs were reachable |
| `C` | Non-production parser/editor/import/API validation | `NOT RUN` - 41/41 | No named tenant, configuration, parser, editor, import surface or API contract was exercised |
| `E` | Non-production end-to-end execution | `NOT RUN` - 41/41 | No controlled event traversed a live collection-to-query path |

The selected `S: PASS` is an independent reviewer decision. It does not convert the other 40 cases or any tenant level into `PASS`.

## Package and author checks

| Check | Result | Claim boundary |
|---|---|---|
| Required publication paths | `PASS` - 35 non-empty files | Presence only |
| Skill frontmatter and adapter YAML | `PASS` - framework validator and YAML parse | Metadata structure only |
| Markdown links, anchors and fences | `PASS` - local targets resolve; fences balanced | Navigation/structure only |
| Secrets, absolute paths and reparse points | `PASS` - no configured high-signal finding | Cannot prove absence of every semantic secret |
| Runtime isolation | `PASS` - 24 files; no root/sibling/scorer dependency | File autonomy, not host runtime |
| Reference navigation | `PASS` - all long references have contents navigation | Navigation only |
| Test catalog | `PASS` - 41 unique cases with all six required sections | Authored oracle completeness only |
| Official URL reachability | `PASS` - 47/47 at snapshot | Reachability is not semantic applicability |

## Independent review gates

| Review | Result | Evidence boundary |
|---|---|---|
| Architecture Researcher | `PASS` - `PLAT-BAS-02` | Agent, Broker VM, XDR Collector and Cortex Engine remain distinct |
| Technical accuracy and official evidence | `PASS` - zero open findings | 45 current sources plus 2 bounded historical pointers |
| Data-flow and access controls | `PASS` - zero open findings | Collection, ingestion, parsing, mapping, RBAC/SBAC and failure-layer separation |
| Adversarial/security | `PASS` - zero open findings | Credentials, hostile logs, fabricated APIs/health, canonical validation output and destructive repairs |
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
- [x] Selected controlled test executed and independently adjudicated; 40 remain `NOT RUN`
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

- No live Cortex tenant, configuration export, license inventory, tenant schema, API session, collector, agent, Broker VM, Cortex Engine, parser compiler or production observation was available.
- No configuration was imported, applied, deployed or rolled back.
- Product features, fields, limits, ports, roles, datasets and UI paths can drift after the snapshot.
- Current product-scoped Cortex Engine documentation must be reopened for the target XSIAM, XDR, XSOAR SaaS or XSOAR On-prem deployment; retiring pages are history only.
- Host loading, discovery and behavioral equivalence remain `NOT RUN`.

## Future tenant evidence record

Record product/deployment/version/build/license, tenant alias, environment/time, reviewer/change owner/approver, identity role and SBAC scope, exact component and sanitized configuration hash, expected source event, collection/transport/ingestion evidence, raw object, parser/mapping version, normalized schema, retention, query timeframe/result, bounded execution/errors/duplicates/delays/partial failures, rollback trigger/evidence and audit location. Until then, `C` and `E` remain `NOT RUN`.

## Astra refinement — 2026-09-06

**Candidate runtime:** 24 files / 150,236 bytes; ordinal SHA-256
`3d513be544dd6d7cf89de52856f6f2ab714c89a3ecef84d812dcd7fbd3cbe38b`.
Recipe: sort relative POSIX paths ordinally, serialize each lowercase file SHA-256
plus two spaces plus its path, join with LF without a terminal LF, encode UTF-8,
then hash that byte sequence.

All 35 publication files, including 24 runtime files and all 41 authored cases,
were read again. Prior approvals were inspected as history, not as proof of the
new candidate. The refinement adds the XSIAM Datasets Rows/XDM diagnostic branch
and corrects two example-index evidence descriptions. PLAT-REG-08 was strengthened;
the catalog still contains 41 cases.

| Level | Delta result | Rationale |
|---|---|---|
| S | `NOT RUN` | No isolated forward response has been scored for this refinement; historical PLAT-BAS-02 remains scoped to its prior runtime |
| D | `PASS` | The exact current Manage user access page was reopened for the new XDM and dataset-access-management claims; 10 other registered source rows were reopened for their scoped existing claims, without redating the whole register |
| C | `NOT RUN` | No target tenant/query editor/API accepted an artifact |
| E | `NOT RUN` | No tenant query, permission change, ingestion or response was executed |

Independent technical, security, and behavioral delta review must bind to the new
runtime before publication is reaffirmed. The historical checklist and source
counts above describe the earlier snapshot, not a new full-suite run.

Local checks: framework quick validator `PASS`; the repository's offline audit
reported `PASS`, 253 authored cases, and no UTF-8, fence, local-link/anchor,
runtime/scorer-path, required-file, or case-schema errors at this check. These are
structural checks, not isolated S evaluations or host/tenant execution.
