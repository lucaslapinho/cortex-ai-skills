# Astra independent Playbook/TIM completion review

**Review date:** 2026-09-06  
**Reviewer:** `astra_platform_security`, independent of the Playbook/TIM completion author  
**Scope:** completion deltas, their official support, and five fresh individual forward responses. No runtime file was changed by this reviewer.

## Decision and exact runtime binding

The reviewed completion deltas pass independent review. The Playbook S-classification finding is closed. All five selected individual responses pass their authored case criteria; this is not a full-suite or tenant-validation claim.

| Package | Runtime files | Runtime bytes | Ordinal runtime SHA-256 |
|---|---:|---:|---|
| `cortex-playbook-engineer` | 20 | 151241 | `ee2624e64bbb650b98a9a7e7594bc8c3896d6f49bbc12fcf19801578f119ed4a` |
| `cortex-tim-engineer` | 21 | 126788 | `e2e49820268e45ee8017ce67d397cb73d9d08cdfd80fc7dc9b16e1f58b2de0fb` |

Both identities were recomputed with the repository manifest tool and match the individual response records. The identity recipe is ordinal POSIX relative paths, lowercase per-file SHA-256, two spaces, LF-separated records, UTF-8, and no terminal newline.

## Coverage and method

The reviewer read 25 package files in full across this cross-review, in addition to relevant architecture and root evidence records:

- Playbook: `SKILL.md`, `CHANGELOG.md`, `VALIDATION.md`; `references/official-sources.md` and `references/testing-deployment-troubleshooting.md`; `templates/context-contract.md` and `templates/playbook-design.md`; all four worked examples; and `tests/basic.md`, `tests/regression.md`, and `tests/troubleshooting.md`.
- TIM: `SKILL.md`, `CHANGELOG.md`, `VALIDATION.md`; `references/official-sources.md` and `references/interoperability-and-distribution.md`; `templates/distribution-change.md`; the EDL-rollout and OpenCTI-version-mismatch examples; and `tests/advanced.md`, `tests/regression.md`, and `tests/troubleshooting.md`.
- The complete five final response records below and their corresponding Fixture, Prompt, Expected observations, Prohibited behaviors, Evidence expected, and Authored result sections were compared directly. Earlier approvals were not used as proof that these new responses passed.
- `tools/evaluate.py` and `tools/evaluate_astra_cases.py` were read in full. Fixture/Prompt extraction excludes scorer sections. Individual evaluation uses one fresh ephemeral process per case, a manual inline runtime load, and no browsing or filesystem actions by the evaluated model.
- The five raw response/event archives were inspected independently. Each contained one case response and only agent-message item events, with no tool/action events. The final publication records preserve the response wording; the harness only rebases resolvable local Markdown links.

## Independent selected-case adjudication

| Case and retained response | S decision | Reason and prohibited-behavior check |
|---|---|---|
| [PB-BAS-03](evidence/astra-isolated/PB-BAS-03.md) | PASS | All inputs and outputs have producer/consumer, type/cardinality, requiredness/default or absence policy, empty/error behavior, sensitivity, namespace evidence, mapping/write ownership, run lifetime, post-run retention, and owners for unresolved dimensions. It selects XSIAM only conditionally, requires separate XSOAR validation, and does not present context separation as confidentiality or RBAC. Names and schemas are explicitly conceptual; no import or execution is claimed. |
| [PB-REG-03](evidence/astra-isolated/PB-REG-03.md) | PASS | Rejects the simulation assumption, identifies logged-in-user effects, distinguishes protection of the original Issue from other state changes, and explains that already-running parallel tasks continue. Protected tasks must be skipped before launch; real action tests require exact authorization, reversible scope, recovery and readback. It reports four canonical validation results without self-awarding S or inventing execution. |
| [TIM-A03](evidence/astra-isolated/TIM-A03.md) | PASS | Treats installed legacy use as unconfirmed, distinguishes deprecated 3.x from the candidate 4.x path, keeps the compatibility baseline time-sensitive and the out-of-box mapping wording XSOAR-scoped. It preserves all three conflicting pagination-output statements without choosing a path, and requires installed/pinned evidence or controlled readback. Migration remains a plan with bounded pilot, markings, relationships, duplicates, reconciliation and rollback; no history reset or uncontrolled parallel fetch is performed. |
| [TIM-A04](evidence/astra-isolated/TIM-A04.md) | PASS | Rejects default-query/shared-credential confinement, covers query/format/count overrides and minimal fields, and leaves XSIAM field behavior unverified. Separate credentials are not mistaken for a native subset restriction. Selection/service, consumer retrieval and firewall enforcement have distinct owners and gates, protected-value checks, staged readback, stop criteria and rollback. No distribution or blocking is asserted or authorized by a verdict alone. |
| [TIM-R07](evidence/astra-isolated/TIM-R07.md) | PASS | Recommends Generic Export Indicators Service as the candidate successor, marks both named legacy integrations deprecated, and retains the more-than-1,000-firewalls exception without presuming eligibility. It inventories tenant/support applicability, preserves migration and approval boundaries, and does not confuse deprecation with removal. |

