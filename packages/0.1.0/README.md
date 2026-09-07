# Final delivery — Cortex AI Skills 0.1.0

The seven Skills were reviewed and improved with Astra, following the attached master prompt and accessible project knowledge. The skill-creator guidance informed standardization, package independence, and separation of tests and answer keys from runtime content.

This is an English translation of the build-time handoff record. For current host requirements and compatibility limitations, consult the [installation guide](../../docs/instalacao.md) and [validation guide](../../docs/validacao.md). Translating this index does not change the ZIPs or their checksums.

## Individual runtime packages

Extract the selected ZIP and use the Skill directory through your host's supported mechanism. Each package contains only SKILL.md, VERSION, agents, references, templates, and examples. No global installation or tenant changes were performed.

| Skill | Package |
|---|---|
| XQL engineering | [Download ZIP](cortex-xql-query-engineer-0.1.0-runtime.zip) |
| Detection engineering | [Download ZIP](cortex-detection-engineer-0.1.0-runtime.zip) |
| Playbook engineering | [Download ZIP](cortex-playbook-engineer-0.1.0-runtime.zip) |
| Threat hunting | [Download ZIP](cortex-threat-hunter-0.1.0-runtime.zip) |
| Threat Intelligence Management | [Download ZIP](cortex-tim-engineer-0.1.0-runtime.zip) |
| Platform engineering | [Download ZIP](cortex-platform-engineer-0.1.0-runtime.zip) |
| Security engineering and coordination | [Download ZIP](cortex-security-engineer-0.1.0-runtime.zip) |

## Source and evidence

[Complete source and reports](cortex-ai-skills-0.1.0-source.zip), [per-file manifest](release-manifest.json), and [checksums for all eight ZIPs](SHA256SUMS).

The source ZIP includes tests and answer keys and must not be installed as a runtime. It includes the knowledge inventory, differences from official documentation, independent reports, and retained responses.

## Validation and limitations

- 23/23 final targeted Astra tests passed in individual sessions with independent review.
- Cumulative S coverage: 74/253 reviewed decisions, consisting of 23 new decisions and 51 historical decisions retained through impact analysis; 179 cases remain NOT RUN.
- 14 Skill structure validations, 7 tooling tests, and the final release audit passed.
- The eight ZIPs and their 443 internal files were checked by hash and decompression; no tests or answer keys were included in the seven runtimes.
- Compilation, import, and execution in a Cortex tenant remain NOT RUN. Automatic discovery and equivalence across hosts/models are not certified.
- Official sources were checked on the recorded dates; documentation conflicts were preserved without inventing inaccessible project context.

Ready for use as an instruction/reference package within the documented limitations; this is not certification for production deployment. At the time of the original build handoff, no commit, push, or deployment had been performed.
