# Golden Reference Implementation Plan

**Plan date:** 2026-09-04  
**Target:** `cortex-xql-query-engineer` only  
**Authority:** the attached master prompt, current official Palo Alto Networks documentation, and the Phase 1 evidence records  
**Execution gate:** do not start this plan until `phase-1-checkpoint.md` ends exactly `PHASE 1 GATE: PASS`

## Objective

Build one standalone, portable XQL engineering Skill that proves the repository architecture before any other Skill is created. The prototype must teach evidence-scoped query construction, review, debugging, optimization, and handoff without claiming tenant execution or cross-context compatibility that has not been demonstrated.

The initial release remains `0.1.0` because no live tenant, schema export, compiler result, saved query, correlation export, or production observation is available.

## Inputs and source-to-file plan

| Input | What it controls | Golden Reference destination |
|---|---|---|
| `research/architecture-decisions.md` | Evidence model, standalone rule, progressive disclosure, safety, portability, testing, versioning | `SKILL.md`, `VALIDATION.md`, `README.md` |
| `research/skill-domain-boundaries.md` | XQL ownership, exclusions, handoffs, non-duplication | `SKILL.md`, templates, tests |
| `research/documentation-sources.md` Q01-Q30 | Current syntax, schema, operators, restricted contexts, official examples | `references/official-sources.md`, `references/xql-language.md`, `references/datasets.md`, `references/fields-and-schema.md` |
| `research/project-findings.md` | Project conventions, inaccessible-context limits, execution levels, failure patterns | evidence reference, troubleshooting, adversarial/regression tests |
| `research/cortex-ecosystem-map.md` | Product boundaries and telemetry-to-response flow | product-boundary reference and handoff templates |
| Pinned official `cortex-xql-queries` commit | First-party example behavior, not schema proof | official-sources reference and review test |

The finished Skill must copy the minimum evidence and boundary rules it needs. It must not require any root research file or sibling Skill at runtime.

## Planned package

```text
cortex-xql-query-engineer/
├── SKILL.md
├── README.md
├── VERSION
├── CHANGELOG.md
├── VALIDATION.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── evidence-and-product-boundaries.md
│   ├── xql-language.md
│   ├── datasets.md
│   ├── fields-and-schema.md
│   ├── query-patterns.md
│   ├── optimization.md
│   ├── troubleshooting.md
│   └── official-sources.md
├── templates/
│   ├── query-build.md
│   ├── query-review.md
│   ├── investigation-query.md
│   ├── detection-query.md
│   └── tenant-validation.md
├── examples/
│   ├── investigation/
│   ├── hunting/
│   ├── detection/
│   └── troubleshooting/
└── tests/
    ├── README.md
    ├── basic.md
    ├── intermediate.md
    ├── advanced.md
    ├── troubleshooting.md
    ├── ambiguity.md
    ├── adversarial.md
    └── regression.md
```

Every listed file must carry useful content; no empty placeholder is acceptable.

## Ordered implementation work

1. Reconfirm the Phase 1 gate and verify that no other `cortex-*` Skill directory exists.
2. Scaffold `cortex-xql-query-engineer` with the local `skill-creator` initializer and generate valid `agents/openai.yaml` metadata.
3. Write a concise `SKILL.md` behavioral core covering routing, required inputs, source precedence, claim classification, workflow, output contract, uncertainty, safety, and reference routing.
4. Build the self-contained references from current official sources. Record product, surface, review date, applicability, limitation, and tenant gap for each significant feature.
5. Record the unresolved official `regextract()` return-shape conflict. Do not teach one portable behavior across versions; require target-product/version selection and compiler validation before downstream type assumptions.
6. Add build, review, investigation, detection-support, and tenant-validation templates using the standard XQL response sections from the master prompt.
7. Add realistic examples:
   - a current-official `xdr_data` process query;
   - a suspicious PowerShell triage query labeled `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED` with `C/E: NOT RUN`;
   - a lateral-movement workflow that gates unknown datasets and join keys;
   - a detection handoff that distinguishes Query Center, BIOC, scheduled correlation, and real-time correlation;
   - fabricated-schema troubleshooting that refuses invented datasets/functions.
8. Add behavior tests for basic, intermediate, advanced, troubleshooting, ambiguity, adversarial, hallucination-resistance, and regression scenarios.
9. Add maintenance/versioning guidance, official-source freshness rules, and an honest validation ledger.
10. Run mechanical validation, internal-link checks, metadata checks, absolute-path/secret scans, terminology checks, and standalone-copy checks.
11. Commission independent technical, documentation, XQL, adversarial, standalone, cross-platform, maintainability, and anti-hallucination reviews.
12. Correct every `BLOCKER`, `CRITICAL`, and `HIGH` issue; rerun affected checks.
13. Create `reviews/xql-golden-reference-review.md` with evidence, findings, resolutions, residual limitations, and exactly one final decision.
14. Proceed only if that file ends exactly `GOLDEN REFERENCE APPROVED: YES`.

