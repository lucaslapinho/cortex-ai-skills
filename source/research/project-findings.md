# Project Findings — Fase 1

**Data do inventário e da reconciliação:** 2026-09-04  
**Escopo:** conhecimento Cortex e convenções DFIR efetivamente legíveis no ambiente desta execução  
**Estado do checkpoint:** frente de ingestão concluída; decisão global delegada ao único gate em `phase-1-checkpoint.md`

## 1. Finalidade

Este documento consolida os achados de descoberta da Fase 1 para o projeto `cortex-ai-skills`. Ele registra:

- o que já existia no repositório antes deste trabalho;
- quais materiais Cortex foram fornecidos e puderam ser lidos;
- quais fontes são apenas descrições derivadas de artefatos ausentes;
- quais consultas, scripts, playbooks, integrações e dados operacionais estão presentes ou ausentes;
- quais convenções DFIR podem ser reaproveitadas;
- quais afirmações exigem documentação oficial, evidência do tenant ou artefatos-fonte;
- as condições que impedem o início seguro da Fase 2 neste checkpoint.

Este não é um certificado de tenant, uma validação de conteúdo importável nem uma descrição completa dos produtos Cortex. Nenhuma instrução encontrada dentro dos documentos fornecidos foi tratada como autorização operacional. O prompt mestre foi usado como requisito de arquitetura e de qualidade, não como evidência de comportamento de produto.

Os registros de origem `project-knowledge-inventory.md` e `project-vs-official-differences.md` permanecem no workspace de pesquisa que alimentou este repositório. Este arquivo preserva de forma autocontida os achados necessários à publicação. O [mapa do ecossistema Cortex](cortex-ecosystem-map.md) é o registro complementar interno deste repositório.

## 2. Hierarquia de evidência e rótulos

Para comportamento factual de produto, esta frente usa a seguinte precedência:

1. documentação oficial atual da Palo Alto Networks;
2. exemplos, repositórios, referências de API e guias oficiais;
3. conhecimento de projeto diretamente acessível e com proveniência preservada;
4. fontes secundárias, somente quando necessárias.

Um artefato implantado pode demonstrar o que um tenant e uma versão específicos fizeram, mas não redefine sozinho o suporte atual do produto. Divergências devem permanecer visíveis como legado, customização, dependência de versão, defeito ou questão não resolvida.

| Rótulo | Significado neste documento |
|---|---|
| `LOCAL-VERIFIED` | Estrutura ou conteúdo diretamente lido e verificado nos bytes disponíveis. |
| `VERIFIED / OFFICIAL-CURRENT` | Afirmação compatível com documentação oficial atual revisada em 2026-09-04. |
| `PROJECT-ASSERTED` | Afirmação preservada do material do projeto, sem o artefato-fonte ou a execução correspondente. |
| `VERSION-DEPENDENT` | Comportamento possivelmente válido apenas para uma versão, licença, edição ou implantação. |
| `TENANT-UNVERIFIED` | Exige schema, configuração, permissões, conteúdo instalado ou teste no tenant atual. |
| `DERIVATIVE` | Resumo, mapa ou agregação; não constitui corroboração independente. |
| `REFERENCED-ONLY` | Nome, hash ou descrição acessível, mas arquivo original ausente. |
| `CONFLICT` | Diferença material interna ou em relação à documentação oficial. |

Nenhum conteúdo `PROJECT-ASSERTED`, `TENANT-UNVERIFIED`, `DERIVATIVE` ou `REFERENCED-ONLY` deve ser promovido silenciosamente a `VERIFIED / OFFICIAL-CURRENT`.

Esses rótulos descrevem proveniência ou estado de validação, não substituem a classe canônica exigida nas Skills. Por exemplo, uma sintaxe pode ser `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED`; uma alegação preservada apenas de um resumo pode ser `UNVERIFIED / PROJECT-ASSERTED / REFERENCED-ONLY`. O mapeamento completo está em `architecture-decisions.md` e deve ser copiado de forma autocontida para cada Skill.

## 3. Proveniência: baseline, entradas e novos artefatos

### 3.1 Baseline pré-existente

O baseline era o repositório genérico de DFIR no commit `a90c40c`, tag `v0.1.0-rc.2`. Antes da criação dos artefatos de pesquisa desta execução:

