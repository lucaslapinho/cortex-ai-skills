# Cortex AI Skills

Seven modular Skills for investigation, engineering, and defensive operations across the **Palo Alto Networks Cortex** ecosystem — with reusable instructions, references, templates, and examples.

[Get started](docs/instalacao.md) · [Usage examples](docs/exemplos.md) · [0.1.0 packages](packages/0.1.0/README.md) · [Validation and limitations](docs/validacao.md) · [Technical documentation](source/README.md)

> Independent, unofficial project with no affiliation to Palo Alto Networks, OpenAI, or Anthropic. These Skills guide an AI assistant; they do not automatically connect to your tenant, execute actions on their own, or replace human validation.

## What is a Skill?

A Skill is a set of instructions that teaches an assistant how to approach a specific task. The `SKILL.md` file defines the workflow; supporting folders provide references, templates, and examples. You supply the problem, product, version, and available data; the assistant applies the method and explains what it knows, what it inferred, and what still needs verification.

**It is not a trained model, a Cortex content pack, a ready-made integration, or an automatically importable playbook.**

## Choose a specialty

| Skill | When to use it | Typical deliverable |
|---|---|---|
| [XQL Query Engineer](source/cortex-xql-query-engineer/README.md) | Write, review, or troubleshoot XQL queries | Proposed query, assumptions, explanation, and validation plan |
| [Detection Engineer](source/cortex-detection-engineer/README.md) | Turn suspicious behavior into a detection proposal | Logic, required telemetry, false positives, and tests |
| [Playbook Engineer](source/cortex-playbook-engineer/README.md) | Design automations and subplaybooks | Workflow, input/output contracts, approvals, and recovery |
| [Threat Hunter](source/cortex-threat-hunter/README.md) | Investigate a threat hypothesis | Hunting plan, pivots, gaps, and alternative explanations |
| [TIM Engineer](source/cortex-tim-engineer/README.md) | Organize the threat intelligence lifecycle | Ingestion, enrichment, expiration, and governed distribution |
| [Platform Engineer](source/cortex-platform-engineer/README.md) | Troubleshoot collection, ingestion, mapping, or integrations | Diagnostic decision tree and configuration checks |
| [Security Engineer](source/cortex-security-engineer/README.md) | Scope cases that span multiple specialties | Scope, priorities, owners, and handoff contracts |

Each Skill works independently. The security Skill may recommend another specialty, but it does not assume that the corresponding Skill is installed.

## Get started in a few steps

1. Choose a Skill and download its **runtime ZIP** from [0.1.0 packages](packages/0.1.0/README.md).
2. Follow the [guide for your application](docs/instalacao.md). Do not install the source ZIP: it contains tests and answer keys.
3. Use anonymized data and a clearly scoped problem.
4. Ask for evidence and validate the output before applying any changes.

Example, after making the Skill available:

```text
Use cortex-xql-query-engineer to review my query.

Product: Cortex XSIAM.
Version and enabled features: [provide what you know].
Objective: investigate suspicious PowerShell executions.
Query, schema, and anonymized sample: [attach].

Read the required accessible files and identify anything missing.
Do not invent datasets, fields, or results.
Explain corrections and preserve the intent of the query.
Check the applicable official documentation.
Separate documentation review from tenant compilation and execution.
Do not execute anything or change the environment.
```

Explore [seven complete examples and a context template](docs/exemplos.md), ready to adapt.

## Where can I use it?

| Application | Usage method | Limitation of this release |
|---|---|---|
| ChatGPT, manual use | Attach the required instructions and references to a conversation | Not equivalent to persistent installation |
| ChatGPT desktop / Codex | Load the runtime through the supported local mechanism | Native discovery is not certified |
| ChatGPT web/mobile, native use | Distribution through a plugin | Plugin not included |
| Claude, manual use | Provide instructions and references and request their application | Confirm which files were actually read |
| claude.ai, native Skill | Custom ZIP import | The 0.1.0 descriptions exceed the currently documented 200-character limit; adaptation and testing are required |
| Claude Code | Runtime under `.claude/skills/<name>/` | Native discovery and execution have not been tested |

Host guidance was checked on **September 7, 2026**. Mechanisms and policies may change; consult the [installation instructions and sources](docs/instalacao.md).

## Quality and limitations

- Seven Skills at version **0.1.0**.
- **23/23** final targeted cases evaluated with Astra passed; this does not mean the entire catalog was executed.
- Recorded cumulative behavioral coverage: **74/253** decisions; **179** cases remain unexecuted.
- **7** tooling tests passed; packages include a manifest and checksums.
- Compilation, import, and execution in a Cortex tenant: **not tested**.

The [historical reports](source/reviews/final-qa.md) preserve build evidence. Publishing on GitHub does not expand the validation scope or establish production efficacy. The [current limitations guide](docs/validacao.md) also records differences identified during publication.

## How knowledge is handled

The project prioritizes current official documentation for product behavior. Verifiable project knowledge informs conventions and context; discrepancies are recorded and never silently resolved. See the [inventory](source/research/project-knowledge-inventory.md) and [differences register](source/research/project-vs-official-differences.md).

Original attachments, raw exports, credentials, and real endpoint records are not published. Never submit secrets or sensitive data in public issues, examples, or prompts.

## Repository layout

```text
README.md                 Home page
docs/                     Installation, examples, and current limitations
source/                   Preserved 0.1.0 source, seven Skills, and evidence
packages/0.1.0/            Seven runtimes, source ZIP, manifest, and checksums
scripts/                  Publication verification
.github/workflows/        Automated validation
```

The `source/` directory preserves the audited structure. It is not an automatic installation directory.

## Development

Publication commands require Python 3.11+ and no third-party libraries:

```text
python -I scripts/validate_publication.py
python -I -m unittest discover -s scripts -p "test_*.py" -v
python -I source/tools/release.py audit --release
python -I scripts/run_source_tests.py
```

These commands check files and structure; they do not call models, consume model quota, or access a tenant. See [how to contribute](CONTRIBUTING.md).

## License

[MIT](LICENSE). Product names and trademarks belong to their respective owners.
