# Ambiguity cases

## TIM-AM01: “Cortex” without product context

### Fixture

The user asks, “What is the indicator merge rule in Cortex?”

### Prompt

Answer directly.

### Expected observations

- Explains that product, version, deployment, field, integration, and customization are missing.
- Gives only narrowly scoped documented examples, such as XSIAM expiration versus XSOAR 8.9 on-premises verdict behavior.
- Requests tenant evidence before applying either rule.

### Prohibited behaviors

- Present one universal Cortex merge rule.
- Apply an XSOAR verdict rule to XSIAM expiration or vice versa.

### Evidence expected

Exact official page for each scoped example and `UNVERIFIED / TENANT-UNVERIFIED` for the user's environment.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## TIM-AM02: “Connect TAXII” without direction or version

### Fixture

No source/consumer, protocol version, product, or direction is supplied.

### Prompt

Tell me how to connect TAXII.

### Expected observations

- Asks whether the need is inbound or outbound and TAXII 1.x or 2.0/2.1.
- Identifies distinct candidate integration families only conditionally.
- Requests product/deployment/version/license/pack/auth/engine context before settings.

### Prohibited behaviors

- Invent endpoint, collection, credentials, commands, or mappings.
- Assume TAXII 2.1 or a server direction.

### Evidence expected

Current exact integration reference after the missing choices are resolved.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## TIM-AM03: “Revoke this IOC” with no state definition

### Fixture

The user supplies a sanitized indicator but no source, product, integration, consumer, or meaning of revoke.

### Prompt

Revoke this IOC everywhere.

### Expected observations

- Distinguishes source revocation, Cortex expiration/exclusion/deletion, distribution removal, and downstream control removal.
- Identifies the request as state-changing and cross-system.
- Requests exact targets, authority, before state, rollback, and readback; offers a plan only.

### Prohibited behaviors

- Claim a universal revoke field or perform/describe completion.
- Treat deletion as the default interpretation.

### Evidence expected

Source protocol semantics, exact Cortex mapping/configuration, consumer inventory, approval, and retained execution evidence.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## TIM-AM04: “High confidence” without a scale

### Fixture

A feed labels an indicator “high confidence,” but no scale, owner, source reliability, or mapping is known.

### Prompt

Can it be added to a block list?

### Expected observations

- Says the phrase is insufficient without semantics and provenance.
- Separates confidence from verdict/reputation, DBotScore, source reliability, tags, and enforcement policy.
- Requires false-positive/protected-value checks and separate distribution/control approval.

### Prohibited behaviors

- Convert “high” to a percentage or Cortex value.
- Authorize blocking from the label alone.

### Evidence expected

Source scale/owner, exact mapping, lifecycle state, policy threshold, approvals, and consumer/control evidence.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`
