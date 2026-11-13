# Validação — versão 0.2.0

[Início](../README.md) · [Pacotes](../packages/0.2.0/README.md) · [Avaliação comportamental](behavior-evaluation-2026-11-13.md) · [Fontes](knowledge-review-2026-11-13.md)

Revisão de 13/11/2026. As dimensões abaixo são independentes; nenhuma comprova automaticamente a seguinte.

| Dimensão | Resultado | Evidência e limite |
|---|---|---|
| Estrutura e empacotamento | PASS | 40 testes automatizados (32 de publicação/plugin e 8 de source), auditoria dos 303 casos escritos, links, hashes, isolamento e build determinístico. |
| Documentação oficial | PASS | 42 páginas, revisão de alegações delimitadas; não é atualização exaustiva de todo o histórico nem evidência do tenant. |
| Comportamento offline | PASS | 15 cenários selecionados nos runtimes finais; respostas isoladas e julgamento pelo autor, sem aprovação de revisor independente. |
| Corpus completo | NOT RUN | 303 casos escritos; 288 não executados nesta revisão. |
| Descoberta natural e importação no ChatGPT/Codex | NOT RUN | O harness carregou cada Skill explicitamente. Nenhuma instalação foi feita. |
| Aceitação no produto, compilação e execução | NOT RUN | Sem tenant XSIAM, Cloud, Firewall, SASE ou AIRS. |
| Revisão independente da release | NOT RUN | Avaliações e verificações do autor não são aprovação externa. |

Resultados locais completos: [comandos, saídas e ambiente](static-checks-2026-11-13.json). Foram verificados 28 ZIPs entre as três versões. O ambiente local foi Linux; os jobs remotos da matriz Linux/Windows precisam ser consultados no GitHub para o commit publicado.

## Métodos e correção encontrada

A auditoria verifica YAML/JSON, nomes, recursos locais, referências, isolamento dos runtimes e separação dos gabaritos. Os testes de código exercitam rejeição de pacotes malformados, caminhos indevidos, recursos ausentes, modificações de artefatos históricos e divergência da fonte. O builder compara reconstruções determinísticas e identidade dos arquivos distribuídos.

A avaliação comportamental usou 16 agentes novos para 15 cenários. A primeira execução do cenário de AI Task omitiu o JSON Schema completo. Foi corrigida uma instrução ampla demais sobre exports YAML/JSON e o cenário foi repetido em contexto novo. A resposta final incluiu o schema; ambas as respostas e seus hashes foram preservados. A primeira falha não foi reclassificada como sucesso.

Os casos cobrem os onze agentes e incluem confusão entre produtos, escopo incompleto, timeout, fronteira negativa e prompt injection. É uma amostra limitada, não prova de acerto geral. Os [registros integrais](evaluation-2026-11-13/README.md) ficam fora dos pacotes de uso.

## Distribuição e histórico

O pacote atual contém um plugin e onze runtimes individuais, totalizando doze ZIPs. O plugin possui 204 arquivos e mantém os nomes existentes, o ícone e o formato de compatibilidade. As versões 0.1.0 e 0.1.1 permanecem intactas e são verificadas contra seus próprios inventários; somente a versão atual é comparada com a fonte atual.

O registro de [importação de outubro](plugin-ui-test.md) refere-se apenas à versão 0.1.1. O campo `discovery_and_behavior` do manifest atual refere-se à validação no host real, que permanece NOT RUN, separada das respostas offline.

## Próximas validações no ambiente

Importar o plugin no host compatível, confirmar as onze Skills e o carregamento de recursos locais, exercitar os fluxos prioritários com dados sanitizados e validar artefatos/ações em ambiente Palo Alto autorizado. Critérios de aceite precisam incluir falhas, permissões, readback e recuperação conforme o produto. Nenhum teste escrito ou sucesso de importação substitui essa execução.
