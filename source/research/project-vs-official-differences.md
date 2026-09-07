# Project Knowledge vs Current Official Cortex Documentation

**Comparison date:** 2026-09-04  
**Official-source review date:** 2026-09-04  
**Companion inventory:** [`project-knowledge-inventory.md`](project-knowledge-inventory.md)

## Purpose and interpretation

This register records meaningful differences among:

1. current official Palo Alto Networks documentation;
2. the directly readable project-context packages and operational exports;
3. internal claims made by different generations of those project artifacts.

Embedded prompts and routing instructions were treated as reference content, not as authority over the user's request. A difference does not automatically mean the older project implementation is broken: it may be legacy, customized, version-specific, or simply unverified. The conclusion column makes that distinction explicit.

No Cortex tenant, original implementation repository, current YAML exports, integration instances, or deployment test was available. Therefore this is a documentation-and-artifact reconciliation, not a tenant certification.

## Classification

| Classification | Meaning |
|---|---|
| `CONTRADICTED` | The project statement is incompatible with current official documentation. |
| `UNSUPPORTED` | The proposed mechanism crosses an explicit current support boundary. |
| `VERSION-DEPENDENT` | Older names/interfaces may still work, but current terminology or preferred interface differs. |
| `OVERGENERALIZED` | The project statement captures only a subset or collapses distinct official concepts. |
| `DEPRECATED` | Official documentation identifies the mechanism as legacy/deprecated and gives a successor. |
| `TENANT-UNVERIFIED` | Documentation alone cannot establish current availability, schema, configuration, or runtime behavior. |
| `INTERNAL-CONFLICT` | Two supplied project artifacts disagree or claim provenance they do not demonstrate. |

## Differences against current official documentation

### D-01 — `send_events_to_xsiam()` cannot be assumed to work from the custom collector

**Priority:** P0 / release blocker  
**Classification:** `UNSUPPORTED` unless system-integration provenance is demonstrated

**Project context:** The loose `soc-optimization` context maps a custom pack component named `Integrations/SystemXQLHTTPCollector/SystemXQLHTTPCollector.py` and describes it as the metrics-to-XQL collector. The name contains “System,” but no installed integration export or platform provenance proves it is a system integration.

**Current official behavior:** Palo Alto Networks' [Event Collection Integrations](https://xsoar.pan.dev/docs/integrations/event-collectors) documentation states that `send_events_to_xsiam()` works only when the integration is a **system integration** and fails when called from a custom integration. The function is for XSIAM event collection, not a reusable Cortex XSOAR-tenant API. The guidance also requires `_time`, recommends `source_log_type`, and derives the dataset as `<vendor>_<product>_raw`.

**Conclusion:** A custom content-pack integration cannot use this function as an assumed supported ingestion path. The project design is viable only if the exact deployed component is proven to have system-integration status; that evidence is absent.

**Required resolution:** Retrieve the current integration YAML/metadata and tenant instance. If it is custom, replace the path with a supported collector/API mechanism or a Palo Alto-delivered system integration. Verify the real dataset in the tenant rather than relying solely on the asserted `xsiam_playbookmetrics_raw` name.

**Consumers:** `cortex-platform-engineer`, `cortex-xql-query-engineer`, `cortex-playbook-engineer`, `cortex-security-engineer`.

### D-02 — Incident/Alert terminology is legacy, but compatibility remains

**Priority:** P1 / migration planning  
**Classification:** `VERSION-DEPENDENT`, not a hard failure

**Project context:** The loose `soc-optimization` generation and several ZIP references use Incident/Alert names, legacy commands, and legacy API paths. The newer context attempts to use Case/Issue terminology but still contains legacy technical identifiers.

