# Risk, posture and runtime

Use this operating method for diagnosis and prioritization. It is an engineering workflow, not a vendor API contract.

| Question | Required evidence | Avoid concluding |
|---|---|---|
| Is the asset covered? | Expected inventory versus discovered scope; collection/scan timestamps, support and exclusions | No finding means secure |
| Is a vulnerability exploitable? | Affected installed version, reachability, prerequisites, mitigations and observed activity | CVSS or an attack-path graphic proves exploitation |
| Is access excessive? | Identity, effective grant/inheritance, resource scope, usage window and business requirement | Unused during one short window means safe to revoke |
| Is data exposed? | Classification, accessible principals, path, encryption/key access and business context | Encryption alone removes public-access risk |
| Does the workload have runtime protection? | Installed/healthy component, assigned policy, supported workload and observed test | An agentless scan proves runtime prevention |
| Did code reach production? | Repository/commit, scan type/status/exclusions, build/artifact and deployment lineage | A repository finding proves deployed impact |

Cortex Cloud AI Security describes discovery and posture of AI resources, relationships and risks. Keep that AI-SPM question separate from AIRS inspecting AI application traffic. Cortex Cloud Runtime Security describes workload-oriented protection and investigation; a product overview does not establish the coverage of a particular sensor, OS or service. [C06, C07 in the source register]

For incomplete inventory: compare expected scope and exclusions; inspect provider permissions and connector errors; test a known asset; inspect indexing and role/filter visibility. For stale scans: distinguish queued, running, failed and completed jobs, resource lifecycle, permissions, image/disk access, quota and network egress. For audit gaps: follow one known event through provider generation, collection and the query consumer. Preserve event and ingest time separately.

Remediation order should follow demonstrated impact and dependencies: reduce exposure or excessive access, fix the vulnerable component, confirm the deployed result and monitor recurrence. Define owner/SLA by organizational policy; do not invent a universal SLA from a severity label. Risk acceptance needs a bounded scope, accountable owner, compensating controls and expiry. A ticket closure or suppressed finding is not remediation evidence.
