# Cortex AI Skills

Sete Skills modulares para apoiar investigação, engenharia e operação defensiva no ecossistema **Palo Alto Networks Cortex** — com instruções reutilizáveis, referências, modelos e exemplos.

[Começar](docs/instalacao.md) · [Exemplos de uso](docs/exemplos.md) · [Pacotes 0.1.0](packages/0.1.0/README.md) · [Validação e limites](docs/validacao.md) · [Documentação técnica em inglês](source/README.md)

> Projeto independente, não oficial e não afiliado à Palo Alto Networks, OpenAI ou Anthropic. As Skills orientam a IA; não conectam automaticamente ao seu tenant, não executam ações por conta própria e não substituem validação humana.

## O que é uma Skill?

Uma Skill é um conjunto de instruções que ensina um assistente a conduzir uma tarefa específica. O arquivo `SKILL.md` define o fluxo; as pastas de apoio trazem referências, templates e exemplos. Você informa o problema, o produto, a versão e os dados disponíveis; o assistente aplica o método e explicita o que sabe, o que inferiu e o que ainda precisa verificar.

**Não é um modelo treinado, um content pack Cortex, uma integração pronta nem um playbook automaticamente importável.**

## Escolha a especialidade

| Skill | Quando usar | Entrega típica |
|---|---|---|
| [XQL Query Engineer](source/cortex-xql-query-engineer/README.md) | Escrever, revisar ou diagnosticar consultas XQL | Consulta proposta, premissas, explicação e plano de validação |
| [Detection Engineer](source/cortex-detection-engineer/README.md) | Transformar comportamento suspeito em proposta de detecção | Lógica, telemetria necessária, falsos positivos e testes |
| [Playbook Engineer](source/cortex-playbook-engineer/README.md) | Projetar automações e subplaybooks | Fluxo, contratos de entrada/saída, aprovações e recuperação |
| [Threat Hunter](source/cortex-threat-hunter/README.md) | Investigar uma hipótese de ameaça | Plano de hunting, pivôs, lacunas e explicações alternativas |
| [TIM Engineer](source/cortex-tim-engineer/README.md) | Organizar o ciclo de vida da inteligência de ameaças | Ingestão, enriquecimento, expiração e distribuição governada |
| [Platform Engineer](source/cortex-platform-engineer/README.md) | Diagnosticar coleta, ingestão, mapeamento ou integrações | Árvore de diagnóstico e verificações de configuração |
| [Security Engineer](source/cortex-security-engineer/README.md) | Enquadrar casos que atravessam várias especialidades | Escopo, prioridades, responsáveis e contratos de passagem |

Cada Skill funciona de forma independente. A de segurança pode recomendar outra especialidade, mas não presume que ela esteja instalada.

## Primeiro uso em poucos passos

1. Escolha uma Skill e baixe seu **ZIP runtime** em [Pacotes 0.1.0](packages/0.1.0/README.md).
2. Siga o [guia do seu aplicativo](docs/instalacao.md). Não instale o ZIP de fontes: ele contém testes e gabaritos.
3. Use dados anonimizados e um problema bem delimitado.
4. Peça evidências e valide a saída antes de aplicar qualquer mudança.

Exemplo, depois de disponibilizar a Skill:

```text
Use cortex-xql-query-engineer para revisar minha consulta.

Produto: Cortex XSIAM.
Versão e recursos habilitados: [informe o que souber].
Objetivo: investigar execuções suspeitas de PowerShell.
Consulta, schema e amostra anonimizada: [anexe].

Leia os arquivos acessíveis necessários e informe o que está ausente.
Não invente datasets, campos ou resultados.
Explique as correções e preserve a intenção da consulta.
Confira a documentação oficial aplicável.
Separe revisão documental de compilação e execução no tenant.
Não execute nem altere nada no ambiente.
```

Há [sete exemplos completos e um modelo de contexto](docs/exemplos.md), prontos para adaptar.

## Onde posso usar?

| Aplicativo | Caminho de uso | Limite desta entrega |
|---|---|---|
| ChatGPT, uso manual | Anexar as instruções e referências necessárias à conversa | Não equivale a instalação persistente |
| ChatGPT desktop / Codex | Carregar runtime pelo mecanismo local suportado | Descoberta nativa não certificada |
| ChatGPT web/mobile, uso nativo | Distribuição via plugin | Plugin não incluído |
| Claude, uso manual | Disponibilizar instruções e referências e solicitar sua aplicação | Confirmar quais arquivos foram efetivamente lidos |
| claude.ai, Skill nativa | Importação de ZIP personalizado | As descrições 0.1.0 excedem o limite atual documentado de 200 caracteres; requer adaptação e teste |
| Claude Code | Runtime em `.claude/skills/<nome>/` | Descoberta e execução nativas não testadas |

Orientações de host conferidas em **7 de setembro de 2026**. Mecanismos e políticas podem mudar; consulte as [fontes e instruções de instalação](docs/instalacao.md).

## Qualidade e limites

- Sete Skills na versão **0.1.0**.
- **23/23** casos finais direcionados avaliados com Astra passaram; isso não equivale a executar todo o catálogo.
- Cobertura comportamental cumulativa registrada: **74/253** decisões; **179** casos permanecem não executados.
- **7** testes do tooling passaram; os pacotes têm manifesto e checksums.
- Compilação, importação e execução em tenant Cortex: **não testadas**.

Os [relatórios históricos](source/reviews/final-qa.md) preservam a evidência da construção. A publicação no GitHub não amplia a validação nem comprova eficácia em produção. O [guia atual de limites](docs/validacao.md) registra também as diferenças encontradas durante a publicação.

## Como o conhecimento é tratado

O projeto prioriza documentação oficial atual para comportamento do produto. Conhecimento de projeto verificável informa convenções e contexto; divergências são registradas, nunca resolvidas silenciosamente. Consulte o [inventário](source/research/project-knowledge-inventory.md) e o [registro de diferenças](source/research/project-vs-official-differences.md).

Não são publicados anexos originais, exportações brutas, credenciais ou registros reais de endpoints. Nunca envie segredos ou dados sensíveis em issues, exemplos ou prompts públicos.

## Organização do repositório

```text
README.md                 Página inicial
docs/                     Instalação, exemplos e limites atuais
source/                   Fonte 0.1.0 preservada, sete Skills e evidências
packages/0.1.0/            Sete runtimes, ZIP de fontes, manifesto e checksums
scripts/                  Verificação da publicação
.github/workflows/        Validação automatizada
```

O diretório `source/` preserva a estrutura auditada. Ele não é uma pasta de instalação automática.

## Desenvolvimento

Requer Python 3.11+ para os comandos de publicação, sem bibliotecas externas:

```text
python -I scripts/validate_publication.py
python -I -m unittest discover -s scripts -p "test_*.py" -v
python -I source/tools/release.py audit --release
python -I -m unittest discover -s source/tools -p test_release.py -v
```

Esses comandos verificam arquivos e estrutura; não chamam modelos, não usam quota e não acessam tenant. Veja [como contribuir](CONTRIBUTING.md).

## Licença

[MIT](LICENSE). Nomes de produtos e marcas pertencem aos respectivos titulares.
