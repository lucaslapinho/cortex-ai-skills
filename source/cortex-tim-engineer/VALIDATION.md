# Validation ledger

## Current completion decision — 2026-09-06

**Current reviewed runtime:** 21 files / 126,788 bytes; ordinal SHA-256 `e2e49820268e45ee8017ce67d397cb73d9d08cdfd80fc7dc9b16e1f58b2de0fb`.

**Decision:** source/runtime-package completion PASS after independent Astra delta review and fresh individual-case evaluation. This section supersedes candidate/pending wording below for this exact snapshot; historical records and failures remain unchanged.

| Level | Current scoped result | Rationale |
|---|---|---|
| S | PASS — 5/37 cumulative; 32 NOT RUN | 3 fresh individual Astra cases passed, plus 2 identified historical decisions retained only through independent revision-impact review; not 37 new Astra runs |
| D | PASS — scoped dated source evidence | Historical September 4 register plus actual September 6 claim-level rechecks; no assertion that every source was reopened on September 6 or that the offline forward performed a fresh D check |
| C | NOT RUN — 37/37 | No named tenant compiler, schema acceptance or controlled import |
| E | NOT RUN — 37/37 | No tenant execution, deployment, result, efficacy or recovery observation |

Fresh final cases: `TIM-A03`, `TIM-A04`, `TIM-R07`. Each received only the runtime files and its Fixture/Prompt in one new ephemeral Astra process; zero tool/action events were observed. Independent reviewers compared the complete retained responses against the applicable oracles; the model did not award its own S pass. Earlier multi-case exploratory batches do not add coverage. Historical raw responses were not all available to rescore and are not described as new runs.

The full-source repository retains the independent Astra domain reviews and response records under reviews; those development artifacts are optional audit material and are excluded from this Skill's runtime. The standalone package carries this scoped decision and exact identity without requiring those root files to function. All runtime/publication links, metadata, UTF-8, test-case structure, and the 18-item checklist passed the final static audit. No unresolved publication finding remains in the reviewed scope; known tenant/host/source-drift limits are retained below.


**Skill version:** `0.1.0`  
**Evidence snapshot:** 2026-09-04  
**Reviewed runtime:** 21 files / 122,561 bytes; ordinal SHA-256 `d49133470ad4d78fe942db1aad61fd6310332ea215b67b9ff274156400637eb4`  
**Ledger status:** independent technical, Platform-domain, adversarial, security, final hallucination/source delta and static compatibility review complete

This ledger distinguishes file-level checks, selected controlled behavior, current documentation and unavailable tenant evidence.

## Astra revision — 2026-09-06

**Candidate runtime:** 21 files / 126,788 bytes; ordinal SHA-256 `e2e49820268e45ee8017ce67d397cb73d9d08cdfd80fc7dc9b16e1f58b2de0fb`. The hash uses ordinal POSIX relative paths, lowercase per-file SHA-256, two spaces, LF-separated records, UTF-8, and no terminal newline.

This revision supersedes the runtime binding above pending independent review of the revised files. Historical selected-case passes remain traceable but must not be promoted automatically to changed prompts or behavior.

| Level | Revised-content result | Rationale |
|---|---|---|
| S | NOT RUN | Consumer-confinement guidance, distribution and OpenCTI examples, the distribution template, and A03/A04/R07 changed; no new independent response evaluation is asserted. |
| D | PASS | I02 and I07-I10 were re-opened on 2026-09-06. Five-source targeted verification supports the affected integration and deprecation claims; it is not a new 32-source review. |
| C | NOT RUN | No tenant integration, schema, or consumer configuration was available. |
| E | NOT RUN | No feed, service, negative-access request, control action, or rollback was executed. |

Static checks and final independent decisions must bind to the newly calculated runtime hash. The remainder of this ledger records the earlier snapshot until that binding is updated.

