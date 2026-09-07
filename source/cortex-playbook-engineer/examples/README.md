# Example Index

Every example is a reasoning demonstration, not an importable playbook. Revalidate product, release, content, commands, context paths, permissions, and safety before implementation.

| Example | Product/surface | Artifact class | Purpose |
|---|---|---|---|
| [Ransomware response design](design/ransomware-response.md) | Cortex XSIAM playbook design | `CONCEPTUAL` | Full lifecycle with approval-gated containment and recovery |
| [Missing parent output](troubleshooting/missing-parent-output.md) | Cortex XSIAM context/sub-playbook troubleshooting | `CONFIGURATION GUIDANCE` | Diagnose output, context scope, filters, permissions, and Quiet Mode |
| [Monolith refactoring](refactoring/monolith-to-subplaybooks.md) | XSIAM/XSOAR design boundary | `CONCEPTUAL` | Split orchestration from reusable sub-playbooks with explicit contracts |
| [Endpoint-isolation decision](safety/endpoint-isolation-approval.md) | Response action policy/playbook design | `CONCEPTUAL` | Decide why and how isolation is approval-gated and verified |

None of these examples contains YAML, JSON, task UUIDs, exact integration commands, tenant values, or observed execution results. None is a `VERIFIED IMPORTABLE ARTIFACT`.
