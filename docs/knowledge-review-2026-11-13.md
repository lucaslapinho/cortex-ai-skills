# Revisão da base de conhecimento — 13/11/2026

## Fonte e método

A fonte inicial foi o repositório `lucaslapinho/cortex-ai-skills`, main em `d423ba010b4422b32009c880bc9205632448f997`. O source/ do ZIP anexado correspondeu ao checkout; não foi presumida sincronização com o plugin instalado. Foram consultados o manual do projeto, a análise arquitetural e os dois documentos de pesquisa fornecidos.

| Arquivo recebido | Bytes | SHA-256 |
|---|---|---|
| `palo_alto_cloud_cortex_xsiam_skill_research.md` | 23459 | `b98d33fc1b8b848f69d5f6a1a2841d9e6f5bde9aa030ae63762c33f9452ad122` |
| `Palo_Alto_Networks_Research_Skill_2026.md` | 27667 | `e03e21c60fb99f574f61d528eff4f09a2a7d28ae2c9ccf987d34f0976a71e86d` |
| `cortex-ai-skills-main(1).zip` | 3185877 | `9b598d3621a2aa96c25db03091c08da0a04474e6bbcc281f2231ee3849911fe4` |
| `02-MANUAL_DE_ENGENHARIA_DE_SKILLS.md` | 15525 | `10ff442c14a770d910ca99afca0bdc5971a03b69b91566c55f9903bd18bebd30` |
| `01-ANALISE_CORTEX_AI_SKILLS.md` | 5774 | `a7e43856240849831a8b802031aa21efda06af69e873e5d474439ccca5dba72f` |

O documento de Cloud disponibilizado termina na seção 4.6, embora seu sumário anuncie outras seções. Os identificadores de fontes nele citados não substituem um registro verificável de URLs. Somente o conteúdo acessível foi aproveitado; as lacunas foram complementadas com documentação oficial, sem afirmar que os capítulos ausentes foram lidos.

O documento de Firewall/SASE/AIRS foi usado como orientação de cobertura. A arquitetura atual de AIRS foi reconciliada com a fonte oficial: Runtime, Supply Chain, Red Teaming e AI Gateway. O agrupamento antigo com AI Access Security foi separado da proteção de aplicações. Não se presumiu equivalência entre Prisma Cloud legado, Cortex Cloud e cada licença XSIAM.

## Revisão por domínio

| Domínio | Mudança substantiva |
|---|---|
| XQL | Retorno/ordenação, escrita target, limites e ambiguidades de API, diferenças de superfície |
| Detection | BIOC versus correlação, requisitos, limites documentados e grouping |
| Playbooks | AI Prompt local/library, inputs/schema, debugger com efeitos reais, permissões por instância |
| Hunting | Entitlement/RBAC, limites de exibição do Graph Search, caminhos versus atividade observada |
| TIM | Expiração/exportação/enforcement, DBotScore, serviço deprecated e parâmetros antigos de cache |
| Platform | Tiers de onboarding, Entra-only, escopo de acesso e componentes de coleta |
| Coordinator | Roteamento Palo Alto, dependências, contratos comuns e áreas sem especialista dedicado |
| Cloud | AWS/Azure/GCP/OCI, outposts, Kubernetes, risco, scan/runtime e linhagem AppSec |
| Firewall | PAN-OS/Panorama/SCM, NAT/política, jobs, herança, backup e Cloud NGFW |
| SASE | Caminho usuário/aplicação, Access/SD-WAN/Browser e direção de inspeção AI Access |
| AIRS | Arquitetura atual, API/network, artefatos, testes, falhas e autorização determinística |

O [registro de proveniência](source-review-2026-11-13.json) contém 42 páginas oficiais com URL consultada/final, hash do conteúdo recebido, data, produto/alegação e limite de evidência. São alegações selecionadas; não houve atualização exaustiva de todos os registros históricos. Textos completos do fabricante não foram incorporados ao pacote.

As referências locais de cada Skill registram as alegações relevantes e quando consultá-las. Conflitos anteriores não resolvidos permanecem explícitos: retorno regextract em referência antiga XDR, exemplos de dedup, origem/contagem da API XQL e restrições históricas de ações em correlação real-time. Datas de acesso não foram usadas como datas de release.

## Critério de conclusão

Estrutura e pacote, aderência documental, comportamento em respostas isoladas, importação/carregamento e execução real são avaliados separadamente. Uma cópia isolada de runtime não equivale a um plugin importado. O [relatório de validação](validacao.md) registra resultados efetivamente observados e pendências.
