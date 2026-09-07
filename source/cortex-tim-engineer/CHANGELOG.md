# Changelog

All notable changes to this Skill are recorded here.

## 0.1.0 - 2026-09-04

### Added

- Standalone Cortex TIM workflow with explicit collection, management, enrichment, lifecycle, distribution, and security-control boundaries.
- Evidence taxonomy, product/version/license gates, official source register, and project-knowledge qualification.
- Guidance for feed quality, provenance, normalization, duplicate handling, scoring dimensions, enrichment, relationships, expiration, and governance.
- Version-scoped interoperability guidance for TAXII, STIX, MISP, OpenCTI, and EDL-related integrations.
- Five reusable templates and five worked, non-tenant-executed examples.
- Seven-category behavioral test catalog with canonical case structure.
- Author-only static validation ledger and explicit independent-review gates.

### Limitations

- Astra completion review on 2026-09-06 added consumer-confinement and minimal-export checks for EDL request overrides, preserved the documented legacy large-fleet support exception, and strengthened existing A04/R07 cases without changing the case count. The distribution template/example now carry explicit S/D/C/E results and rationales. The revised runtime awaits independent review and behavioral evaluation; no new S pass is claimed.
- Preserved an internal inconsistency in the current OpenCTI 4.x pagination-output documentation and kept the exact path unverified; updated migration/troubleshooting guidance and existing A03 coverage.

- No live tenant, installed-integration inventory, schema validation, import, execution, distribution, deployment, downstream enforcement, production-volume test, or measured performance evidence.
- Independent technical, Platform-domain, adversarial, and static compatibility reviews completed; selected oracle-isolated behavior passed after distribution and validation-contract corrections.
- Corrected the XSIAM dataset register to the documented `indicators` name and removed the unsupported `indicator_relationship`/TIM-add-on assertion; removed an unsupported common fetch-history attribution; restricted TAXII 2 complex-observation, OpenCTI out-of-box mapping, and TAXII/TAXII2 Server collection-query statements to their explicit XSOAR wording while leaving XSIAM applicability unverified.
