# SASE service boundaries

Baseline 2026-11-13; see [official sources](official-sources.md).

| Service or feature | Primary question | Boundary |
|---|---|---|
| Prisma Access | Secure access for mobile users and networks, including private applications | Identify SCM or Panorama management and actual licensed components; Mobile Users, Remote Networks and Service Connections have different roles. [S01] |
| Prisma SD-WAN | Application-aware WAN paths and branch/datacenter connectivity | Establish ION/site/circuit and current management model; sharing SCM does not make it the PAN-OS SD-WAN plugin. [S02] |
| PAN-OS SD-WAN | SD-WAN functionality on supported PAN-OS firewalls | Separate product/plugin/version contract; documented interoperability is not configuration equivalence. [S03] |
| Prisma Browser | Browser-mediated workspace and access controls | Verify browser, extension or mobile surface; do not infer all endpoint traffic is controlled. [S04] |
| AI Access Security | Employee access and data sent to GenAI applications | The reviewed guide describes prompts/uploads and explicitly excludes scanning/logging GenAI responses. Recheck the exact channel/support matrix. [S05] |
| Prisma AIRS | Protection of AI applications, models and agents | Separate application architecture, runtime and supply-chain controls; route to the AIRS specialist. |

Prisma Access supports distinct management approaches. Choose documentation for the installed one and verify available features, licenses, locations and capacity before design. Its logging architecture does not itself establish ingestion into Cortex XSIAM. [S01]

For DLP and AI Access Security, determine the detection profile, data direction, enforcement channel, exception scope and handling of blocked content. Use synthetic sensitive-data fixtures. A dashboard count or supported application name is not proof that the intended prompt/file action is blocked in that deployment. [S05]
