# Uso e instalação — 0.2.1

[Início](../README.md) · [Pacotes](../packages/0.2.1/README.md) · [Validação](validacao.md)

## Escolha o artefato

| Artefato | Destino |
|---|---|
| [cortex-ai-skills-plugin-0.2.1.zip](../packages/0.2.1/cortex-ai-skills-plugin-0.2.1.zip) | Fluxo de importação de plugin compatível com o manifest do pacote |
| ZIP `*-runtime.zip` | Uma Skill individual em host com suporte ao formato |
| ZIP do GitHub | Desenvolvimento, revisão e reconstrução; não usar como plugin |

Verifique o arquivo contra [SHA256SUMS](../packages/0.2.1/SHA256SUMS). O plugin contém `.codex-plugin/plugin.json`, o ícone original, licença e onze diretórios `skills/<nome>/`, cada um com SKILL.md, VERSION, agents, references, templates e examples. Não inclui gabaritos nem configurações de conexão com tenants.

## ChatGPT Work ou host de plugins

Use o fluxo de importação de plugin disponibilizado pela sua conta e selecione o ZIP de plugin completo. Se o host mantiver uma instalação antiga, verifique o procedimento de atualização/substituição disponível e a versão efetiva após a operação. Não conclua que atualizar o GitHub atualizou uma instalação já existente.

Após a importação, confirme a listagem das onze Skills, selecione uma e faça uma solicitação simples com um recurso local. Depois valide os fluxos reais no ambiente autorizado. Esses passos são verificações necessárias, não testes realizados nesta entrega.

## Skill individual

Extraia o runtime selecionado em um local de Skills aceito pelo host. Preserve a pasta com o nome estável e seus recursos locais. Confira as regras atuais de descoberta e o seletor do ambiente; `$skill-name` nos adapters é específico do host OpenAI, não um comando universal.

Nomear uma Skill em uma conversa não prova que ela está instalada ou foi carregada. Confirme os arquivos acessíveis e use exemplos sanitizados para a primeira execução.

## Limites observados

O formato de compatibilidade está documentado na [fonte oficial](https://developers.openai.com/plugins/build/plugins), consultada em 13/11/2026. O [teste de UI de outubro](plugin-ui-test.md) é histórico e se aplica somente ao plugin 0.1.1. Importação, descoberta automática e execução em produto da versão 0.2.1: **NOT RUN**.

A atualização 0.2.1 inclui cortex-playbook-engineer 0.2.0. Recursos interativos dependem das capacidades do host; há fallback completo em Markdown. Nenhuma atualização da instalação existente foi feita nesta entrega.
