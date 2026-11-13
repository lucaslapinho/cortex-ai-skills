# AIRS architecture and modes

Baseline 2026-11-13. The reviewed official architecture identifies four pillars: AI Runtime Security, AI Supply Chain Security, AI Red Teaming and AI Gateway. Treat older research that lists AI Access Security as an AIRS pillar as a different portfolio grouping. Workforce AI access controls remain relevant, but are not the same application protection boundary. [A01 in official sources]

| Pillar | Design input | Evidence ceiling |
|---|---|---|
| Runtime | Application flows and inspection/enforcement points | Only observed/supported traffic and modes are covered |
| Supply Chain | Model or agent artifact/version and provenance | Artifact result does not certify all runtime behavior |
| Red Teaming | Authorized target, threat hypotheses and test corpus | Results apply to tested app/version/scenarios |
| AI Gateway | Provider routing, identity, policy and bypass paths | Gateway configuration alone does not prove every call passes through it |

Runtime has API and network deployment approaches. The reviewed overview scopes contextual grounding/RAG and inline data redaction capabilities to API-based protection; do not automatically promise them for network mode. Model/provider/protocol, streaming, payload support, TLS visibility, regions and deployment constraints need current product-specific verification. [A02]

Cortex Cloud AI-SPM asks what AI resources exist and what posture risks surround them. AI Access Security asks how employees use GenAI apps and send data. AIRS asks how the organization's AI application, model/agent artifacts and inference flows are protected. A project may need all three, with separate owners and evidence.

Never fabricate an API URL, SDK method, request schema or universal scan policy. Use the current official reference for the selected runtime component before producing executable code. Preserve unresolved values explicitly when the target environment is unknown.
