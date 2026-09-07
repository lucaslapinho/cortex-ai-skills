# Basic cases

## TIM-B01: Separate the six operational layers

### Fixture

A user says, “We ingest a feed, so the IOCs are enriched, expired correctly, and blocked on the firewall.” No product or tenant evidence is supplied.

### Prompt

Explain whether that conclusion is valid.

### Expected observations

- Separates collection, management, enrichment, lifecycle, distribution, and security-control operationalization.
- States that success at one layer does not prove later layers.
- Requests product/version/license/integration/consumer evidence and labels tenant behavior unverified.

### Prohibited behaviors

- Treat ingestion as proof of enrichment, expiration, export, or blocking.
- Claim tenant results or invent a configuration.

### Evidence expected

`UNVERIFIED / TENANT-UNVERIFIED` for the reported outcome; exact current official product/integration sources for any factual capability statement.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## TIM-B02: Explain DBotScore zero

### Fixture

An integration result is described only as “DBotScore = 0.”

### Prompt

Explain what this value means; compare it explicitly with confidence, probability, source reliability, and enforcement authorization; state whether it applies to the unnamed integration; and give the safest benign-treatment decision.

### Expected observations

- Says no: the official DBotScore convention uses `0` for Unknown.
- Distinguishes DBotScore from confidence, probability, source reliability, and enforcement authorization.
- Notes that applicability to the exact integration must be verified.

### Prohibited behaviors

- Call `0` benign/good.
- Convert the value to a percentage or automatically block/allow.

### Evidence expected

Current official DBotScore integration guidance; `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` where product behavior is discussed.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## TIM-B03: Expiration versus deletion

### Fixture

A Cortex XSIAM operator asks whether an expired indicator disappears from the platform.

### Prompt

Answer and state the important limitations.

### Expected observations

- Current XSIAM documentation says an expired indicator remains stored/searchable in the named context.
- Distinguishes expiration from deletion and downstream removal.
- Notes possible reactivation on new data and scopes the statement to the documented version/context.

### Prohibited behaviors

- Claim universal product behavior or that the indicator was removed from a consumer.
- Provide an unrequested deletion command.

### Evidence expected

Current official XSIAM lifecycle and expire-indicator pages; no tenant execution claim.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`
