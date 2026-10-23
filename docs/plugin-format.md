# Plugin format and documentation evidence

[Home](../README.md) · [Install](instalacao.md) · [Validation](validacao.md)

Consulted on **2026-10-23**. This record concerns packaging, not factual Cortex product behavior.

## Confirmed diagnosis

The supplied `cortex-ai-skills-main.zip` has SHA-256:

```text
b254a75a1095bd828d029247ae6b11d1af661234e0d52f7ca38958db9deaa8b5
```

It contains one repository wrapper, 313 files plus directory records, seven `source/*/SKILL.md` files, and no supported plugin manifest. CRC/decompression passed. Its files match the initial checkout after line-ending normalization; only three root text files differ in line endings.

The old seven individual runtime ZIPs are Skill packages, not plugin packages. The absence of a manifest is a confirmed structural incompatibility with documented plugin import. The account's generic failure message does not establish a backend code or exclude another independent issue.

## Official sources checked

| Source | Bounded use |
|---|---|
| [Package your plugin](https://developers.openai.com/plugins/build/plugins) | Compatibility manifest support, root-relative paths, skills directory, local marketplace distinction |
| [Manifest fields and submission](https://developers.openai.com/plugins/deploy/submission#manifest-fields) | Metadata and Codex presentation fields |
| [Submission/package errors](https://developers.openai.com/plugins/deploy/submission-errors) | Shared archive, manifest, Skill, and image constraints; public-only rules distinguished |
| [Connect and test](https://developers.openai.com/plugins/deploy/connect-chatgpt) | Supported connection/testing workflow; not evidence of personal account acceptance |
| [Build skills](https://learn.chatgpt.com/docs/build-skills) | Skill entrypoints, supporting resources, and host loading distinctions |

These pages were opened/read, not merely identified in search results. No tenant or account-installation result follows from documentation.

## Chosen package profile

Use the supported compatibility fallback:

```text
.codex-plugin/plugin.json
skills/<skill-name>/SKILL.md
```

The manifest declares `skills: "./skills/"`. It contains identity, SemVer, contributor attribution from MIT LICENSE, a Security presentation category, descriptions, capabilities, starter prompts, and paths to an original square SVG used for both icons.

There is no competing portable `plugin.json`, MCP configuration, remote connection, hook, or extra setup Skill. Exactly the seven existing identities are distributed. A temporary staging tree is generated from canonical `source/`; only the ZIPs and release metadata are retained.

## Documentation discrepancies and scope

- The manifest table allows a longer package description than the error reference. This repository chooses the stricter 1,024-character bound.
- A field table allows more than one form for `skills`; the error reference requires a string resolving to root `skills/`. This repository uses exactly `"./skills/"`.
- The public directory has tighter presentation text limits than package validation. Our metadata fits those smaller limits, but the validator is a repository profile, not a declaration that all public-submission conditions apply to personal import.
- The compatibility documentation describes both logo and composerIcon as Codex validation requirements. The original SVG satisfies that documented profile. This package was accepted by one account's importer; individual validation failures were not deliberately exercised there.
- Verified developer identity, policy attestations, public scans, and MCP-specific review material concern publication surfaces. No public-directory submission is performed here.

No requirement was invented for privacy or terms URLs, MCP credentials, support infrastructure, or production tenant access.

## Local validation profile

The implementation checks JSON/YAML parsing, unique names, the seven expected directories, declared paths, icons, resource links and anchors, and canonical byte identity. Archive checks include CRC/readability, original filenames before normalization, duplicates/case collisions, path traversal, file/directory conflicts, symlinks, nested ZIPs, and documented size ceilings.

The build uses fixed timestamps, stable POSIX ordering, fixed compression settings, and normalized permissions. Repeated builds with the same files and parameters are compared byte for byte. The importable ZIP contains only manifest, license, presentation asset, and complete runtime resources.

## Review limits

Local checks establish a well-formed supported-format package. A subsequent [account UI test](plugin-ui-test.md) observed successful import, installation and a seven-Skill listing for this artifact. Reference loading and task behavior still require separate tests. Import success does not validate Cortex schemas, rule deployment, playbook import, execution, or efficacy.
