# Traffic and policy diagnosis

Baseline 2026-11-13. Use the actual flow tuple and named product release. For PAN-OS, the reviewed NAT guide describes original/pre-NAT addresses for rule matching and distinguishes security policy post-NAT zones from NAT policy pre-NAT zones. Translation does not itself permit a session. Preserve original/translated addresses and zones in separate columns before proposing a rule. [F05 in official sources]

| Layer | Discriminating evidence |
|---|---|
| Ingress and routing | Interface/zone, route lookup, next hop, tunnel, forward/return symmetry; timestamped flow |
| NAT | Ordered rule, original tuple, translated tuple and relevant zones; no inferred security permission |
| Security | Effective rule order, match criteria, App-ID/application dependencies, service, User-ID and action |
| Inspection | Attached security profiles, subscriptions/content, decryption decision, trust and exception scope |
| Session | Actual session/log evidence, byte direction, termination reason and client/server result |
| Logging | Configured forwarding, received event, parser, timestamps and query visibility; no invented dataset |

For AWS Cloud NGFW, the reviewed guide separates NGFW resource, endpoints, local/global rulestacks and VPC route-table steering. Resource creation alone does not prove traffic traverses inspection. Azure's reviewed resource guide separately points to routing, forced tunneling and egress NAT; use that provider's contract rather than copying AWS rulestacks or routes. [F06, F07]

For cleanup, compare counters with rule lifetime/reset, observation window, traffic seasonality, logging, device/HA coverage and owner confirmation. For a deny, compare intended and actual application/user, DNS destination, NAT and routing before altering rules. For SSL failures, separate certificate trust/pinning, decryption policy, transport and server behavior. A broad allow or decryption bypass is not the default diagnostic action.

For cloud VM-Series/CN-Series, verify platform-specific deployment, traffic insertion, autoscaling/HA and version support in current official guides before proposing commands. This Skill supplies the reasoning contract; it does not bundle an unverified installation manifest.
