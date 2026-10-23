# ChatGPT account import test — 2026-10-23

This records observations from the user's account after explicit confirmation to import/install and verify the seven Skills.

## Artifact

- File: `cortex-ai-skills-plugin-0.1.1.zip`.
- Size: 440,288 bytes.
- SHA-256: `de85688224c01a32f59d49fbb3aa6dae72ba13503ef50e6146344db56ac646ea`.
- The archive was unchanged between independent review and upload.

## Observed actions and results

1. Opened the signed-in Chrome session at ChatGPT Plugins.
2. Chose Add → Upload plugin archive, opening New Plugin.
3. Selected the generated ZIP; the dialog displayed its exact filename.
4. After user confirmation, clicked Add plugin. Processing completed at the Cortex AI Skills detail page.
5. Clicked Install plugin. The control changed to Manage/Try in chat, and Cortex AI Skills appeared under Installed.
6. Expanded the Skill list. The page showed **Skills 7**, with:

| Canonical Skill | Visible label |
|---|---|
| cortex-detection-engineer | Cortex Detection Engineer |
| cortex-platform-engineer | Cortex Platform Engineer |
| cortex-playbook-engineer | Cortex Playbook Engineer |
| cortex-security-engineer | Cortex Security Engineer |
| cortex-threat-hunter | Cortex Threat Hunter |
| cortex-tim-engineer | Cortex TIM Engineer |
| cortex-xql-query-engineer | Cortex XQL Query Engineer |

Information showed version **0.1.1** and category Security. The importer supplied the account developer display name; original contributor attribution remains in the manifest/license.

## Evidence scope

Import acceptance, completed installation and seven-item interface listing: **PASS for this account/artifact/date**.

Reference loading during a task, behavior of every Skill, portability to another account, Cortex schema/compiler acceptance, tenant execution, deployment and efficacy: **NOT RUN**.

No conversation was sent, private tenant inspected, Cortex API called, or public plugin-directory submission performed. The account URL and screenshot are retained locally rather than published in this repository.

The [build manifest](../packages/0.1.1/release-manifest.json) predates this test and intentionally retains build-time NOT RUN labels. This record supplies the later UI evidence without rewriting deterministic artifacts.
