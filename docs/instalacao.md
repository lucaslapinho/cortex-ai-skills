# Uso e instalação — 0.2.1

[Início](../README.md) · [Pacotes](../packages/0.2.1/README.md) · [Validação](validacao.md)

## Escolha o artefato

| Artefato | Destino |
|---|---|
| [cortex-ai-skills-0.2.1-extract-first.zip](../packages/downloads/cortex-ai-skills-0.2.1-extract-first.zip) | Download dos onze ZIPs individuais. Extraia este primeiro. |
| [cortex-playbook-engineer-0.2.0-runtime.zip](../packages/0.2.1/cortex-playbook-engineer-0.2.0-runtime.zip) | Upload individual do Playbook Engineer na aba Skills |
| [cortex-ai-skills-plugin-0.2.1.zip](../packages/0.2.1/cortex-ai-skills-plugin-0.2.1.zip) | Importação de plugin para carregar as onze Skills |
| ZIP gerado por **Code → Download ZIP** no GitHub | Desenvolvimento, revisão e reconstrução |

## Upload de Skills no ChatGPT

Para carregar as onze Skills pela tela **Upload a skill**, extraia `cortex-ai-skills-0.2.1-extract-first.zip` uma vez. Selecione os arquivos `*-runtime.zip` que saíram da extração, sem descompactá-los. Se o seletor permitir selecionar vários arquivos, envie-os juntos. Caso contrário, envie um por vez. As [Skills também estão disponíveis para download individual](../packages/0.2.1/README.md).

Baixe o ZIP `cortex-playbook-engineer-0.2.0-runtime.zip` diretamente pelo link acima. Envie o ZIP intacto em **Plugins → Skills → Create → Upload from your computer**, se essa opção estiver disponível no seu workspace. O arquivo tem uma única pasta `cortex-playbook-engineer/`, com `SKILL.md` e os recursos associados. Consulte o [fluxo de upload da OpenAI](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

Se aparecer “Couldn't upload this skill”, confira o nome do arquivo selecionado e a aba em que o envio foi feito. Caso o erro persista com o ZIP individual, compare o SHA-256 com o índice abaixo e registre o texto completo exibido pelo importador. A mensagem genérica, por si só, não identifica a causa.

Verifique o arquivo contra [SHA256SUMS](../packages/0.2.1/SHA256SUMS). O plugin contém `.codex-plugin/plugin.json`, o ícone original, licença e onze diretórios `skills/<nome>/`, cada um com SKILL.md, VERSION, agents, references, templates e examples. Não inclui gabaritos nem configurações de conexão com tenants.

## ChatGPT Work ou host de plugins

Use o fluxo de importação de plugin disponibilizado pela sua conta e selecione o ZIP de plugin completo. Se o host mantiver uma instalação antiga, verifique o procedimento de atualização/substituição disponível e a versão efetiva após a operação. Não conclua que atualizar o GitHub atualizou uma instalação já existente.

Após a importação, confirme a listagem das onze Skills, selecione uma e faça uma solicitação simples com um recurso local. Depois valide os fluxos reais no ambiente autorizado. Esses passos são verificações necessárias, não testes realizados nesta entrega.

## Skill individual no Codex ou em outro host com carregamento por pasta

Extraia o runtime selecionado em um local de Skills aceito pelo host. Preserve a pasta com o nome estável e seus recursos locais. Confira as regras atuais de descoberta e o seletor do ambiente; `$skill-name` nos adapters é específico do host OpenAI, não um comando universal.

Nomear uma Skill em uma conversa não prova que ela está instalada ou foi carregada. Confirme os arquivos acessíveis e use exemplos sanitizados para a primeira execução.

## Limites observados

O formato de compatibilidade está documentado na [fonte oficial](https://developers.openai.com/plugins/build/plugins), consultada em 13/11/2026. O [teste de UI de outubro](plugin-ui-test.md) é histórico e se aplica somente ao plugin 0.1.1. Importação, descoberta automática e execução em produto da versão 0.2.1: **NOT RUN**.

A atualização 0.2.1 inclui cortex-playbook-engineer 0.2.0. Recursos interativos dependem das capacidades do host; há fallback completo em Markdown. Nenhuma atualização da instalação existente foi feita nesta entrega.
