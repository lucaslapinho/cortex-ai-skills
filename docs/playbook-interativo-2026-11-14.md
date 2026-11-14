# Atualização do engenheiro de playbooks — 14/11/2026

Conteúdo cortex-playbook-engineer 0.2.0, distribuído no plugin 0.2.1. O objetivo é construir e corrigir tasks no editor visual com menos informação repetida, mantendo os artefatos técnicos completos.

## Análise do anexo

O documento “Cortex AI Skills — Modelo de resposta interativa e progressiva para Tasks do XSIAM” foi lido como proposta de interação. Foram incorporados cartões por task, inputs separados dos caminhos de contexto, prompt completo, schema separado, checklist e correção pontual.

O YAML original não foi fornecido nesta atualização: IDs, conexões e produtores descritos no relatório continuam como informação relatada. Não se tornaram padrões nativos nem prova de funcionamento. TimeFrame exige produtor conhecido ou ausência explícita. O exemplo novo é Windows-only; Linux permanece fora desse exemplo.

Foram reconsultadas as páginas oficiais [AI Prompt tasks](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/playbooks/build-your-playbook/add-objects-from-the-task-library/add-ai-prompt-tasks.md) e [Test your playbook](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/playbooks/build-your-playbook/test-your-playbook.md) em 14/11/2026. A distinção entre dialetos e limites está no [registro de alegações](../source/cortex-playbook-engineer/references/ai-input-dialects.md). Documentação do host foi inspecionada localmente; isso não garante disponibilidade universal.

## Comportamento entregue

| Situação | Comportamento |
|---|---|
| Construção passo a passo | Uma task atual, campos necessários, conteúdo completo para copiar e próxima observação útil |
| Erro específico | Causa provável, alteração mínima e reteste direcionado |
| Pedido de entrega completa | Todas as tasks e artefatos pedidos, sem interação intermediária obrigatória |
| Host com recursos interativos | Checklist local, detalhes expansíveis e nota selecionável; perguntas nativas para lacunas materiais |
| Host somente Markdown | Card e checklist textual completos; nenhum botão fictício |
| Progresso marcado pelo usuário | Estado informado, separado de aceitação no editor e execução no Debugger |

O painel possui seleção de texto para cópia manual. Não envia mensagens, não altera XSIAM e não cria persistência entre sessões. Não há callback de continuação inventado nem conexão com tenant.

## Mudanças por arquivo

| Arquivo | Mudança |
|---|---|
| [SKILL.md](../source/cortex-playbook-engineer/SKILL.md) | Gatilhos de modo guiado, leitura progressiva, intake proporcional e apresentação compacta |
| [interactive-task-guidance.md](../source/cortex-playbook-engineer/references/interactive-task-guidance.md) | Modos, capacidades do host, progresso, validação e tratamento de erro |
| [ai-input-dialects.md](../source/cortex-playbook-engineer/references/ai-input-dialects.md) | Evidência datada, alias/placeholder/path e limites de generalização |
| [task-card.md](../source/cortex-playbook-engineer/templates/task-card.md) | Modelo compacto e campos por tipo de task |
| [interactive-task-panel.md](../source/cortex-playbook-engineer/templates/interactive-task-panel.md) | Fragmento opcional de controles locais e fallback |
| [ai-triage-contract.md](../source/cortex-playbook-engineer/templates/ai-triage-contract.md) | Seleção explícita do dialeto, mantendo contrato completo |
| [windows-ai-task.md](../source/cortex-playbook-engineer/examples/windows-ai-task.md) | Exemplo completo Windows com lacunas de mapeamento explícitas |
| [Casos de regressão](../source/cortex-playbook-engineer/tests/interactive-2026-11-14.md) | Oito cenários de comportamento, fora do runtime |
| [Verificações de templates](../scripts/test_task_templates.py) | Schema, aliases e callbacks com elementos simulados |

VERSION, adapter, README, changelogs, relatórios e índices foram alinhados. O validador preserva a identidade da distribuição 0.2.0. Os outros dez runtimes não mudaram.

## Uso

```text
Use cortex-playbook-engineer para construir este playbook uma task por vez.
Use os recursos interativos disponíveis para checklist e detalhes.
Mostre os campos, prompt completo, inputs e JSON Schema da task atual.
Preserve o dialeto de inputs observado no meu editor.
```

Para uma correção: “Corrija apenas este erro, mantendo o restante da task”. Para entrega em lote: “Entregue todas as tasks agora”.

## Validação e próxima etapa

Ver [resultados e limites](validacao.md). Lógica local e respostas offline verificadas; renderização real no host, instalação, aceitação do editor e execução no XSIAM permanecem NOT RUN. Próxima validação operacional: carregar a nova versão no host compatível e conferir uma task com dados sanitizados no ambiente autorizado.
