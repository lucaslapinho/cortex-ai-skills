# Management planes and state transitions

Baseline 2026-11-13. Sources are in [official sources](official-sources.md).

| Surface | Distinction that changes the procedure |
|---|---|
| Local PAN-OS | Candidate versus running configuration; local object scope and management access. |
| Panorama | Device groups/policy versus templates/device and network settings; commit to Panorama versus push to managed devices. Verify the effective target and each job result. [F01] |
| Strata Cloud Manager | Folder/device inheritance, snippet associations and overrides; candidate configuration, configuration push and asynchronous jobs. Use the documented scope and API family. [F02, F03, F04] |
| Cloud NGFW AWS/Azure | Managed service with provider-specific policy, routing and lifecycle; do not assume a local PAN-OS XML API or identical AWS/Azure contract. [F06, F07] |

SCM snippets support reusable configuration. Ordering and inheritance affect conflicting values; duplicate policy rule names can fail validation. Before moving an object, inspect actual hierarchy, association and effective configuration. The reviewed documentation contains availability language that depends on the feature/tenant; verify enabled UI and entitlement instead of promising universal access. [F02]

SCM operations documentation distinguishes candidate push from running state and exposes job status. Identify the correct tenant/service-account scope and versioned API schema before giving an executable request. A generic OAuth example or successful token does not prove write authorization. [F03, F04]

Change record: intent → effective scope and before-state → minimal diff → candidate validation → authorized commit/push → recorded job/result → effective configuration readback → controlled allowed/denied traffic → log confirmation. Keep concurrent changes and partial device failures visible. Never retry a timed-out write until its state is reconciled.

Backup/restore planning must name the exact artifact, export source, version, encryption/secret handling, off-device retention and verified recovery procedure. A configuration export is evidence of that export only; it does not establish a restorable device-state or Panorama recovery package. Do not store plaintext secrets in a repository. For upgrades/HA, fetch the target version's support matrix and upgrade/recovery instructions at execution time; no fixed preferred release is bundled here.
