# AI input dialects and source boundaries

Reviewed: 2026-11-14. Product scope: Cortex XSIAM AI Prompt tasks; not automatically XSOAR, another editor or every tenant release.

| Evidence | Supported claim | Limit |
|---|---|---|
| [Add AI Prompt tasks](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/playbooks/build-your-playbook/add-objects-from-the-task-library/add-ai-prompt-tasks.md), read 2026-11-14 | Custom-task instructions mark prompt inputs with brackets, map Extracted Inputs separately, and provide custom structured output. The page also contains `${...}` in system/helper examples. | These examples do not establish one universal prompt dialect. Confirm mode and extracted inputs in the actual editor. |
| Same official page, task-name instruction | The custom task name starts with a letter and excludes spaces/special characters. | This statement is about task names, not a universal alias regex. |
| [Test your playbook](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/playbooks/build-your-playbook/test-your-playbook.md), read 2026-11-14 | Debugger tasks run with the logged-in user's permissions and can affect real state; skips/overrides help bound a test. | A breakpoint does not stop already-running parallel tasks. A checklist is not a Debugger result. |
| User-supplied interactive-task proposal, inspected 2026-11-14 | A reported tenant error requires English letters, numbers and underscores in input names; the proposal uses `${Alias}` and separate context paths. | PROJECT-ASSERTED: original playbook export and target editor were not inspected. No task IDs, path producers or graph edges were independently validated. |
| Host capability instructions inspected 2026-11-14 | This Work session provides structured questions and inline HTML rendering with local controls. | LOCAL-VERIFIED availability only; other hosts may lack these features. Read live host documentation; no fixed API dependency. |

## Binding procedure

1. Identify product, task type (system, duplicated/local or custom) and the actual prompt field. Use a supplied working example, current Extracted Inputs or inspected UI before changing dialect.
2. Keep three distinct values: alias `WindowsEvidence`; prompt reference `${WindowsEvidence}` **or** `[WindowsEvidence]`; mapped value `${<observed.context.path>}`. Angle-bracket source is an unresolved placeholder, never paste it into a live mapping.
3. If the user provides a working `${}` dialect, emit that variant. With no tenant evidence, use the documented custom-editor bracket form conditionally and name the verification step. Do not emit mixed variants in one copyable prompt.
4. Choose simple ASCII aliases, for example `WindowsEvidence` or `collection_status`. This is a conservative naming convention, not a claim that a regex establishes product acceptance. Dots may belong in context paths, not the alias in the reported error.
5. Cross-check every prompt alias against Extracted Inputs and mappings. Distinguish unavailable evidence, empty successful collection and collection failure. Never silently map several aliases to the same unrelated object.
6. Inspect resolved values before the AI task. Literal `${Alias}` or `[Alias]` in the sent payload may indicate unresolved substitution; do not mark the task tested while those remain. Preserve the original evidence text if it legitimately contains such characters; inspect bindings rather than blindly deleting tokens.
7. Validate the proposed JSON Schema and actual output namespace separately in the target editor. Use a deterministic error/manual route for malformed output, missing required fields or unresolved evidence. Do not fabricate a playbook export from this task contract.

Example mapping for the reported error, only if that path is supplied for the target:

| Field | Replacement |
|---|---|
| Input name `Core.Endpoint` | `Endpoint` |
| Prompt reference in the observed dollar dialect | `${Endpoint}` |
| Mapped source value | Keep `${Core.Endpoint}` |

This fixes an alias/path conflation; it does not prove the source path exists. A source path is valid only for its supplied target and observed producer. A reported task #21 or proposed edge to #25 is not a reusable native task identifier.

## Validation scope

D: PASS only for the two official pages and claims above. S: separate behavioral evaluation required. C/E: NOT RUN in the absence of named tenant evidence. A JSON parser, interactive checkbox or syntactically plausible mapping cannot close those gaps.
