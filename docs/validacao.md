# Validation, provenance, and limitations

[Home](../README.md) · [Install](instalacao.md) · [Format evidence](plugin-format.md)

## Version and evidence boundaries

Plugin distribution **0.1.1** includes seven Skills currently at **0.1.1**, following a targeted official-source refresh on **2026-10-23**. The canonical source is `source/`. Build output is a generated view, with every packaged runtime byte compared against that source.

The eight historical archives, their manifest, and SHA256SUMS in `packages/0.1.0/` remain unchanged. The historical source ZIP is checked member by member against its original manifest. Current source is separately validated against the new release rather than falsely required to equal 0.1.0.

## What the checks establish

| Check | Evidence boundary |
|---|---|
| Manifest and metadata | JSON/YAML parsing; exactly seven unique names; valid paths, SemVer and presentation asset |
| Canonical preservation | All runtime files identical to current source; changes from 0.1.0 listed in the new manifest |
| Runtime completeness | Local references and anchors resolve within each standalone Skill |
| Archive integrity | Actual ZIP re-read/CRC checks, unsafe paths/types/collisions rejected, hidden manifest retained |
| Determinism | Two complete builds produce identical archives and release metadata |
| Individual distribution | Seven independently rooted runtime ZIPs generated alongside the plugin |
| Regression tooling | Missing manifests, incomplete Skills, missing references, malformed metadata, altered files, unsafe ZIPs and invalid SemVer exercised |
| Knowledge refresh | Selected current Palo Alto source claims inspected; every Skill includes a dated scope record |

The [release manifest](../packages/0.1.1/release-manifest.json) and [SHA256SUMS](../packages/0.1.1/SHA256SUMS) identify the artifacts. Independent review and executed test counts are recorded in the [0.1.1 package index](../packages/0.1.1/README.md).

## Account import and remaining tests

| Layer | Result |
|---|---|
| Personal ChatGPT import acceptance | PASS — observed in the user's account on 2026-10-23 |
| Installation and seven-Skill interface listing | PASS — installed entry, Manage/Try in chat and seven names observed |
| Supporting-reference loading after installation | NOT RUN |
| Fresh controlled behavioral evaluation of all revised Skills | NOT RUN |
| Cortex tenant schema/compiler or playbook import | NOT RUN |
| Cortex execution, deployment, efficacy, or performance | NOT RUN |

**Local validation and one-account import/installation completed.** See [UI test evidence](plugin-ui-test.md) and the [independent review](plugin-review-0.1.1.md).

With the user's explicit confirmation, Add plugin accepted the generated ZIP. Install plugin then completed, and the installed details showed version 0.1.1 and all seven Skill names. No task was sent or tenant accessed during this UI check. The deterministic build manifest retains its build-time NOT RUN labels; this separate UI record adds the later observation without changing archive bytes.

## Historical results remain historical

The September 0.1.0 record includes 23 final targeted Astra cases, 74 cumulative reviewed decisions from a 253-case catalog, and 179 cases not run. Those numbers do not become fresh passes for 0.1.1.

Three additional October scenarios address updated behavior and documented contradictions. They are authored separately from the 253 historical cases and remain NOT RUN unless an independent evaluation is explicitly retained. Historical source reports and old runtime hashes remain traceable in the archived source and dated ledgers.

## Source and review findings

The refresh preserves contradictory official examples and APIs instead of choosing an unsupported method or context path. See the [difference register](../source/research/project-vs-official-differences.md) and each Skill's dated refresh reference.

Independent packaging review found two malformed-input issues during development: permissive SemVer prerelease parsing and ZIP names normalized/truncated by Python before validation. Both were corrected, regression-tested, and independently rechecked. Neither finding required changing technical Skill content.

The historical helper's Windows temporary-path spelling limitation remains documented in its source context; the existing test runner canonicalizes its fixture directory. This does not change packaged runtime behavior.

## Reproduce the checks

With Python 3.11+ from the repository root:

```text
python -m pip install -r requirements-dev.txt
python -I scripts/validate_publication.py
python -I -m unittest discover -s scripts -p "test_*.py" -v
python -I source/tools/release.py audit
python -I scripts/run_source_tests.py
python -I scripts/build_plugin.py build --output dist/review-build
python -I scripts/build_plugin.py validate --zip dist/review-build/cortex-ai-skills-plugin-0.1.1.zip
```

Use a new build directory. The CI matrix runs the checks on Linux and Windows with Python 3.11/3.13. Inspect the actual Actions run rather than inferring success from workflow presence.

Repository-level research inventory and prior case evidence are developer material and are excluded from the importable ZIP. Each Skill retains its bundled official-source register. Public-reference links are retained, but host network access is never presumed.

## Project knowledge

The [inventory](../source/research/project-knowledge-inventory.md) records material that was actually accessible and consumed, including this task's repository ZIP. No additional ChatGPT project library, original private tenant export, or live tenant was fabricated or claimed as ingested.

The current source review is a targeted refresh, not a fresh verification of every historical source. Respect each record's dates, scope, and limitations.