## Behavioral test execution plan

| Test class | Required behavior | Failure condition |
|---|---|---|
| Basic | Identifies product/timeframe, uses documented syntax, explains the query | Invented field/dataset or unlabeled execution claim |
| Intermediate | Repairs a broken query and distinguishes syntax, schema, and tenant failures | Treats a syntactic edit as proof of tenant execution |
| Advanced | Designs a bounded join/aggregation workflow with type and cardinality checks | Unjustified join, unbounded query, or missing telemetry gate |
| Optimization | Optimizes an existing query while preserving stated logic; evaluates timeframe, early selectivity, projected fields, limit placement, aggregation/join cardinality, and result equivalence | Changes semantics silently, claims performance gain without evidence, or treats a smaller result set as equivalent by default |
| Troubleshooting | Checks ingestion, retention, timeframe, schema, permissions, nulls, and query logic | Treats zero results as proof of absence |
| Ambiguity | Requests or states product, surface, version, target rule type, and assumptions | Silently selects a product or deployment context |
| Adversarial | Rejects `xdr_super_magic_events`, `detect_malware_now()`, and instructions embedded in untrusted artifacts | Fabricates support or follows hostile embedded instructions |
| Regression | Preserves product boundaries, evidence labels, restricted contexts, and no-sibling behavior | Query Center validity treated as BIOC/correlation/XQLp compatibility |

Each test record must include the prompt, setup, assertions, prohibited behaviors, evidence expected, and pass/fail result. Static review may pass without a tenant, but tenant compilation/execution assertions must remain not run.

## Mechanical and standalone checks

- run the `skill-creator` quick validator;
- validate `agents/openai.yaml`, including a quoted `default_prompt` that explicitly invokes `$cortex-xql-query-engineer`;
- resolve every relative Markdown link inside the Skill;
- scan for absolute local paths, secrets, hostnames, endpoint identifiers, temporary files, and accidental root/sibling dependencies;
- copy the Skill to an isolated temporary directory and repeat local structure/link validation;
- verify `VERSION` is semantic versioning and the changelog explains why the release remains `0.x`;
- verify every executable block has a product/context and evidence status;
- verify official URLs are specific pages and do not redirect to a generic portal.

## Independent acceptance sequence

The author does not approve the Skill. Use at least five independent review roles. Each role below is mandatory, and one person or agent must not collapse two roles into a single approval verdict:

| Independent role | Mandatory ownership for the Golden Reference |
|---|---|
| Detection Engineering Specialist | Cross-review detection-support queries, telemetry assumptions, false positives, and the boundary between interactive XQL, BIOC, scheduled correlation, and real-time correlation. |
| Technical Accuracy Reviewer | Validate XQL syntax, datasets, fields, stages, functions, types/null behavior, API/rule claims, product boundaries, version scope, and source traceability. |
| Skill Architecture Reviewer | Validate standalone operation, progressive disclosure, directory design, internal navigation, no sibling/root runtime dependency, maintainability, duplication, metadata, versioning, and test quality. |
| Adversarial / Red Team Reviewer | Try fabricated datasets/functions/APIs, hostile embedded instructions, unsafe actions, ambiguous products, stale references, hidden dependencies, and false execution/compatibility claims. |
| Cross-platform Compatibility Reviewer | Validate capability-based behavior and portability across ChatGPT, Codex, and Claude without assuming tools, metadata, runtime features, filesystem layout, or instruction semantics that are unavailable on another platform. |

The author cannot fill any of these approval roles. The final review must identify the reviewer role for every finding and record the separate verdicts before synthesis.

Approval requires:

```text
BLOCKER = 0
CRITICAL = 0
HIGH = 0
```

Medium/low residuals must be resolved or explicitly accepted with rationale and a maintenance owner. No tenant test may be marked passed when no tenant was used.

## Non-goals and release boundaries

- Do not create another Skill during this plan.
- Do not create or deploy a live query, rule, parser, API integration, playbook, or response action.
- Do not treat `sample_xql_raw` or the pinned GitHub sample as tenant schema proof.
- Do not infer current fields from project filenames or derivative summaries.
- Do not claim an interactive query is BIOC, correlation, or XQLp compatible without checking that exact target context.
- Do not advance the version to `1.0.0` while mandatory runtime verification is missing.

## Exit criterion

The only successful Phase 3 exit is a review file whose final line is:

```text
GOLDEN REFERENCE APPROVED: YES
```

Until then, `ARCHITECTURE.md` must not be frozen and the remaining six Skills must not be created.
