# Independent release review — 0.1.1

Review date: **2026-10-23**. Distribution: `cortex-ai-skills-plugin-0.1.1.zip`.

## Retained artifact

- 440,288 bytes; SHA-256 `de85688224c01a32f59d49fbb3aa6dae72ba13503ef50e6146344db56ac646ea`.
- Independent ZIP read/CRC: PASS.
- One root compatibility manifest, seven Skills, 163 unique regular members: PASS.
- Seven frontmatters and seven actual adapter YAML mappings: PASS.
- All 160 runtime files match canonical source bytes: PASS.
- All 523 local references/anchors resolve within the owning Skill: PASS.
- No scorer, repository-level research, prior evidence, or nested ZIP members: PASS.
- Seven standalone ZIPs match plugin runtime resources: PASS.
- Independent full rebuild reproduces eight ZIPs, manifest and checksums byte for byte: PASS.
- Historical eight 0.1.0 ZIP sizes, hashes and CRC match preserved manifest; no changes under that directory: PASS.

The packaging reviewer did not author the builder, tests, manifest, or assets. The same reviewer authored two domain refreshes; those content changes were reviewed independently by another reviewer and were not self-graded in this packaging pass.

## Development findings and disposition

| Finding | Severity | Disposition |
|---|---|---|
| Permissive SemVer prerelease/build components | MEDIUM | Closed: strict identifiers plus regression cases; independent malformed-version reruns rejected them |
| ZIP filename truncation/normalization before validation | MEDIUM | Closed: inspect original filenames before normalized spelling; NUL/backslash/duplicate path regressions passed |
| New guidance lacked directly relevant authored scenarios | MEDIUM | Closed for coverage presence: three separate October scorer cases added; behavior remains NOT RUN |
| Source README version and plugin availability text stale | LOW | Closed in coordinated documentation update |
| Root wording ambiguously excluded all source registers | LOW | Closed: Skill-local official registers are explicitly included |

No unresolved BLOCKER, CRITICAL, HIGH or MEDIUM finding remains in the inspected packaging/source-refresh scope.

## Domain/source review

A reviewer independent of the XQL/Detection/Hunting author checked their new official-source claims and metadata. Another reviewer independently reopened the Playbook/TIM/Platform/Security claims. The retained discrepancies and product boundaries were supported within the stated scope.

These are documentation and source reviews, not fresh behavioral passes. The three new scorer scenarios and revised Skills' controlled S evaluation remain NOT RUN. C/E tenant levels remain NOT RUN.

## Executed local checks

- Plugin regression suite: **19/19 PASS**.
- Existing publication tests: **6/6 PASS**.
- Existing source tooling tests: **7/7 PASS**.
- Current source structural audit and publication verification: PASS.
- Seven Skill quick validators: PASS (domain authors' scoped runs).
- Later root-operated account test: import accepted, installation completed, and seven names listed after explicit user confirmation. The independent ZIP review predates that UI action; see the separate [UI record](plugin-ui-test.md).

The exact import/discovery/behavior limits remain in [validation](validacao.md). No public directory submission or tenant test follows from this record.
