# Worked examples

These examples demonstrate response structure and safety boundaries. They are not tenant exports, importable configurations, API payloads, deployment instructions, or proof of product execution. Placeholder organizations, sources, indicators, and consumers are fictional.

| Example | Main lesson | Evidence boundary |
|---|---|---|
| [Indicator lifecycle design](lifecycle/indicator-lifecycle.md) | Expiration, reactivation, revocation, deletion, and downstream removal are distinct | `CONCEPTUAL / DERIVATIVE / TENANT-UNVERIFIED` |
| [Multi-source duplicate diagnosis](feeds/multi-source-duplicates.md) | Diagnose transport replay, normalized identity, and product merge behavior separately | Mixed official facts and unverified hypotheses |
| [TAXII 2 ingestion assessment](interoperability/taxii-ingestion.md) | Protocol support does not guarantee mapping or relationship fidelity | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` |
| [EDL distribution rollout](distribution/edl-rollout.md) | Distribution and security-control operationalization require separate gates | Plan only; no export or enforcement |
| [OpenCTI version mismatch](troubleshooting/opencti-version-mismatch.md) | Installed versions and deprecated integration families must be verified | Diagnosis remains conditional without inventory |

When adapting an example, replace its evidence label with the evidence actually available. Never retain a positive result merely because the example shows the desired structure.
