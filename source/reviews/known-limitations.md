# Known limitations

**Repository version:** `0.1.0`  
**Evidence snapshot:** 2026-09-06 completion; 2026-09-04 historical baseline

These are explicit evidence and operating limits, not hidden release certifications. Repository publication readiness means that the source packages, documentation, safety controls, and recorded review gates are suitable for publication. It does not mean that an artifact is ready to import, deploy, or execute unchanged in a particular Cortex tenant.

## Tenant and product validation

- No named Cortex XDR, Cortex XSIAM, Cortex XSOAR, TIM, Cortex Cloud, Broker VM, or other Cortex tenant/deployment was available for this build.
- No tenant license, edition, feature flag, content-pack inventory, role, RBAC/SBAC scope, dataset inventory, schema, retention setting, integration instance, or installed component was inspected.
- No XQL query or XQLp artifact was compiled or executed. No BIOC, correlation rule, parser, mapping, playbook, integration, feed, API request, collector, or platform configuration was imported, deployed, or run.
- No Issue, Case, alert, incident, indicator, enrichment, notification, containment, recovery, or downstream-enforcement result was observed.
- No production efficacy, false-positive rate, false-negative rate, completeness, latency, throughput, capacity, loss, cost, or performance claim was measured.

Accordingly, tenant-dependent `C` and `E` validation remain `NOT RUN` throughout the repository. Documentation and controlled response evaluation cannot promote a claim to `TENANT-SCHEMA-VERIFIED`, `TENANT-COMPILED`, or `TENANT-EXECUTED`.

## Astra completion evidence limits

The final targeted battery passed 23 fresh one-case-per-process Astra evaluations. Together with 51 historical decisions retained through explicit revision-impact review, cumulative reviewed S coverage is 74/253; 179 cases remain NOT RUN. Older raw outputs were not all available to rescore. The new full response records are retained; old batch omissions and citation failures are not erased. No full-suite Astra, cross-model-equivalence or statistical efficacy claim is made.

A Playbook file-read setup failed under the local read-only execution policy. The fallback manually supplied the runtime inline without disabling that policy. All seven Skills have this scoped manual-inline controlled evidence; native discovery/loading remains separately unverified. Current source-check dates are per claim, not a blanket September 6 full-register refresh. D labels describing supplied dated records in a forward do not count as fresh official checks.

The official OpenCTI pagination-output conflict, dedup normative/example type conflict and migrated real-time-action omission remain unresolved product-documentation limits. The Skills preserve them and require target evidence; source-publication readiness does not resolve an unseen tenant.

## Behavioral-test coverage

The repository contains seven categorized test files per Skill and a total of 253 authored cases. The Golden XQL review records complete-suite controlled evaluation and a revision-aware bridge to the current hardened runtime: all impacted adversarial controls were rerun and the superseding runtime hashes are explicit. That result would not transfer automatically across a future changed runtime or test package; a new affected prompt, fixture, or operating instruction still requires revision-impact analysis and a targeted rerun. The other Skills received independent controlled evaluation of selected risk-based cases rather than exhaustive execution of every authored case. Their unexecuted cases remain explicitly `NOT RUN`; a passed sample is not represented as full-suite coverage.

Tests are static or simulated response evaluations unless their ledger says otherwise. They do not establish tenant behavior, query compilation, import acceptance, deployment success, production detection efficacy, or action safety in a real environment.

## Host compatibility

- Package structure and instruction portability are reviewed separately from runtime behavior. Static review passed for runtime-only packages containing `SKILL.md`, `VERSION`, `agents/`, `references/`, `templates/`, and `examples/`; publication records and scorer tests must not be installed into forward-model context.
- ChatGPT desktop Skill loading, discovery, and behavioral runtime were not run.
- ChatGPT web/mobile requires distinct plugin packaging that this repository does not include; no plugin compatibility is inferred.
- Claude Code discovery/loading and behavioral runtime were not run.
- claude.ai custom-Skill upload and behavioral runtime were not run.
- Claude API Skill upload, `skill_id` use, code-execution behavior, and runtime package/network behavior were not run.
- Codex automatic discovery was not run. The Golden XQL record includes only its specifically documented tests-free manual-load smoke result; that result does not transfer to the other Skills.
- A supplemental `gpt-5.4-mini` XQL stress probe remained safe but did not include every required API-verification detail in one adversarial case. The canonical `gpt-5.6-sol` high-reasoning rerun passed the full rubric. Neither result proves equivalent behavior across models or hosts.
- The repository was statically checked on the recorded Windows build host. Equivalent Linux and macOS host executions were not performed.
- `agents/openai.yaml` is optional OpenAI UI, invocation-policy, and dependency metadata. Discovery and implicit capability matching derive from `SKILL.md` name/description subject to current host behavior; another host may require different installation or invocation metadata.

See [compatibility-review.md](compatibility-review.md) for the exact package, discovery, load, and runtime matrix. A static `PASS` never implies a runtime `PASS`.

## Documentation and version drift

- Official sources were reviewed at dated snapshots. Public documentation, living repositories, release behavior, licensing, product names, schemas, APIs, commands, content packs, and deprecation state can change afterward.
- Link reachability proves only that a URL responded at the time checked; it does not by itself prove semantic applicability or future availability.
- Version-sensitive claims require a new source refresh and target-product check before implementation.
- Retiring XSOAR Administrator Guide pages are retained only as explicitly `DEPRECATED` source-history pointers. Current product/version-specific Engine pages were identified separately for XSIAM, XDR, XSOAR 8 SaaS, and XSOAR 8.14 On-prem; they must still be reopened for the target deployment, and the retiring page must not be used to call the Engine concept deprecated.
- Tenant dataset and field availability must be verified in the target schema. A plausible name, documentation example, or another tenant's export is not proof.

## Project-knowledge boundary

Only artifacts that were actually readable in the execution environment were ingested. ChatGPT Project/File Library material, prior conversations, saved objects, and original scripts/playbooks mentioned but not exposed to the workspace could not be inspected and were not reconstructed. This limitation is recorded in the [project knowledge inventory](../research/project-knowledge-inventory.md) and [project-versus-official differences](../research/project-vs-official-differences.md).

Project-specific material is operational context, not product authority. Current official Palo Alto Networks documentation controls factual product behavior when the two conflict; unresolved differences remain visible rather than being silently overwritten.

## Templates, examples, and state changes

- Templates and worked examples are guidance. They are not import-ready artifacts unless an exact target schema, validator, controlled import, and retained evidence explicitly establish that status; this release makes no such claim.
- XQL blocks labeled as documentation-grounded still remain tenant-uncompiled and tenant-unexecuted.
- Placeholder fields, datasets, policies, routes, commands, endpoints, identities, and configuration values must be resolved from the named product/version and target environment.
- Read-only analysis is the default. Recommendations for isolation, disabling, deletion, blocking, deployment, rule enablement, feed distribution, notification, or API writes do not authorize those actions.
- A future state-changing use requires explicit authorization, least privilege, bounded scope, stop conditions, partial-failure handling, rollback or recovery, post-action verification, and evidence retention.

## Release interpretation

All Skills remain at `0.1.0` because material tenant and host-runtime evidence is intentionally absent. Publication does not warrant promotion to `1.0.0`, vendor certification, support entitlement, guaranteed portability, or fitness for a particular production environment. Operators must consult each Skill's `VALIDATION.md` and the [final QA report](final-qa.md) for the exact validated scope.
