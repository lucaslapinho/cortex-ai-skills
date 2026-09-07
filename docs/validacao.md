# Validation, provenance, and limitations

[Home](../README.md) · [Installation](instalacao.md)

## What was preserved

This publication uses the previously prepared and reviewed **0.1.0** collection. The `source/` tree and all eight ZIPs retain their original bytes. The README, guides, contribution policy, and publication validator form a separate layer outside that tree.

Reports within `source/` and the package handoff record describe the build stage, including the absence of a commit or push at that time. These are historical statements; they do not mean this published repository is offline. No historical approval marker automatically authorizes execution of actions.

The public documentation and package index have been translated into English. Existing guide paths are retained to preserve shared links. Historical source evidence, release assets, checksums, and the release tag have not been rewritten as part of the translation.

## Build evidence

| Layer | Available record | What it does not demonstrate |
|---|---|---|
| Structure | 14 recorded validations and a release audit | Native discovery or execution in each application |
| Tooling | 7 build-tool unit tests | Production detection efficacy |
| Behavior | 23 approved final targeted cases with Astra | Execution of all 253 catalog cases |
| Cumulative coverage | 74 reviewed decisions, including 51 historical decisions; 179 unexecuted | 74 new tests on the same model |
| Packages | Eight ZIPs, 443 internal files, manifest, and checksums | An authorship signature or a semantic guarantee that all sensitive data is absent |
| Tenant | Compilation/import/execution not performed | Schema validity, performance, or playbook acceptance |

Details: [Final QA](../source/reviews/final-qa.md), [Astra review](../source/reviews/astra-review.md), and [historical limitations](../source/reviews/known-limitations.md).

## Compatibility difference identified during publication

**HOST-001 — claude.ai metadata, 2026-09-07.**

The [current Claude custom Skills guide](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) limits `description` to 200 characters. All seven preserved descriptions exceed this limit. This narrows the historical static compatibility conclusion: the general directory format is insufficient to establish acceptance by the current importer.

Conclusion: **adaptation is required to meet this documented limit; upload has not been performed**. Do not generalize this limit to Claude Code or other surfaces. Version 0.1.0 was not modified to imply that testing occurred. The [installation guide](instalacao.md) explains manual use and preparation of an adapted copy, which requires a new identity and validation.

The distinction between local Skills and plugins in ChatGPT was also rechecked. A ChatGPT web/mobile plugin remains **not included**. [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills).

## Historical tooling detail on Windows

**TOOLS-001 — alternate temporary-directory spelling, 2026-09-07.**

The first GitHub Actions run passed on Linux, but the link-rewriting test failed on both Windows runners. The 0.1.0 helper compares the resolved target with a base that must be canonical. The historical fixture does not normalize its temporary base; a Windows 8.3 alternate name can cause an incorrect comparison.

This publication's test runner resolves the temporary directory before executing the seven original tests. This preserves source files and their hashes, skips no tests, and uses the same kind of canonical base supplied by the evaluation CLI. Directly calling the helper with noncanonical bases remains a limitation of the historical version, not a claimed runtime fix.

## Project knowledge

Research documents are verifiable, sanitized summaries, not complete copies of the attachments. The [accessible-source inventory](../source/research/project-knowledge-inventory.md) and [differences from Palo Alto documentation](../source/research/project-vs-official-differences.md) were preserved.

This publication stage did not repeat all factual Palo Alto research or behavioral testing. Respect the dates and scope of each record. New host documentation is not new validation of Cortex behavior.

## Local reproduction

From the repository root, with Python 3.11+:

```text
python -I scripts/validate_publication.py
python -I -m unittest discover -s scripts -p "test_*.py" -v
python -I source/tools/release.py audit --release
python -I scripts/run_source_tests.py
```

The publication validator checks local links, high-confidence credential patterns, file limits, ZIP hashes, members against the manifest, and equivalence with the preserved source. It is a scoped technical control, not an absolute anonymization guarantee or a comprehensive security review.

The same commands run in the validation workflow. Check the actual result in the Actions tab; the existence of a workflow does not mean a run passed.

## Safe use

- Use only authorized environments and investigations.
- Start with read-only analysis and minimized data.
- Do not expose credentials, sensitive real-world evidence, or customer information in issues.
- Validate schemas and commands against the applicable product, version, license, and integration.
- Require specific authorization, a recovery plan, and verification before changes.
- Do not interpret an absence of evidence as proof of absence.