- 93 arquivos de texto legíveis, todo o histórico Git alcançável e cinco blobs Git não alcançáveis foram pesquisados;
- não havia ocorrência de termos da família Cortex/Palo Alto, consultas XQL salvas, APIs Cortex, integrações Cortex ou playbooks XSOAR/XSIAM;
- oito arquivos `.pyc` eram derivados gerados de fontes Python legíveis e não continham conhecimento independente;
- o repositório fornecia metodologia, modelos, procedimentos e validadores DFIR independentes de produto.

As fontes centrais desse baseline são os arquivos externos de desenvolvimento `SKILL.md`, `README.md`, `references/methodology.md`, `references/evidence-handling.md`, `references/chain-of-custody.md`, `references/timeline-analysis.md` e `references/reporting.md` do projeto DFIR de origem. Eles não são dependências de runtime nem fazem parte do pacote publicável `cortex-ai-skills`.

Os dois registros privados sob `.research/` também pertenciam ao baseline. Eles contêm somente resumos saneados de uma revisão anterior de curso/Drive. Os documentos privados subjacentes não estavam presentes e não são evidência diretamente acessível. Esses registros não devem ser publicados nem usados para alegar acesso às fontes originais.

### 3.2 Entradas Cortex acessíveis nesta execução

Foram legíveis quatro grupos de entrada:

1. **Família solta `soc-optimization`:** seis artefatos derivados que descrevem um snapshot descontinuado, identificado pelo projeto como versão `2.1.19`.
2. **Família do ZIP `cortex-project-context`:** pacote independente com 21 entradas UTF-8 sob `skills/cortex-project-context/`, incluindo contexto de identidade, DNS, OpenCTI, triagem/SLA N1 e Continuous Assessment.
3. **Exportações e lotes operacionais:** doze tabelas de endpoints, uma planilha e dois conjuntos de lotes de nomes de máquinas.
4. **Prompt mestre anexado:** requisitos para sete Skills modulares, Golden Reference XQL, evidência, revisão, testes e isolamento entre Skills.

Esses grupos não formam uma única base homogênea. Em especial, os arquivos soltos e os arquivos de mesmo nome dentro do ZIP descrevem corpora distintos e não podem ser unidos por nome.

### 3.3 Artefatos recém-criados

Os seguintes arquivos foram criados durante a atual frente de ingestão/pesquisa e não pertencem ao baseline:

- o inventário externo de conhecimento do projeto (`project-knowledge-inventory.md`);
- o registro externo de diferenças entre projeto e documentação oficial (`project-vs-official-differences.md`);
- [mapa do ecossistema Cortex](cortex-ecosystem-map.md);
- este `project-findings.md`.

Eles são artefatos de desenvolvimento da Fase 1. Não devem se tornar dependências obrigatórias de runtime de nenhuma Skill publicável. Cada Skill deverá carregar internamente o mínimo necessário de fontes, limites e controles para operar sozinha.

## 4. Conhecimento Cortex efetivamente acessível

### 4.1 Família solta `soc-optimization`

Os seis arquivos soltos descrevem, sem fornecer o código-fonte original:

- contratos como `SOCFramework.Artifacts`, `SOCFramework.Product` e `SOCFramework.shadow_mode`;
- orquestração Foundation/NIST, roteamento por categoria de produto, playbooks folha, métricas, seleção blue/green e gates de contenção em shadow mode;
- riscos alegados de conteúdo legado/V2/duplicado/placeholder, lacuna de roteamento Cloud, divergência em `modification_time`, propagação ausente de entradas de contenção, falhas de collector/emergency flush, `value_tags` inconsistentes, CI fail-open e dependências não verificadas.

Status: `LOCAL-VERIFIED` quanto ao texto disponível; `PROJECT-ASSERTED` e `VERSION-DEPENDENT` quanto à implementação. O snapshot alegado de 156 arquivos, seu commit, seus YAML/Python/JSON e seu estado de implantação não estavam acessíveis.

O relatório completo dessa família incorpora cópias dos quatro Markdown soltos; essas cópias são `DERIVATIVE` e não aumentam o peso da evidência.

### 4.2 Família `cortex-project-context.zip`

O ZIP foi verificado estruturalmente:

- 21 caminhos relativos únicos e seguros;
- 239.785 bytes descompactados;
- UTF-8 estrito e manifesto JSON válido;
- descompactação integral bem-sucedida;
- SHA-256 `1bf727c0afef71f256f9244671b88d74ae6ecca3d610261db2611f0670b96427`.

