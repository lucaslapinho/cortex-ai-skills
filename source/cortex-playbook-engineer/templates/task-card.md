# Current task card

Use the sections that help the current step. Fill them with known values or explicit proposals, not this template's angle-bracket placeholders. Full designs use the full design template; an error correction uses only cause, replacement and retest.

**Task <observed ID or proposed name> — <purpose>**

`<artifact class> · <product/version or unknown> · <type> · <OS if relevant> · <scoped status>`

Previous/next: <observed, reported or proposed connections; unknown if not supplied>.

**Configure**

<Short, evidenced editor location and current action.>

| Field/input alias | Value or prompt reference | Source/producer and missing-data behavior |
|---|---|---|
| <field> | <exact value or explicitly unresolved> | <evidence and treatment> |

**Copyable content**

For AI tasks: complete prompt in one selected dialect; separate full JSON Schema; explicit proposed/observed output name. For notifications: complete subject/body HTML and mappings. For commands: exact verified command/arguments only; otherwise a capability proposal and the decisive metadata needed. Never replace these with a checklist or screenshots.

**Check this task**

<Three to six specific checks; interactive only if supported. Include expected resolved input/output and the relevant failure path.>

**Next observation**

<Smallest evidence needed to continue in guided mode; no compulsory screenshot or redundant confirmation.>

## Fields by task type

| Type | Required detail for that task |
|---|---|
| Standard/command | Installed command/instance evidence, arguments, producer, returned paths, timeout/error behavior |
| Condition | Verified left operand, operator and right value, null/empty/multiple behavior, true/false/unknown destinations |
| AI | Full prompt, alias/placeholder/source mapping, missing data, full JSON Schema, output name and malformed-output route |
| Manual/approval | Question, authorized respondent, choices, expiry/no-response and audit record; distinguish information from authorization |
| Notification | Recipient scope, subject, full requested HTML, escaped mapped values, duplicate/failure handling |
| Response | Explicit authorized target/action, exclusions, deterministic gate, batch bound, readback and recovery |

Keep full contract dimensions in the associated design/contract when requested; expose the fields needed now without losing unresolved items. A simple current task does not require seventeen headings.
