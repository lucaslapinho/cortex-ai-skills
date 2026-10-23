# Official source register

## Contents

- [Use and precedence](#use-and-precedence)
- [Core Cortex XSIAM TIM sources](#core-cortex-xsiam-tim-sources)
- [Cortex XSOAR scoped source](#cortex-xsoar-scoped-source)
- [Integration references](#integration-references)
- [Official example repository](#official-example-repository)
- [Freshness procedure](#freshness-procedure)
- [Unsupported conclusions](#unsupported-conclusions)

## Use and precedence

This register was author-reviewed on 2026-09-04. It records the narrow claim each source can support; it is not proof of tenant applicability or runtime behavior. Before an implementation or change, re-open the exact page and confirm product, version, deployment, license/add-on, content pack, integration version, and direction.

Precedence:

1. current official Palo Alto Networks product documentation;
2. current official Palo Alto Networks integration references, API references, examples, and product guides;
3. verified project-specific artifacts available in the current workspace;
4. secondary material only when necessary and clearly labeled.

No secondary sources are needed for the bundled factual baseline.

The [2026-10-23 targeted refresh](2026-10-23-refresh.md) rechecks eleven specific product/integration pages, including current lifecycle URLs and retained OpenCTI documentation conflicts. This supplements the historical register; it does not assign a new review date to other entries.

## Core Cortex XSIAM TIM sources

| ID | Official source | Narrow supported use | Boundary |
|---|---|---|---|
| X01 | [What is Threat Intel Management](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/What-is-Threat-Intel-Management) | XSIAM 3.x TIM purpose, entitlement wording, aggregation/scoring/sharing, feeds/lists, relationships, lifecycle, and high-level source-to-distribution flow | High-level overview; not tenant configuration, integration mapping, or enforcement evidence |
| X02 | [Configure Threat Intelligence feed integrations](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Configure-Threat-Intelligence-feed-integrations) | Feed parameters are integration-dependent; common fetch enablement, interval, reliability, expiration, engine/proxy, exclusion, and certificate settings; multi-feed expiration precedence | Common settings are non-exhaustive; checkpoint/reset or fetch-history behavior requires exact integration-specific evidence, and the tenant must be inspected |
| X03 | [Indicator lifecycle](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Indicator-lifecycle) | Indicator type/value, validation/formatting, reputation/enrichment, mapping, expiration, and possible reactivation on new data | Does not prove a tenant transition or custom mapping |
| X04 | [Indicator type profile](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Indicator-type-profile) | Documented processing order, reputation/expiration profile, and cache behavior for its named context | Cache default/path is not universal and can be version/customization dependent |
| X05 | [Expire an indicator](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Expire-an-indicator) | Expired indicators remain stored/searchable; manual expiration has documented precedence | State-changing operation; no tenant action authorized by this reference |
| X06 | [Exclude indicators from enrichment](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Exclude-indicators-from-enrichment) | Scope-specific enrichment exclusion and documented supported types | Not a universal exclusion list and not deletion |
| X07 | [Delete and exclude indicators](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Delete-and-exclude-indicators) | Distinguishes deletion/exclusion behavior in current XSIAM documentation | Destructive; requires approval, recovery, and tenant validation |
| X08 | [Export indicators](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Export-indicators) | Table export to CSV/STIX and integration/playbook/Generic Export Indicators Service paths | Export does not prove consumer receipt or enforcement |
| X09 | [Manage external dynamic lists](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Manage-external-dynamic-lists) | Current XSIAM EDL management context and migration boundary | Exact service configuration and consumer behavior remain tenant-specific |
| X10 | [Forward requests to long-running integrations](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Forward-Requests-to-Long-Running-Integrations) | Engine-forwarding and long-running integration deployment considerations | Does not define every integration endpoint/auth flow |
| X11 | [Threat Intelligence permissions](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Threat-Intelligence-permissions) | View/edit and adjacent permission considerations for current XSIAM TIM | Effective tenant permissions still require inspection |
| X12 | [Generate issues from indicators using indicator rules](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Generate-issues-from-indicators-using-indicator-rules-for-prevention-and-detection) | Current product boundary for indicator-rule operationalization | Does not authorize creation, enablement, or prevention action |
| X13 | [Manage indicator relationships](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Manage-indicator-relationships) | Current high-level support for indicator relationships | Do not infer native field or relationship-type schema |
| X14 | [Run indicator extraction in the CLI](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Run-indicator-extraction-in-the-CLI) | Current extraction/enrichment operational context and batch-performance caution | Does not justify unsafely running commands or apply to every surface |
| X15 | [Extract indicators](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Extract-indicators) | Inline/out-of-band extraction concepts for the documented context | Extraction is not feed ingestion, verdict correctness, or enforcement |
| X16 | [Datasets and presets](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Datasets-and-presets) | Lists the current XSIAM Indicators dataset as `indicators` in the documented catalog | The reviewed page does not document an `indicator_relationship` dataset or associate that name with the TIM add-on; fields and tenant availability remain unverified |

These entries are `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` unless newer or tenant evidence changes the label.

## Cortex XSOAR scoped source

| ID | Official source | Narrow supported use | Boundary |
|---|---|---|---|
| S01 | [Indicator verdict — Cortex XSOAR 8.9 on-premises](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSOAR/8.9/Cortex-XSOAR-On-prem-Documentation/Indicator-verdict) | Legacy XSOAR 8.9 on-premises verdict values and documented reliability/recency/tie and multi-value merge behavior | `DEPRECATED / OFFICIAL-CURRENT / TENANT-UNVERIFIED`; 8.9 is EOL and must not be a new-design baseline |
| S02 | [Product support lifecycle — Cortex XSOAR on-premises](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSOAR/8.9/Cortex-XSOAR-On-prem-Documentation/Product-support-lifecycle) | Current lifecycle table records XSOAR 8.9 EOL on 2026-04-07 | Lifecycle evidence only; continued tenant presence does not restore support |

S01 is retained only to interpret an explicitly legacy 8.9 environment. Prefer a supported target release and revalidate its behavior; do not transfer the legacy merge rule to XSIAM or another XSOAR version.

Older XSOAR indicator-concept pages that explicitly show an end-of-life product context must not be used as a current cross-product baseline.

## Integration references

Palo Alto Networks hosts current Cortex integration references at `xsoar.pan.dev`. Availability statements and settings remain tied to the named integration and current content release.

| ID | Official source | Narrow supported use | Boundary |
|---|---|---|---|
| I01 | [TAXII Feed](https://xsoar.pan.dev/docs/reference/integrations/taxii-feed) | Inbound TAXII 1.x feed; documented supported products/minimum versions and instance mapping context | Not TAXII 2 and not outbound service behavior |
| I02 | [TAXII 2 Feed](https://xsoar.pan.dev/docs/reference/integrations/taxii-2-feed) | Inbound TAXII 2.0/2.1; supported product list; TLP red enrichment handling; the complex-observation note is worded specifically for Cortex XSOAR TIM indicators | Availability includes XSIAM, but the XSOAR-specific representation statement must not be transposed to XSIAM; validate XSIAM relationship handling separately |
| I03 | [TAXII Server](https://xsoar.pan.dev/docs/reference/integrations/taxii-server) | Outbound long-running TAXII 1.x server; availability and product-specific access/auth paths; collection-as-indicator-query wording explicitly names Cortex XSOAR | Do not transpose XSOAR collection/query semantics to XSIAM; exact selection, endpoint, auth, hosting, and engine path depend on product/deployment |
| I04 | [TAXII 2 Server](https://xsoar.pan.dev/docs/reference/integrations/taxii2-server) | Outbound long-running TAXII 2.0/2.1 server; supported product versions and product-specific deployment paths; collection-as-indicator-query and API/object wording explicitly name Cortex XSOAR | XSIAM selection/object semantics remain unverified; published performance examples are not tenant performance guarantees |
| I05 | [MISP v3](https://xsoar.pan.dev/docs/reference/integrations/misp-v3) | Named MISP v3 integration availability, parameters/commands, and breaking-change notes | Verify installed pack; do not turn reference parameters into universal schema |
| I06 | [MISP Feed](https://xsoar.pan.dev/docs/reference/integrations/misp-feed) | Separate MISP Feed integration availability and feed context | Not interchangeable with MISP v3 |
| I07 | [Generic Export Indicators Service](https://xsoar.pan.dev/docs/reference/integrations/edl) | Current long-running service for serving indicator output/EDL use across listed products | Tenant/engine settings, URL/auth/TLS, selection, and capacity require exact validation |
| I08 | [Export Indicators Service](https://xsoar.pan.dev/docs/reference/integrations/export-indicators) | Official deprecation notice and successor reference | Deprecated; do not recommend for a new design without an explicit legacy reason |
| I09 | [PAN-OS EDL Management](https://xsoar.pan.dev/docs/reference/integrations/palo-alto-networks-pan-os-edl-management) | Official deprecation notice, successor direction, and stated support exception for customers with more than 1,000 firewalls | Legacy presence does not prove that the tenant qualifies for the exception or that the integration was removed |
| I10 | [OpenCTI Feed 4.x](https://xsoar.pan.dev/docs/reference/integrations/open-cti-feed-4x) | Current named integration; availability includes XSOAR and XSIAM; OpenCTI compatibility baseline; the out-of-box type list and automatic-creation wording explicitly name XSOAR | Version statement is time-sensitive; do not transpose the XSOAR mapping statement to XSIAM, whose exact mapping and tenant behavior remain unverified |
| I11 | [OpenCTI Feed 3.x](https://xsoar.pan.dev/docs/reference/integrations/open-cti-feed) | Official deprecation notice pointing to OpenCTI 4.x | Deprecated integration, not a current implementation baseline |
| I12 | [DBotScore](https://xsoar.pan.dev/docs/integrations/dbot) | Official normalized score convention and integration output context | Not a probability, universal provider output, or automatic enforcement rule |
| I13 | [Feed integrations developer guide](https://xsoar.pan.dev/docs/integrations/feeds) | Development contract and feed-integration design context | Developer guidance is not proof of an installed tenant integration's behavior |

## Official example repository

| ID | Source | Use | Boundary |
|---|---|---|---|
| R01 | [Palo Alto Networks Cortex content repository](https://github.com/demisto/content) | Official integration and content examples; construction research reviewed commit `61e517ae49cef61e248791e4c65d06cdeff67ad8` | `OFFICIAL-EXAMPLE`; repository HEAD or an example is not the installed tenant pack and is not normative over current docs |

Use a pinned commit when reviewing implementation details. Record the file path, integration version metadata, and commit hash. Never claim the tenant runs that revision without inventory evidence.

## Freshness procedure

### Targeted Astra refresh — 2026-09-06

I02 and I07-I10 were re-opened. The TAXII 2 Feed and OpenCTI product-wording boundaries remain applicable. I07's request/field behavior supports the new consumer-confinement review; I08-I09 retain their deprecation direction, including I09's fleet-size exception. I10's pagination-output prose, declared-output section, and example conflict; the exact usable path remains unverified. The detailed reasoning is in [OpenCTI](interoperability-and-distribution.md#opencti) and [consumer confinement](interoperability-and-distribution.md#consumer-confinement). This five-source refresh is not a new full-register review and does not establish installed-pack or tenant behavior.

For a product-sensitive answer:

1. record current UTC date;
2. open the exact official page, not only a search excerpt;
3. verify title, product, version family, deployment, and published/updated date where shown;
4. verify integration availability and current version metadata;
5. inspect deprecation or replacement banners;
6. compare the target tenant's installed version if evidence is available;
7. label the claim and record what remains tenant-unverified;
8. update the source register, affected guidance, examples, and regression cases together if behavior changed.

If the source cannot be opened, use `REFERENCED-ONLY` and do not repeat its remembered behavior as current fact.

## Unsupported conclusions

This register does not establish:

- that the target tenant owns the required license or add-on;
- that a named integration is installed, enabled, configured, healthy, or permissioned;
- an undocumented feed object, indicator, relationship, or API schema;
- a source-to-Cortex field mapping;
- a score conversion formula;
- that a fetch, enrichment, expiration, export, or deletion occurred;
- that a consumer retrieved an EDL or TAXII collection;
- that a firewall or other control attached, committed, or enforced a policy;
- production capacity, latency, completeness, correctness, or false-positive rate.

Those facts require retained tenant or downstream evidence and remain `NOT RUN` in the bundled validation ledger.
