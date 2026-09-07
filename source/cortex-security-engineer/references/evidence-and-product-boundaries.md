# Evidence and Product Boundaries

## Contents

- [Core rule](#core-rule)
- [Canonical evidence taxonomy](#canonical-evidence-taxonomy)
- [Qualifiers and validation depth](#qualifiers-and-validation-depth)
- [Source precedence](#source-precedence)
- [Cortex product boundaries](#cortex-product-boundaries)
- [Tenant claims](#tenant-claims)
- [Evidence ledger](#evidence-ledger)
- [Language for conclusions](#language-for-conclusions)

## Core rule

Make the strongest claim supported by the weakest material dependency. A current product page can verify a documented capability; it cannot prove entitlement, visibility, configuration, schema population, compiler acceptance, execution, results, or efficacy in a tenant.

Record observations separately from interpretation:

- **Observation:** what a supplied artifact, official page, or authorized tenant test actually shows.
- **Interpretation:** why that observation may support a requirement, risk, or control.
- **Alternative:** a benign, coverage, permission, version, or product explanation.
- **Unknown:** the evidence still required.

## Canonical evidence taxonomy

Use exactly one primary class for a claim.

| Class | Meaning | Typical use |
|---|---|---|
| `VERIFIED` | Direct authoritative evidence supports the claim in its declared scope. | Current product documentation or recorded tenant observation |
| `VERSION-DEPENDENT` | Official behavior differs by release, product, rollout, or documented version. | Conflicting scoped references or release transition |
| `INFERRED` | Evidence supports a reasoned conclusion but does not directly establish it. | Proposed risk, likely dependency, predicted operational effect |
| `CONCEPTUAL` | Design intent or pseudologic, not an implemented or tested artifact. | Standalone fallback when specialist mechanics are unavailable |
| `UNSUPPORTED` | Applicable authoritative material states the construct or behavior is not supported. | Explicitly forbidden surface or combination |
| `DEPRECATED` | Applicable authoritative material marks it obsolete or on a removal path. | Legacy API/product behavior with a stated deprecation |
| `UNVERIFIED` | Required evidence is absent, inaccessible, stale, ambiguous, or untrusted. | Unknown tenant field, role, entitlement, result, or configuration |

Do not use popularity, plausible naming, a UI label, a filename, a copied ticket, an assistant assertion, or a sibling package as verification.

## Qualifiers and validation depth

Add qualifiers without creating a second class:

- `OFFICIAL-CURRENT` — reviewed current first-party documentation for the named product/release on a recorded date;
- `OFFICIAL-EXAMPLE` — a first-party example, scoped to its page or pinned revision;
- `LOCAL-VERIFIED` — a local structural fact directly inspected in the current workspace, not vendor behavior;
- `PROJECT-ASSERTED` — a project artifact makes the claim, without elevating it to product truth;
- `DERIVATIVE` — analysis derived from identified evidence rather than stated directly by an authority;
- `REFERENCED-ONLY` — the source is named but was not directly available for inspection;
- `TENANT-UNVERIFIED` — no direct evidence from the target tenant;
- `TENANT-SCHEMA-VERIFIED` — the exact dataset/fields/types were observed in the named context;
- `TENANT-COMPILED` — the exact query, rule, parser, script, or editor artifact was accepted in the named context;
- `TENANT-EXECUTED` — the exact artifact completed under recorded identity, scope, time, and evidence capture.

For executable-looking material, state exactly one canonical primary status, applicable qualifiers, and the separate S/D/C/E results. For example, documentation-grounded syntax with no tenant check is normally `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED`, while pseudologic is `CONCEPTUAL`; neither establishes C or E. Use `TENANT-SCHEMA-VERIFIED`, `TENANT-COMPILED`, or `TENANT-EXECUTED` only when retained evidence supports that exact depth and scope. Never invent a second “executability ceiling” taxonomy or advance evidence because a later workflow stage is desired.

## Source precedence

Use this order:

1. current official Palo Alto Networks documentation for the exact product, release, and surface;
2. release notes or migration/correction material for that product and release;
3. authoritative tenant observation captured under a named identity and context;
4. pinned first-party examples;
5. local research or design records with provenance;
6. third-party sources as leads only.

When sources conflict:

1. keep both claims and scopes visible;
2. check product, release, date, license, and surface;
3. use `VERSION-DEPENDENT` or `UNVERIFIED`;
4. propose the smallest discriminating documentation or tenant check;
5. do not silently choose the more convenient source.

## Cortex product boundaries

As of the source review date:

- **Cortex XSIAM** is documented as a converged security-operations platform, with capabilities subject to edition, license, rollout, permissions, and tenant configuration.
- **Cortex XDR** is a distinct extended-detection-and-response product. Shared terms do not make XSIAM guidance automatically portable.
- **Cortex XSOAR** is a security orchestration, automation, case-management, collaboration, and threat-intelligence platform with versioned deployment models and APIs.
- **Threat Intel Management (TIM)** in XSIAM is a licensed capability for indicator aggregation, scoring, sharing, and workflows. An indicator or reputation does not prove intent, compromise, or detection coverage.
- **Cortex Cloud** has cloud application, posture, runtime, asset, case, automation, and data surfaces with its own licensing and release behavior. Cortex Cloud release notes do not correct XSIAM/XDR/XSOAR behavior unless a product-specific source says so.

For every concrete recommendation, state:

| Dimension | Required value |
|---|---|
| Product | Exact named product |
| Release | Exact line/build if material, otherwise `UNKNOWN` |
| License/edition | Observed entitlement or `REQUIRES TENANT VALIDATION` |
| Surface | Exact UI/editor/API/runtime surface |
| Identity | Role/service/API identity, safely aliased |
| Data scope | RBAC/SBAC/dataset/object scope or `UNKNOWN` |
| Environment | Design, development, non-production, or production |
| Evidence date | Documentation and tenant observation dates |

Do not treat these object families as synonyms:

- installed endpoint software, DLP Endpoint Application definitions, and ASPM/Cloud Business Applications;
- XSIAM Cases/Issues and legacy XSOAR incident terminology;
- interactive Query Center XQL, BIOC, scheduled correlation, real-time correlation, and XQLp;
- detection-rule schedule and automation Job schedule;
- playbook visibility, playbook edit rights, integration command permission, and response-action authorization;
- dataset access, dataset-row SBAC, query-execution permission, and result visibility.

See [product and surface map](product-surface-map.md) for routing.

## Tenant claims

No tenant claim is valid without a record that includes:

- tenant safe alias, product, version/release, license and environment;
- exact identity plus RBAC, SBAC, dataset, and object scope;
- exact artifact/hash and surface;
- absolute time range and timezone;
- schema/configuration snapshot as applicable;
- compiler/editor/API response;
- sanitized result or error, count, and evidence location;
- coverage, ingestion, retention, parser/mapping, and clock assumptions;
- tester, date, and approval boundary.

A zero result does not establish absence. A positive result does not establish maliciousness. A successful editor save does not establish execution. Component execution does not establish end-to-end efficacy.

## Evidence ledger

Use one row per material claim:

| ID | Claim | Product/release/surface | Source | Observation | Class/qualifiers | Scope limit | Next check | Owner |
|---|---|---|---|---|---|---|---|---|
| `EV-001` | `<claim>` | `<scope>` | `<link or record>` | `<fact>` | `<class / qualifiers>` | `<limit>` | `<check>` | `<role>` |

Hash mutable exports and preserve their provenance. Do not paste secrets, full endpoint identifiers, private case content, or unnecessary personal data into the ledger.

## Language for conclusions

Prefer bounded statements:

- “Current XSIAM documentation reviewed on 2026-09-04 describes this permission dependency; effective tenant access is unverified.”
- “The supplied artifact records zero rows under the named identity and timeframe; absence of activity is not established.”
- “This is a conceptual control contract. The detection, playbook, and platform mechanics need separate specialist and tenant validation.”
- “Proceed to non-production validation after the named owner verifies the remaining gates.”

Avoid:

- “Cortex supports this everywhere.”
- “The tenant has the data.”
- “This query/rule/playbook works.”
- “The indicator is malicious.”
- “The control is production ready.”
