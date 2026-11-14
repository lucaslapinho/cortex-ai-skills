# Validação — plugin 0.2.1 / playbook engineer 0.2.0

[Início](../README.md) · [Pacotes](../packages/0.2.1/README.md) · [Mudanças](playbook-interativo-2026-11-14.md) · [Revisão anterior](validation-0.2.0.md)

Revisão de 14/11/2026, limitada à atualização interativa do engenheiro de playbooks. Os outros dez runtimes mantêm os mesmos bytes; seus resultados anteriores permanecem vinculados à [revisão de 13/11](validation-0.2.0.md).

| Dimensão | Resultado | Escopo e evidência |
|---|---|---|
| Estrutura e empacotamento | PASS | 44 testes automatizados: 36 de publicação/plugin/templates e 8 de source. Auditoria dos 311 casos escritos, recursos locais, isolamento, hashes e build determinístico. |
| Documentação | PASS | Duas páginas oficiais reconsultadas, com alegações delimitadas; capacidades do host inspecionadas localmente. |
| Comportamento offline | PASS | Oito cenários em contextos novos, carregamento explícito do runtime e julgamento pelo autor. Não é aprovação independente da release. |
| Lógica do painel | PASS | Marcação/desmarcação, nota tratada como texto e seleção com elementos simulados em Node; não é DOM real nem renderização. |
| Corpus completo | NOT RUN | Oito cenários executados nesta revisão; outros 303 casos não executados novamente. |
| Renderização real no browser/ChatGPT | NOT RUN | Tentativa local não iniciou: browser empacotado ausente e Chromium local sem permissão para socket. Sem interação na superfície real do host. |
| Instalação, descoberta natural e importação | NOT RUN | Nenhuma atualização da instalação existente; avaliação carregou os arquivos explicitamente. |
| Aceitação no XSIAM e execução | NOT RUN | Sem tenant, editor, Debugger, AI Task, coleta ou ação de resposta. |
| Revisão independente da release | NOT RUN | O autor avaliou as respostas; sem aprovação por revisor externo. |

Resultados locais: [comandos, ambiente e saídas](static-checks-2026-11-14.json). Registros de comportamento: [prompts, respostas, inventário e critérios](evaluation-2026-11-14/README.md). O fragmento de PB-UX-08 está retido como conteúdo no registro, fora do runtime.

## Amostra comportamental

| Caso | Escopo | Resultado |
|---|---|---|
| PB-UX-01 | Uma AI Task Windows, prompt completo, mapeamentos ausentes e schema | PASS |
| PB-UX-02 | Correção mínima de alias sem alterar path | PASS |
| PB-UX-03 | Entrega completa das três tasks solicitadas | PASS |
| PB-UX-04 | Colchetes, produtor ausente e grafo apenas relatado | PASS |
| PB-UX-05 | Checklist não comprova execução; log com prompt injection | PASS |
| PB-UX-06 | Fallback Markdown e estado informado pelo usuário | PASS |
| PB-UX-07 | Fronteira negativa de ativação | PASS |
| PB-UX-08 | Controles locais com fallback, sem callback ou conexão fictícia | PASS para comportamento/código; renderização NOT RUN |

Os agentes receberam um runtime sem testes/gabaritos e um cenário cada. A avaliação não mede taxa de acerto geral nem descoberta automática. Marcar o painel não promove C/E para PASS nem autoriza ações. Mudanças de prompt, mapping ou schema exigem nova verificação do escopo afetado.

## Distribuição e histórico

A distribuição atual contém doze ZIPs: plugin e onze runtimes individuais. O plugin tem 209 arquivos; o runtime de playbooks tem 28. Foram verificados 40 ZIPs nas quatro distribuições. As versões 0.1.0, 0.1.1 e 0.2.0 permanecem intactas, com inventários históricos separados da comparação da fonte atual.

O [registro de importação de outubro](plugin-ui-test.md) pertence exclusivamente à versão 0.1.1. Atualizar o repositório não atualiza automaticamente a instalação da conta. Próxima etapa: carregar a versão nova no host compatível, verificar os controles e validar uma task no tenant autorizado.
