# Cortex AI Skills

Seven modular Skills for evidence-scoped security work across the **Palo Alto Networks Cortex** ecosystem, informed by official documentation and practical project experience.

[Download the ChatGPT plugin](packages/0.1.1/README.md) · [Install](docs/instalacao.md) · [Usage examples](docs/exemplos.md) · [Validation](docs/validacao.md) · [Changelog](CHANGELOG.md)

> Independent project, unaffiliated with Palo Alto Networks, OpenAI, or Anthropic. The Skills provide instructions and references. Human validation and applicable tenant authorization remain necessary.

## Import all seven Skills into ChatGPT

Use **[cortex-ai-skills-plugin-0.1.1.zip](packages/0.1.1/cortex-ai-skills-plugin-0.1.1.zip)** in your account's **New Plugin** ZIP upload flow.

The plugin contains a supported `.codex-plugin/plugin.json` compatibility manifest, a presentation icon, the project license, and seven complete runtime directories under `skills/`. Everything is generated from the canonical `source/` Skills.

**Imported and installed successfully in the user's ChatGPT account on 2026-10-23; all seven Skills are listed.** Task-level reference loading and Cortex execution still require separate tests. See the [installation steps](docs/instalacao.md) and [account UI test](docs/plugin-ui-test.md).

| Download | Purpose |
|---|---|
| `cortex-ai-skills-plugin-0.1.1.zip` | Import the seven Skills as one plugin |
| `cortex-<specialty>-0.1.1-runtime.zip` | Install one standalone Skill in a compatible host |
| GitHub repository ZIP / historical `-source.zip` | Development source and review evidence; not the plugin upload |

Find the current files and checksums in [0.1.1 packages](packages/0.1.1/README.md). [Historical 0.1.0 packages](packages/0.1.0/README.md) remain available with their original archives, manifest, and checksums.

## Choose a specialty

| Skill | Use it to |
|---|---|
| [XQL Query Engineer](source/cortex-xql-query-engineer/README.md) | Build, review, explain, and troubleshoot queries with explicit schema and product boundaries |
| [Detection Engineer](source/cortex-detection-engineer/README.md) | Design detection logic, telemetry requirements, tuning, tests, and lifecycle decisions |
| [Playbook Engineer](source/cortex-playbook-engineer/README.md) | Design workflows, subplaybook contracts, approvals, error handling, and recovery |
| [Threat Hunter](source/cortex-threat-hunter/README.md) | Test hypotheses, plan pivots, assess coverage, and consider competing explanations |
| [TIM Engineer](source/cortex-tim-engineer/README.md) | Govern indicator ingestion, enrichment, expiration, interoperability, and distribution |
| [Platform Engineer](source/cortex-platform-engineer/README.md) | Troubleshoot collection, ingestion, mapping, integrations, and access |
| [Security Engineer](source/cortex-security-engineer/README.md) | Scope cross-domain requests and coordinate explicit handoffs |

Each Skill remains standalone. Bundling does not add a Cortex connection, MCP server, external action, or automatic response capability.

## Example request

After the plugin or selected runtime is available:

```text
Use cortex-xql-query-engineer to review my query.

Product: Cortex XSIAM.
Version and enabled features: [provide what you know].
Objective: investigate suspicious PowerShell executions.
Query, schema, and anonymized sample: [attach].

Read the accessible files required for this task and identify missing inputs.
Preserve the query's intent and explain corrections.
Do not invent datasets, fields, results, or tenant access.
Check the applicable official documentation.
Separate documentation review from compilation and execution.
```

See [seven complete examples](docs/exemplos.md) for detection, playbooks, hunting, TIM, platform, and security coordination.

## What changed in 0.1.1?

- Added deterministic plugin packaging and retained individual runtime generation.
- Refreshed selected official Palo Alto sources on **2026-10-23**, with a local refresh record in each Skill.
- Recorded API/example inconsistencies and product-specific limits instead of guessing a resolution.
- Added three focused regression scenarios for the changed guidance; they are authored tests, not new behavioral passes.
- Preserved historical review evidence and versioned 0.1.0 downloads.

Plugin and Skill versions are tracked separately. All seven Skills are currently `0.1.1` because their references changed; the packaging change alone would not require a Skill-version change.

## Validation boundaries

The package checks validate the generated ZIP, seven identities, YAML/JSON, icons, local references, canonical file hashes, archive safety, and deterministic rebuilding. The [validation guide](docs/validacao.md) records the actual checks and independent review.

The September 0.1.0 build had 23 final targeted Astra cases and 74 cumulative reviewed decisions out of its 253-case catalog. These are historical results. They do not establish fresh behavioral validation of 0.1.1. Account import and the seven-Skill listing were observed; task behavior, tenant compilation and execution remain **NOT RUN**.

Host support depends on the application and account. See [installation](docs/instalacao.md) for standalone and manual-use paths.

## Knowledge and evidence

Current official Palo Alto documentation governs factual product claims. Readable project material supplies conventions and context. The [knowledge inventory](source/research/project-knowledge-inventory.md) records accessible artifacts, and the [differences register](source/research/project-vs-official-differences.md) preserves conflicts.

Source refreshes apply only to the inspected claims and their recorded dates. They do not establish tenant licensing, installed content, schemas, results, or production efficacy.

## Repository layout

```text
source/                   Canonical seven Skills, references, and historical evidence
plugin/                   Plugin metadata and original presentation asset
scripts/                  Plugin builder, publication checks, and tests
docs/                     Installation, examples, requirements, and validation
packages/0.1.1/            Current plugin and individual runtime ZIPs
packages/0.1.0/            Preserved historical artifacts
```

Generated Skills are not maintained as a second source tree.

## Build and check

Python 3.11+; PyYAML is a development dependency only. Use an activated virtual environment for these commands, because isolated Python ignores user-site packages:

```text
python -m pip install -r requirements-dev.txt
python -I scripts/build_plugin.py build --output dist/local-build
python -I scripts/build_plugin.py validate --zip dist/local-build/cortex-ai-skills-plugin-0.1.1.zip
python -I scripts/validate_publication.py
python -I -m unittest discover -s scripts -p "test_*.py" -v
python -I scripts/run_source_tests.py
```

The output directory must be new. Builds do not install plugins, call models, or access a Cortex tenant. See [contributing](CONTRIBUTING.md).

## License

[MIT](LICENSE). Product names and trademarks belong to their owners.
