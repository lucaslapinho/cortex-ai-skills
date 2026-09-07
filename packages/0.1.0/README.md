# Entrega final — Cortex AI Skills 0.1.0

As sete Skills foram revisadas e melhoradas com Astra, seguindo o prompt principal anexado e o conhecimento de projeto acessível. A skill-creator orientou a padronização, a autonomia dos pacotes e a separação dos testes/gabaritos do conteúdo de uso.

## Pacotes individuais de uso

Descompacte o ZIP escolhido e use o diretório da Skill no mecanismo suportado pelo seu host. Cada pacote contém apenas SKILL.md, VERSION, agents, references, templates e examples. Não houve instalação global ou alteração de tenant.

| Skill | Pacote |
|---|---|
| Engenharia XQL | [Baixar ZIP](cortex-xql-query-engineer-0.1.0-runtime.zip) |
| Engenharia de detecções | [Baixar ZIP](cortex-detection-engineer-0.1.0-runtime.zip) |
| Engenharia de playbooks | [Baixar ZIP](cortex-playbook-engineer-0.1.0-runtime.zip) |
| Threat hunting | [Baixar ZIP](cortex-threat-hunter-0.1.0-runtime.zip) |
| Threat Intelligence Management | [Baixar ZIP](cortex-tim-engineer-0.1.0-runtime.zip) |
| Engenharia de plataforma | [Baixar ZIP](cortex-platform-engineer-0.1.0-runtime.zip) |
| Engenharia de segurança e coordenação | [Baixar ZIP](cortex-security-engineer-0.1.0-runtime.zip) |

## Fontes e evidências

[Código completo e relatórios](cortex-ai-skills-0.1.0-source.zip), [manifesto por arquivo](release-manifest.json) e [checksums dos oito ZIPs](SHA256SUMS).

O ZIP de fontes inclui testes e gabaritos: não deve ser instalado como runtime. Inclui o inventário de conhecimento, as divergências com documentação oficial, os relatórios independentes e as respostas retidas.

## Validação e limites

- 23/23 testes finais direcionados com Astra passaram em sessões individuais e revisão independente.
- Cobertura S cumulativa: 74/253 decisões revisadas, sendo 23 novas e 51 históricas preservadas por análise de impacto; 179 casos permanecem NOT RUN.
- 14 validações de estrutura das Skills, 7 testes do tooling e auditoria final de liberação passaram.
- Os oito arquivos ZIP e seus 443 arquivos internos foram conferidos por hash e descompactação; nenhum teste/gabarito foi incluído nos sete runtimes.
- Compilação, importação e execução em tenant Cortex permanecem NOT RUN. Descoberta automática e equivalência entre hosts/modelos não estão certificadas.
- Fontes oficiais foram verificadas nas datas registradas; conflitos documentais foram preservados, sem inventar contexto de projeto inacessível.

Pronto para uso como pacote de instruções/referências com os limites documentados; não constitui certificação de implantação em produção. Nenhum commit, push ou deployment foi realizado.