O pacote contém políticas, mapas, decisões, glossário, workflows, dependências, riscos, segurança, manutenção e manifestos. Seus padrões úteis incluem:

- pipeline `gatilho/Issue/Job → normalização → enriquecimento/XQL → decisão determinística → evidência → IA consultiva → ação/relatório/status`;
- entradas e saídas explícitas entre parent/sub-playbook;
- namespaces de contexto controlados;
- IA consultiva, com saída estruturada e fora de decisões destrutivas sem gates determinísticos;
- falha degradada, idempotência, no-overlap para Jobs, shadow mode e aprovação para contenção;
- proteção de segredos, resistência a prompt injection e validação de interpolação/HTTP/API.

O `FULL_CONTEXT.md` é a agregação normalizada do `SKILL.md` e de 17 arquivos Markdown, com pequeno preâmbulo. Ele é `DERIVATIVE`, não uma fonte adicional.

O pacote preserva seis achados P0 alegados:

1. webhooks completos embutidos em cinco baselines YAML;
2. ramo de brute force Entra comprometido resolvido como falso positivo;
3. password spray sem autenticação bem-sucedida tratado como falso positivo;
4. uso de `Resolved - TruePositive` apesar de um PDF local alegar que o motivo é inválido;
5. argumentos de contenção passados como literais por ausência de `${...}`;
6. divergência entre descrições de AI Tasks e chaves de contexto consumidas, sem contrato de saída visível.

Esses itens continuam relevantes, mas são `PROJECT-ASSERTED`: os YAML/PDF originais não estavam presentes. Nenhuma reprodução de segredo, hostname ou identificador sensível é permitida.

### 4.3 Exportações operacionais

As doze exportações rotuladas como XSIAM contêm, em conjunto, 3.457 registros únicos com duas colunas: `Endpoint ID` e `Endpoint Name`. Não há sobreposição de nomes entre as doze exportações. A estrutura é compatível com exportação TSV do Host Inventory segundo a documentação oficial, mas os arquivos não registram a aplicação selecionada, o filtro, a tela de origem, o tenant ou o intervalo temporal.

Um arquivo com extensão `.csv` contém TABs e deve ser tratado como extensão/conteúdo divergentes, preservando-se o original e a proveniência de qualquer cópia corrigida. A planilha contém 908 nomes únicos; os lotes de texto têm relações parciais ou desconhecidas com ela. Nomes e IDs não são reproduzidos aqui por sensibilidade operacional.

Status: estrutura `LOCAL-VERIFIED`; associação a aplicativo, objeto de produto e finalidade operacional `TENANT-UNVERIFIED`.

### 4.4 Conhecimento oficial já reconciliado

O inventário e o registro de diferenças mapearam documentação oficial atual sobre, entre outros temas:

- terminologia Case/Issue, Insights e Findings;
- contexto e sub-playbooks;
- XQL, datasets, presets e boas práticas;
- correlation rules;
- Host Inventory;
- ingestão de alertas externos e APIs legadas;
- coletores de eventos e `send_events_to_xsiam()`;
- estrutura de content packs e `demisto-sdk`;
- DBotScore;
- TIM, ciclo de indicadores e EDL;
- Jobs, automação e limites entre XSIAM, XDR e XSOAR.

Essa reconciliação é datada de 2026-09-04 e deve ser refeita no momento de implementação. Ela não substitui validação de schema, licença, RBAC, versão e disponibilidade no tenant.

## 5. Conhecimento inacessível ou apenas referenciado

Não estavam acessíveis e não foram alegados como ingeridos:

- conhecimento mais amplo do ChatGPT Project, histórico de conversas ou biblioteca de arquivos não montados;
- tenant XSIAM/XDR/XSOAR ao vivo, schema, autocomplete do Query Builder, RBAC, content packs instalados, Jobs, instâncias de integração e histórico de implantação;
- onze fontes locais anteriores apenas nomeadas no manifesto do ZIP, incluindo YAML, DOCX e PDF;
- oito itens apenas nomeados como pertencentes a uma Project File Library anterior;
- o repositório/snapshot `soc-optimization` alegadamente composto por 156 arquivos;
- consultas XQL executadas, resultados ao vivo, exports de correlation rules ou schemas de comandos instalados.

Hashes e nomes preservados permitem futura verificação de identidade, mas não provam conteúdo, correção, implantação ou suporte atual. Não se pode afirmar que “todo o conhecimento do ChatGPT” foi usado.

