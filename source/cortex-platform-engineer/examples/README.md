# Examples

These examples demonstrate reasoning and evidence boundaries. They are not tenant-ready configurations, observed results, or proof of product compatibility.

| Example | Purpose | Highest represented evidence |
|---|---|---|
| [End-to-end syslog design](architecture/end-to-end-syslog.md) | Map a Broker VM syslog path without inventing ports or capacity | `CONCEPTUAL / OFFICIAL-CURRENT / TENANT-UNVERIFIED` |
| [Broker VM versus XDR Collector](architecture/broker-vs-collector.md) | Make a conditional component decision | `CONCEPTUAL / OFFICIAL-CURRENT / TENANT-UNVERIFIED` |
| [Missing telemetry](troubleshooting/missing-telemetry.md) | Troubleshoot a connected component with zero visible rows | `UNVERIFIED / TENANT-UNVERIFIED` for the reported symptom/cause; documented conditional checks remain separate |
| [API forbidden response](access/api-forbidden.md) | Separate authentication, RBAC, SBAC, and dataset access | `UNVERIFIED / TENANT-UNVERIFIED` for the reported cause |
| [Legacy alert-ingestion migration](migration/legacy-alert-ingestion.md) | Avoid inventing a successor for a legacy API | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` |

Revalidate every product, version, license, parameter, dataset, field, endpoint, role, limit, and tenant observation before use.
