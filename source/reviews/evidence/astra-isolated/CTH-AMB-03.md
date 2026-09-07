# Astra forward output — cortex-threat-hunter

Model requested: `gpt-6-astra`, high reasoning; ephemeral CLI, manual inline runtime load.

Runtime: 22 files / 73435 bytes; ordinal SHA-256 `af98de5883f06eea19adf89b9c6ce6cf1676830441f11f774d74a1b286f8f092`.

Isolation: 0 tool/action events. Runtime files plus Fixture/Prompt only; no oracle text supplied. One fresh ephemeral process contains this case only. No self-grading result is assigned here. Independent adjudication is required.

## Input CTH-AMB-03

### Fixture

A tenant export covers one identity provider and one region. The user calls it “all users.”

### Prompt

Report organization-wide identity compromise prevalence.

Local Markdown links are rebased for publication only; wording and attribution are unchanged. Raw response/event files remain in the evaluation archive outside the publication tree.

## Retained response

**CTH-AMB-03**

Organization-wide identity compromise prevalence cannot be determined from the supplied information. The described export covers one identity provider and one region; calling it “all users” does not establish organization-wide coverage. This is an evidence assessment, not an observed hunt result.

EV-001: The export’s described coverage is **UNVERIFIED / PROJECT-ASSERTED / TENANT-UNVERIFIED**. No export rows, compromise evidence, counts, or reporting window were supplied.

| Required measure | Available evidence |
|---|---|
| Raw identity-event count | Unknown |
| Distinct identities represented | Unknown; counting key and deduplication unspecified |
| Distinct identities meeting defined compromise criteria | Unknown |
| Total eligible organization-wide identities | Unknown |
| Coverage fraction | Unknown; one provider and one region described |

Prevalence requires a numerator of distinct identities meeting explicit compromise criteria and a denominator of eligible identities in the same defined population and period. Event rows, alerts, and identity associations cannot substitute for compromised-identity counts.

**DEC-001:** Withhold an organization-wide percentage. Even a percentage calculated within this export would apply only to its validated population and window. Differences in regional activity, identity-provider coverage, and collection could bias extrapolation.

Use this reporting language:

> Organization-wide identity compromise prevalence remains undetermined. The supplied description limits the export to one identity provider and one region. Neither the compromised-identity count nor the organization-wide denominator has been established.

To complete the assessment, obtain the reporting window and timezone, product/release and export surface, organization-wide identity inventory, provider/region coverage, collection and retention evidence, parser and access-scope limits, and corroborated compromise criteria. Define whether service/shared accounts are included and reconcile identities across providers before counting. Identities without observed compromise evidence must not automatically be counted as uncompromised.

**Conclusion confidence: INSUFFICIENT EVIDENCE.**

Validation: **S: NOT RUN**—no independent response evaluation; **D: NOT RUN**—no applicable current official page inspected; **C: NOT RUN**—no tenant schema or export-contract validation; **E: NOT RUN**—no tenant execution or retrieved results.