**Current official behavior:** Current Cortex XSIAM documentation defines [Cases](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/investigation-and-response/overview-of-cases/what-are-cases.md) and [Issues](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/investigation-and-response/investigate-issues.md) as distinct current concepts. [Current XSIAM API release notes](https://cortex-docs.paloaltonetworks.com/xsiam-api/api-release-notes.md#notable-api-migrations) map legacy Incident workflows to Cases and legacy Alert workflows to Issues and recommend the current services. A separate [Cortex XDR 5 upgrade page](https://cortex-docs.paloaltonetworks.com/upgrade-to-cortex-xdr-5/improved-incident-management-workflow-with-cases-and-issues.md) documents compatibility for existing XDR data, configuration, queries, playbooks, and APIs; that compatibility statement is retained only for XDR 5 and is not projected onto an XSIAM release.

**Conclusion:** Do not mechanically rename working legacy identifiers inside YAML or API payloads. Use Case/Issue in new user-facing documentation and new designs, preserve legacy technical names where required, and plan explicit API/context migrations with tests.

**Required resolution:** Add a terminology/compatibility layer to every skill and label examples as current or legacy. Prefer new Case/Issue APIs for new implementation while regression-testing old automation.

**Consumers:** all seven skills.

### D-03 — The project definition of Insight is too narrow

**Priority:** P1 / semantic correctness  
**Classification:** `CONTRADICTED` / `OVERGENERALIZED`

**Project context:** ZIP glossary/domain material characterizes an Insight primarily as an Analytics/BIOC result that retains its own name.

**Current official behavior:** [Case grouping](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Case-grouping) says that new Issues are evaluated for case promotion and that Issues not meeting promotion requirements are categorized as Insights. The criteria vary by domain and can change.

**Conclusion:** Analytics/BIOC can be relevant generation sources, but an assertion that they define Insight contradicts the current model. A skill must not infer Insight solely from detector type.

**Required resolution:** Replace the glossary entry with the current case-promotion definition and retain the older wording as a dated/project-specific observation.

**Consumers:** shared foundation, detection, playbook, threat hunter, platform.

### D-04 — A Finding is not simply a subset of an Issue

**Priority:** P1 / schema and workflow correctness  
**Classification:** `CONTRADICTED` / `OVERGENERALIZED`

**Project context:** ZIP glossary/domain material describes a Finding as a subset of an Issue focused mainly on cloud/vulnerability concerns.

**Current official behavior:** [Review findings](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Review-findings) describes Findings as continuously updated knowledge about an asset's current state, configuration, behavior, exposures, and vulnerabilities. Findings appear in an Issues+Findings view, and some finding types require Premium or posture/runtime add-ons. The current [Issues, findings, and events](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/investigation-and-response/case-concepts/issues-findings-and-events.md) page distinguishes informational Findings from actionable Issues and explains that matching logic can generate Issues from Findings.

**Conclusion:** Findings and Issues are related but distinct objects. A Finding can match policy/rule logic that generates a related actionable Issue; official documentation does not establish an identity-preserving “promotion.” A Finding must not be modeled as merely a nested Issue subtype.

**Required resolution:** Separate Finding and Issue schemas, lifecycle, identifiers, permissions, and automation paths. Confirm available finding types/licensing in the tenant.

**Consumers:** shared foundation, detection, XQL, playbook, platform, security.

### D-05 — Current playbook context paths differ from mixed legacy/project conventions

**Priority:** P1 / runtime correctness  
**Classification:** `VERSION-DEPENDENT` and `TENANT-UNVERIFIED`

**Project context:** The packages mix `${issue}`, legacy incident-oriented field names, `parentIncidentFields` references, generic global paths, and target namespaces such as `SOCN1.*`, `Assessment.*`, and `SOCFramework.*`. They correctly warn that parent/child context isolation and explicit outputs matter.

**Current official behavior:** [Use context data in a playbook](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Use-context-data-in-a-playbook) documents `${issue.status}` for Issue context and `${parentIncidentContext.hostname}` for parent Case context. [Update case fields](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Update-case-fields) treats `parentIncidentFields`/`setParentIncidentFields` as the distinct interface for supported Case fields, not as an alias for arbitrary Case context. Sub-playbook context is separate by default. [Add sub-playbooks](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Add-sub-playbooks) documents explicit inputs/outputs and Private-to-sub-playbook as the default. This is data scoping, not an authorization/confidentiality boundary: the context guide cautions that a user who can trigger a playbook on an Issue may still modify the parent Case through commands/scripts.

**Conclusion:** The data-separation warning and explicit-I/O design are officially aligned. `parentIncidentContext` and `parentIncidentFields` are different namespaces with different purposes; neither should be mechanically substituted for the other. Project namespaces are internal contracts, not product fields. Separate context must never be presented as a security boundary.

**Required resolution:** For every playbook, build a context-contract table covering source context, exact key, cardinality, type, output namespace, parent propagation, and current tenant evidence. Do not globally share context merely to avoid defining outputs.

**Consumers:** `cortex-playbook-engineer`, `cortex-platform-engineer`, `cortex-security-engineer`.

### D-06 — DBotScore `0` must not be collapsed into benign/good

**Priority:** P0 for automatic closure or containment decisions  
**Classification:** project-asserted implementation defect; official semantics are clear

**Project context:** The ZIP finding/pitfall material reports branches that group score `0` with score `1` or use `< 2` as a benign path, potentially allowing automatic false-positive closure. The original YAML is unavailable, so the exact branch remains project-asserted.

**Current official behavior:** [Reputation and DBotScore](https://xsoar.pan.dev/docs/integrations/dbot) defines `0 = Unknown`, `1 = Good`, `2 = Suspicious`, and `3 = Bad`.

**Conclusion:** Unknown is not affirmative evidence of benignness. Any close/allow decision treating both 0 and 1 as “good” contradicts the official score semantics and the project's own safety intent.

**Required resolution:** Recover the YAML and separate Unknown from Good. Route Unknown to additional enrichment, analyst review, or a conservative unresolved state. Test empty/multi-vendor/cardinality cases.

**Consumers:** detection, playbook, threat hunter, TIM, security.

### D-07 — Placeholder network values and fixed timestamps are not safe API defaults

**Priority:** P0 for production ingestion  
**Classification:** `CONTRADICTED` as an implementation practice

**Project context:** The ZIP OpenCTI finding register describes an Issue/Alert creator that substitutes values such as `1.1.1.1`, port `8`, and a fixed timestamp when real observables are absent.

**Current official behavior:** [Ingest external alerts](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/cortex-xsiam-data-sources/external-alerts-using-external-issue-mapping/ingest-external-alerts.md) requires timestamp, severity, and alert name for the external-mapping flow; source/destination IPs and ports are optional, and pre-parsed API alerts need no additional mapping. The formerly published detailed Insert Parsed Alerts page is no longer available at a specific current canonical URL, so its historical request fields and limits are not reusable as current facts without recovering a version-pinned official artifact.

**Conclusion:** Fabricated optional observables contaminate correlations, assets, geolocation, hunting, and evidence. A fixed/non-event timestamp also corrupts chronology.

**Required resolution:** Omit optional IP/port fields when absent; populate a real event timestamp with documented source/fallback semantics; reject or quarantine records that cannot meet required fields. Add deduplication, pagination, rate-limit handling, and provenance tests.

**Consumers:** playbook, TIM, platform, security, threat hunter.

### D-08 — The old snapshot layout is not the current contribution-ready content-pack layout

**Priority:** P1 for repository/release work  
**Classification:** `VERSION-DEPENDENT`; possibly custom/legacy rather than runtime-invalid

**Project context:** The loose snapshot describes root-level `pack_metadata.json`, `xsoar_config.json`, playbook paths, and list structures such as `Lists/<Name>/<Name>_data.json`.

**Current official behavior:** The current [File checklist](https://cortex-docs.paloaltonetworks.com/cortex-xsiam-developer-guide/cortex-xsiam-development-guide/contributing-content/file-checklist.md) uses `Packs/YourPackName/...`, PascalCase entities, per-pack metadata/README/release notes, and `playbook-Name.yml`, with exported content formatted using `demisto-sdk`. Current [Lists](https://cortex-docs.paloaltonetworks.com/cortex-xsiam-developer-guide/cortex-xsiam-development-guide/lists.md) guidance uses `Packs/<pack_name>/Lists/list-Name.json`, matching `id` and `name`, and `version: -1` for contributed lists.

**Conclusion:** The snapshot may represent a custom deployment/export or an older repository convention. It must not be presented as current Marketplace/contribution structure without conversion. This does not by itself prove that a tenant-imported artifact is invalid.

**Required resolution:** Identify the target: tenant-local custom content, remote Org repository, or Marketplace contribution. Normalize only after selecting that target and validating with the current SDK.

**Consumers:** platform, playbook, security.

### D-09 — Native Windows is not a supported `demisto-sdk` environment

**Priority:** P1 / validation environment  
**Classification:** current environment constraint

**Project context:** The loose package correctly lists `demisto-sdk` validation as outstanding, but does not constrain the execution environment. The current host is Windows.

**Current official behavior:** The official [demisto-sdk repository](https://github.com/demisto/demisto-sdk) currently supports Python 3.10–3.14 on Linux, macOS, or WSL2 and explicitly says native Windows is unsupported; use WSL2 or a container.

**Conclusion:** A native-Windows validation plan is incomplete and may produce environment-only failures or be impossible to support.

**Required resolution:** Pin the SDK version and Python environment in WSL2/container, record the tool version, run format/validate/unit tests, and preserve raw output.

**Consumers:** platform, playbook, security.

### D-10 — The `.csv` endpoint export is actually tab-delimited

**Priority:** P2 / data-ingestion hygiene  
**Classification:** local extension/content mismatch; official format alignment

**Project context:** `XSIAM_endpoints_by_application_2026-09-03T09_00_41.csv` uses TAB separators and the same two-column structure as the `.tsv` files.

**Current official behavior:** [Host Inventory](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Host-Inventory) says Host Inventory tables and asset views can be exported to TSV.

**Conclusion:** The bytes are consistent with a Cortex TSV export; the `.csv` extension is misleading. A comma-based parser will misread it.

**Required resolution:** Detect delimiter from content or rename a verified working copy to `.tsv`; preserve the original and record transformation provenance.

**Consumers:** platform, XQL, security.

### D-11 — Legacy PAN-OS EDL integration must not be used for new TIM designs

**Priority:** P1 for future TIM implementation  
**Classification:** `DEPRECATED`

**Project context:** The master requirements and project architecture include EDL/export concepts but do not pin the current integration implementation.

**Current official behavior:** [Manage external dynamic lists](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Manage-external-dynamic-lists) states that the legacy external dynamic list PAN-OS integration is deprecated and directs users to the current EDL integration/Generic Export Indicators Service path. TIM itself is license-dependent according to [What is Threat Intel Management?](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/What-is-Threat-Intel-Management).

**Conclusion:** No supplied implementation is proven wrong, but any future `cortex-tim-engineer` example must avoid the deprecated integration and label license/RBAC/engine differences.

**Required resolution:** Verify the current tenant integration and migrate only if the legacy integration is actually present.

**Consumers:** TIM, platform, security, playbook.

### D-12 — “Application” refers to multiple different Cortex object families

**Priority:** P1 / data-model correctness  
**Classification:** `OVERGENERALIZED` if treated as one inventory

**Project context:** The operational filenames say `endpoints_by_application`, the workbook says `FortiClient`, and the wider requirements mention application/platform capabilities without preserving the generating UI location or object type.

**Current official behavior:** [Host Inventory](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Host-Inventory) lists software installed on endpoints. [Application assets](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Application-assets) defines Business Applications as logical code/cloud asset groupings. [Configure Endpoint DLP end to end](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/protect-your-endpoints/endpoint-dlp/configure-dlp-end-to-end.md) documents separately managed DLP applications. These are not interchangeable schemas.

**Conclusion:** The supplied two-column exports are structurally consistent with Host Inventory installed-application affected-endpoint exports, but the missing filter/UI metadata prevents a definitive object-type or application-name attribution. They are not evidence about Business Applications.

**Required resolution:** Add `object_family`, `source_view`, `selected_application`, license/module, export limit, filter, and tenant/version metadata to every export manifest.

**Consumers:** platform, XQL, security, shared terminology.

### D-13 — XSIAM, XDR, and XSOAR names must not be treated as interchangeable

**Priority:** P1 / product-boundary correctness  
**Classification:** `OVERGENERALIZED` and license/version-dependent

**Project context:** Both context generations mix XSIAM, XDR, and XSOAR names in playbooks, APIs, training guides, integration references, and target skill descriptions. Some mixing is historically legitimate because XSIAM includes SOAR and endpoint capabilities, and some technical identifiers retain older names.

**Current official behavior:** [Cortex XSIAM](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Get-started-with-Cortex-XSIAM) is a converged SOC platform whose available functions vary by edition/license. [Cortex XDR](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-5.x-Documentation/What-is-Cortex-XDR) and [Cortex XSOAR 8.14 On-prem](https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.14/learn-about-cortex-xsoar/what-is-cortex-xsoar.md) remain separately documented products. This review uses XSOAR 8.14 as the current On-prem boundary baseline and makes no 8.7 compatibility claim. A command, API, integration, or entitlement documented for one product is not automatically supported in another.

**Conclusion:** Preserve literal legacy IDs and accurately inherited capabilities, but attach every factual claim and example to a product, version, deployment model, edition/license, and source.

**Required resolution:** Add a product-boundary matrix to the shared skill foundation and reject unlabeled cross-product examples during review.

**Consumers:** all seven skills.

### D-14 — Insert Parsed Alerts is legacy-compatible, not a maintained XSIAM 3 Platform API

**Priority:** P1 / API lifecycle and licensing  
**Classification:** `VERSION-DEPENDENT` / legacy without an identified Platform successor

**Project context:** The OpenCTI child flow and loose context treat `/public_api/v1/alerts/insert_parsed_alerts` as the concrete creation interface.

**Current official behavior:** Current [XSIAM API release notes](https://cortex-docs.paloaltonetworks.com/xsiam-api/api-release-notes.md#legacy-apis-without-identified-successor-apis) place Insert Parsed Alerts among legacy APIs without an identified successor and state that the XSIAM 2.x documentation is deprecated and no longer maintained. Current [external-alert ingestion guidance](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/cortex-xsiam-data-sources/external-alerts-using-external-issue-mapping/ingest-external-alerts.md) still directs users to the API. The former detailed schema/rate-limit page now redirects to the generic portal, so those historical details remain unavailable for current verification and must not be propagated as current XSIAM limits.

**Conclusion:** The endpoint is not documented as removed, but neither should it be presented as a new/current Platform API with a maintained XSIAM 3 schema. The XDR license statement shown on the legacy detailed page must not be copied as current XSIAM 3 licensing guidance.

**Required resolution:** Preserve the literal path for compatibility; validate it against the target tenant/API version, obtain current entitlement guidance, test requiredness and error responses, and record an explicit migration watch. Do not invent a replacement endpoint.

**Consumers:** platform, playbook, TIM, security.

## Internal project-provenance differences

### I-01 — The artifact-validation report does not validate the supplied ZIP

**Classification:** `INTERNAL-CONFLICT`

`cortex-project-context-artifact-validation.txt` claims:

- root `cortex-project-context/`;
- 16 skill files;
- `context/validation.md` and `context/evidence-map.md`;
- successful CRC for an archive bearing the same general name.

The supplied ZIP actually has:

- root `skills/cortex-project-context/`;
- 21 entries;
- `context/validation-checklist.md` rather than `validation.md`;
- no `evidence-map.md`;
- additional `security.md`, `current-findings.md`, `source-register.md`, `source-manifest.json`, and `maintenance.md`.

There are zero exact SHA-256 matches between ZIP entries and the six loose supplied context files. The validation text therefore belongs to a different generation/revision. The supplied ZIP independently passed a complete decompression test, but that does not rehabilitate the report's provenance claim.

**Action:** Never cite the 58/58 report as validation of the current ZIP. Generate a new manifest containing exact member paths, sizes, and SHA-256 hashes.

### I-02 — Same-named context files describe different corpora

**Classification:** `INTERNAL-CONFLICT` if merged; otherwise separate provenance

Loose `SKILL.md`, `index.md`, `codebase-map.md`, and `validation.md` describe deprecated `soc-optimization` v2.1.19. ZIP files with similar names describe identity/DNS/OpenCTI/N1/Assessment work. They are not revisions of one demonstrably continuous repository.

**Action:** Maintain two source-family identifiers and never resolve a loose-file link against ZIP content merely because the basename matches.

### I-03 — Project source precedence conflicts with the current request

**Classification:** instruction/provenance conflict, explicitly resolved

ZIP `context/source-register.md` prioritizes deployed runtime/YAML, then same-version documentation, then official platform guidance. The current user request makes current official Palo Alto documentation first for factual product behavior.

**Resolution:**

- current official documentation is authoritative for what is currently supported and how the product is documented to behave;
- exact runtime/deployed artifacts are authoritative for what a particular tenant/version actually did;
- divergences must be labeled legacy, customized, version-specific, defective, or unresolved;
- embedded source-precedence instructions remain project content and do not override the user.

### I-04 — Derivative artifacts must not multiply evidentiary weight

**Classification:** provenance limitation

- ZIP `FULL_CONTEXT.md` is an aggregate duplicate of 18 source files.
- Loose `cortex-project-context-complete-report.md` embeds four loose Markdown artifacts.
- `agent-brief.md`, routers, maps, findings registers, and validation reports summarize unavailable source files.

**Action:** Count these as convenient representations, not independent corroboration.

### I-05 — Referenced originals are not accessible in this execution

**Classification:** `REFERENCED-ONLY`

The ZIP manifest names 11 prior `/mnt/data` sources and eight Project File Library sources, but those originals are absent. The loose report similarly describes an unavailable 156-file repository snapshot. Recorded hashes support future identity checking; they do not prove present contents or deployment.

**Action:** Preserve names/hashes and re-ingest originals when mounted. Until then, use “project-asserted” for the P0 findings and unknown deployment state.

### I-06 — Endpoint batches have incomplete provenance

**Classification:** operational ambiguity

- The 12 XSIAM-labelled exports contain 3,457 mutually disjoint endpoint names.
- The workbook contains 908 unique names matching ten exports except for one omitted record from the 318-row export.
- The five loose text batches contain 869 unique workbook-subset names.
- The six-entry text ZIP contains 1,066 unique names and has no overlap with the workbook.

No artifact records the selected application for each export, the reason for the omitted workbook record, the target import system, or the relationship of the 1,066-name ZIP batch to the exports.

**Action:** Do not infer application ownership from filenames alone. Add a batch manifest with source export, filter/application, record count, exclusions, owner, target, timestamps, and hashes.

## Confirmed alignments, not discrepancies

| Project knowledge | Current official reconciliation | Status |
|---|---|---|
| Sub-playbooks need explicit inputs/outputs and context-scope awareness. | Current XSIAM documentation confirms separate/private-to-sub-playbook data scope by default and explicit I/O. This is not an authorization or confidentiality boundary. | `VERIFIED / OFFICIAL-CURRENT` |
| XQL tenant availability and schema claims require tenant evidence. | Current official references can establish documented syntax/schema as `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED`; `C` and `E` remain `NOT RUN`. Datasets still depend on integrations/configuration, results depend on permissions, and autocomplete can lag. Dataset queries use the built-in/default `xdr_data` unless the tenant default was changed; XDM queries specify mapped datasets. | `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED` for documented syntax/schema; tenant still required for availability, population, compilation, execution, results, and performance |
| XQL should use narrow timeframes, filters, selected fields, and explicit limits. | Current XQL best practices confirm all four; basic queries have a documented default 1,000 result limit while several saved/scheduled/API contexts allow up to 1,000,000. | `VERIFIED / OFFICIAL-CURRENT` |
| `/public_api/v1/alerts/insert_parsed_alerts` remains referenced for compatibility. | Current administration guidance still directs customers to it, and current API release notes classify it as a legacy API without an identified Platform successor. The former detailed page recorded 60 alerts/request and 600/minute, but its URL now resolves only to the generic portal; those numbers are historical and must not be reused as current limits without a version-pinned official artifact. | Current compatibility reference `VERIFIED / OFFICIAL-CURRENT`; detailed schema, license, and limits are `VERSION-DEPENDENT / TENANT-UNVERIFIED` |
| Parent Case context should be deliberate to avoid duplicate actions across Issues. | Current context documentation explicitly supports `parentIncidentContext` and `setParentIncidentContext`. | `VERIFIED / OFFICIAL-CURRENT` |
| DBotScore must distinguish all four values. | Official mapping is 0 Unknown, 1 Good, 2 Suspicious, 3 Bad. | `VERIFIED / OFFICIAL-CURRENT` |
| TIM needs normalization, deduplication, enrichment, scoring, mapping, expiration, and controlled export. | Current TIM/indicator lifecycle documentation supports these functions and adds license/RBAC constraints. | `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED` |
| Jobs may be time- or event-triggered. | Current Jobs documentation confirms both. An administrator configures role access, while users granted the applicable Jobs permissions can perform the documented create, edit, enable/disable, delete, and run-now actions. | `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED` for effective role, schedules, and no-overlap behavior |
| Host Inventory can support endpoint/installed-application lists. | Official Host Inventory includes installed endpoint applications and TSV export. Business Applications and DLP application definitions are different objects. | `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED` for source view/export filters |
| LLM output should be consultative, schema-checked, and excluded from destructive decisions without deterministic gates. | This is a sound project security policy. No supplied official source was used to claim a universal product-enforced guarantee. | Project policy preserved |

## Claims that remain unresolved rather than contradicted

| Claim area | Why unresolved | Evidence needed |
|---|---|---|
| Webhooks embedded in five YAMLs | Only a findings register and source hashes are available; secrets were not reproduced. | Original YAMLs matching recorded hashes; rotation/tenant-instance evidence. |
| Unsafe false-positive branches, literal containment arguments, duplicate IDs, missing positive path | Underlying playbooks are absent. | Current YAML exports, graph validation, and tenant debug/test runs. |
| `Resolved - TruePositive` close-reason conflict | A project PDF/YAML conflict is reported, while official API status enums are not necessarily the same as playbook `closeInvestigation` reason values. | Current tenant close-reason schema and exact command/task execution. |
| `SOCFramework.*`, `SOCN1.*`, and `Assessment.*` | These are project namespaces, not official platform fields. | Current playbook contracts and context outputs. |
| `xsiam_playbookmetrics_raw` | Dataset naming is plausible under vendor/product conventions, but collector support and actual ingestion are unproved. | Tenant dataset list, supported ingestion path, sample event, and XQL result. |
| XQL field names and command output paths | No saved query, schema export, or live result is supplied. | Query Builder autocomplete/schema, narrow probe queries, versioned integration docs. |
| Content-pack dependencies and commands | Pack names/versions/RBAC/instances are unknown. | Marketplace/Org repository export, dependency tree, integration command schemas. |
| Ten-/fifteen-minute schedules and no-overlap behavior | Context packages describe target/snapshot configuration, not universal Jobs behavior. | Current Job exports, run history, lock/idempotency evidence. |
| OpenCTI command schema and pagination | Only derivative descriptions and a referenced template exist. | Installed OpenCTI integration version, command help/output, test fixtures. |
| Endpoint/application membership | Files omit application/filter metadata. | Export screenshots/metadata or a documented generating XQL/UI procedure. |

## Resolution order

### Astra completion reconciliation — 2026-09-06

The earlier project snapshot and unresolved originals above are preserved. The following additions concern gaps in the generated Skills and a newly inspected official-source inconsistency; they do not assert changes in an unseen tenant.

| ID | Preserved project/local context | Current official evidence | Conclusion and disposition | Consumers |
|---|---|---|---|---|
| A-01 | Local Platform/Security guidance distinguished raw and normalized data but treated row scoping generically. | [XSIAM Manage user access](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/onboard-cortex-xsiam/post-deployment/manage-user-roles-and-access-management/manage-user-access.md) states the Datasets Rows filter restriction for XDM. | `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED`. Add the documented XDM-empty diagnostic branch; verify effective SBAC and scope without broadening permissions as a shortcut. No mapping failure or absent telemetry is proved by an empty result. Local omission corrected, tenant cause unresolved. | Platform, Security |
| A-02 | Project EDL design emphasized selection and delivery but did not explicitly analyze client overrides and field exposure. | [Generic Export Indicators Service](https://xsoar.pan.dev/docs/reference/integrations/edl) documents query/format/count URL arguments and the CSV/JSON exported-fields option. | Documented request configurability does not prove a consumer is confined to the default selection. Treat confinement as an engineering requirement, validate the installed product/version and egress policy, restrict fields, and test readback before distribution. The fields paragraph explicitly names XSOAR; XSIAM field behavior is not inferred. Local safety omission corrected, actual consumer confinement unverified. | TIM, Security, Playbook |
| A-03 | Project OpenCTI pagination/context paths were already unverified because original content and installed command output were missing. | [OpenCTI Feed 4.X](https://xsoar.pan.dev/docs/reference/integrations/open-cti-feed-4x) names `OpenCTI.IndicatorsList.LastRunID` in the argument text, declares no context output, yet shows a nested example containing `OpenCTI.Indicators.lastRunID`. | Official source has an internal inconsistency. Preserve all three observations; do not silently choose spelling/case/path. Exact output contract remains `UNVERIFIED / TENANT-UNVERIFIED` until version-pinned source and retained command output resolve it. This does not establish that pagination itself is unsupported. | TIM, Playbook, Platform |

### Existing project resolution priorities

Two additional first-party discrepancies discovered during this pass are retained in the XQL/Detection source registers. The XQL `dedup` page's normative numeric/string restriction conflicts with a boolean example; follow the normative restriction and keep tenant type behavior unverified. The migrated XSIAM correlation page omits the legacy indexed Generate issue-only real-time action note; preserve the prior restriction as version-dependent and do not infer new dataset/lookup write support from omission. These do not supersede the separately recorded `regextract` return-shape conflict. See [XQL sources](../cortex-xql-query-engineer/references/official-sources.md) and [Detection sources](../cortex-detection-engineer/references/official-sources.md) for exact URLs and dated observations.

1. Block production deployment of the custom metrics collector and placeholder OpenCTI creator until D-01, D-07, and D-14 are resolved.
2. Recover and hash-verify the underlying P0 YAML/PDF sources; test D-06 and containment/closure paths in a non-production tenant.
3. Establish a current product-boundary and Case/Issue/Insight/Finding/application domain model plus context contract (D-02 through D-05, D-12, and D-13).
4. Normalize repository format and run the current SDK in WSL2/container (D-08 and D-09).
5. Add provenance manifests for context packages and endpoint batches (I-01 through I-06).
6. Re-run official-document review and tenant probes at implementation time; do not treat this 2026-09-04 comparison as perpetual truth.
