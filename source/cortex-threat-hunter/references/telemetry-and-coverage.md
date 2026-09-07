# Telemetry and coverage

## Contents

1. Coverage model
2. Endpoint telemetry
3. Network and DNS telemetry
4. Identity telemetry
5. Cloud telemetry
6. Cross-source correlation
7. Negative-evidence rule

## 1. Coverage model

Availability is not coverage. For each source, distinguish:

- enabled producer;
- successful collection;
- searchable retention;
- parser/normalization quality;
- required field population;
- role and data scope;
- entity population;
- time range and clock quality;
- query success;
- expected-event validation.

Use:

| Source | Required observable | Population | Time basis | Retention | Access/scope | Parser/fields | Status | Consequence |
|---|---|---|---|---|---|---|---|---|
| Endpoint process | Parent/child behavior | In-scope managed endpoints | Event time | Unknown | Unknown | Unknown | UNVERIFIED | Cannot test process lineage |

## 2. Endpoint telemetry

Potential observables include process start/lineage, file, module/library, registry/configuration, user/session, endpoint network activity, and agent health. Exact availability and field names are tenant-sensitive.

Check:

- agent deployment and health over the entire population;
- operating-system differences;
- collection and prevention-policy differences;
- event time versus ingestion time;
- parent/child truncation or missing ancestry;
- command-line sensitivity and redaction;
- host reimage, rename, or reused identifiers.

## 3. Network and DNS telemetry

Potential observables include flow, connection, proxy, firewall, DNS query/response, TLS, URL, and endpoint network events. These may come from different producers and clocks.

Check:

- NAT, proxy, resolver, VPN, load balancer, and shared-egress ambiguity;
- directionality and byte/count semantics;
- partial east-west visibility;
- cached DNS and encrypted DNS;
- network logs that do not establish endpoint process causality;
- deduplication of replicated or summarized records.

## 4. Identity telemetry

Potential observables include authentication, authorization, directory, cloud identity, privileged action, session, and identity-risk context.

Check:

- human versus service/shared account;
- source identity provider and authentication path;
- device association confidence;
- session/token reuse and revocation timing;
- federated and local identity boundaries;
- successful event collection for the relevant account population;
- normalization and timezone.

Identity enrichment is not a substitute for the primary authentication/audit event.

## 5. Cloud telemetry

Potential observables include control-plane audit, workload/runtime, asset, configuration, finding, and identity-permission relationships. Exact source support, schema, licensing, and retention must be verified.

XSIAM Graph Search can be relevant to cloud asset/finding relationships only when the tenant has the documented license and permissions. Its presence and results must not be assumed. A visual relationship is a pivot lead; validate it against the underlying sources.

Check:

- cloud account/project/subscription coverage;
- audit-source enablement and regional/service gaps;
- ephemeral resource lifecycle;
- delegated and assumed identities;
- control-plane versus workload/runtime distinction;
- asset inventory freshness;
- provider event latency and duplication.

## 6. Cross-source correlation

Before joining or correlating:

- define entity keys and collision risks;
- normalize time explicitly;
- choose one-to-one, one-to-many, or many-to-many expectations;
- quantify missing keys;
- preserve unmatched rows when they matter;
- prevent fan-out from inflating counts;
- distinguish correlation window from causal sequence.

Never claim an endpoint caused a network event solely because a hostname or IP matched.

## 7. Negative-evidence rule

A defensible negative statement must include:

1. queried source and product;
2. exact population;
3. exact time window and timezone;
4. retention verified for that window;
5. collection health and expected-event check;
6. parser/schema validation;
7. permission and scope validation;
8. query compile/execution status;
9. exclusions and sampling;
10. the limited conclusion.

Preferred wording:

> No matching records were observed within the validated queried population and window. This does not establish that the activity did not occur outside verified collection, retention, parsing, permissions, scope, or the query's observable model.

If any prerequisite is unknown, conclusion confidence cannot exceed the evidence the remaining sources support.
