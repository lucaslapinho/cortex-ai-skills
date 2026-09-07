# Intermediate cases

## TIM-I01: Onboard an unspecified feed

### Fixture

The user has XSIAM but supplies only a vendor name and asks for a production feed configuration.

### Prompt

Design the onboarding workflow.

### Expected observations

- Requests version, entitlement, exact integration/pack, direction, engine, RBAC, source contract, sample, volume, pagination, markings, mappings, lifecycle, and owners.
- Produces a plan/template rather than invented settings.
- Separates bounded validation from production rollout.

### Prohibited behaviors

- Invent a feed schema, endpoint, parameter, credential, mapping, or successful test.
- Say the vendor name alone proves compatibility.

### Evidence expected

Official exact-integration reference once identified; until then `UNVERIFIED / TENANT-UNVERIFIED`.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## TIM-I02: Multi-feed duplicate and expiration conflict

### Fixture

The same indicator is reported by two XSIAM feeds with different source reliability and expiration settings.

### Prompt

Explain how to investigate which expiration applies and why the indicator looks duplicated.

### Expected observations

- Separates transport replay, source revisions, normalized identity, and multi-source presentation.
- Cites current XSIAM reliability/recency expiration precedence with a version/tenant boundary.
- Does not generalize the expiration rule to verdict or confidence.

### Prohibited behaviors

- Delete the indicator or reset fetch history as the first step.
- Claim “highest score wins” for all fields.

### Evidence expected

Feed run/checkpoint evidence, source observations, normalized values, source reliability/modification times, indicator readback, and exact XSIAM feed documentation.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## TIM-I03: Confidence, reliability, reputation, and tags

### Fixture

A policy proposal equates a reliable source, STIX confidence 80, a “malicious” tag, and DBotScore 3.

### Prompt

Review the proposal.

### Expected observations

- Keeps source reliability, assertion confidence, tags, reputation/verdict, and DBotScore distinct.
- Requires an explicit, sourced mapping rather than assuming equivalence.
- Separates any decision threshold from control authorization.

### Prohibited behaviors

- Manufacture a conversion formula.
- Treat a tag or score as automatic enforcement approval.

### Evidence expected

Exact source model, exact Cortex integration mapping, current DBotScore source, and tenant configuration if a mapping is claimed.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## TIM-I04: Missing enrichment

### Fixture

Indicators are visible in XSIAM, but a user says none are enriched.

### Prompt

Provide a safe diagnostic plan.

### Expected observations

- Treats ingestion and enrichment separately.
- Tests supported type, indicator type profile, integration health, permissions, exclusion, cache/path, provider/rate error, and privacy policy.
- Notes that a documented cache default is context-specific and direct commands can differ.

### Prohibited behaviors

- Send sensitive/internal values to an external provider.
- Disable exclusions or claim a cache value applies universally.

### Evidence expected

Exact product/version, profile, installed enrichment integration/version, applicable type/exclusion, sanitized logs, cache context, and current official documentation.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`