## 6. Consultas, scripts, playbooks e integrações

| Categoria | Presente | Ausente ou não comprovado | Consequência |
|---|---|---|---|
| Consultas XQL | Casos de uso, nomes alegados de datasets/namespaces e diretrizes de segurança em documentos derivados | Nenhuma consulta salva, resultado ao vivo, schema ou export do Query Builder | Sintaxe, estágios, funções e campos podem ser apresentados como XQL executável **não executado** quando uma fonte oficial atual os documenta; disponibilidade, população, resultados e desempenho do tenant continuam `TENANT-UNVERIFIED` até observação ou execução. |
| Scripts do baseline | Validadores externos de manifesto, hashes e estrutura de repositório no projeto DFIR de origem | Nenhum script Cortex/XQL/API diretamente disponível | Reaproveitar padrões de validação; não rotular esses scripts como integração Cortex nem criar dependência externa. |
| Scripts Cortex | Descrições derivadas de automações/collectors e nomes de arquivos no corpus ausente | Fonte Python/YAML, metadados, versão, comandos e execução | Permanecem `REFERENCED-ONLY`; não são importáveis nem testáveis neste estado. |
| Procedimentos DFIR | Dezenove workflows Markdown, incluindo triagem, timeline, credenciais, lateral movement, exfiltração e ransomware | Execução Cortex | São procedimentos, não playbooks XSOAR/XSIAM. |
| Playbooks Cortex | Arquiteturas, contratos e achados descritos pelas duas famílias de contexto | YAML atual, grafo validado, IDs, inputs/outputs reais e teste no tenant | Usar somente como padrões/hipóteses até recuperar os originais. |
| Integrações | Referências a AD, Microsoft Graph, Teams, OpenCTI, HttpV2, TIM, AI Tasks e collector de eventos | Instâncias, versões, RBAC, dependências, ajuda de comandos, schemas e status de sistema/custom | Nenhum comando ou output path deve ser inventado. O collector requer resolução específica antes de uso. |
| Dados operacionais | Exportações tabulares e lotes de endpoints | Metadados de geração e finalidade do lote | Exigir manifesto de origem, filtro, contagem, exclusões, owner, destino, timestamps e hashes. |
| Regras/detecções | Casos de uso e decisões derivadas | Correlation rule exportada, thresholds validados, telemetria comprovada e resultados | Projetar somente após modelo de ameaça, cobertura e schema do tenant. |

## 7. Convenções DFIR reaproveitáveis

O baseline oferece uma fundação metodológica forte, mas não uma tradução pronta para Cortex.

### 7.1 Ciclo de trabalho

`Preserve → Acquire → Validate → Examine → Correlate → Hypothesize → Test → Conclude → Document`

Aplicação futura: preservar exports originais, criar cópias de trabalho verificadas, registrar ferramentas/versões e manter cada transformação rastreável.

### 7.2 Classes de raciocínio

- Evidência observada;
- informação derivada;
- correlação;
- hipótese;
- explicação alternativa;
- validação.

Saída de parser, alerta, correlação ou modelo é pista até ser corroborada. Mapeamento ATT&CK deve ocorrer depois da identificação do comportamento, não como substituto da evidência.

### 7.3 Incerteza e confiança

Valores desconhecidos devem usar `Unknown`, `Not provided` ou `Requires validation`, sem preenchimento especulativo. Os níveis internos reutilizáveis são `CONFIRMED`, `HIGH CONFIDENCE`, `MODERATE CONFIDENCE`, `LOW CONFIDENCE` e `INSUFFICIENT EVIDENCE`.

Esses níveis não substituem os rótulos de verificação de produto deste documento. Uma conclusão analítica pode ter alta confiança enquanto a disponibilidade de um campo no tenant continua `TENANT-UNVERIFIED`.

### 7.4 Impacto, contexto e autorização

Rótulos reutilizáveis:

- impacto: `READ-ONLY`, `LOW IMPACT`, `MODIFIES SYSTEM`, `DESTRUCTIVE`;
- contexto: `OFFLINE`, `LOCAL-LIVE`, `REMOTE`, `NETWORK`, `PRIVILEGED`.

Ações como isolamento, bloqueio, desativação de conta, término de processo ou exclusão exigem verificação, confiança, escopo, autorização/policy gate, blast radius, rollback e verificação pós-ação.

### 7.5 Identificadores e registros

