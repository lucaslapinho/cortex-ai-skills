# Compatibility review

**Repository version:** `0.1.0`  
**Evidence snapshot:** 2026-09-06 completion; 2026-09-04 historical baseline  
**Scope:** static packaging, isolation and documented host-surface requirements for all seven Skills  
**Reviewer boundary:** independent compatibility review; host loading, discovery and behavior are separate evidence

## Verdict

`PASS` for static publication and runtime-package compatibility. Every Skill can be constructed as an oracle-free standalone runtime with no broken or out-of-package dependency. This result does not claim that any host loaded, discovered or behaviorally executed every Skill.

## Runtime-package boundary

Install a selected Skill by constructing a separate runtime directory containing only:

- `SKILL.md`;
- `VERSION`;
- `agents/`;
- `references/`;
- `templates/`; and
- `examples/`.

Do not expose `README.md`, `CHANGELOG.md`, `VALIDATION.md`, `tests/`, scorer material, prior outputs, root research/reviews or sibling Skills to the forward model. The repository checkout is a publication tree, not an automatic-discovery tree.

The combined runtime boundary contains 153 files and 252 relative links. Independent scanning found zero broken links, zero targets outside the selected runtime, zero absolute local dependencies and zero reparse points. All seven isolated runtime packages passed the framework validator.

## Host-surface matrix

| Surface | Static packaging result | Load/upload | Discovery | Behavioral runtime | Evidence boundary |
|---|---|---|---|---|---|
| ChatGPT desktop | `PASS` - standalone runtime files and platform-neutral `SKILL.md` | `NOT RUN` | `NOT RUN` | `NOT RUN` | Use the currently supported workspace mechanism; no desktop session was exercised |
| ChatGPT web/mobile | `N/A` for this source tree - plugin package not included | `NOT RUN` | `NOT RUN` | `NOT RUN` | A plugin is a distinct package; no plugin compatibility is inferred |
| Codex CLI/IDE | `PASS` - runtime-only directory is structurally compatible with documented Skills locations | XQL: `PASS` for the separately recorded tests-free manual-load smoke; other six: `NOT RUN` | `NOT RUN` | XQL controlled evaluation is recorded separately; general host runtime `NOT RUN` | Manual load does not prove automatic discovery or transfer to another Skill |
| Claude Code | `PASS` - runtime-only directory is structurally compatible with `.claude/skills/<skill-name>/` guidance | `NOT RUN` | `NOT RUN` | `NOT RUN` | No Claude Code process was exercised |
| claude.ai | `PASS` - runtime selection is ZIP-constructible without scorer files | `NOT RUN` | `NOT RUN` | `NOT RUN` | No custom-Skill upload or code-execution session was exercised |
| Claude API | `PASS` - runtime selection is upload-constructible | `NOT RUN` | `N/A` - API uses explicit uploaded Skill identity | `NOT RUN` | No `skill_id`, code-execution container, network behavior or package installation was exercised |

Static `PASS` never promotes load, discovery or behavioral runtime to `PASS`.

## Per-Skill static result

| Skill | Runtime files | Runtime links | Validator | Standalone dependency closure | Six host surfaces documented |
|---|---:|---:|---|---|---|
| `cortex-xql-query-engineer` | 22 | included in 252 | `PASS` | `PASS` | `PASS` |
| `cortex-detection-engineer` | 22 | included in 252 | `PASS` | `PASS` | `PASS` |
| `cortex-playbook-engineer` | 20 | included in 252 | `PASS` | `PASS` | `PASS` |
| `cortex-threat-hunter` | 22 | included in 252 | `PASS` | `PASS` | `PASS` |
| `cortex-tim-engineer` | 21 | included in 252 | `PASS` | `PASS` | `PASS` |
| `cortex-platform-engineer` | 24 | included in 252 | `PASS` | `PASS` | `PASS` |
| `cortex-security-engineer` | 22 | included in 252 | `PASS` | `PASS` | `PASS` |

