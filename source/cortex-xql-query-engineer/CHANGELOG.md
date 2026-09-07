# Changelog

### Independent Astra oracle reconciliation — 2026-09-06

- Aligned XQL-REG-07 expected observations with the already-recorded real-time-action documentation discrepancy. Fixture, prompt, runtime and prohibited behaviors are unchanged; independent rescoring uses the retained response.

All notable changes to this Skill are recorded here. Versions follow semantic versioning independently from other Skills in the repository.

## Astra completion delta — 2026-09-06 (0.1.0 candidate)

- Read all 33 package files afresh; previous approvals were not treated as proof of content quality.
- Added equal-time dedup retention checks and strengthened existing `XQL-ADV-02`/`XQL-REG-05` without adding cases; clarified official deprecation evidence.
- Reopened key language and rule sources; preserved regextract, dedup example/type and migrated real-time-action discrepancies.
- Preserved historical evaluation identities separately from the changed candidate. No new independent `S` or tenant `C/E` pass is claimed by this author-side delta.

## [0.1.0] — 2026-09-04

### Added

- Standalone behavioral core for XSIAM and XDR XQL construction, review, explanation, troubleshooting, and optimization.
- Canonical primary statuses, provenance/tenant qualifiers, and independent S/D/C/E validation results.
- Product and execution-surface gates for Query Center, API-started queries, BIOC, scheduled correlation, real-time correlation, and XQLp.
- Current-official source index, language/schema references, templates, realistic examples, and behavior-focused test cases.
- Anti-hallucination controls for fabricated datasets, fields, functions, APIs, and hostile embedded instructions.
- Honest validation ledger separating static review from tenant schema, compilation, execution, and operational evidence.

### Corrected and revalidated

- Hardened unverified API handling so supplied endpoints or payloads are never reproduced as executable requests before the official contract, product/version, authorization, polling, terminal/error/cancellation, and quota behavior are verified.
- Hardened comment and product-surface inference: query text, comments, datasets, and snapshots cannot establish portable XSIAM/XDR syntax or target context by themselves.
- Independently reran the affected adversarial and regression cases against the current oracle-free runtime, recorded superseding hashes, and retained the original Golden history plus model-variance limitation.
- Removed the competing executability shorthand vocabulary, converged all runtime guidance and examples on the frozen canonical taxonomy, and independently reran basic, intermediate, and advanced taxonomy cases against the superseding runtime.
- Constrained every S/D/C/E template result to `PASS`, `FAIL`, `NOT RUN`, or `N/A` plus an explicit rationale; independent revision-impact review confirmed that query behavior, sources and the Golden test chain were unchanged.
- Expanded the four explicit example validation blocks from compact summaries into level-specific canonical results with rationale; query text, sources, expected output, and test oracles were unchanged.
- Normalized punctuation that prevented the framework validator from reading the UTF-8 Skill under the Windows locale-default Python mode; both native and explicit UTF-8 validation now pass.

### Known limitations

- No live Cortex tenant, schema export, Query Center compiler, correlation-rule editor, BIOC editor, XQLp validator, or production observation was available.
- Official documentation contains a version-sensitive conflict for `regextract()` return shape; the Skill intentionally does not normalize it.
- Product features, limits, licenses, permissions, and schemas can drift after the 2026-09-04 review snapshot.

The release remains `0.1.0`, not `1.0.0`, because these tenant-dependent and cross-platform runtime validations are material and incomplete.
