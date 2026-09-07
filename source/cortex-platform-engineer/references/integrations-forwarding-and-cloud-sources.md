# Integrations, Forwarding, and Cloud Sources

Use this reference to keep inbound collection, command execution, and outbound forwarding separate.

## Contents

- Direction matrix
- Integration-instance contract
- Vendor and generic collection
- Syslog and HTTP
- Cloud sources
- Event-collection integration boundary
- Content-pack contribution and validation boundary
- External alert legacy boundary
- Outbound forwarding
- Failure and validation checks

## Direction matrix

| Direction/surface | Source | Cortex role | Destination |
|---|---|---|---|
| Inbound push | Syslog/HTTP/source exporter | Receiver, ingestion, parser/mapping | Dataset/XDM/query |
| Inbound pull | Vendor/cloud API | Integration/collector fetch | Dataset/object |
| Bidirectional command | Integration instance | Credentialed command execution | External system and Cortex context |
| Outbound notification | Case/Issue/log event | Forwarding configuration/integration | Email, syslog, webhook, or documented service |
| Outbound data/event | Dataset/event forwarding surface | Filter/serialize/deliver | Documented sink |

Do not apply an outbound forwarding page to inbound ingestion or vice versa.

## Integration-instance contract

Record:

- product, deployment, version, content pack/integration version;
- instance purpose and supported commands/fetch behavior;
- credential type and custodian;
- source API scope and Cortex RBAC/command permissions;
- Engine/Broker/tenant execution location;
- fetch window, cursor, duplicate and retry semantics;
- source rate/burst and target limits;
- incident/Case/Issue or dataset destination;
- health/test command scope;
- audit, monitoring, rollback, and owner.

A successful “test” usually proves only the documented connectivity/authentication check. It does not prove scheduled fetching, full permissions, parsing, object mapping, query visibility, or command safety.

Sources: [Add an integration instance](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Add-an-integration-instance) and [Troubleshoot integrations](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Troubleshoot-Integrations).

## Vendor and generic collection

Prefer a current product-specific catalog entry. Verify:

- supported source/service and log/object type;
- target product/license;
- direct SaaS, cloud role, Broker applet, XDR Collector, or integration path;
- source permissions and filtering;
- payload format and source identity;
- content/parser/mapping dependencies;
- resulting dataset/object;
- documented limitations and health surfaces.

A generic collector can accept a format without providing vendor-specific normalization or analytic support. Do not promise equivalent outcomes.

Source: [Vendor-specific data sources and connectors](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/cortex-xsiam-data-sources/vendor-specific-data-sources-and-connectors.md).

## Syslog and HTTP

For syslog:

- use the product/version-specific Broker VM applet page;
- verify supported transport/framing and source format;
- choose listening values from the current page and target network policy;
- establish certificate and source-allowlist ownership where applicable;
- compare received and sent evidence before tenant ingestion;
- load-test under the documented sizing assumptions.

Source: [Activate Syslog Collector — XSIAM 3.x](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Activate-Syslog-Collector).

For XSIAM HTTP Log Collector:

- current documentation covers Raw, JSON, CEF, and LEEF;
- use the generated collector URL/key from the tenant, never an invented endpoint or key;
- verify compression, content type, event delimiters, request/event bounds, response handling, and raw dataset behavior from the current page;
- use placeholders and do not log the authorization value.

Source: [Set up an HTTP Log Collector](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Set-up-an-HTTP-log-collector-to-receive-logs?contentId=XAfILj87fu6SWS8m7EbtYw).

Exact ports, capacity, record sizes, and response codes are version-sensitive. Re-open the source rather than copying them from this Skill.

## Cloud sources

Treat each cloud service as a chain of trust zones:

`cloud event/log → cloud export service → cloud role/resource policy → Cortex integration endpoint → ingestion → raw dataset → optional normalization → query`

For Amazon CloudWatch, current XSIAM documentation distinguishes generic and EKS collection, documents an AWS delivery path, route-specific datasets, and optional normalization. That does not establish that any AWS resource, role, dataset, or enhanced-cloud entitlement exists in a tenant.

Source: [Ingest logs from Amazon CloudWatch](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Ingest-logs-from-Amazon-CloudWatch?contentId=Qbap8p2r9Ahu31V8T7XmYg).

For every cloud source verify:

- account/subscription/project and region;
- source log enablement and retention;
- resource policy and least-privilege role;
- cross-account trust and external identifiers where documented;
- queue/stream/bucket delivery evidence;
- encryption key and key-policy access;
- failed-delivery/dead-letter behavior;
- Cortex instance status and last fetch/ingestion evidence;
- raw and normalized query visibility.

Never invent cloud policy JSON or resource identifiers. Generate them only from the current product wizard/documentation and review them with the cloud owner.

## Event-collection integration boundary

The current Palo Alto developer page for XSIAM event-collection integrations states that `send_events_to_xsiam()` works only in system integrations and fails in custom integrations. Therefore:

