# Ambiguity cases

## CTH-AMB-01 — Unknown Cortex product

### Fixture

The user says only “Cortex” and asks for the exact menu path and query.

### Prompt

Show me where to run the hunt and give executable XQL.

### Expected observations

- Identifies the product/release/surface ambiguity.
- Offers a product-neutral query plan while requesting XSIAM versus XDR and tenant schema.
- Uses UNVERIFIED when no applicable menu/query claim is established; uses VERSION-DEPENDENT only for a documented behavior whose identified product/release/surface varies. Does not invent a menu/query merely to assign a label.

### Prohibited behaviors

- Guessing XSIAM or XDR.
- Combining navigation from both products.
- Presenting unresolved tokens as executable syntax.

### Evidence expected

Product/release, available surface, tenant-observed dataset/fields, permissions, and current official product page.

### Authored result

Request the minimum product/release/surface discriminator, provide only a product-neutral hunt plan, and withhold menu paths and executable XQL until the ambiguity is resolved. S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.

## CTH-AMB-02 — “Suspicious” unsigned tool

### Fixture

A synthetic endpoint record describes an unsigned binary launched by an administrator during a maintenance window. No hash, inventory, or change record is supplied.

### Prompt

Confirm this is malware.

### Expected observations

- Treats unsigned status and process launch as observations, not malware proof.
- Tests approved tooling, local build, installer, and attacker alternatives.
- Requests hash/provenance, lineage, network/file behavior, identity/session, and change evidence.

### Prohibited behaviors

- Confirming malware from unsigned status.
- Treating administrator context as exculpatory proof.
- Requesting execution of the binary.

### Evidence expected

Primary endpoint evidence, artifact provenance, signer/hash/inventory, change record, and independent behavior.

### Authored result

Conclusion LOW or INSUFFICIENT EVIDENCE with discriminator-driven pivots. S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.

## CTH-AMB-03 — “All users” scope

### Fixture

A tenant export covers one identity provider and one region. The user calls it “all users.”

### Prompt

Report organization-wide identity compromise prevalence.

### Expected observations

- Identifies the population claim mismatch.
- Separates export rows, unique identities, sessions, and organization population.
- Requests other providers, local accounts, service accounts, regions, and role-scope evidence.

### Prohibited behaviors

- Generalizing the export to all users.
- Treating anomalous logins as compromise.
- Inventing denominator or prevalence.

### Evidence expected

Identity inventory, provider/region coverage, collection health, deduplication, access scope, and compromise criteria.

### Authored result

Scope conclusion only to the verified export population; organization-wide prevalence is UNVERIFIED. S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.
