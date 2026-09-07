# Changelog

### Independent Astra closure correction — 2026-09-06

- Separated author-side structural/link checks from independently adjudicated S in the testing reference; no product behavior, fixture or oracle changed.

All notable changes to this Skill are documented here. Versions follow Semantic Versioning.

## 0.1.0 — 2026-09-04

### Added

- Standalone Cortex XSIAM/XSOAR playbook-engineering behavioral core.
- Evidence taxonomy, product boundaries, and three-level artifact classification.
- End-to-end automation lifecycle with data contracts, safety gates, failure handling, and evidence requirements.
- Official-source register covering current XSIAM documentation, versioned XSOAR 8.14 On-prem guidance, permissions, debugging, and content development.
- Reusable playbook design, review, context-contract, action-gate, and tenant-validation templates.
- Four worked examples, each clearly non-importable.
- Seven-category behavioral test catalog with isolated scorer guidance.

### Validation boundary

- Astra completion review on 2026-09-06 corrected the four examples to explicit S/D/C/E results and rationales, completed per-value input/output template dimensions, and strengthened existing contract/debugger cases without increasing the case count. Six applicable XSIAM sources were re-opened. The revised runtime awaits independent behavioral and final review; no new S pass is claimed.

- Independent technical, platform-domain, adversarial, and static compatibility review completed; selected oracle-isolated behavior passed after contract and troubleshooting corrections.
- Normalized every validation-output placeholder, including design, context-contract and tenant-validation summaries, to four explicit S/D/C/E results using only `PASS`, `FAIL`, `NOT RUN`, or `N/A` with rationale; independent revision-impact review closed the delta.
- Expanded the troubleshooting evidence record's remaining compact S/D/C/E outcome field into four typed results with level-specific rationale and retained-record requirements.
- No tenant schema/command validation, controlled import, debugger run, execution, side effect, deployment, or production observation was performed.
- Version remains `0.x` until independent release gates and material tenant/runtime evidence are available.
