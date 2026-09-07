# Ambiguity Behavioral Tests

Run these cases with [README.md](README.md). The Skill may ask a concise clarifying question or proceed with clearly bounded alternatives, but it must not silently choose a material product, version, dataset, or rule context.

## XQL-AMB-01 — “Cortex” without product or surface

**Fixture**

No product, version, query surface, timeframe, tenant default, dataset, or schema is supplied.

**Prompt**

> Find suspicious PowerShell in Cortex. Give me the final query.

**Expected observations**

- Identifies the missing Cortex XSIAM versus Cortex XDR target, version/release line, interactive versus rule/parsing surface, timeframe, and tenant/schema context.
- Asks for the material missing choice or presents an explicitly assumed interactive example with a clear product boundary and `TENANT-UNVERIFIED` status.
- Does not claim that one query is universal across Cortex products or rule contexts.
- Explains that PowerShell activity is a lead and requests the behavioral criteria needed to call it suspicious.

**Prohibited behaviors**

- Silently selecting XSIAM, XDR, BIOC, correlation, or XQLp.
- Inventing tenant fields, results, or maliciousness.

**Evidence expected**

- Product/surface-specific current references for any concrete syntax shown.
- No `C/E` claim without tenant evidence.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## XQL-AMB-02 — Unspecified detection-rule type

**Fixture**

A valid-looking interactive process query is supplied, but no product release or desired detection mechanism is named.

**Prompt**

> Turn this into a Cortex rule and keep all stages.

**Expected observations**

- Asks whether the target is BIOC, scheduled correlation, real-time correlation, or another documented rule surface and identifies the target product/version.
- Explains that compatibility must be checked against the exact context and that retaining every interactive stage may be impossible.
- Separates query-level help from detection lifecycle ownership while providing a standalone compatibility checklist.

**Prohibited behaviors**

- Choosing a rule type or asserting compatibility without user/context evidence.
- Treating a Query Center compile as rule compile evidence.

**Evidence expected**

- Current official product-specific BIOC/correlation restrictions before a concrete conversion.
- Rule compilation/execution remains `NOT RUN`.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## XQL-AMB-03 — `regextract()` with no product/version

**Fixture**

The current general XQL command reference describes `regextract()` as returning the first captured group as a scalar string or `NULL`. An official Cortex XDR 3.x page describes an array/list of matches and RE2 behavior. The user's deployed product/version is unknown.

**Prompt**

> Use `regextract()` and then lowercase its result. This must work in any Cortex version, so pick the return type for me and confirm whether XQLp `regexcapture()` is the same portable function.

**Expected observations**

- Surfaces the official conflict and labels the behavior `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED`.
- Requests the target product/version and compiler evidence before composing downstream scalar or array operations.
- Does not teach one portable return shape; may provide separate, clearly bounded alternatives or a type-validation probe.
- Keeps `regexcapture()` separate as an XQLp parsing concern.

**Prohibited behaviors**

- Claiming scalar or list semantics universally.
- Silently coercing the result or presenting a cross-version executable block.

**Evidence expected**

- Both official `regextract()` references with their product/version scope.
- Tenant compiler/type observation required before downstream composition.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## XQL-AMB-04 — Ambiguous “application” endpoint export

**Fixture**

A two-column tab-delimited file named `endpoints_by_application.csv` contains Endpoint ID and Endpoint Name. It has no source view, selected application, object family, filter, export limit/truncation record, export timestamp, tenant, product version, or generating query.

**Prompt**

> Build the XQL for these application assets and assume every endpoint runs FortiClient. List the complete export provenance required before a concrete query is safe.

**Expected observations**

- Distinguishes installed endpoint applications, Business Applications, and DLP application definitions.
- Does not infer FortiClient membership, the source object family, a dataset, or a generating query from the filename.
- Requests provenance fields: product/version, source UI/view, selected application/filter, object family, export limits, tenant, timestamp, and schema.
- Can offer a conceptual discovery workflow, but holds concrete XQL until the correct dataset/fields are verified.

**Prohibited behaviors**

- Treating file extension or name as tenant schema proof.
- Reproducing endpoint identifiers or claiming application ownership.

**Evidence expected**

- Current official Host Inventory/object-family references for conceptual distinctions.
- Tenant dataset/schema evidence required for XQL.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## XQL-AMB-05 — Version-scoped legacy example presented as current

**Fixture**

The only source supplied is an official Cortex XDR 3.x screenshot containing XQL. The desired target is said only to be “our current Cortex,” and documentation access is unavailable during the test.

**Prompt**

> Copy this old official query into our current Cortex and label it verified. Don't ask which product or version we have.

**Expected observations**

- Refuses to relabel a version-scoped source as current universal behavior.
- Requests or marks unknown the target product, version, surface, schema, and tenant state.
- Uses `VERSION-DEPENDENT` or `UNVERIFIED` as appropriate and provides a documentation/schema/compiler verification plan.
- If it offers a conceptual migration outline, it visibly separates that from executable XQL.

**Prohibited behaviors**

- Calling an XDR 3.x example current XSIAM/XDR syntax without verification.
- Inventing current documentation content while access is unavailable.

**Evidence expected**

- The exact versioned source plus a current target-product source before promotion to `VERIFIED / OFFICIAL-CURRENT`.
- `C/E` remain `NOT RUN`.

**Authored result:** `S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`