Local revision checks passed: framework quick validation; strict UTF-8; balanced Markdown fences; 52 local file links; and 37 unique authored cases. These are structural author checks, not new independent S results. No file was added or removed.

## Validation levels

| Level | Meaning | Current result | Rationale |
|---|---|---|---|
| `S` | Controlled oracle-isolated response evaluation | `PASS` - 3 selected; 34 `NOT RUN` | Independent reviewers retained current `TIM-A04` and `TIM-T02` by scoped revision impact, then reran and passed oracle-isolated `TIM-T03` against this exact runtime; that response explicitly kept TAXII collection/query wording XSOAR-scoped and XSIAM selection semantics `UNVERIFIED`; older A03/B02/I02 results do not bind to this runtime |
| `D` | Current official-document support for material factual claims | `PASS` - 32/32-source register | Independent technical review rechecked all URLs plus the corrected X02/X16 attribution and I02-I04/I10 product wording; 6/6 Platform-relevant pages remain rechecked for `TIM-T03` |
| `C` | Named configuration/schema/import or product validation | `NOT RUN` - 37/37 | No tenant, integration inventory, schema or configuration target was available |
| `E` | Fetch, enrichment, lifecycle, export, enforcement or production observation | `NOT RUN` - 37/37 | No integration, consumer or downstream control was executed |

The evaluated model did not self-award `S`; selected `PASS` decisions are independent adjudications and do not imply full-suite coverage.

## Package and author checks

| Check | Result | Claim boundary |
|---|---|---|
| Required publication paths | `PASS` - 32 non-empty files | Presence only |
| Skill frontmatter and adapter YAML | `PASS` - framework validator and YAML parse | Metadata structure only |
| Markdown links, anchors and fences | `PASS` - local targets resolve; fences balanced | Navigation/structure only |
| Secrets, fixed paths and reparse points | `PASS` - no configured high-signal finding | Cannot prove absence of every semantic secret |
| Runtime isolation | `PASS` - 21 files; no root/sibling/scorer dependency | File autonomy, not host runtime |
| Test catalog | `PASS` - 37 unique cases with all six required sections | Authored oracle completeness only |
| Official URL reachability | `PASS` - 32/32 at snapshot | Reachability is not semantic applicability or tenant support |

## Independent review gates

| Review | Result | Evidence boundary |
|---|---|---|
| Technical accuracy | `PASS` - zero open findings | Current sources, documented `indicators` dataset name, integration-specific fetch-history evidence boundary, and XSOAR-scoped TAXII/OpenCTI wording without XSIAM transposition |
| Platform-domain cross-review | `PASS` - rerun `TIM-T03` | Oracle-isolated response on the reviewed runtime separated hosting, engine, network/TLS/auth, product-scoped selection/content, consumer retrieval and enforcement |
| Distribution/lifecycle review | `PASS` - `TIM-A04`, `TIM-T02` | Successor/deprecation and expiration/removal boundaries |
| Security and adversarial | `PASS` - zero open findings | Secrets, unsafe blocks, TLS, reset and fabricated API controls |
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
- [x] Selected controlled tests executed and independently adjudicated; 34 remain `NOT RUN`
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

- No live tenant, installed-integration inventory, schema validation, import, fetch, enrichment, distribution, deployment, downstream enforcement, production-volume test or measured performance evidence exists.
- TAXII, STIX, MISP, OpenCTI and EDL-related behavior remains product/version/integration scoped.
- A served feed does not prove consumer retrieval or enforcement.
- Host loading, discovery and behavioral equivalence remain `NOT RUN`.

## Future tenant evidence record

Record product/deployment/version/license, integration and content-pack versions, tenant alias, role, direction, source/destination, instance and engine placement, authentication method without secrets, input hash/count/timeframe, mappings/markings, exact artifact hash, before state, observed result/errors/counts/timing, duplicate/score/enrichment/relationship/expiration/exclusion behavior, consumer readback, enforcement state, rollback, reviewer and retained sanitized evidence.
