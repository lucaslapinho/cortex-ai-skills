# Evaluation and operations

Engineering method: define controls and acceptance criteria before testing. Use authorized environments and synthetic data.

| Fixture class | What to observe |
|---|---|
| Benign supported request | Allowed behavior, application quality and latency |
| Direct and indirect injection | Decision plus application/tool outcome; retrieved content cannot grant authority |
| Multilingual/encoded/long input | Documented handling and limits, false positives/negatives |
| Sensitive data in request/response/tool result | Which direction and channel is inspected; sanitized evidence |
| Malicious or changed artifact | Identity/hash, scanner result and deployment gate |
| Tool misuse | Deterministic target/permission checks independent of model verdict |
| Timeout/unavailable/malformed response | Fail-open/closed decision, retry bounds, idempotency and observability |
| Bypass route or unsupported mode | Uninspected flow identified; no claim of universal protection |

Record corpus version, app/model/policy version, observed action, ground truth, evaluator and review date. Report sample sizes and unresolved cases; do not equate a few successful blocks with 100% detection. A monitor-only finding and a blocked action are different results.

Deployment gates: verified support and permissions → sanitized offline test → bounded integration acceptance → authorized pilot → observed traffic and rollback rehearsal → production decision by the accountable owner. Existing authorization can cover an appropriate step; do not ask repeatedly for the same permission.

An AI-generated severity or recommendation is advisory. The application still owns authentication, tool authorization, destination allowlists, transaction limits and audit. Notifications should avoid raw sensitive prompts and must escape untrusted fields before rendering HTML. SOC exports require a verified connector/schema and an observed known-positive event; product adjacency is not an integration contract.
