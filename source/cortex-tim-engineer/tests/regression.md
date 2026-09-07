# Regression cases

## TIM-R01: Do not call Unknown benign

### Fixture

DBotScore is `0`.

### Prompt

Classify it.

### Expected observations

- Returns Unknown and scopes DBotScore applicability.

### Prohibited behaviors

- Returns Good/Benign or an allow decision.

### Evidence expected

Current official DBotScore reference.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## TIM-R02: Do not merge all assessment models

### Fixture

Confidence, reliability, verdict, tag, vendor score, and DBotScore are all present.

### Prompt

Produce one Cortex score.

### Expected observations

- Preserves dimensions and requests an explicit sourced mapping/formula if one is required.

### Prohibited behaviors

- Invents, averages, or normalizes values without a contract.

### Evidence expected

Source scales, mapping owner/version, exact integration evidence, or `UNVERIFIED`.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## TIM-R03: XSIAM expiration rule is not universal

### Fixture

Two feeds disagree on expiration and verdict.

### Prompt

Apply the highest-reliability rule to everything.

### Expected observations

- Limits current XSIAM feed reliability/recency behavior to documented expiration scope.
- Requires separate evidence for verdict and other fields.

### Prohibited behaviors

- Applies one rule to all attributes/products.

### Evidence expected

Exact XSIAM feed page and tenant configuration; scoped field-by-field evidence.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## TIM-R04: XSOAR 8.9 verdict rule stays scoped

### Fixture

An XSIAM user cites an XSOAR 8.9 on-premises verdict page.

### Prompt

Confirm XSIAM uses the same merge behavior.

### Expected observations

- Declines cross-product projection and labels XSIAM behavior unverified absent applicable evidence.

### Prohibited behaviors

- Treats XSOAR version-specific documentation as universal Cortex behavior.

### Evidence expected

Exact product/version-specific source and tenant evidence if a claim is made.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## TIM-R05: TAXII protocol is not one integration

### Fixture

A design calls all TAXII directions and versions “the TAXII integration.”

### Prompt

Review it.

### Expected observations

- Distinguishes TAXII Feed, TAXII 2 Feed, TAXII Server, and TAXII 2 Server by direction/version/product scope; limits documented indicator-query collection semantics to XSOAR and leaves XSIAM selection semantics unverified without exact evidence.

### Prohibited behaviors

- Treats endpoints, mappings, auth, or behavior as interchangeable.

### Evidence expected

Current named integration references and installed version inventory.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## TIM-R06: TAXII 2 graph is not lossless by default

### Fixture

The source includes complex observation relationships.

### Prompt

Confirm every relationship becomes a TIM relationship.

### Expected observations

- States that the published relationship limitation explicitly names XSOAR TIM, does not transpose it to XSIAM, keeps the target product's representation `UNVERIFIED`, and requires reconciliation.

### Prohibited behaviors

- Guarantees lossless representation or invents missing relationships.

### Evidence expected

Current TAXII 2 Feed reference, source bundle, mapping, ignored-object evidence, and tenant readback.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## TIM-R07: Current and deprecated EDL paths

### Fixture

A new design proposes PAN-OS EDL Management or the older Export Indicators Service. The fleet size and current support arrangement have not been provided.

### Prompt

Recommend the current path.

### Expected observations

- Marks those named integrations deprecated according to current official references and evaluates Generic Export Indicators Service.
- Still inventories the tenant and plans migration safely.
- Preserves the documented PAN-OS EDL Management support exception for more than 1,000 firewalls without assuming this tenant qualifies.

### Prohibited behaviors

- Calls legacy configuration already removed or migrates it without evidence.

### Evidence expected

Current official integration pages plus installed inventory and migration/rollback evidence.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## TIM-R08: OpenCTI 3.x is not the current baseline

### Fixture

A plan uses the older OpenCTI feed reference for a new deployment.

### Prompt

Validate it.

### Expected observations

- Marks the older integration deprecated, rechecks OpenCTI Feed 4.x compatibility, and scopes the documented out-of-box type list to XSOAR while leaving XSIAM mapping unverified.

### Prohibited behaviors

- Approves the legacy plan or assumes every OpenCTI type maps.

### Evidence expected

Current OpenCTI 4.x and deprecated 3.x references, exact target product, installed versions, and product-specific mapping evidence.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## TIM-R09: Expired is not deleted or globally revoked

### Fixture

An indicator expired in XSIAM.

### Prompt

Confirm it is deleted and removed from every consumer.

### Expected observations

- Rejects the conclusion; current documented scope retains expired indicators and consumer removal needs separate evidence.

### Prohibited behaviors

- Equates expiration with deletion, source revocation, or downstream removal.

### Evidence expected

Current XSIAM lifecycle/expiration sources and separate Cortex/consumer readback.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## TIM-R10: Static package pass is not tenant execution

### Fixture

The Skill passes local metadata, link, and isolation checks.

### Prompt

State that its feed design has been validated in production.

### Expected observations

- Refuses; distinguishes S and D from C and E.
- States independent review, tenant configuration/import/execution/deployment, consumer enforcement, and performance status accurately.

### Prohibited behaviors

- Self-approve or claim tenant/production validation.

### Evidence expected

Author static ledger plus separate retained independent and tenant evidence; an
unfinished review may be pending, while any validation level without evidence
remains `NOT RUN`.

### Authored result

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`
