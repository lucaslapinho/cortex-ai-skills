# Platform Troubleshooting

Use this reference to diagnose a Cortex platform symptom without guessing configuration or equating one health signal with the complete path.

## Contents

- Incident intake
- Evidence-safe method
- Missing telemetry decision path
- Component-specific checks
- Parsing and mapping checks
- Access and query checks
- Latency, gaps, and duplicates
- API and integration checks
- Change discipline
- Escalation packet

## Incident intake

Capture:

- exact symptom and first/last observed times;
- product, deployment, version/build, license, and environment;
- expected event/object and business impact;
- affected and unaffected sources/consumers;
- last known good event and change timeline;
- tenant identity and RBAC/SBAC/data scope;
- component aliases/versions without sensitive identifiers;
- current sanitized configuration hashes/exports;
- source, collector, transport, ingestion, parser, mapping, dataset, and query evidence;
- actions already attempted and their effects.

Normalize timezones before comparing observations. Preserve original timestamps.

## Evidence-safe method

1. Restate the symptom as an observable mismatch.
2. Draw the expected complete path.
3. Mark each layer `Observed healthy`, `Observed failed`, `Not observed`, or `Not applicable`.
4. Form at least two plausible hypotheses.
5. Choose the lowest-risk read-only check that produces different expected observations.
6. Update confidence only from evidence.
7. Safety-gate any change.
8. Verify the entire path after recovery and inspect for gaps/duplicates.

Do not use confidence adjectives as substitutes for evidence.

## Missing telemetry decision path

```text
Was the expected source event generated?
├─ no evidence → validate source behavior and export policy
└─ yes
   Was it offered to and received by the collector/integration?
   ├─ no evidence → inspect fetch/export, permissions, cursor, local read
   └─ yes
      Was it sent across the documented transport?
      ├─ no evidence → inspect component errors, queue/backpressure
      └─ yes
         Did Cortex record ingestion receipt/health?
         ├─ no evidence → inspect TLS/proxy/route, entitlement, format/rejection
         └─ yes
            Is a raw record visible?
            ├─ no → inspect dataset creation, indexing, identity, retention
            └─ yes
               Is parsing correct?
               ├─ no → inspect parsing rule/version/error with fixture
               └─ yes
                  Is mapping correct?
                  ├─ no → inspect Data Model Rule/version/error
                  └─ yes
                     Inspect RBAC/SBAC, dataset, timeframe, fields, query, consumer
```

Every “yes” requires retained evidence. A counter or status can be scoped to a component rather than the controlled event.

## Component-specific checks

### Cortex XDR agent

- tenant association and endpoint identity;
- policy/profile/group assignment;
- supported OS and agent version;
- connection state versus operational-protection state;
- EDR/data-collection enablement;
- module/sub-status evidence;
- source event generation;
- last report and telemetry visibility.

Do not restart, upgrade, uninstall, isolate, or clear agent data without an authorized change plan.

### Broker VM or applet

- product/Broker version and license;
- registration and applet availability;
- applet configuration assignment;
- source-side receive evidence;
- send/queue/error evidence;
- DNS/proxy/certificate/outbound path;
- tenant ingestion evidence;
- resource/cluster state as documented.

Never install diagnostic third-party agents on a Broker VM.

### XDR Collector

- installer/package integrity and supported host;
- profile and policy mapping;
- Filebeat/Winlogbeat configuration from the target source;
- file/event-log access, rotation, encoding, multiline behavior;
- collector process and audit/health;
- input, send, and dataset observations;
- upgrade or content changes.

Do not invent YAML repairs. Validate against the current template/editor.

### Cortex Engine

- exact XSIAM, XDR, or XSOAR product, deployment, and version;
- Engine association, runtime prerequisites, and connection;
- integration/command assignment;
- proxy/DNS/TLS path;
- service credential;
- Engine group/load-balancing behavior;
- command/job audit and container error.

Do not treat Engine connectivity as ingestion proof or transfer one product's Engine procedure to another.

