# Cortex AI Skills — Palo Alto Networks

**Versão 0.2.0: onze Skills especializadas para Cortex, Cloud, Firewall, SASE e segurança de aplicações de IA.** O identificador do projeto e os sete agentes originais foram preservados. O `cortex-security-engineer` coordena solicitações que atravessam produtos.

[Baixar plugin 0.2.0](packages/0.2.0/cortex-ai-skills-plugin-0.2.0.zip) · [Pacotes individuais](packages/0.2.0/README.md) · [Uso e instalação](docs/instalacao.md) · [Validação](docs/validacao.md) · [Changelog](CHANGELOG.md)

Projeto independente, sem afiliação à Palo Alto Networks ou OpenAI. “Agente” designa uma Skill com instruções e recursos; o pacote não cria conexões com tenants nem executa ações de segurança automaticamente.

## Escolha o especialista

| Skill | Versão | Responsabilidade |
|---|---|---|
| [cortex-security-engineer](source/cortex-security-engineer/SKILL.md) | 0.2.0 | Coordenar arquitetura, decisões e dependências entre as soluções Palo Alto |
| [cortex-cloud-engineer](source/cortex-cloud-engineer/SKILL.md) | 0.1.0 | Cortex Cloud: posture, runtime, AppSec, AWS, Azure, GCP, OCI e Kubernetes |
| [palo-alto-firewall-engineer](source/palo-alto-firewall-engineer/SKILL.md) | 0.1.0 | NGFW, PAN-OS, PA/VM/CN-Series, Cloud NGFW, Panorama e SCM |
| [prisma-sase-engineer](source/prisma-sase-engineer/SKILL.md) | 0.1.0 | Prisma Access, Prisma SD-WAN, Prisma Browser e AI Access Security |
| [prisma-airs-engineer](source/prisma-airs-engineer/SKILL.md) | 0.1.0 | Runtime, Supply Chain, Red Teaming e AI Gateway |
| [cortex-xql-query-engineer](source/cortex-xql-query-engineer/SKILL.md) | 0.1.2 | XQL, schema, compatibilidade da superfície e desempenho |
| [cortex-detection-engineer](source/cortex-detection-engineer/SKILL.md) | 0.1.2 | BIOC, correlação, tuning e ciclo de vida de detecções |
| [cortex-playbook-engineer](source/cortex-playbook-engineer/SKILL.md) | 0.1.2 | Playbooks, AI Tasks, contexto, notificações e tratamento de falhas |
| [cortex-threat-hunter](source/cortex-threat-hunter/SKILL.md) | 0.1.2 | Hipóteses, investigação, Graph Search e cobertura de evidências |
| [cortex-tim-engineer](source/cortex-tim-engineer/SKILL.md) | 0.1.2 | Inteligência, indicadores, scoring, EDL e ciclo de vida |
| [cortex-platform-engineer](source/cortex-platform-engineer/SKILL.md) | 0.1.2 | XSIAM/XDR/XSOAR: coleta, ingestão, acesso, integrações e APIs |

Cada Skill funciona sem depender das outras. Referências locais fornecem uma base datada; contratos sujeitos a mudança devem ser conferidos no produto, versão, licença e ambiente específicos. A [matriz de cobertura](source/cortex-security-engineer/references/portfolio-routing.md) explicita também os limites: não é certificação de domínio de todas as funcionalidades ou SKUs do fabricante.

## Como solicitar

```text
Use cortex-security-engineer para revisar esta arquitetura Palo Alto.
Objetivo: integrar os riscos de Cortex Cloud ao SOC no XSIAM e avaliar a política de rede.
Produtos, versões e gestão: [informar Cortex, Panorama/SCM e cloud].
Evidências sanitizadas: [configuração, eventos e schemas disponíveis].
Escopo autorizado: análise e preparação de alterações, sem executar em produção.
Entregue a decisão, os responsáveis, os passos concretos, a validação e as lacunas.
Responda em português brasileiro.
```

Para uma tarefa específica, nomeie diretamente o especialista. Veja [exemplos](docs/exemplos.md). O agente de playbooks inclui um [contrato completo de AI triage](source/cortex-playbook-engineer/templates/ai-triage-contract.md), com prompt, inputs e schema proposto, sem inventar caminhos nativos do tenant.

## Fonte, distribuição e evidências

| Material | Finalidade |
|---|---|
| `source/` | Fonte canônica, documentação de desenvolvimento e casos de avaliação |
| `plugin/` | Manifest de compatibilidade e ícone de apresentação |
| `packages/0.2.0/` | Plugin e onze runtimes gerados da mesma fonte, com SHA-256 |
| `docs/` | Instruções, revisão das fontes e resultados das verificações |
| ZIP do repositório | Código-fonte de desenvolvimento; não é o ZIP de importação do plugin |

As distribuições 0.1.0 e 0.1.1 permanecem intactas. A importação observada em 23/10/2026 pertence exclusivamente à versão 0.1.1. **A versão 0.2.0 não foi importada nesta atualização, nem executada em um tenant Palo Alto.** Os resultados estáticos e comportamentais têm escopo separado no [relatório de validação](docs/validacao.md).

## Desenvolvimento e verificação

```bash
python -m pip install -r requirements-dev.txt
python -I source/tools/release.py audit
python -I scripts/run_source_tests.py
python -I -m unittest discover -s scripts -p 'test_*.py' -v
python -I scripts/build_plugin.py build --output dist/local-build
python -I scripts/build_plugin.py validate --zip dist/local-build/cortex-ai-skills-plugin-0.2.0.zip
python -I scripts/validate_publication.py
```

O diretório de build precisa ser novo. Testes, gabaritos, avaliações e relatórios não entram no runtime. Publicação não implica instalação, aceitação no importador, execução real ou eficácia operacional. Veja [contribuição](CONTRIBUTING.md), [arquitetura](source/ARCHITECTURE.md) e [revisão das fontes](docs/knowledge-review-2026-11-13.md).
