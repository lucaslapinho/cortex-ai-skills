# Example: End-to-End Syslog Design

## Objective and success criteria

Design a Cortex XSIAM 3.x path for a network appliance to send syslog through a Broker VM applet. Success means one authorized, sanitized marker is proven at the source, collector, ingestion, raw-dataset, and intended query layers.

## Applicable product and evidence

- Product: Cortex XSIAM 3.x.
- Deployment: SaaS tenant with customer-network Broker VM.
- License/add-on: `Unknown`; must be confirmed.
- Status: `CONCEPTUAL / OFFICIAL-CURRENT / TENANT-UNVERIFIED`.
- No tenant, Broker, source, port, certificate, dataset, volume, or result was inspected.

Official boundary: [Activate Syslog Collector](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Activate-Syslog-Collector).

## Expected path

| Layer | Expected state | Trust/owner | Failure point |
|---|---|---|---|
| Data | Sanitized appliance event with unique marker and source time | Source owner | Event not generated or filtered |
| Source export | Syslog export enabled in a currently supported format | Source owner | Wrong facility/filter/format |
| Collector | Product-documented Syslog Collector applet receives the marker | Platform owner | Wrong listener/source allowlist/applet |
| Transport | Source-to-Broker and Broker-to-tenant paths meet current requirements | Network/platform owners | DNS, proxy, TLS/certificate, route |
| Ingestion | Tenant records receipt/health evidence | Platform owner | Entitlement, rejection, backpressure |
| Parsing/mapping | Raw record parsed; optional mapping tested separately | Data owner | Format/parser/mapping mismatch |
| Dataset | Literal raw dataset observed in tenant inventory | Data owner | Name assumed, creation delay, access |
| Query | Intended identity retrieves marker in a bounded window | Query/identity owners | Retention, RBAC/SBAC, timeframe/filter |

## Trust and credential boundaries

- Source administrator controls export configuration.
- Network owner controls source-to-Broker route and certificate policy where applicable.
- Platform owner controls the hardened Broker VM and applet.
- Tenant owner controls license, ingestion, parser/mapping, and dataset access.
- Querying identity is subject to RBAC/SBAC and dataset permissions.

No secret belongs in the design document.

## Configuration plan

1. Confirm XSIAM release, entitlement, Broker version, and current syslog applet procedure.
2. Measure source event size/rate/burst; do not size from a universal limit.
3. Select transport, framing, format, and listening values from the current page and network policy.
4. Capture the current Broker/applet configuration and a supported recovery path.
5. Configure a non-production or bounded canary source under change approval.
6. Send one sanitized marker.
7. correlate source, receive, send, ingestion, raw, parsing/mapping, and query evidence.
8. test malformed, duplicate, delayed, denied-source, and recovery cases.

No literal port or throughput is supplied because the target version/topology was not inspected.

## Safety and rollback

- Named target/owner/approver and maintenance window are required.
- Preserve the supported current configuration/export.
- Bound the source to a canary and protect existing listeners.
- Define duplicate/replay behavior before retry.
- Roll back the source export and applet change if the marker fails or impacts existing traffic.
- Verify existing and new sources after any rollback.

## Validation status

- S: `NOT RUN` - this worked example was not independently oracle-scored; author/static review is not S evidence.
- D: `PASS` - the exact current Syslog Collector source and bounded XSIAM product claim were independently reviewed on 2026-09-04; this does not establish tenant applicability.
- C: `NOT RUN` - no named tenant, schema, configuration editor, or import was available.
- E: `NOT RUN` - no event was sent and no collection, ingestion, dataset, or query result was observed.

No connection, ingestion, dataset, or query result is claimed.
