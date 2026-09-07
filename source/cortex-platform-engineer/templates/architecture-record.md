# Cortex Platform Architecture Record

Use for architecture, deployment, or product-boundary reviews. Replace every placeholder; never preserve bracketed text as an asserted tenant fact.

## Objective and success criteria

- Business objective:
- Observable success:
- Explicit non-goals:
- Environment:
- Change authorized: `No / Yes — approval reference`

## Applicable products and deployments

| Product | Deployment | Version/build | License/add-on | Tenant/environment | Evidence |
|---|---|---|---|---|---|
| `<XSIAM / XDR / XSOAR>` | `<SaaS / On-prem>` | `<value / Unknown>` | `<value / Unknown>` | `<sanitized alias>` | `<status / source>` |

## Evidence status

- Canonical status:
- Qualifiers:
- Documentation review date:
- Tenant evidence available:
- Tenant evidence missing:
- Freshness risks:

## Expected data or object

- Event/object:
- Source:
- Generation condition:
- Source timestamp/timezone:
- Correlation marker:
- Classification/sensitive fields:
- Expected volume and basis:

## End-to-end path

| Layer | Component/input | Expected output | Owner | Trust boundary | Evidence | State |
|---|---|---|---|---|---|---|
| Data |  |  |  |  |  |  |
| Source/export |  |  |  |  |  |  |
| Collector/agent/integration |  |  |  |  |  |  |
| Transport |  |  |  |  |  |  |
| Ingestion |  |  |  |  |  |  |
| Parsing |  |  |  |  |  |  |
| Mapping |  |  |  |  |  |  |
| Dataset/object |  |  |  |  |  |  |
| Query/consumer |  |  |  |  |  |  |

Allowed layer states: `Observed healthy`, `Observed failed`, `Not observed`, `Not applicable`. Record a timestamp and identity for observations.

## Component decision

| Candidate | Supported target evidence | Fit | License/version gap | Operational owner | Decision |
|---|---|---|---|---|---|
| Cortex XDR agent |  |  |  |  |  |
| Broker VM/applet |  |  |  |  |  |
| XDR Collector |  |  |  |  |  |
| Integration |  |  |  |  |  |
| Cortex Engine (name product/version) |  |  |  |  |  |

## Identity and credentials

| Boundary | Principal | Required privilege | Secret location/custodian | Rotation | Audit |
|---|---|---|---|---|---|
|  |  |  | `<approved secret store; no value>` |  |  |

## Availability, capacity, and retention

- Observed event size/rate/burst:
- Published guidance and exact version:
- Failure domain:
- Supported HA/retry model:
- Buffer/replay/duplicate semantics:
- Recovery objective/data-loss tolerance:
- Retention/data residency:
- Load/failover tests:

## Failure model

| Failure point | User-visible effect | Detection signal | Owner | Safe check | Recovery |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Change and rollback

- Exact target:
- Current configuration/export/hash:
- Proposed change and authoritative source:
- Scope/exclusions:
- Approval/window:
- Canary/non-production:
- Timeout/retry/idempotency:
- Blast radius:
- Rollback trigger/steps/owner:
- Post-change checks:

## Validation

- [ ] Product/deployment/version/license confirmed
- [ ] Expected event generated
- [ ] Source export/fetch observed
- [ ] Component receive/send observed
- [ ] Transport/ingestion observed
- [ ] Raw record observed
- [ ] Parsing validated
- [ ] Mapping validated
- [ ] Dataset/schema/retention confirmed
- [ ] Intended identity can query
- [ ] Negative identity denied
- [ ] Gap/duplicate/latency checked
- [ ] Rollback/cleanup and audit verified

Record unchecked items as `NOT RUN`, not as failures or passes.

## Official references

- `<exact product/version page>`

## Handoff

- Open risks:
- Next owner:
- Required evidence:
- Decision deadline:
