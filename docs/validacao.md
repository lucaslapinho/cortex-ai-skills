# Validação, proveniência e limites

[Início](../README.md) · [Instalação](instalacao.md)

## O que foi preservado

A publicação usa o conjunto **0.1.0** preparado e revisado anteriormente. A árvore `source/` e os oito ZIPs mantêm seus bytes originais. README, guias, política de contribuição e verificador de publicação são uma camada nova, fora dessa árvore.

Os relatórios dentro de `source/` e o índice histórico de pacotes descrevem o momento de construção, inclusive a ausência de commit/push naquele momento. Essas declarações são históricas; não significam que este repositório publicado esteja offline. Nenhum marcador histórico de aprovação é uma autorização automática para executar ações.

## Evidência de construção

| Camada | Registro disponível | O que não demonstra |
|---|---|---|
| Estrutura | 14 validações registradas e auditoria de liberação | Descoberta ou execução nativa em cada aplicativo |
| Tooling | 7 testes unitários da construção | Eficácia de detecção em produção |
| Comportamento | 23 casos finais direcionados com Astra aprovados | Execução dos 253 casos do catálogo |
| Cobertura cumulativa | 74 decisões revisadas, incluindo 51 históricas; 179 não executadas | 74 novos testes no mesmo modelo |
| Pacotes | Oito ZIPs, 443 arquivos internos, manifesto e checksums | Assinatura de autoria ou ausência semântica de todo dado sensível |
| Tenant | Compilação/importação/execução não executadas | Validade de schema, desempenho ou aceitação de playbook |

Detalhes: [QA final](../source/reviews/final-qa.md), [revisão Astra](../source/reviews/astra-review.md) e [limitações históricas](../source/reviews/known-limitations.md).

## Diferença de compatibilidade identificada na publicação

**HOST-001 — metadados claude.ai, 2026-09-07.**

O [guia atual de Skills personalizadas do Claude](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) limita `description` a 200 caracteres. As sete descrições preservadas ultrapassam esse limite. Isso restringe a conclusão histórica de compatibilidade estática: o formato geral de diretório não basta para declarar aceitação pelo importador atual.

Conclusão: **adaptação necessária para conformidade documental com esse limite; upload ainda não executado**. Não generalizar esse limite para o Claude Code ou outras superfícies. A versão 0.1.0 não foi modificada para aparentar que o teste ocorreu. O [guia de instalação](instalacao.md) explica uso manual e preparação de uma cópia adaptada, que precisa de nova identidade e validação.

A distinção entre Skills locais e plugins no ChatGPT também foi reconferida. Plugin para ChatGPT web/mobile continua **não incluído**. [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills).

## Particularidade do tooling histórico no Windows

**TOOLS-001 — diretório temporário com nome alternativo, 2026-09-07.**

A primeira execução no GitHub Actions passou no Linux, mas o teste de reescrita de links falhou nos dois runners Windows. O helper 0.1.0 compara o destino resolvido com uma base que deve estar em forma canônica. O fixture histórico não normaliza sua base temporária; um nome alternativo 8.3 do Windows pode causar a comparação incorreta.

O runner de testes desta publicação resolve o diretório temporário antes de executar os sete testes originais. Isso preserva as fontes e seus hashes, não ignora testes e mantém o mesmo tipo de base canônica usado pelo CLI de avaliação. O uso direto do helper com bases não canônicas continua sendo uma limitação da versão histórica, não uma correção de runtime alegada.

## Conhecimento de projeto

Os documentos de pesquisa são sínteses verificáveis e sanitizadas, não cópias completas dos anexos. Foram preservados o [inventário de fontes acessíveis](../source/research/project-knowledge-inventory.md) e as [divergências com documentação Palo Alto](../source/research/project-vs-official-differences.md).

Esta etapa de publicação não repetiu toda a pesquisa factual Palo Alto nem os testes comportamentais. Respeite as datas e o escopo de cada registro. Documentação nova de hosts não é validação nova de comportamento Cortex.

## Reprodução local

Na raiz do repositório, com Python 3.11+:

```text
python -I scripts/validate_publication.py
python -I -m unittest discover -s scripts -p "test_*.py" -v
python -I source/tools/release.py audit --release
python -I scripts/run_source_tests.py
```

O verificador de publicação verifica links locais, padrões de credenciais de alta confiança, limites de arquivos, hashes dos ZIPs, membros contra o manifesto e equivalência com a fonte preservada. É um controle técnico de escopo limitado, não uma garantia absoluta de anonimização ou uma revisão completa de segurança.

Os mesmos comandos são executados pelo workflow de validação. Consulte o resultado real na aba Actions; a existência do workflow não significa que uma execução passou.

## Uso seguro

- Use apenas ambientes e investigações autorizados.
- Comece com análise somente leitura e dados minimizados.
- Não exponha credenciais, evidência real sensível ou informações de clientes em issues.
- Valide schema e comandos no produto, versão, licença e integração aplicáveis.
- Exija autorização específica, plano de recuperação e verificação antes de mudanças.
- Não interprete ausência de evidência como prova de ausência.