Os modelos existentes usam IDs estáveis como `S-###`, `E-###`, `O-###`, `D-###`, `F-###`, `H-###` e `COC-###`, além de logs append-only, matriz de achados/hipóteses e cadeia de custódia. Esses padrões são adequados para rastrear fontes, consultas, resultados, achados e decisões das Skills.

### 7.6 Controles de evidência

- proteger originais e trabalhar sobre cópias verificadas;
- usar SHA-256 como padrão de integridade;
- preservar timestamp bruto, interpretação, timezone e incerteza;
- qualificar evidência negativa pela cobertura disponível;
- minimizar PII e segredos;
- tratar conteúdo inserido em evidência como dados não confiáveis;
- separar integridade do provedor de integridade no recebimento;
- manter source IDs e ligação entre afirmação e fonte.

## 8. Diferenças materiais já identificadas

O detalhe original, a evidência oficial e a resolução exigida foram preservados no registro externo `project-vs-official-differences.md`. O resumo autocontido para este repositório é:

| ID | Situação | Classificação | Implicação para as Skills |
|---|---|---|---|
| D-01 | `send_events_to_xsiam()` não pode ser presumido em collector customizado; a função oficial exige integração de sistema. | `UNSUPPORTED` sem prova de proveniência | Bloquear o caminho de métricas até recuperar metadados e confirmar a integração/tenant. |
| D-02 | Incident/Alert são termos legados; Case/Issue são os termos atuais, com compatibilidade a ser migrada com teste. | `VERSION-DEPENDENT` | Não renomear identificadores técnicos mecanicamente; rotular exemplos atuais e legados. |
| D-03 | Insight não é definido apenas como resultado Analytics/BIOC. | `CONTRADICTED` / `OVERGENERALIZED` | Usar o modelo atual de promoção de Issues e preservar a definição antiga como observação datada. |
| D-04 | Finding não é simplesmente um subtipo de Issue. | `CONTRADICTED` / `OVERGENERALIZED` | Separar schemas, IDs, ciclo, permissões e automação; validar licenças. |
| D-05 | `${issue.*}`, `${parentIncidentContext.*}` e `parentIncidentFields` têm finalidades distintas; contexto separado não é fronteira de segurança. | `VERSION-DEPENDENT` / `TENANT-UNVERIFIED` | Exigir contrato de contexto por playbook, com tipo, cardinalidade e propagação. |
| D-06 | DBotScore `0` significa Unknown, não Good. | Semântica oficial clara; defeito alegado ainda depende do YAML | Nunca fechar/liberar automaticamente agrupando 0 e 1; recuperar e testar a lógica. |
| D-07 | IPs, portas e timestamp fictícios não são defaults seguros para ingestão. | Prática `CONTRADICTED` | Omitir opcionais ausentes, usar tempo real/proveniente e rejeitar/quarentenar registros inválidos. |
| D-08 | O layout do snapshot antigo não é o layout atual de contribuição de content packs. | `VERSION-DEPENDENT` | Definir o alvo — tenant custom, Org repository ou Marketplace — antes de normalizar. |
| D-09 | `demisto-sdk` não suporta Windows nativo. | Restrição atual de ambiente | Validar em WSL2 ou container, com versões e saídas registradas. |
| D-10 | Um export `.csv` é, pelos bytes, tab-delimitado. | Divergência local | Detectar delimitador ou renomear somente cópia verificada, preservando o original. |
| D-11 | A integração PAN-OS EDL legada está descontinuada para novos designs TIM. | `DEPRECATED` | Usar o caminho atual apenas após verificar tenant, licença e integração. |
| D-12 | “Application” pode significar software instalado, Business Application ou objeto DLP. | `OVERGENERALIZED` | Registrar família do objeto, tela, filtro, licença e origem do export. |
| D-13 | XSIAM, XDR e XSOAR não são intercambiáveis. | `OVERGENERALIZED` / dependente de licença e versão | Vincular toda afirmação a produto, versão, implantação, edição/licença e fonte. |
| D-14 | Insert Parsed Alerts continua referenciado pela administração atual, mas é listado como API legada sem sucessora Platform identificada; compatibilidade efetiva e schema permanecem não verificados no tenant. | `VERSION-DEPENDENT` | Preservar o path apenas como candidato de compatibilidade, recuperar referência oficial versionada, testar no tenant e manter watch de migração; não inventar substituto. |

Há também seis diferenças internas de proveniência:

