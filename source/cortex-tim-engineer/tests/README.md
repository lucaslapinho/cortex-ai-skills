# Behavioral test catalog

These tests are maintainer/scorer material. They must not be included in the oracle-free runtime manifest or shown to the forward model with expected observations.

## Categories

| Category | File | Cases | Purpose |
|---|---|---:|---|
| Basic | [basic.md](basic.md) | 3 | Core terminology, evidence, and lifecycle |
| Intermediate | [intermediate.md](intermediate.md) | 4 | Feed design, duplicates, scoring, enrichment |
| Advanced | [advanced.md](advanced.md) | 4 | Interoperability, relationship loss, migration, controlled distribution |
| Troubleshooting | [troubleshooting.md](troubleshooting.md) | 4 | Competing hypotheses and stage localization |
| Ambiguity | [ambiguity.md](ambiguity.md) | 4 | Missing product, version, direction, source semantics, and authority |
| Adversarial | [adversarial.md](adversarial.md) | 8 | Prompt injection, unsafe changes, false attestations, and sensitive data |
| Regression | [regression.md](regression.md) | 10 | Known factual and boundary failures |
| **Total** |  | **37** |  |

## Canonical case schema

Every case contains exactly these material sections:

1. `Fixture`
2. `Prompt`
3. `Expected observations`
4. `Prohibited behaviors`
5. `Evidence expected`
6. `Authored result`

Every validation level uses exactly `PASS`, `FAIL`, `NOT RUN`, or `N/A`, with a rationale; use `N/A` only when that level genuinely does not apply. Every authored result records `S`, `D`, `C`, and `E` as `NOT RUN` until the corresponding evidence is retained and independently scored. A review task may be pending, but `PENDING` is not a validation-level result. Static presence of an expected observation is not a behavioral pass.

## Controlled execution procedure

1. Copy only the runtime manifest: `SKILL.md`, `VERSION`, `agents/`, `references/`, `templates/`, and `examples/`.
2. Confirm no root, sibling, test, review, validation-ledger, or prior-output artifact is reachable by the forward model.
3. Provide only the case fixture and prompt.
4. Record platform/model/version, Skill loading method, network availability, UTC time, prompt hash, response hash, and response artifact.
5. Have an independent scorer compare the response with expected and prohibited behavior.
6. Record findings by severity and retain superseding reruns rather than erasing earlier failures.
7. Keep S, D, C, and E distinct: static/behavioral response quality; official-document accuracy; tenant configuration/schema/import; tenant execution/deployment/results.

No case can establish a tenant fetch, enrichment, expiration, export, enforcement, or performance result unless a separate approved tenant test supplies retained evidence. The bundled authoring phase performs no such operation.
