# Example: Broker VM or XDR Collector?

## Objective

Choose a collection component for logs located on an on-premises Windows or Linux host without treating Broker VM and XDR Collector as interchangeable.

## Evidence status

`CONCEPTUAL / OFFICIAL-CURRENT / TENANT-UNVERIFIED`.

Inputs still required: product/version, license, source type, source reachability, host OS, event size/rate, format, credential location, HA requirement, and current tenant catalog.

## Conditional comparison

| Criterion | Broker VM applet | XDR Collector |
|---|---|---|
| Product boundary | Verify exact XSIAM/XDR applet for the target release | Verify current XSIAM/XDR Collector support |
| Primary pattern | Hardened bridge hosting documented applets | Dedicated Windows/Linux on-premises log/event collector |
| Host flexibility | Closed appliance; no arbitrary third-party agents | Installed on a supported customer-managed collector host |
| Collection methods | Applet-specific, such as the documented syslog surface | Product-documented Filebeat/Winlogbeat profiles/policies |
| Credential boundary | Applet and source specific | Collector-host/source specific |
| Dataset behavior | Route-specific | Collector dataset behavior is separately documented |
| Sizing/HA | Exact Broker/applet/version guidance | Exact collector/version/profile guidance |

Sources: [What is the Broker VM](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/What-is-the-Broker-VM) and [XDR Collectors](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/XDR-Collectors?contentId=qfIZLEv731a8gqLwBz0GGg).

## Decision rule

- Prefer a product-documented Broker applet when the source/protocol and desired architecture match that applet and the hardened-appliance boundary is acceptable.
- Prefer an XDR Collector candidate when the source is supported through its Windows/Linux collection profiles and a customer-managed collector host is appropriate.
- Prefer a direct vendor/cloud integration when the current catalog provides one and its trust/operational model is preferable.
- Return `UNVERIFIED` if the current product/license/catalog was not checked.

This is not a final recommendation. It does not specify ports, OS versions, sizes, profiles, or datasets.

## Required validation

For either candidate:

1. confirm the current catalog and license;
2. validate host/component support;
3. map trust and credential boundaries;
4. observe source input, component receive/send, tenant ingestion, raw data, parsing/mapping, and query visibility;
5. measure the actual workload and recovery behavior;
6. document owner, upgrade, rollback, and monitoring.

## Prohibited shortcut

Installing a monitoring or log-shipping agent on the Broker VM is not a valid workaround; the current official page describes it as a closed, hardened appliance and prohibits third-party agents.