These are external scorer decisions. The evaluated responses themselves correctly leave S as NOT RUN. PB-REG-03 reports D PASS only for the supplied, dated PB10 verification record and expressly states that it did not perform a fresh official-source check. That bounded inherited record is not a new documentary check by the forward model. The other four responses report D NOT RUN. All five report C/E NOT RUN.

The responses are proposed designs/reviews with future evidence requirements, not substitutes for actual debug logs, target allowlists, run/task identifiers, permission tests, or rollback records from a tenant.

### Raw evidence corroboration

Archive directory names below identify the evaluation archives outside the publication tree; `response.md` and `events.jsonl` were readable there during this review. They are not runtime dependencies or portable publication links.

| Case | Raw archive directory name | Raw response SHA-256 |
|---|---|---|
| PB-BAS-03 | `cortex-astra-forward-191h3msh` | `bbe315b6a90a5ade61d47c979b2a2ac8b3b0d8756eabf41dee5dcb32e787c16e` |
| PB-REG-03 | `cortex-astra-forward-_9qsgrl7` | `cca32172ba77083d6c92df6bca730447c63eea05b98e6bb87473822576f7e7a1` |
| TIM-A03 | `cortex-astra-forward-1e2kpucu` | `eb945af1fc71d84fb98650240ab90f91f8e3a0e017b249f8094fd90374a304de` |
| TIM-A04 | `cortex-astra-forward-5zd2r220` | `cfe72197fa2e92db61a5695336c24391a2b4f505d774ec2b0aaf2b226bd004eb` |
| TIM-R07 | `cortex-astra-forward-jsyh0dip` | `786ea0fdcbe06e0cfe668860ef859428f24451f4e0fdbfdd229804f01f470545` |

## Official sources independently reopened

The reviewer checked the following exact official sources on 2026-09-06. For the six Cortex-documentation pages, direct HTTPS Markdown retrieval returned HTTP 200 and their substantive contents were read; the browser retrieval failure for PB10 was not treated as evidence of document absence. Website agent-instruction footers were not followed.

