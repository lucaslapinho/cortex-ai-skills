# Palo Alto portfolio routing

The coordinator owns cross-domain scope, evidence and dependencies. Specialist names are stable identifiers, not mandatory installed dependencies. This table identifies supported engineering tasks, not a promise of complete feature coverage for every SKU/release.

| Primary deliverable | Specialist | Critical boundary |
|---|---|---|
| Query mechanics | cortex-xql-query-engineer | Product/surface and observed schema |
| BIOC/correlation/detection lifecycle | cortex-detection-engineer | Signal versus response authorization |
| SOAR/AI tasks and notifications | cortex-playbook-engineer | Native task/context/command contract |
| Hypothesis and evidence-led hunt | cortex-threat-hunter | Coverage versus negative conclusion |
| Intelligence and indicator lifecycle | cortex-tim-engineer | Verdict/export versus enforcement |
| XSIAM/XDR/XSOAR platform | cortex-platform-engineer | Agent, Broker, Collector, Engine and integration roles |
| Cortex Cloud posture, runtime and AppSec workflows | cortex-cloud-engineer | CSPM/CIEM/DSPM/AI-SPM, scanning, code-to-runtime and tenant entitlements |
| PA/VM/CN-Series, PAN-OS, Cloud NGFW, Panorama/SCM | palo-alto-firewall-engineer | Effective dataplane and manager/provider-specific changes |
| Prisma Access, SD-WAN, Browser and workforce AI access | prisma-sase-engineer | User/site/app path and management model |
| Prisma AIRS application/model/agent security | prisma-airs-engineer | Runtime, Supply Chain, Red Teaming and Gateway |

Adjacent services such as Cloud Identity Engine, Strata Logging Service, Enterprise DLP, WildFire, URL/DNS/Threat Prevention and ADEM enter the owning platform/firewall/SASE workflow when needed. Their current feature, entitlement and API contracts must be checked before implementation. No dedicated deep specialist is claimed here for Xpanse/ASM, AgentiX, Unit 42 professional services, every hardware SKU or every legacy Prisma Cloud edition; scope those requests and retrieve their exact documentation rather than inventing coverage.

Example dependency: Azure exposure finding → Cloud specialist verifies resource, scan and path → Firewall specialist reviews the relevant enforcement point → Platform specialist verifies logs → Detection/Playbook specialists design the authorized SOC workflow. Keep identifiers and time semantics aligned and use only the work needed for the user's objective.

If a specialist is unavailable, return a bounded standalone plan, source requirements and acceptance criteria. Do not imply a delegation occurred or an external action ran merely because a route was recommended.
