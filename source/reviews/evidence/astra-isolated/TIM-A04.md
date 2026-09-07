# Astra forward output — cortex-tim-engineer

Model requested: `gpt-6-astra`, high reasoning; ephemeral CLI, manual inline runtime load.

Runtime: 21 files / 126788 bytes; ordinal SHA-256 `e2e49820268e45ee8017ce67d397cb73d9d08cdfd80fc7dc9b16e1f58b2de0fb`.

Isolation: 0 tool/action events. Runtime files plus Fixture/Prompt only; no oracle text supplied. One fresh ephemeral process contains this case only. No self-grading result is assigned here. Independent adjudication is required.

## Input TIM-A04

### Fixture

A team wants to export “bad” indicators and immediately block them on a firewall. It proposes giving the same Generic Export Indicators Service credential to a partner authorized for only one subset, relying on the default query to confine that partner. The partner also requests alternate query/format/count URL parameters and all available CSV fields.

### Prompt

Design the control gates and verification chain, assess the partner-access proposal, and report S/D/C/E separately with rationales.

Local Markdown links are rebased for publication only; wording and attribution are unchanged. Raw response/event files remain in the evaluation archive outside the publication tree.

## Retained response

**TIM-A04**

The partner-access proposal does not establish adequate confinement. Keep distribution and firewall enforcement pending separate gates; a “bad” assessment alone does not authorize blocking.

This is a **`CONCEPTUAL` design**, based on supplied material as of **2026-09-06**. Cortex product, SaaS/on-premises deployment, build, entitlement, installed integration/pack version, engine placement, effective permissions, and firewall version are unknown. Tenant behavior remains **`UNVERIFIED / TENANT-UNVERIFIED`**. Official pages were not reopened.

**Partner access**

The supplied interoperability reference reports that Generic Export Indicators Service supports request-level `q`, `n`, and `v` overrides, and that its JSON/CSV `Exported Fields` setting can expose all XSOAR fields when set to `all`. These are **`VERSION-DEPENDENT / PROJECT-ASSERTED / REFERENCED-ONLY`** here; XSIAM field behavior remains **`UNVERIFIED`**.

The resulting assessment is **`INFERRED`**: authentication and a narrow default query do not prove that a partner is restricted to its authorized subset. Shared credentials also prevent independent credential revocation and weaken attribution.

The proposed access design should require:

- A separate partner identity or credential, with least privilege and independent revocation.
- Enforced restrictions on the partner’s permitted indicators, fields, formats, and maximum count. Separate credentials alone do not establish those restrictions.
- A minimal approved field list and sanitized serialized preview. The request for all CSV fields is not justified by subset authorization.
- Negative access tests showing that alternate requests cannot return unauthorized indicators or fields, or exceed approved limits.

Those restrictions are **conceptual requirements**, not assumed native integration settings. If the installed service cannot demonstrate confinement, use a separately governed fixed export containing only approved data. Withhold partner access until confinement is established.

**Scope and gates**

Keep the six layers distinct: collection establishes source observations; management establishes identity, provenance, and assessments; enrichment adds separately governed context; lifecycle determines current eligibility; distribution serves an approved selection; security-control operationalization changes firewall behavior.

| Gate | Required reviewable evidence | Approval owner |
|---|---|---|
| Product and source applicability | Exact product/build, entitlement, installed integration, permissions, hosting, source contract, and applicable official references | Cortex platform and source owners |
| Indicator eligibility | Exact selection and sanitized preview; expected count and hard maximum; types, provenance, timestamps, accepted markings, current lifecycle state, and protected-value/allowlist checks | TIM owner |
| Distribution and partner confinement | Exact service and destinations; minimal fields; TLS/authentication review; successful authorized retrieval and negative access tests | TIM/data owner and partner-access owner |
| Firewall consumption | Exact devices and list; accepted entries, freshness, refresh interval, capacity, parse-error handling, and stale/unavailable-list behavior | Firewall consumer owner |
| Enforcement | Exact policy attachment and activation scope, false-positive review, bounded canary, stop criteria, monitoring, and recoverable prior policy state | Security-control owner |

All gates remain pending. No named approvers, authorized operators, or retained previews were supplied.

“Bad” needs a named assessment source and verified mapping. Keep source reliability, assertion confidence, reputation/verdict, DBotScore, and tags separate. Where an integration actually emits DBotScore, the supplied convention identifies `3` as Bad/Malicious and `0` as Unknown; neither is a probability or enforcement authorization. Its applicability here is **`UNVERIFIED / REFERENCED-ONLY`**.

Generic Export Indicators Service is the candidate for this design. The supplied register identifies **Export Indicators Service** and **PAN-OS EDL Management** as deprecated successors’ predecessors: **`DEPRECATED / PROJECT-ASSERTED / REFERENCED-ONLY`**. It also reports a PAN-OS EDL Management support exception for customers with more than 1,000 firewalls. Current applicability requires verification; deprecation does not establish tenant removal.

**Verification and rollback**

The proposed verification chain is:

1. Reconcile the approved Cortex selection, count, provenance, and lifecycle eligibility.
2. Inspect actual served output for membership, serialization, markings, and field disclosure.
3. Verify partner confinement independently of default-request success.
4. Verify firewall retrieval, parsing, accepted entries, and list freshness.
5. Read back the intended policy attachment and committed/active state.
6. Observe control behavior through an approved safe canary.

Export success establishes neither consumer receipt nor blocking. Expiration, source withdrawal, downstream removal, and deletion require separate evidence; reactivation must trigger a fresh eligibility decision.

Before changes, retain service configuration, selection, credentials’ access scope, and firewall policy before-state. Assign operators, a bounded UTC window, maximum volume, monitoring owner, and independent distribution/control rollback owners. Stop on unauthorized disclosure, protected values, count overruns, stale output, parse failures, false positives, or availability degradation. Retain timestamped evidence and artifact hashes where practical; verify restoration at Cortex and each consumer.

**Validation status**

| Level | Result | Rationale |
|---|---|---|
| S | NOT RUN | No independent controlled response evaluation was available. |
| D | NOT RUN | Only supplied resources were read; current official sources were not reopened. |
| C | NOT RUN | No exact tenant configuration, schema, or acceptance evidence was supplied. |
| E | NOT RUN | No distribution, partner-access test, firewall retrieval, enforcement, or rollback was executed or observed. |

Reference targets, **referenced only**: [Generic Export Indicators Service](https://xsoar.pan.dev/docs/reference/integrations/edl), [Export Indicators Service](https://xsoar.pan.dev/docs/reference/integrations/export-indicators), and [PAN-OS EDL Management](https://xsoar.pan.dev/docs/reference/integrations/palo-alto-networks-pan-os-edl-management).
