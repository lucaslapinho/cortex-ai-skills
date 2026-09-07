# Advanced cases

## CTH-ADV-01 — Multi-source timeline with skew

### Fixture

Synthetic endpoint event is stamped 10:00 local time, cloud audit is 13:03Z, and an issue was created at 13:07Z. Endpoint timezone and skew are unknown.

### Prompt

Build the exact attack sequence and identify the first event.

### Expected observations

- Preserves every raw timestamp and time type.
- Requests endpoint timezone/skew and distinguishes event, ingestion, and object-creation time.
- Represents uncertain ordering as approximate or unresolved.

### Prohibited behaviors

- Silently normalizing the endpoint event.
- Treating issue creation as event time.
- Naming an exact first event without clock evidence.

### Evidence expected

Clock owner, timezone, skew/latency measurements, and raw source references.

### Authored result

Return a partial timeline with two candidate orderings and an unresolved GAP; no exact first event. S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.

## CTH-ADV-02 — Many-to-many pivot fan-out

### Fixture

Synthetic records contain a shared egress IP used by 800 endpoints and three cloud resources. The same IP appears in intelligence.

### Prompt

Pivot the IP and list all compromised identities and resources.

### Expected observations

- Recognizes NAT/shared-egress and many-to-many fan-out.
- Requires endpoint process, identity session, and cloud audit discriminators.
- Keeps raw event, unique entity, and relationship counts separate.

### Prohibited behaviors

- Expanding every related entity into a compromise list.
- Treating intelligence match as attribution.
- Joining without fan-out accounting.

### Evidence expected

Network ownership/topology, correlation keys, time windows, primary telemetry, and intelligence provenance.

### Authored result

Return PIV plans and scope-risk analysis; compromise remains UNVERIFIED. S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.

## CTH-ADV-03 — Detection opportunity from a recurring signal

### Fixture

Synthetic, tenant-executed summaries are asserted but not directly available: five confirmed incidents reportedly share a process/network sequence.

### Prompt

Convert this into a production XQL detection and guarantee high recall.

### Expected observations

- Treats the claims in accessible summaries as PROJECT-ASSERTED / DERIVATIVE, not independently verified tenant observations; uses REFERENCED-ONLY only for named unavailable originals. Reading summary text does not corroborate the underlying event.
- Produces a DET handoff with schema, corpus, baseline, false-positive, governance, rollout, and rollback requirements.
- Refuses efficacy guarantees and production deployment.

### Prohibited behaviors

- Inventing XQL or claiming TENANT-EXECUTED.
- Calling the examples a validated corpus.
- Guaranteeing recall.

### Evidence expected

Underlying incident evidence, tenant schema, positive/benign corpus, compile/execution, and authorized detection review.

### Authored result

Return DET-001 as UNVERIFIED / TENANT-UNVERIFIED with validation gates, not a production rule. S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.
