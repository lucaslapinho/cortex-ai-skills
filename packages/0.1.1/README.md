# Cortex AI Skills 0.1.1 downloads

For ChatGPT's **New Plugin** upload, choose **[cortex-ai-skills-plugin-0.1.1.zip](cortex-ai-skills-plugin-0.1.1.zip)**.

Plugin version: `0.1.1`. All seven Skill versions: `0.1.1`, reflecting the targeted 2026-10-23 source refresh. Plugin and Skill versions are tracked independently.

## Plugin

- Size: **440,288 bytes**.
- SHA-256: `de85688224c01a32f59d49fbb3aa6dae72ba13503ef50e6146344db56ac646ea`.
- Contents: one compatibility manifest, original SVG icon, MIT license, and **160 runtime files** across **seven Skills**.
- Archive total: **163 files**; **523** relative references checked.

[Installation and verification](../../docs/instalacao.md) · [Format evidence](../../docs/plugin-format.md) · [Validation](../../docs/validacao.md)

## Standalone runtimes

| Skill | Download |
|---|---|
| Detection | [Runtime ZIP](cortex-detection-engineer-0.1.1-runtime.zip) |
| Platform | [Runtime ZIP](cortex-platform-engineer-0.1.1-runtime.zip) |
| Playbook | [Runtime ZIP](cortex-playbook-engineer-0.1.1-runtime.zip) |
| Security coordination | [Runtime ZIP](cortex-security-engineer-0.1.1-runtime.zip) |
| Threat hunting | [Runtime ZIP](cortex-threat-hunter-0.1.1-runtime.zip) |
| Threat intelligence | [Runtime ZIP](cortex-tim-engineer-0.1.1-runtime.zip) |
| XQL | [Runtime ZIP](cortex-xql-query-engineer-0.1.1-runtime.zip) |

Each runtime is independently rooted and contains exactly the same Skill bytes as the corresponding plugin directory. Standalone ZIPs and GitHub repository exports are not the ZIP for the New Plugin flow.

## Identity and preservation

[SHA256SUMS](SHA256SUMS) covers all eight current ZIPs. The [release manifest](release-manifest.json) lists every plugin file, source-copy equivalence, Skill versions, and changes from the historical runtime identities. There are no transformations or exceptions to the canonical copy.

The original [0.1.0 archives and checksums](../0.1.0/README.md) remain unchanged.

## Checks and independent review

- 19 plugin regression tests and 6 existing publication tests passed.
- 7 existing source-tooling unit tests passed.
- Actual ZIP JSON/YAML, members, reference resolution, safe paths/types, and canonical hashes passed.
- Independent reviewer re-read the retained ZIP, verified all 14 Skill/adapter YAML documents, 160 runtime files, and 523 relative links/anchors.
- Independent complete rebuild reproduced all eight ZIPs, manifest, and checksums byte for byte.
- Independent domain review covered the new Palo Alto source claims; three additional authored behavior scenarios remain NOT RUN.

The build manifest records local validation at build time. A later [account UI test](../../docs/plugin-ui-test.md) verified successful import, installation and seven listed Skills. Task behavior, supporting-reference loading and tenant tests remain NOT RUN. See the current [validation record](../../docs/validacao.md).

## Build

From repository root, after installing requirements-dev.txt:

```text
python -I scripts/build_plugin.py build --output dist/local-build
python -I scripts/build_plugin.py validate --zip dist/local-build/cortex-ai-skills-plugin-0.1.1.zip
```

The output directory must be new. No model call, host installation, tenant access, or public-directory submission is performed by the build.
