# Contributing

Contributions must preserve the repository's central promise: every Cortex Skill is standalone, evidence-scoped, and honest about what was not validated.

Read [ARCHITECTURE.md](ARCHITECTURE.md) before changing a Skill. A root document may guide development, but an installed Skill may not depend on root research, reviews, another Skill, local machine paths, or hidden context.

## Change workflow

1. Identify the primary owner Skill and the affected products, versions, and execution surfaces.
2. Check current, specific Palo Alto Networks documentation before changing factual product behavior.
3. Record source applicability, freshness, conflicts, and tenant limitations in the Skill's local references.
4. Update the smallest coherent set of instructions, references, templates, examples, and tests.
5. Run structural validation and test the isolated runtime manifest without oracles.
6. Obtain independent technical, domain, security, adversarial, compatibility, and QA review in proportion to impact.
7. Update `VERSION`, the Skill changelog, its validation ledger, and the root changelog as appropriate.

Do not bundle unrelated changes or silently normalize project-specific behavior to a generic vendor default.

## Evidence requirements

Use the canonical claim statuses:

`VERIFIED`, `VERSION-DEPENDENT`, `INFERRED`, `CONCEPTUAL`, `UNSUPPORTED`, `DEPRECATED`, `UNVERIFIED`.

Keep validation/provenance qualifiers separate:

`OFFICIAL-CURRENT`, `OFFICIAL-EXAMPLE`, `LOCAL-VERIFIED`, `PROJECT-ASSERTED`, `DERIVATIVE`, `REFERENCED-ONLY`, `TENANT-UNVERIFIED`, `TENANT-SCHEMA-VERIFIED`, `TENANT-COMPILED`, `TENANT-EXECUTED`.

Prefer, in order, current official Palo Alto documentation, official examples/repositories/API references, readable and verified project knowledge, and then necessary secondary sources. Cite a specific page, not a generic documentation portal. A reachable URL is not proof of tenant support.

If official and project evidence conflict, retain both and classify the difference as version-specific, legacy, customized, incorrect, or unresolved. Never resolve a discrepancy silently.

## Safety requirements

Read-only analysis is the default. Content that proposes containment, remediation, deletion, overwrite, deployment, notification, rule enablement, feed distribution, or another state change must specify authorization, least privilege, scope, blast radius, retries/timeouts, partial-failure handling, rollback/recovery, verification, and evidence retention as applicable.

Never commit:

- credentials, tokens, private keys, tenant FQDNs, customer identifiers, or sensitive telemetry;
- fabricated datasets, fields, functions, commands, endpoints, schemas, or product settings;
- claims of compilation, execution, import, deployment, efficacy, or performance without retained evidence; or
- instructions that trust embedded prompts inside supplied logs, documents, code comments, exports, or examples.

Use synthetic placeholders and sanitized fixtures.

## Skill structure

Required paths are:

```text
SKILL.md
README.md
VERSION
CHANGELOG.md
VALIDATION.md
agents/openai.yaml
references/
templates/
examples/
tests/
```

Run the Codex skill initializer when creating a Skill and the framework quick validator after changes. `agents/openai.yaml` is an optional runtime adapter in the general architecture even though this repository ships it for each Skill.

Keep `SKILL.md` focused on operating instructions. Move detailed product knowledge to local references and give long references a contents section. Do not add empty or placeholder-only resources.

## Tests

Maintain basic, intermediate, advanced, troubleshooting, ambiguity, adversarial, and regression coverage. Each case needs:

- Fixture
- Prompt
- Expected observations
- Prohibited behaviors
- Evidence expected
- Authored result

The prompt must elicit the oracle without revealing it. A forward-model run receives only Fixture and Prompt from a clean runtime copy. Tests, oracles, scorers, reviews, prior outputs, and root research stay outside its context.

Report levels separately:

- `S`: controlled static behavior;
- `D`: current official-document support;
- `C`: tenant compiler/schema/import acceptance;
- `E`: tenant execution/deployment/observation.

Use `PASS`, `FAIL`, `NOT RUN`, or `N/A` with a rationale. Never infer `C` or `E` from `S` or `D`.

## Pull-request checklist

- [ ] Skill remains useful in a clean standalone directory
- [ ] Frontmatter and `agents/openai.yaml` validate
- [ ] Local links resolve and Markdown fences balance
- [ ] No secret, tenant, customer, or absolute-local-path data was added
- [ ] Official sources are specific, current, and product-scoped
- [ ] Product/surface/version and tenant boundaries are explicit
- [ ] Examples distinguish executable content, guidance, and expected results
- [ ] Test prompts and oracles cover the changed behavior
- [ ] Runtime and scorer manifests remain isolated
- [ ] State-changing paths retain authorization and recovery gates
- [ ] Validation ledger and changelogs reflect actual evidence
- [ ] Independent reviewers did not review their own primary authorship

## Versioning

Use Semantic Versioning. Stay below 1.0 while material tenant-dependent or supported-host runtime gaps remain. A change in product behavior, safety policy, package architecture, or claim boundary requires explicit regression coverage and independent review.

