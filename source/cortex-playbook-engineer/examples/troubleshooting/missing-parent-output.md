# Troubleshooting a Missing Parent Output

**Artifact classification:** `CONFIGURATION GUIDANCE`  
**Applicable product/surface:** Cortex XSIAM sub-playbook and context behavior; target release/tenant unknown  
**Evidence status:** context separation and explicit I/O concepts are `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED`; the fictional symptom below has no tenant execution evidence  
**Execution status:** diagnostic plan only

## Fixture

A parent playbook invokes a reusable enrichment sub-playbook. The child task appears complete, but the parent decision sees no enriched entity list. The supplied screenshot says “From Previous Tasks,” and an operator assumes the value must be available globally.

No export, sanitized context, command help, pack version, run ID, or task error is available.

## Why the symptom is ambiguous

Current XSIAM guidance says sub-playbook context is separate by default unless sharing is configured, and inputs/outputs should be explicit. It also warns that task inputs read from context. A missing value can therefore reflect:

- child producer returned a legitimate empty value;
- producer failed or timed out;
- installed command output schema changed;
- output was ignored, filtered, transformed, or not mapped;
- child output was not declared/mapped to the parent;
- value remained in separate child context;
- wrong literal path, type, cardinality, or case was selected;
- another task overwrote a shared key;
- effective role/command permission prevented execution; or
- Quiet Mode changed what is visible/indexed without removing context.

The screenshot cannot select among them.

## Safe diagnostic sequence

1. Record XSIAM release, playbook/child versions, content relationship, run/task identity, logged-in identity, and exact sanitized error.
2. Inspect the producer task in the debugger with protected/external tasks skipped or output-overridden.
3. Compare the exact installed command/script output schema with the child output declaration.
4. Determine whether outputs were ignored or extended and whether a filter/transform changed the value.
5. Inspect child context separately, then the declared child outputs and parent mapping.
6. Verify separate versus shared/global context selection.
7. Check type/cardinality, null/empty, list versus scalar, and stable association key.
8. Look for concurrent writers or overwrite behavior on the same key.
9. Test the actual playbook, context, and integration-command permissions with a positive and negative identity.
10. Compare Quiet Mode presentation with actual sanitized context.

Do not invent a replacement context path.

## Candidate correction

If evidence shows the child produced the right typed value in private child context but did not export it, the configuration-level correction is:

- define a named, structured child output with documented sub-keys;
- map the verified producer result to that output;
- map the child output explicitly into the parent;
- keep context separate unless global sharing has a documented need;
- validate valid, empty, error, multiple, duplicate, and wrong-type fixtures; and
- serialize any writes to the same destination key.

This is conditional guidance, not an observed root cause.

## Test result boundaries

| Level | Result | Rationale |
|---|---|---|
| S | NOT RUN | This authored example has not itself been evaluated as an isolated model response. |
| D | PASS | PB04, PB05, PB09, PB10, and PB15 were re-opened on 2026-09-06; they support the stated XSIAM context, visibility, debugger, and permission boundaries. They do not select the fictional root cause. |
| C | NOT RUN | No target mapping, command schema, or export was validated. |
| E | NOT RUN | No parent/child workflow or corrective change was executed. |

## References

- [Data contracts and context](../../references/data-contracts-and-context.md)
- [Playbook concepts](../../references/playbook-concepts.md)
- [Testing and troubleshooting](../../references/testing-deployment-troubleshooting.md)
- [Context contract template](../../templates/context-contract.md)
