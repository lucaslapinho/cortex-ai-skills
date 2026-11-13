# Example: tunnel connected, private application unavailable

Synthetic request: “GlobalProtect is connected and internet works; allow all traffic to fix a private app.”

Response pattern: collect app name/address and timestamp, then compare private DNS, route and return path, relevant service/private-app connection, effective identity/policy and app response. Keep connection success and private-app access separate. Use a known-working user/app comparator. Do not implement a broad allow as a diagnostic shortcut.

Document basis: [S01](../references/official-sources.md); the ordering is an engineering diagnostic method. No live tenant checks occurred; C/E: NOT RUN.
