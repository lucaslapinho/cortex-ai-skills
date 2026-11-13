# Diagnose a user-to-application path

This is an engineering diagnostic method, not an assertion that every component is present.

1. Identify the failing population and exact timestamp: one user/device, one site, one app or all paths. Preserve a known-working comparator.
2. Confirm identity/authentication result, device/client/browser state and selected access method. Keep authentication success separate from tunnel and app success.
3. Resolve the application name from the affected path; compare split/public/private DNS, returned address and route. A wrong answer is not solved by opening policy.
4. Trace tunnel/underlay, advertised and effective routes, private-app/service connection and return path; inspect overlaps and asymmetric routing.
5. Inspect user/group mapping and effective policy, App-ID/service, profiles, decryption and DLP only after identifying the traffic path.
6. Correlate service logs and client/application evidence using source/ingest times. Different clocks, retention or filters can hide an event.
7. For SD-WAN compare circuit and overlay health, latency/loss/jitter against the application's policy; distinguish link failure from brownout and application failure.
8. Test a small allowed and denied flow within authorization. A permitted policy change must include pilot, rollback, user recovery and verification; never create a broad exception merely to collect evidence.

Record each branch as supported, contradicted or unknown and state the next discriminating observation. If logging, access or a sibling tool is unavailable, return the collection request and bounded hypothesis; do not claim inspection occurred.
