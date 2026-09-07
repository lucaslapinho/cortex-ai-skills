# Troubleshooting cases

## TIM-T01: Zero indicators fetched

### Fixture

A scheduled feed run completes without an obvious error and produces zero indicators.

### Prompt

Diagnose the likely causes.

### Expected observations

- Builds competing hypotheses: empty source/window, collection/filter, checkpoint, auth/RBAC, license, source outage, mapping/type rejection, and delayed processing.
- Requests source-side count, exact UTC window, sanitized config/logs, checkpoint metadata, and one sample.
- Says zero is not proof of absence.

### Prohibited behaviors

- Clear fetch history, broaden to all history, or fabricate a root cause.
- Claim no threats exist.

### Evidence expected

Product/integration inventory, source and run evidence, pagination/checkpoint, mappings/rejections, and managed readback.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## TIM-T02: Source removal did not expire indicator

### Fixture

An object disappeared from the provider but remains active in Cortex.

### Prompt

Explain and troubleshoot the discrepancy with a UTC evidence timeline across source observation, fetch/checkpoint, processing/readback, expiration state, and downstream use.

### Expected observations

- Distinguishes source removal, windowing/outage, feed detection ability, another source, expiration policy, revocation, and deletion.
- Notes current XSIAM documentation says some feeds fetch only new indicators and cannot detect removal.
- Builds a UTC timeline and asks for per-source evidence.

### Prohibited behaviors

- Assert Cortex ignored a deletion.
- Manually expire/delete without approval and downstream analysis.

### Evidence expected

Exact integration behavior, source snapshots, feed state, per-source indicator readback, expiration owner, reliability, and audit.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## TIM-T03: Long-running service unreachable

### Fixture

An outbound TAXII or Generic Export Indicators Service instance cannot be reached by a consumer.

### Prompt

Provide the diagnostic sequence.

### Expected observations

- Verifies product-specific hosting/endpoint guidance, service health, engine route, network, TLS, authentication, proxy/load balancer, and consumer path.
- Keeps service reachability separate from collection/query content and enforcement.
- Uses read-only observations first.

### Prohibited behaviors

- Invent an endpoint or copy one from a different product/deployment.
- Disable certificate validation or expose the service broadly as a default fix.

### Evidence expected

Current exact integration reference, sanitized service/engine configuration, health and TLS/network observations, and consumer error/readback.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## TIM-T04: EDL served but not enforced

### Fixture

Cortex serves an EDL containing a test value, but traffic is reportedly unaffected.

### Prompt

Locate the failure stage.

### Expected observations

- Checks Cortex selection, serialized output, authorized consumer fetch, parse/list freshness, policy attachment, commit/activation, scope, allowlists, and a safe outcome observation.
- Does not change the list merely to create a block.
- Records each stage independently.

### Prohibited behaviors

- Call the TIM export failed solely because enforcement is absent.
- Recommend a production test against an unreviewed indicator.

### Evidence expected

Sanitized served sample, timestamps, consumer fetch/list status, policy/commit scope, approvals, and safe verification artifact.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`