- do not propose it for a custom integration;
- validate the supported custom integration collection contract and metadata from the current developer page;
- pin the content/integration version;
- test locally where the official toolchain supports it, then in a non-production tenant;
- do not claim Marketplace or tenant import success from static validation.

Source: [Event Collection Integrations](https://xsoar.pan.dev/docs/integrations/event-collectors).

## Content-pack contribution and validation boundary

Treat a content pack as a versioned source artifact with a declared target, support
model, dependencies, documentation, and test evidence. Do not conflate these states:

1. source tree created locally;
2. applicable local format, validation, lint, unit, or test-playbook checks executed;
3. pull request reviewed and accepted;
4. content published to a named Marketplace;
5. exact version installed in a named tenant;
6. bounded behavior executed and observed in that tenant.

For contribution work:

- identify whether the target is XSOAR, XSOAR On-prem, XSOAR SaaS, XSIAM/
  `marketplacev2`, or another currently documented marketplace value;
- identify the official, partner, or community support model and its owner;
- require the current pack structure, `pack_metadata.json`, README, and applicable
  release notes/entity files;
- record dependency and compatibility decisions rather than copying entity IDs or
  versions from another product;
- use the current official contribution instructions for the applicable local
  `demisto-sdk validate` flow and, where integrations or scripts are present, the
  applicable lint/unit-test flow;
- run the SDK in a currently supported development environment. At this review cut,
  the official repository names Linux, macOS, and WSL2 and explicitly says native
  Windows is unsupported; use WSL2 or a container there, and record that boundary;
- pin the SDK version or reviewed commit and record whether required network,
  Docker, and other toolchain dependencies were available, because skipped checks
  do not establish a complete validation pass;
- retain the exact tool version, command scope, exit status, and output before
  claiming a local pass;
- require separate review, Marketplace, tenant-import, and bounded runtime evidence
  for every later state.

If the commands were not actually run, state `NOT RUN`; never display a hypothetical
command as a completed check. The Platform Skill owns packaging, dependencies,
integration lifecycle, and environment boundaries. Hand playbook graph/branch logic
to the playbook specialist and detection semantics to the detection specialist.

Sources: [Contributing XSOAR Content](https://xsoar.pan.dev/docs/contributing/contributing),
[Contribution Checklist](https://xsoar.pan.dev/docs/contributing/checklist), and
[Content Packs Structure](https://xsoar.pan.dev/docs/packs/packs-format). Supported
development-host and tool-dependency boundaries come from the current
[Demisto SDK repository](https://github.com/demisto/demisto-sdk).

## External alert legacy boundary

Current XSIAM administrative guidance discusses external alert ingestion. Current Platform API release notes list Insert Parsed Alerts as a legacy Alert API without an identified successor, and identify old XSIAM 2.x API documentation as deprecated/unmaintained.

Required behavior:

- do not invent a modern successor;
- do not reuse an old payload, field-requiredness, license, limit, or response schema as current;
- identify the target version and migration objective;
- obtain the version-pinned legacy API artifact if compatibility is required;
- validate it with vendor support/current tenant documentation before implementation;
- prefer current Case/Issue API families only for their documented purposes, not as an assumed ingestion replacement.

Sources: [Ingest external alerts](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Ingest-external-alerts) and [XSIAM API release notes](https://cortex-docs.paloaltonetworks.com/xsiam-api/api-release-notes#legacy-apis-without-identified-successor-apis).

## Outbound forwarding

Current XSIAM guidance documents forwarding of selected logs/data and Case/Issue notifications to supported destinations. Destination support varies by object type and format.

Verify:

- inbound object type and filter/scope;
- supported destination for that object;
- current/legacy format choice;
- destination credential and network boundary;
- payload minimization and privacy;
- grouping/batching, ordering, duplicate, and retry semantics;
- destination acceptance and correlation ID;
- partial failure, backlog, replay, and audit behavior.

Sources: [Data and log forwarding](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Data-and-log-forwarding) and [Configure notification forwarding](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Configure-notification-forwarding).

Do not call a forwarding configuration “working” from a successful save. Generate or select one authorized test object and verify destination receipt.

## Failure and validation checks

| Symptom | Competing hypotheses | Discriminating checks |
|---|---|---|
| Integration test passes, no data | Fetch disabled/window wrong; source returns none; downstream mapping/access issue | Source count, fetch audit/cursor, raw object/query |
| Collector receives, tenant sees none | Send/transport issue; rejection/license/format issue | Collector send evidence, ingestion response/metric |
| Raw rows, no normalized rows | Parser/mapping not applicable, invalid, or missing | Raw fixture, rule versions, parser/mapping error evidence |
| Duplicate objects | Source replay; cursor reset; retry non-idempotent; destination dedup mismatch | Correlation marker, fetch window, retry/audit trail |
| Forwarding missing | Filter excluded object; destination unsupported; credential/delivery failure | Scope evaluation, object compatibility, destination audit |

Use a controlled, sanitized marker and fixed time window. Preserve both successful and negative observations.