- o relatório “58/58” valida outra revisão e não o ZIP fornecido;
- arquivos soltos e homônimos do ZIP descrevem corpora distintos;
- a precedência de fontes embutida no ZIP foi substituída pela precedência definida pelo usuário;
- agregações e resumos não contam como fontes independentes;
- originais nomeados em manifestos continuam ausentes;
- lotes de endpoints não têm proveniência operacional suficiente.

## 9. Consumo recomendado por Skill

| Skill | Conhecimento de projeto reutilizável | Limite obrigatório |
|---|---|---|
| `cortex-xql-query-engineer` | Disciplina de evidência, segurança de consultas, casos de uso, exports e namespaces internos | Verificar sintaxe, estágio, função, operador e campo mostrado em fonte oficial atual para usar `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED`; manter `C: NOT RUN` e `E: NOT RUN` sem evidência de tenant. Nenhuma consulta fornecida prova execução no tenant. |
| `cortex-detection-engineer` | Casos de identidade/DNS/OpenCTI, decisão determinística, blue/green e riscos de falso positivo | Validar tipo de regra, schema, limiar, cobertura, telemetria e efeitos de Case/Issue. |
| `cortex-playbook-engineer` | Parent/child, I/O explícito, contexto namespaced, falha degradada, shadow mode, gates e achados P0 | Recuperar YAML; verificar comandos, IDs, close reasons, content packs e contexto no tenant. |
| `cortex-threat-hunter` | Hipóteses, timeline, pivôs, evidência negativa e disciplina de correlação | Não inferir retenção, cobertura, dataset ou campos; registrar lacunas e probes. |
| `cortex-tim-engineer` | OpenCTI, DBotScore, deduplicação, paginação, ciclo de indicadores e EDL | Validar licença, integração, versão, schema de comandos, RBAC e caminho EDL atual. |
| `cortex-platform-engineer` | Mapas de dependência, release validation, exports, Jobs/idempotência e manifestos | Separar produtos e alvos de implantação; confirmar integrações, datasets, APIs e estado do tenant. |
| `cortex-security-engineer` | Segredos, prompt injection, least privilege, aprovação, contenção e sensibilidade de dados | Rever originais antes de confirmar exposições; validar RBAC/permissões e nunca reproduzir dados sensíveis. |

Todos devem reutilizar a proveniência, a taxonomia de evidência, os IDs estáveis, os controles de incerteza e a política de não tratar conteúdo hostil como instrução.

## 10. Status, qualifiers e níveis de validação

Não usar “executável” como sinônimo de “executado” ou “validado no tenant”. A classe canônica (`VERIFIED`, `VERSION-DEPENDENT`, `INFERRED`, `CONCEPTUAL`, `UNSUPPORTED`, `DEPRECATED` ou `UNVERIFIED`) e os qualifiers aplicáveis permanecem separados destes resultados:

| Nível | Requisito | Resultados permitidos |
|---|---|---|
| `S` | Avaliação controlada do comportamento contra oracle isolado. | `PASS`, `FAIL`, `NOT RUN`, `N/A` com racional. |
| `D` | Fonte oficial atual sustenta os claims materiais no produto/contexto indicado. | `PASS`, `FAIL`, `NOT RUN`, `N/A` com racional. |
| `C` | Schema/editor/compiler/API/import do tenant nomeado aceitou ou expôs o artefato exato. | `PASS`, `FAIL`, `NOT RUN`, `N/A` com racional. |
| `E` | O artefato exato executou ou produziu o resultado/ação observado no ambiente delimitado. | `PASS`, `FAIL`, `NOT RUN`, `N/A` com racional. |

Para elevar exemplos ou artefatos aos níveis dependentes de tenant/importação, ainda é necessário:

1. exportar a lista de datasets/schema do tenant e validar campos no Query Builder;
2. recuperar YAML/Python/JSON/DOCX/PDF originais e comparar seus hashes com os manifestos;
3. identificar versões de content packs, itens destacados/modificados, Jobs, integrações, AI Tasks e schema atual de Case/Issue;
4. executar `demisto-sdk` em WSL2/container, seguido de testes de playbook em tenant não produtivo;
5. registrar aplicação/filtro/tela de origem para cada export de endpoints;
6. resolver os itens P0 e as diferenças D-01 a D-14 sem apagar o contexto histórico;
7. revalidar documentação oficial no momento de cada implementação.

