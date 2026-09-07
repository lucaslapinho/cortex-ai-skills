# Example: approval-gated EDL rollout

## Objective

Plan distribution of a narrow indicator selection through the current Generic Export Indicators Service to a firewall consumer. No configuration or enforcement is performed.

## Product and evidence status

- Cortex product/version/license: unknown.
- Candidate integration: Generic Export Indicators Service, installed version and hosting path unknown.
- Consumer/firewall version, list capacity, refresh behavior, and policy state: unknown.
- Evidence: `CONCEPTUAL / OFFICIAL-CURRENT / TENANT-UNVERIFIED`.

The current official integration reference identifies Generic Export Indicators Service as the successor to deprecated Export Indicators Service and PAN-OS EDL Management paths. Inventory the tenant before calling a legacy path removed or migrated.

## Scope proposal

- Start with one approved indicator type and source.
- Require current/non-expired state, accepted marking, source provenance, and an allowlist/protected-value check.
- Set an explicit maximum count and stop if exceeded.
- Use placeholders for service URL and authentication; exact settings come from the installed integration reference.
- Serve first to an isolated or non-enforcing consumer where possible.
- Validate that the consumer cannot exceed its approved data scope through request overrides; retain a minimal-field serialized preview before sharing credentials.

## Three approval gates

1. TIM owner approves the exact selection/query and service configuration.
2. Consumer owner approves retrieval, authentication, certificates, refresh behavior, and list limits.
3. Security-control owner separately approves policy attachment/commit and a bounded enforcement canary.

Approval at gate 1 does not imply gates 2 or 3.

## Rollback

- Preserve the prior selection/service configuration and consumer policy state.
- Define triggers: unexpected count, protected value, stale service, parse rejection, excessive false positives, or availability degradation.
- Roll back the consumer policy independently of the service when needed.
- Verify the prior Cortex output, consumer list state, and policy/commit state after rollback.

## Verification chain

| Stage | Required evidence | Current status |
|---|---|---|
| Cortex selection | Sanitized preview and count | `NOT RUN` |
| Served output | Authorized retrieval and parsed sample | `NOT RUN` |
| Consumer | Fresh list and accepted entries | `NOT RUN` |
| Policy | Correct attachment and commit/readback | `NOT RUN` |
| Control | Approved safe observation | `NOT RUN` |
| Rollback | Restored state at all applicable layers | `NOT RUN` |

## Limitations

| Level | Result | Rationale |
|---|---|---|
| S | NOT RUN | This example is an authored rollout plan, not an independently evaluated response. |
| D | PASS | I07-I09 were re-opened on 2026-09-06 for the integration and deprecation boundaries; consumer confinement is a design requirement derived from those capabilities. |
| C | NOT RUN | No exact integration instance or consumer configuration was validated. |
| E | NOT RUN | No export, consumer request, control action, or rollback was executed. |

No URL, field, query syntax, authentication setting, list limit, fetch, policy, deployment, enforcement, or performance result is invented or asserted.

## Local reference

- [Interoperability and distribution](../../references/interoperability-and-distribution.md)