Each Skill README explicitly distinguishes ChatGPT desktop, ChatGPT web/mobile plugin packaging, Codex CLI/IDE, Claude Code, claude.ai and Claude API: 42/42 required matrix rows were present. Across the seven Skill READMEs, 34 relative links resolved with zero failures.

## Metadata and discovery semantics

All seven `agents/openai.yaml` files are optional OpenAI UI, invocation-policy and dependency metadata. They are not the source of Skill discovery or implicit task matching. Those behaviors derive from `SKILL.md` frontmatter, especially `name` and `description`, subject to the current host's documented mechanism.

The runtime contains no core `$cortex-*` selector dependency. A README may show host-specific invocation examples, but another host can expose a different selector or use natural capability matching.

## Official compatibility baselines

The review used current primary documentation at the snapshot date:

- [OpenAI Build skills](https://learn.chatgpt.com/docs/build-skills)
- [OpenAI Codex Skills](https://developers.openai.com/codex/skills)
- [Claude Code Skills](https://code.claude.com/docs/en/skills)
- [Anthropic Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)

Host packaging and discovery mechanisms can change. Reopen the relevant official page immediately before distribution.

## Findings and closure

| ID | Discovery severity | Finding | Remediation and retest | Final status |
|---|---|---|---|---|
| `CP-001` | `HIGH` | README wording could cause installation of publication files and scorer oracles. | Root and all seven Skill READMEs now instruct construction of the six-part runtime-only tree and explicitly exclude tests and publication records. Runtime closure retest passed. | `CLOSED` |
| `CP-002` | `MEDIUM` | Host compatibility collapsed materially different ChatGPT and Claude surfaces. | All seven matrices now contain the six required host rows with static/load/discovery/runtime boundaries. Independent count: 42/42. | `CLOSED` |
| `CP-003` | `MEDIUM` | Required root review artifacts and synchronized ledgers were absent during the first pass. | The stricter pre-Astra scan found eleven residual compact or rationale-free S/D/C/E outputs. Corrections and later Astra deltas are independently reviewed; final runtime/publication identities and ledgers are synchronized. | `CLOSED` |
| `CP-004` | `LOW` | `agents/openai.yaml` could be read as the source of discovery and implicit matching. | Every README now calls it optional UI/invocation-policy/dependency metadata and assigns discovery/matching to `SKILL.md`. | `CLOSED` |

## Residual limitations

- ChatGPT loading and behavioral runtime remain `NOT RUN`.
- Codex automatic discovery remains `NOT RUN`; only XQL has a separately recorded manual-load smoke result.
- Claude Code discovery/loading and claude.ai/Claude API upload/runtime remain `NOT RUN`.
- Linux and macOS execution were not performed; the static build audit ran on Windows.
- Static compatibility cannot prove identical instruction-following across models, hosts or future versions.
- No Cortex tenant behavior follows from host-package compatibility.

Unresolved findings: `BLOCKER 0; CRITICAL 0; HIGH 0; MEDIUM 0; LOW 0`.

## Astra compatibility completion

Current OpenAI and Anthropic primary host pages were reopened on September 6. The six-surface static matrix remains applicable. The 23 controlled outputs in [Astra review](astra-review.md) now cover all seven Skills by manual inline runtime load in ephemeral CLI processes; this does not establish file-based discovery, desktop upload, Claude execution, or general host equivalence. The blocked Playbook file-read setup is retained as NOT RUN, not a successful native load.

The offline packager selects only each Skill's six-part runtime, excludes tests and publication/review material, and refuses overwrites and source-tree output destinations. The seven unit tests and independent tooling review pass. The independent final synchronization reviewer confirmed all seven runtime/publication identities, all 23 final evidence headers and the stated compatibility boundaries. Final synchronization QA: PASS.

COMPATIBILITY REVIEW: PASS