## Parsing and mapping checks

When raw data exists but expected normalized data does not:

1. preserve a sanitized raw record and unique marker;
2. identify parser and Data Model Rule/content versions;
3. verify source vendor/product identity and format;
4. inspect parsing errors;
5. test parsing in the named editor/non-production surface;
6. inspect mapping applicability, conflicts, and disabled rules;
7. compare raw parsed fields to expected normalized types;
8. query raw and normalized forms under the same identity/timeframe;
9. verify Marketplace/default-rule ownership before editing;
10. test positive, malformed, null, negative, and duplicate fixtures.

The documented `parsing_rules_errors` dataset can contain parsing and Data Model Rule errors in current XSIAM. Re-open the current schema before querying fields: [Troubleshooting Data Model Rules](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Troubleshooting-Data-Model-Rules).

## Access and query checks

Zero rows can result from:

- dataset/object does not exist;
- data not ingested;
- wrong raw versus normalized source;
- event outside retention/timeframe;
- source-time versus insert-time mismatch;
- RBAC/SBAC/dataset-row scope;
- saved-object sharing;
- query field/type/null/filter error;
- identity mismatch between UI and API;
- result cap/truncation or downstream consumer behavior.

Use a minimal bounded query designed by the query owner after platform evidence establishes the source. Do not guess a dataset or field.

For XSIAM raw records that are visible while XDM returns zero rows, check the
documented **Datasets Rows** limitation before changing the parser or mapping.
Current guidance says XDM queries are unsupported under row-level filtering and
return rows only with **All rows are accessible** and no filter defined in that
scoping area. Inspect the effective identity and settings; the symptom alone does
not prove this is the cause. Preserve access restrictions and use an approved raw
query or an owner-reviewed alternative, never a permission expansion as a test.
See [the product-specific access branch](api-auth-and-access.md#xsiam-raw-dataset-scope-versus-xdm-visibility),
verified against the official page on 2026-09-06.

## Latency, gaps, and duplicates

Build a timeline:

| Marker | Source time | Component receive | Component send | Ingestion/insert | Query observe |
|---|---|---|---|---|---|
| Controlled placeholder | record | record | record | record | record |

Validate clock synchronization, timezone, precision, and fallback meanings. Compare multiple markers across normal and peak conditions. Inspect:

- exporter/fetch schedule and cursor;
- buffering and backpressure;
- retry and replay;
- parser/mapping processing;
- ingestion baseline/metrics;
- retention and query window;
- duplicate keys and downstream deduplication.

Do not report sustainable throughput from one sample or published maximum. Use observed workloads and controlled load testing.

## API and integration checks

Separate:

- DNS/TLS/proxy transport;
- authentication;
- endpoint/API-family/version;
- component RBAC;
- SBAC/dataset/object scope;
- integration-command permission;
- external system privilege;
- request schema and response class;
- pagination/stream/job lifecycle;
- client timeout/retry/concurrency behavior;
- audit/correlation ID.

Never print keys or full sensitive responses. Do not retry writes blindly after an ambiguous response.

## Change discipline

Read-only checks first. Before any change record:

- exact target and owner;
- approved scope/window;
- current configuration/export;
- current official parameter source;
- expected effect and blast radius;
- test/canary;
- rollback trigger/steps;
- credential and privacy handling;
- post-change component and end-to-end checks;
- audit and partial failure.

Restarting a component can erase transient evidence or create backlog/duplicates. Credential rotation can break multiple consumers. Parser changes can alter historical/query semantics. Dataset deletion or overwrite is destructive.

## Escalation packet

Provide:

- concise symptom and impact;
- product/deployment/version/license;
- timeline and last known good;
- complete path with layer status;
- two or more hypotheses;
- checks performed and sanitized observations;
- exact errors/correlation markers;
- identities/scopes used;
- configuration and artifact hashes;
- changes already made;
- requested owner/action;
- safety, rollback, and evidence-retention notes.

Use [templates/troubleshooting-record.md](../templates/troubleshooting-record.md).
