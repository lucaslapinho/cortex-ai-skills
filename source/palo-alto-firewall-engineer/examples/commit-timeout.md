# Example: timed-out Panorama operation

Synthetic request: “Commit completed, push timed out. Repeat it on every firewall.”

Response pattern: separate the local Panorama commit from device deployment. Reconcile the original push job, device results, effective configurations and pending changes before proposing another write. Identify failed/unknown devices and preserve the authorized intended scope. Do not infer failure from timeout or broaden the push to unaffected devices. State which readback and controlled traffic check would prove the requested effect.

Document basis: [F01](../references/official-sources.md). No operation was performed in this example; C/E: NOT RUN.
