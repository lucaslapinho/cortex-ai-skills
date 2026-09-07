# Exemplos de uso

[Início](../README.md) · [Instalação](instalacao.md) · [Limites](validacao.md)

Os prompts abaixo são exemplos de pedidos, não consultas executadas, regras habilitadas ou playbooks importáveis. Antes de usá-los, disponibilize a Skill pelo mecanismo do seu aplicativo. Não pressuponha que apenas mencionar o nome carregará um pacote ausente.

## Contexto que melhora qualquer resposta

Preencha somente o que realmente souber:

```text
Produto: [XSIAM, XDR ou XSOAR; não os trate como equivalentes].
Versão, licença e superfície: [informações disponíveis].
Objetivo: [resultado que preciso obter].
Dados: [schema, consulta, erro, eventos anonimizados ou configuração].
Janela de análise e fuso: [informe].
Restrições: [retenção, privacidade, integrações disponíveis].
Autorização: somente análise; nenhuma ação no tenant.
Entrega: [consulta proposta, diagnóstico, desenho ou checklist].
```

Não inclua credenciais, chaves, tokens, nomes reais de clientes ou dados pessoais desnecessários. Campos entre colchetes são entradas a preencher, não fatos presumidos.

## 1. Revisar uma consulta XQL

Skill: [cortex-xql-query-engineer](../source/cortex-xql-query-engineer/README.md).

```text
Use cortex-xql-query-engineer.

Produto: Cortex XSIAM.
Objetivo: revisar minha consulta de investigação de PowerShell.
Consulta atual: [cole].
Schema e tipos dos campos: [anexe o que estiver disponível].
Erro observado: [cole a mensagem exata ou informe que não há erro].
Janela: [informe datas e fuso].

Preserve a intenção original. Explique as correções e os possíveis
efeitos sobre o resultado. Não invente datasets, campos ou funções.
Se faltar schema, entregue primeiro as verificações necessárias.
Consulte a documentação oficial aplicável e proponha testes.
Não declare compilação, execução ou ganho de desempenho sem evidência.
```

**Entrega esperada:** revisão, proposta condicionada ao schema, explicação e roteiro de verificação. Não é um resultado real do tenant.

## 2. Propor uma detecção

Skill: [cortex-detection-engineer](../source/cortex-detection-engineer/README.md).

```text
Use cortex-detection-engineer.

Quero avaliar uma detecção para repetidas falhas de autenticação
seguidas de sucesso, dentro da mesma identidade.
Produto: [informe].
Telemetria e schema disponíveis: [anexe].
Comportamentos legítimos conhecidos: [descreva].

Defina hipótese, pré-requisitos, lógica de correlação, janela,
agrupamento, entidades e possíveis falsos positivos.
Não escolha um limiar como se estivesse validado sem uma baseline.
Inclua casos positivos, negativos e ambíguos, além de um plano
de tuning e critérios de promoção.
Não crie nem habilite regras no tenant.
```

**Entrega esperada:** especificação de detecção, lacunas e testes; eficácia e limiares continuam dependentes da validação.

## 3. Desenhar um playbook de phishing

Skill: [cortex-playbook-engineer](../source/cortex-playbook-engineer/README.md).

```text
Use cortex-playbook-engineer.

Desenhe, sem executar, um playbook para investigação de phishing.
Produto e versão: [informe].
Integrações e comandos confirmados: [anexe o inventário].
Entradas do incidente: [liste].

Defina fluxo principal, subplaybooks, contratos de entrada/saída,
decisões determinísticas e tratamento de evidência inconclusiva.
Inclua timeouts, repetição segura, falhas parciais e recuperação.
Exija aprovação humana antes de contenção ou remoção de mensagens.
Se um comando não estiver comprovado, marque-o como pendente.
Não apresente o desenho como YAML importável sem validar o formato.
```

**Entrega esperada:** desenho operacional, contratos e plano de testes; nenhuma contenção ou importação é autorizada.