Testes estáticos, hashes, estrutura de ZIP e coerência documental não provam runtime, segurança operacional, compatibilidade de tenant ou produção.

## 11. Checkpoint da Fase 1

### Trabalho concluído

- inspeção abrangente do workspace e histórico Git;
- identificação do baseline sem conteúdo Cortex;
- ingestão dos arquivos fornecidos e do prompt mestre acessível;
- separação das duas famílias de contexto;
- inventário de consultas, scripts, playbooks, integrações, dados e referências;
- verificação estrutural do ZIP e das exportações;
- reconciliação inicial com documentação oficial atual;
- registro de diferenças, riscos, limites de acesso e consumo por Skill;
- criação deste relatório sem gerar Skills finais.

### Evidência coletada

- baseline DFIR legível e seus validadores;
- seis artefatos soltos da família `soc-optimization`;
- 21 entradas do ZIP e seu manifesto;
- doze exportações de endpoints, planilha e lotes;
- requisitos do prompt mestre;
- documentação oficial registrada no inventário e no relatório de diferenças.

### Arquivos criados ou modificados nesta frente

- criados: os quatro artefatos listados na seção 3.3;
- modificado por este trabalho específico: somente `research/project-findings.md` dentro de `cortex-ai-skills`.

### Testes e verificações realizados

- pesquisa textual no baseline, histórico alcançável e blobs não alcançáveis;
- leitura e classificação de todos os artefatos relevantes acessíveis;
- verificação de caminhos, UTF-8, JSON, descompactação, contagens e SHA-256 do ZIP;
- comparação de duplicação/proveniência entre arquivos soltos e ZIP;
- verificação de delimitador, cabeçalhos, unicidade e relações dos exports/lotes;
- revisão documental oficial e classificação das diferenças.

Não realizados: execução XQL, validação de schema no Query Builder, teste de API, `demisto-sdk`, importação de content pack, teste de playbook, inspeção de RBAC ou homologação no tenant.

### Achados principais

1. O baseline é metodologicamente útil, mas não contém conhecimento Cortex factual.
2. O contexto Cortex disponível é majoritariamente derivado e mistura legado, target state e alegações sem os originais.
3. Não existe consulta XQL executável nem playbook/import verificável fornecido.
4. Existem riscos P0 preservados que não podem ser confirmados ou descartados sem os YAML/PDF.
5. A documentação oficial atual confirma parte dos padrões, corrige conceitos e impõe limites relevantes.
6. A proveniência dos exports de endpoints é insuficiente para reutilização operacional direta.

### Riscos abertos

- collector de métricas possivelmente fora do limite de suporte;
- dados fictícios em ingestão OpenCTI;
- lógica alegadamente insegura de DBotScore, fechamento e contenção;
- termos, context paths e APIs legados misturados com o modelo atual;
- ausência de schema, versões, licenças, RBAC e execução do tenant;
- originais, repositório de implementação e biblioteca anterior indisponíveis;
- relatório de validação associado à revisão errada do ZIP.

### Gate de qualidade

| Gate | Estado | Justificativa |
|---|---|---|
| Ingestão do material acessível | `PASS` | Fontes disponíveis foram lidas, classificadas e delimitadas. |
| Proveniência e não alucinação | `PASS` | Baseline, derivados, fontes ausentes e conflitos foram distinguidos. |
| Inventário de projeto | `PASS` | Categorias presentes e ausentes estão registradas. |
| Verificação de runtime/tenant | `NOT RUN` | Tenant e fontes executáveis não estavam disponíveis. |
| Resolução de P0/diferenças | `OPEN` | Exige originais e/ou tenant. |
| Fase 1 global | `SUPERSEDED` | Estado histórico desta frente. A decisão consolidada e independente existe somente em `phase-1-checkpoint.md`. |

### Elegibilidade para a próxima fase

**ESTADO HISTÓRICO DESTA FRENTE: SUPERSEDED.**

Este arquivo não autoriza nem bloqueia sozinho a Fase 2. O checkpoint único em `phase-1-checkpoint.md` incorpora a conclusão dos cinco entregáveis, o gate independente e suas correções. A ausência de tenant não impede exemplos `VERIFIED / OFFICIAL-CURRENT / TENANT-UNVERIFIED` sustentados por documentação; exige que `C` e `E` permaneçam `NOT RUN` e impede claims de schema, compilação, execução, resultado, desempenho ou importabilidade no tenant.
