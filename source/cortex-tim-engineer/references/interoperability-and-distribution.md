# Interoperability and controlled distribution

## Contents

- [Core rule](#core-rule)
- [Integration-family matrix](#integration-family-matrix)
- [STIX and TAXII](#stix-and-taxii)
- [MISP](#misp)
- [OpenCTI](#opencti)
- [EDL and Generic Export Indicators Service](#edl-and-generic-export-indicators-service)
- [Distribution is not enforcement](#distribution-is-not-enforcement)
- [Network and authentication boundary](#network-and-authentication-boundary)
- [Change-control sequence](#change-control-sequence)
- [Interoperability validation](#interoperability-validation)

## Core rule

A protocol standard describes an interchange model. A Cortex integration implements a particular subset, direction, mapping, authentication model, and operational behavior. Never replace exact integration documentation with generic protocol knowledge.

For every path, record:

```text
producer -> interface/integration + version -> transformation/mapping -> Cortex product + version
         -> selection/query -> export/service + version -> consumer -> security policy/control
```

Validate each arrow separately.

## Integration-family matrix

The table is a documentation map reviewed on 2026-09-04, not a tenant inventory.

| Named official integration/capability | Direction and scope supported by its current reference | Critical boundary |
|---|---|---|
| TAXII Feed | Inbound TAXII 1.x feed; reference lists supported Cortex products/minimum versions | Do not use it as TAXII 2 or outbound-server evidence. |
| TAXII 2 Feed | Inbound TAXII 2.0/2.1 feed; reference lists XSOAR and XSIAM availability | The complex-observation representation note explicitly names XSOAR TIM; XSIAM applicability, mappings and settings require separate exact evidence. |
| TAXII Server | Outbound, long-running TAXII 1.x server integration | The documented collection-as-indicator-query wording explicitly names Cortex XSOAR. XSIAM selection semantics are unverified; endpoint/auth/deployment behavior is product-specific. |
| TAXII 2 Server | Outbound TAXII 2.0/2.1, long-running server integration | The documented collection-query and API/object wording explicitly names Cortex XSOAR. XSIAM selection/object semantics are unverified; XSOAR 6, XSOAR 8, XSIAM, and engine-hosted paths differ, so do not invent a URL. |
| MISP v3 | Named MISP integration with feed/command behavior in its reference | Upgrade notes include breaking changes; verify installed pack and exact configuration. |
| MISP Feed | Separate inbound feed integration | Do not equate its behavior with MISP v3 or generic MISP semantics. |
| OpenCTI Feed 4.x | Current named OpenCTI feed family; reference lists XSOAR/XSIAM availability and an OpenCTI compatibility baseline | Its out-of-box type list and automatic-creation wording explicitly name XSOAR; XSIAM mapping remains unverified. |
| OpenCTI Feed 3.x | Older integration | Official reference marks it deprecated in favor of OpenCTI 4.x. |
| Generic Export Indicators Service | Current long-running service for serving selected indicators, including EDL use | Hosting, auth, certificate, and engine/tenant settings vary. |
| Export Indicators Service | Older export service | Official integration reference marks it deprecated in favor of Generic Export Indicators Service. |
| PAN-OS EDL Management | Legacy integration path | Official integration reference marks it deprecated in favor of Generic Export Indicators Service. |
| Table export | Current XSIAM UI documentation describes CSV and STIX export | A downloaded file is not a continuous feed or downstream policy change. |

The current rows are `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` until the named tenant is inspected. `OpenCTI Feed 3.x`, `Export Indicators Service`, and `PAN-OS EDL Management` are instead `DEPRECATED / OFFICIAL-CURRENT / TENANT-UNVERIFIED`: current official references identify their replacements, but no tenant state was inspected.

## STIX and TAXII

Keep the following separate:

- STIX object/pattern semantics;
- TAXII protocol version and collection behavior;
- inbound TAXII feed behavior;
- outbound TAXII server behavior;
- Cortex indicator representation;
- mapping of source fields, markings, relationships, and revocation;
- export serialization and consumer interpretation.

For inbound TAXII:

1. confirm TAXII 1.x versus 2.0/2.1;
2. confirm collection, auth, TLS, time window, pagination, and rate behavior;
3. inspect representative objects and patterns as untrusted data;
4. verify exact integration mapping and ignored expressions;
5. test create/update/replay/revoke/expire behavior in a bounded environment;
6. compare source counts and object hashes with Cortex readback;
7. document any relationship or marking loss.

For outbound TAXII:

1. confirm the server integration and protocol version;
2. for XSOAR, validate exact supported indicator-query syntax; for XSIAM, obtain current product/tenant evidence for selection semantics; define collection ownership;
3. validate exposure, authentication, certificate, engine placement, and availability;
4. test authorized and unauthorized access;
5. verify pagination and stable retrieval at the consumer;
6. test withdrawal/expiration behavior explicitly;
7. monitor service and consumer independently.

Never publish documentation examples as tenant endpoints. Do not claim lossless round-trip fidelity without a retained comparison.

## MISP

“MISP support” is insufficient. Determine whether the requirement uses the MISP v3 integration, MISP Feed, or another currently documented package component. Validate:

- product and installed content/integration version;
- direction and supported operations;
- URL/auth/TLS without exposing secrets;
- event/attribute scope and markings;
- mapping, type handling, tags, scores, and timestamps;
- incremental collection, pagination, update, and deletion semantics;
- upgrade/breaking-change notes;
- bounded test and readback.

Do not assume a MISP tag becomes a Cortex tag, a MISP confidence value becomes DBotScore, or source deletion becomes indicator deletion.

## OpenCTI

The current official OpenCTI Feed 4.x integration reference reviewed for this Skill states availability for XSOAR and XSIAM and compatibility with OpenCTI 5.12.17 or later. Its out-of-box indicator-type list and automatic-creation wording explicitly name XSOAR. Treat that mapping statement as XSOAR-scoped, keep XSIAM mapping `UNVERIFIED`, and treat the compatibility version as time-sensitive; re-open the page before implementation.

The older OpenCTI Feed integration reference is deprecated in favor of the 4.x integration. A migration assessment should include:

- current OpenCTI server version;
- installed Cortex content pack/integration version;
- supported versus unmapped object/indicator types;
- authentication and permissions;
- pagination/checkpoint and replay behavior;
- markings, relationships, scores, and revocation mapping;
- parallel-run or rollback plan;
- source-to-Cortex count and sample reconciliation.

Do not infer that every OpenCTI entity becomes an indicator or that a graph is preserved merely because connectivity succeeds.

**Documentation discrepancy, checked 2026-09-06:** the OpenCTI Feed 4.x `last_run_id` argument text points to `OpenCTI.IndicatorsList.LastRunID`, while its example nests `lastRunID` under `OpenCTI.Indicators`; the same page says the command has no context output. Preserve this conflict. The usable pagination-output path is `UNVERIFIED` until installed command metadata, pinned applicable implementation, or controlled tenant readback resolves it. Do not repair the path by guessing capitalization or nesting.

## EDL and Generic Export Indicators Service

Use the current Generic Export Indicators Service integration reference and current product EDL/export documentation for new designs. It is a long-running service that can host selected indicator output for consumers. Exact instance settings, filters, output format, URL structure, authentication, certificates, tenant/engine deployment, and limits must come from the current reference and tenant configuration.

An EDL design must specify:

- exact indicator selection/query and type constraints;
- markings, allowlists, age/expiration, confidence/verdict policy, and maximum scope;
- stable serialization and handling of invalid entries;
- access control, TLS, exposure, logging, and secret rotation;
- refresh cadence and fail-open/fail-closed behavior at the consumer;
- list-size and consumer capacity assumptions;
- health checks and stale-list detection;
- rollback to a retained known-good selection/configuration;
- Cortex service readback, consumer fetch readback, and policy/enforcement readback as three separate checks.

### Consumer confinement

The [current integration reference](https://xsoar.pan.dev/docs/reference/integrations/edl), re-opened on 2026-09-06, documents request-level `q`, `n`, and `v` overrides. Its JSON/CSV `Exported Fields` option can expose all XSOAR fields when set to `all`; XSIAM field behavior still requires applicable evidence. These are `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` claims.

**Design implication — `INFERRED`:** a narrow default query and authentication do not establish a consumer's allowed data scope. Before sharing credentials, test whether that consumer can broaden selection, format, fields, or count. Require enforced request/data restrictions or a separately governed fixed export for narrower-trust consumers; these are conceptual controls, not assumed native settings. Minimize fields and inspect serialized output. If confinement cannot be demonstrated, withhold distribution to that consumer.

Mark the older Export Indicators Service and PAN-OS EDL Management integration paths `DEPRECATED / OFFICIAL-CURRENT` where their current official references say so. The PAN-OS EDL Management page retains an explicit support exception for customers with more than 1,000 firewalls; confirm applicability with the product owner before a migration decision. Deprecation does not prove immediate removal from a tenant; inventory and migration evidence are still required.

## Distribution is not enforcement

Use this chain:

```text
Cortex selection
  -> serialized/served output
  -> authenticated consumer fetch
  -> consumer validation
  -> policy attachment
  -> policy commit/activation
  -> observed control behavior
```

Success at one stage proves nothing about later stages. In particular:

- export success is not consumer fetch success;
- fetch success is not policy attachment;
- policy attachment is not committed enforcement;
- a block action is not necessarily correct or effective;
- absence of alerts is not evidence that blocking worked.

Security-control operationalization requires independent approval, protected-asset and allowlist checks, bounded rollout, owner, rollback, and verification.

## Network and authentication boundary

Long-running integrations can expose services or route through engines. Validate:

- supported hosting location for the exact product/version;
- inbound/outbound network path and source restrictions;
- certificate trust and hostname validation;
- supported authentication and credential storage;
- proxy/load-balancer behavior if applicable;
- least-privilege service identity and rotation;
- logging without secrets;
- availability, restart, upgrade, and health monitoring;
- rate and denial-of-service controls.

Never recommend disabling certificate validation as a routine fix. A temporary exception, if the product supports one, needs explicit risk acceptance, tight scope, expiry, and a remediation owner.

## Change-control sequence

1. Verify official capability and tenant applicability.
2. Inventory source, service, consumers, and downstream controls.
3. Define a narrow selection and sanitized preview.
4. Test in a non-production or isolated consumer where possible.
5. Obtain approval for distribution and separate approval for enforcement.
6. Retain the exact before state and rollback artifact.
7. Roll out in bounded stages with stop criteria.
8. Read back Cortex output, consumer state, and control state independently.
9. Monitor false positives, staleness, availability, size, and latency without claiming unmeasured capacity.
10. Record outcome, exceptions, and rollback readiness.

## Interoperability validation

- [ ] Named integration, direction, protocol version, product, license, deployment, and pack version confirmed
- [ ] Generic protocol behavior not substituted for product behavior
- [ ] Data contract, mappings, ignored objects, relationships, markings, and revocation assessed
- [ ] Pagination/checkpoint/replay and source mutation bounded
- [ ] Credentials, TLS, exposure, and engine routing reviewed
- [ ] Deprecated integration identified and migration planned where applicable
- [ ] Selection/filter reviewed for privacy and false-positive risk
- [ ] Distribution approval separate from enforcement approval
- [ ] Cortex, consumer, and control readback separated
- [ ] Import, deployment, execution, and performance status not overstated