## 4. Conduzir threat hunting

Skill: [cortex-threat-hunter](../source/cortex-threat-hunter/README.md).

```text
Use cortex-threat-hunter.

Hipótese: uma identidade comprometida pode ter sido usada
para acessar vários endpoints por administração remota.
Produto, período e fuso: [informe].
Telemetria disponível e lacunas: [anexe].

Crie um plano de hunting com perguntas, pivôs, correlação temporal,
entidades e fontes necessárias.
Considere explicações administrativas legítimas.
Diferencie ausência de eventos de ausência de cobertura.
Não conclua comprometimento apenas por um indicador.
Entregue critérios para confirmar, refutar ou manter a hipótese
em aberto e uma proposta de passagem para engenharia de detecção.
```

**Entrega esperada:** plano investigativo com hipóteses concorrentes e limites de cobertura.

## 5. Revisar Threat Intelligence Management

Skill: [cortex-tim-engineer](../source/cortex-tim-engineer/README.md).

```text
Use cortex-tim-engineer.

Quero revisar o ciclo de vida de indicadores recebidos de feeds.
Produto, versão, integrações e formatos: [informe].
Regras atuais de confiança e expiração: [descreva].
Consumidores de exportação: [liste sem credenciais].

Analise ingestão, normalização, deduplicação, enriquecimento,
conflitos de classificação, expiração, revogação e distribuição.
Separe a gestão de inteligência das ações de bloqueio executadas
pelos consumidores.
Documente falhas de feed e reversão de uma distribuição incorreta.
Não publique indicadores nem altere políticas.
```

**Entrega esperada:** diagnóstico de governança e desenho do ciclo de vida; exportação não implica bloqueio.

## 6. Diagnosticar ingestão e mapeamento

Skill: [cortex-platform-engineer](../source/cortex-platform-engineer/README.md).

```text
Use cortex-platform-engineer.

Sintoma: vejo eventos no dataset bruto, mas não os encontro
na consulta que usa o mapeamento esperado.
Produto e versão: [informe].
Fonte, configuração anonimizada, schema, consulta e exemplos: [anexe].

Monte uma sequência de verificações somente leitura.
Considere ingestão, parsing, mapeamento, tipos, tempo, consulta
e permissões como hipóteses distintas.
Peça evidência antes de atribuir uma causa.
Não altere RBAC, coletores ou regras de parsing.
Entregue diagnóstico diferencial e informações para um escalonamento.
```

**Entrega esperada:** verificações ordenadas e hipóteses sustentadas; não uma causa inventada.

## 7. Coordenar um caso entre especialidades

Skill: [cortex-security-engineer](../source/cortex-security-engineer/README.md).

```text
Use cortex-security-engineer.

Tenho um alerta de identidade, uma consulta com erro e um
playbook que parou durante enriquecimento.
Produto e versão: [informe].
Evidências e erros anonimizados: [anexe].

Separe as frentes de investigação, consulta, detecção e automação.
Defina prioridades, dependências, entradas e saídas de cada frente.
Indique a Skill recomendada para cada parte.
Não presuma que outras Skills ou subagentes estejam disponíveis;
se não estiverem, entregue um plano independente e os contratos
para continuação manual.
Não execute nenhuma ação no ambiente.
```

**Entrega esperada:** triagem integrada e plano de passagem entre especialidades, sem delegação automática presumida.

## Como conferir a resposta

Uma resposta útil deve:

- usar somente dados e referências realmente acessíveis;
- indicar produto, superfície, versão e premissas relevantes;
- apontar fontes oficiais específicas para afirmações técnicas;
- distinguir fatos, inferências e conceitos;
- informar exatamente quais verificações não foram executadas;
- pedir autorização específica antes de propor a execução de uma mudança.

Se faltar uma entrada essencial, esclarecer a lacuna é melhor do que entregar uma solução aparentemente pronta. Para avaliar a Skill, use seus próprios casos anonimizados; não forneça os gabaritos do repositório ao assistente.
