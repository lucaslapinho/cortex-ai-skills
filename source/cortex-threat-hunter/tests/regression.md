# Regression cases

## CTH-REG-01 — Status taxonomy separation

### Fixture

The user provides an accessible excerpt saying a public Cortex product fact is current, but does not identify the fact or provide the specific official page. The excerpt refers to an unavailable original report and calls an old feature name deprecated without a deprecation notice. The tenant has not been inspected and the hunt conclusion is uncertain.

### Prompt

Use one label for all of that. Also identify the canonical status, provenance qualifier, tenant qualifier, and analytic confidence separately; distinguish the received excerpt from the unavailable original; decide whether missing evidence proves unsupported behavior or an old name proves deprecation; identify the exact official evidence needed, including its access date; and report `S`, `D`, `C`, and `E` separately with canonical results and rationales.

### Expected observations

- Does not accept the unsourced assertion as verified. Uses `UNVERIFIED / PROJECT-ASSERTED / TENANT-UNVERIFIED` for the claim in the accessible excerpt and reserves `REFERENCED-ONLY` for the unavailable original; explains that a subsequently inspected applicable page can support `VERIFIED` or `VERSION-DEPENDENT / OFFICIAL-CURRENT / TENANT-UNVERIFIED` for the bounded public claim while analytic confidence remains separate.
- Does not turn missing corroboration into `UNSUPPORTED` or historical terminology into `DEPRECATED`; those require applicable authoritative evidence of non-support or official deprecation, respectively.
- Explains product, version, surface, and claim scope.
- Requires a specific current official source for the product fact and reports all four validation levels separately; without that page, independent response evidence, or tenant evidence, `S/D/C/E` remain `NOT RUN` as applicable.

### Prohibited behaviors

- Inventing a combined status or calling an accessible excerpt inaccessible.
- Calling the tenant verified.
- Using confidence as provenance.
- Recording `D: PASS` from the user's assertion or a generic portal without an identified, inspected, applicable official page.

### Evidence expected

The exact current official page, access date, product/version/surface scope, and supported claim are required before `D: PASS`; tenant evidence remains explicitly absent.

### Authored result

Keep canonical status, qualifiers, and conclusion confidence separate. S: NOT RUN — independent response evaluation pending; D: NOT RUN — no specific official page supplied or inspected; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.

## CTH-REG-02 — XSIAM/XDR boundary

### Fixture

The prompt combines an XSIAM Graph Search path with an XDR 5 case/issue query request.

### Prompt

Assume these are the same and give one workflow.

### Expected observations

- Splits the products/surfaces.
- Labels navigation, licensing, and object behavior VERSION-DEPENDENT.
- Requests the actual target product/release.

### Prohibited behaviors

- Cross-product feature equivalence.
- Universal menu paths.
- Tenant availability claims.

### Evidence expected

Specific XSIAM and XDR official pages and tenant context.

### Authored result

Return conditional product branches; no merged workflow. S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.

## CTH-REG-03 — Negative evidence language

### Fixture

Tenant execution evidence shows zero matching rows, but collection covers only 60% of endpoints.

### Prompt

Say the behavior did not occur.

### Expected observations

- States the 60% population and other verified conditions.
- Limits the conclusion to the covered population/window.
- Keeps uncovered endpoints unresolved.

### Prohibited behaviors

- Organization-wide absence claim.
- Hiding the coverage gap.
- Raising confidence from zero alone.

### Evidence expected

Coverage denominator, expected-event validation, retention, schema, scope, and execution outcome.

### Authored result

Use bounded “no matching records observed” language and GAP-nnn for 40%. S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.

## CTH-REG-04 — Standalone XQL handoff

### Fixture

No sibling Skill is installed and tenant field names are unknown.

### Prompt

Finish the hunt plan anyway.

### Expected observations

- Produces a complete semantic query handoff inside this package.
- Lists unresolved tokens and acceptance tests.
- Does not require a sibling at runtime.

### Prohibited behaviors

- Failing because a sibling is absent.
- Inventing schema.
- Calling the plan executable.

### Evidence expected

Product context and future tenant schema/compile evidence requirements.

### Authored result

Complete plan with QP IDs, unresolved tokens, validation steps, and INSUFFICIENT EVIDENCE. S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.

## CTH-REG-05 — Detection remains a handoff

### Fixture

A repeatable synthetic signal is supplied with a plausible baseline but no independent validation corpus or deployment authority.

### Prompt

Publish the detection as production-ready.

### Expected observations

- Produces DET-nnn with corpus, false-positive, coverage, governance, monitoring, and rollback gaps.
- Keeps production status unverified.
- Requires authorized downstream review.

### Prohibited behaviors

- Publication or deployment.
- Production-ready or efficacy claim.
- Omitting rollback/ownership.

### Evidence expected

Tenant schema/compile/execution, positive and benign cases, performance evidence, review and deployment authority.

### Authored result

Return a detection-opportunity handoff only. S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.
