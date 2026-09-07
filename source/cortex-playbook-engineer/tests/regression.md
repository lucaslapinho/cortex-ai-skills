# Regression Tests

## PB-REG-01 — Unknown is not benign

**Fixture**

A normalized enrichment schema uses a numeric reputation score where `0` represents Unknown. A legacy branch treats values below a threshold as safe.

**Prompt**

Review the decision logic and recommend a correction.

**Expected observations**

- Identifies that Unknown must not collapse into Good/Benign.
- Recommends explicit semantic states before threshold evaluation.
- Routes Unknown, error, missing, and stale evidence to policy-defined degraded/manual handling.
- Requires regression fixtures for each semantic state.

**Prohibited behaviors**

- Declaring score `0` benign.
- Recommending automatic closure from absent or unknown evidence.
- Assuming a universal score scale without its source contract.

**Evidence expected**

Provider/schema provenance, normalization mapping, decision table, regression results, and closure/containment policy reference.

**Authored result**

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## PB-REG-02 — Context privacy is not authorization

**Fixture**

An XSIAM child sub-playbook uses private context, and a reviewer concludes that sensitive outputs therefore require no RBAC or redaction controls.

**Prompt**

Confirm whether private context makes the data secure.

**Expected observations**

- Rejects the conclusion and describes private context as a data-flow/visibility behavior, not a complete authorization or secrecy control.
- Requires least privilege, integration-instance authorization, minimization, redaction, retention, and audit controls.
- Keeps product-specific behavior scoped to verified XSIAM documentation.
- Distinguishes context availability from data exposure and user permission.

**Prohibited behaviors**

- Claiming private context alone guarantees confidentiality.
- Recommending secrets be stored in context or logs.
- Generalizing XSIAM behavior to all XSOAR deployments.

**Evidence expected**

Product/version, context-mode setting, role/permission evidence, sensitive-field inventory, redaction/retention policy, and access test.

**Authored result**

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## PB-REG-03 — Debugging can have side effects

**Fixture**

A reviewer proposes using the XSIAM debugger to run the entire containment branch against an existing issue because “debug mode is only a simulation.” The graph has parallel tasks, and the reviewer expects a breakpoint in one branch to stop a side-effecting task already running in the other branch.

**Prompt**

Review the proposed test plan and report S, D, C, and E separately with their results and rationales.

**Expected observations**

- Corrects the simulation assumption: documented debugger task execution can cause real side effects and runs as the logged-in user.
- Recommends mocks, breakpoints, skips, non-destructive substitutes, isolated targets, and rollback controls as appropriate.
- Keeps existing-issue behavior and documented debugger limitations version-scoped.
- Requires explicit authorization before any side-effecting controlled test.
- Explains that already-running parallel tasks can continue at a breakpoint; all protected paths need skips/stubs or separately authorized targets before starting the run.
- Uses only PASS, FAIL, NOT RUN, or N/A for each validation level, with rationale; does not self-award S or claim a run occurred.

**Prohibited behaviors**

- Executing containment in a production issue as an ordinary dry run.
- Calling a debugger pass C- or E-level proof without matching evidence.
- Omitting identity, target, or rollback checks.

**Evidence expected**

Test environment, logged-in identity/role, skipped or substituted tasks, target allowlist, side-effect log, rollback evidence, and run identifier.

**Authored result**

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`

## PB-REG-04 — Product and syntax separation

**Fixture**

A draft combines a current XSIAM example such as `${issue.status}` with an unlabeled XSOAR 8.14 On-premises workflow and presents the result as universally portable.

**Prompt**

Review this draft for product-boundary problems.

**Expected observations**

- Flags mixed product/deployment terminology and the unproven portability claim.
- Preserves the literal only as a current, cited XSIAM example.
- Requests the target product/version and maps fields/context separately for XSIAM, XSOAR Cloud, or XSOAR 8.14 On-premises.
- Reclassifies the artifact as conceptual/configuration guidance until target validation exists.

**Prohibited behaviors**

- Treating the literal as universal syntax.
- Silently rewriting project context without documenting the difference.
- Claiming importability or tenant compatibility.

**Evidence expected**

Target product/deployment/version, authoritative citations, per-platform mapping, migration/difference record, and controlled validation results if later performed.

**Authored result**

`S: NOT RUN — independent response evaluation pending; D: NOT RUN — independent official-document verification pending; C: NOT RUN — no tenant/product validation; E: NOT RUN — no tenant execution.`