| Source | Bounded claim checked |
|---|---|
| [PB04 — Configure playbook settings](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/playbooks/build-your-playbook/configure-playbook-settings.md) | XSIAM triggers, grouped input/output configuration, edit permission and Quiet Mode context/visibility boundaries. |
| [PB05 — Add sub-playbooks](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/playbooks/build-your-playbook/add-objects-from-the-task-library/add-sub-playbooks.md) | Explicit parent/child I/O, private/default versus shared context, installed content and update boundaries. |
| [PB07 — Configure script error handling](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/playbooks/build-your-playbook/add-objects-from-the-task-library/configure-script-error-handling-in-a-playbook.md) | Stop, Continue and error-path behavior for the supported script task scope, not every task class. |
| [PB09 — Use context data in a playbook](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/context-data/use-context-data-in-a-playbook.md) | XSIAM Issue/parent-Case context, literal legacy names, separate/shared child context and permission caveats. |
| [PB10 — Test your playbook](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/playbooks/build-your-playbook/test-your-playbook.md) | Logged-in-user execution, real effects, existing-Issue protection limits, session-local skips/overrides and continued execution of already-running parallel tasks at a breakpoint. |
| [PB15 — Configure integration permissions](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/cortex-xsiam-data-sources/administration-and-troubleshooting/integrations/configure-integration-permissions.md) | Role restrictions per command and per instance, with documented CLI and Work Plan consequences. |
| [I02 — TAXII 2 Feed](https://xsoar.pan.dev/docs/reference/integrations/taxii-2-feed) | XSOAR/XSIAM availability and TAXII 2.0/2.1 support are distinct from complex-observation representation wording expressly naming XSOAR TIM. |
| [I07 — Generic Export Indicators Service](https://xsoar.pan.dev/docs/reference/integrations/edl) | Request-level q/n/v overrides; JSON/CSV all-fields wording scoped to XSOAR; authenticated retrieval is not evidence of subset confinement. The confinement control remains an explicit engineering inference, not an invented native setting. |
| [I08 — Export Indicators Service](https://xsoar.pan.dev/docs/reference/integrations/export-indicators) | Deprecation and the named Generic Export Indicators Service replacement. |
| [I09 — PAN-OS EDL Management](https://xsoar.pan.dev/docs/reference/integrations/palo-alto-networks-pan-os-edl-management) | Deprecation, named replacement and retained support exception for customers with more than 1,000 firewalls. |
| [I10 — OpenCTI Feed 4.X](https://xsoar.pan.dev/docs/reference/integrations/open-cti-feed-4x) | Listed products and compatibility baseline, XSOAR-specific automatic mapping, and conflicting argument/context-output/example pagination statements. The exact installed output path remains unverified. |

This is a six-source Playbook and five-source TIM targeted D review, not a fresh review of either full historical register. No conclusion establishes tenant availability, exact installed behavior or performance.

## Finding closure and revision impact

**P2 S-scope inconsistency — CLOSED.** In Playbook `references/testing-deployment-troubleshooting.md`, lines 27 and 47 previously allowed author structure/link checks to be described as S. The corrected text requires a retained oracle-isolated response and independent adjudication and explicitly records structural checks separately. It now agrees with `SKILL.md` and the authored example result tables.

The correction changes validation classification only, not product behavior or case oracles. The earlier two-case batch used runtime `ac23c52e0f5d57cfcacd713d9e8d58a3906fa6e4750bf3374c1fa72da0883976`; its responses already kept S NOT RUN. A narrow revision-impact bridge is therefore defensible for that correction, but is not needed as final behavioral proof: both Playbook cases were subsequently rerun individually against the final `ee2624e...` runtime and independently passed above.

The earlier [Playbook batch](evidence/astra-playbook.md) and [TIM batch](evidence/astra-tim.md) are historical exploratory evidence, not the final selected response set and not extra independent cases to add to coverage counts.

- PB-BAS-03 and TIM-A04 changed materially in this completion pass. Their earlier historical S approvals must not be transferred to the expanded oracles. The new individual responses above replace those approvals for current selected-case reporting.
- PB-REG-03, TIM-A03 and TIM-R07 are additionally evaluated selected cases in this final set; they do not establish complete regression coverage.
- PB-TRB-02 and TIM-T02/T03 have no material oracle/domain change in these reviewed deltas. Their previous summary decisions remain historical and may be described as such, but their older raw responses were not found in the publication evidence tree and were not independently rescored in this pass. This report does not count them as new Astra executions or newly adjudicated S cases.

## Limits

- Current selected S coverage from this report: Playbook 2 of 28 cases; TIM 3 of 37 cases. The remaining cases are not asserted to have run in this final individual battery.
- The evaluated model was requested as `gpt-6-astra` with high reasoning. Manual inline loading is not automatic Skill discovery, desktop/IDE host certification, Claude loading or model equivalence.
- The reviewer inspected harness construction and retained raw events, but a no-tool transcript is not a general proof against every possible form of contamination. No scorer sections were supplied by the inspected harness.
- C/E remain NOT RUN. No live Cortex tenant, SDK/schema acceptance, controlled import, feed, debugger execution, EDL access test, firewall enforcement or rollback result exists from this review.
- The package/delta review and the selected S/D decisions do not independently authorize publication, installation or deployment. Root final QA must bind the release artifacts and ledgers to the final hashes.
