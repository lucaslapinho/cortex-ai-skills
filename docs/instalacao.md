# Installation and first use

[Home](../README.md) · [Examples](exemplos.md) · [Validation](validacao.md) · [Plugin format](plugin-format.md)

Plugin documentation and actual account import checked on **2026-10-23**. The generated package was imported and installed, and the interface listed all seven Skills. See the [scoped UI result](plugin-ui-test.md).

## 1. Choose the correct ZIP

For the ChatGPT **New Plugin** screen, download:

**[cortex-ai-skills-plugin-0.1.1.zip](../packages/0.1.1/cortex-ai-skills-plugin-0.1.1.zip)**

Do not select `cortex-ai-skills-main.zip`, a GitHub repository export, a source ZIP, or an individual runtime ZIP in that plugin upload flow. They serve different purposes.

The reported repository ZIP contained seven Skills in `source/` and historical runtime ZIPs, but no plugin manifest. Its structure therefore did not meet the documented plugin-package requirements. The generic UI message does not reveal the actual backend error code.

The new plugin ZIP has this structure directly at the archive root:

```text
.codex-plugin/plugin.json
assets/cortex-skills.svg
LICENSE
skills/
  cortex-detection-engineer/SKILL.md
  cortex-platform-engineer/SKILL.md
  cortex-playbook-engineer/SKILL.md
  cortex-security-engineer/SKILL.md
  cortex-threat-hunter/SKILL.md
  cortex-tim-engineer/SKILL.md
  cortex-xql-query-engineer/SKILL.md
```

Each Skill also includes its complete runtime references, templates, examples, VERSION, and OpenAI adapter. Tests and review evidence remain outside the importable package.

## 2. Verify the download

Compare the file hash with [0.1.1 SHA256SUMS](../packages/0.1.1/SHA256SUMS):

```powershell
Get-FileHash -LiteralPath './cortex-ai-skills-plugin-0.1.1.zip' -Algorithm SHA256
```

All 64 hexadecimal characters must match the line for that filename. Checksums establish equivalence with the published artifact, not account acceptance or an independent author signature.

## 3. Import and verify in ChatGPT

1. Open the **New Plugin** screen used by your account and choose its ZIP upload option.
2. Upload `cortex-ai-skills-plugin-0.1.1.zip` and review the name, description, and included capabilities.
3. Complete the import/enable steps offered by your account and workspace policy.
4. Check the installed plugin details or Skills list for the seven exact names shown above.
5. Start a fresh conversation, select an available Skill through the host's selector, and try a read-only example.
6. Confirm that the needed supporting references can be read. A plausible answer alone is not proof that all seven Skills were discovered.

Exact controls and availability depend on your account. This package's import and installed seven-Skill listing were observed in one account. Useful task behavior and access to all supporting resources are separate tests.

Example request:

```text
Use cortex-platform-engineer to plan a read-only diagnosis.

I can see events in a raw dataset but not in the mapped query.
Product, version, schema, sample events, and error: [attach].
Identify the files and references you actually used.
List missing evidence and the next checks. Do not change the tenant.
```

## 4. Personal import, local Codex, and public publication

The plugin uses `.codex-plugin/plugin.json`, a currently supported compatibility format. OpenAI also documents a portable root `plugin.json` format. This package intentionally uses one format and one manifest. [Package your plugin](https://developers.openai.com/plugins/build/plugins).

Personal import is separate from local marketplace installation and public directory submission. Public listing identity checks, attestations, and public scans are not represented here as verified prerequisites of the user's personal upload.

For local Codex testing, extract the plugin to a folder and expose it through a documented repository or personal marketplace. Follow the current [local packaging instructions](https://developers.openai.com/plugins/build/plugins) and [connect/test guidance](https://developers.openai.com/plugins/deploy/connect-chatgpt). No marketplace or global configuration is installed by this repository's build.

## 5. Standalone Skills and manual use

Download an individual `*-0.1.1-runtime.zip` from the [package index](../packages/0.1.1/README.md). Preserve its Skill folder and supporting files.

For documented Codex standalone discovery, use a project `.agents/skills/<skill-name>/` directory or the personal `$HOME/.agents/skills/` location. In CLI/IDE, use `$` or the available selector; in ChatGPT, use the host's available selector. [Build skills](https://learn.chatgpt.com/docs/build-skills).

For manual use in an assistant that accepts the files, attach `SKILL.md` and the resources needed for the task, identify their original relative paths, and explicitly ask the assistant to apply them. Require it to name what it actually read and report missing references. This does not establish persistent native installation.

Claude Code can use runtime directories under project `.claude/skills/` or personal `~/.claude/skills/`. [Claude Code documentation](https://code.claude.com/docs/en/skills). claude.ai has a different custom-Skill import mechanism; verify its current metadata requirements before adapting a runtime. [Claude guidance](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills). The September review recorded a description-length restriction; this plugin release does not certify Claude import or silently change the descriptions to meet another host's rules.

Do not install the full `source/` directory or source archives as runtime Skills. They contain tests and answer keys. [Historical 0.1.0 downloads](../packages/0.1.0/README.md) remain available.

## 6. Reproduce the build

From the repository root with Python 3.11+ in an activated virtual environment:

```text
python -m pip install -r requirements-dev.txt
python -I scripts/build_plugin.py build --output dist/local-build
python -I scripts/build_plugin.py validate --zip dist/local-build/cortex-ai-skills-plugin-0.1.1.zip
```

Use a new output directory for each build. The command produces the plugin, seven individual runtimes, a per-file release manifest, and SHA256SUMS. It builds a temporary staging directory, validates it, checks the actual ZIP, and compares bytes across deterministic rebuilds. It copies canonical runtime files without transforming them.

## If import still fails

Record the time and time zone, account/workspace context, exact filename, plugin version, and SHA-256. If accessible, capture the failed import request's status, technical response, and request ID through your browser's developer tools or approved diagnostics. Remove tokens, cookies, authorization headers, and private data before sharing.

Compare any actual error with the [official submission/package error reference](https://developers.openai.com/plugins/deploy/submission-errors). Some rules on that page are public-directory-specific. Do not infer a particular error code from “Couldn't add plugin. Try again.”
