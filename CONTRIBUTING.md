# Como contribuir

Obrigado por contribuir com o Cortex AI Skills.

Para melhorias nas instruções ou exemplos técnicos, siga a [política detalhada](source/CONTRIBUTING.md) e a [arquitetura](source/ARCHITECTURE.md). Inclua produto, versão, fonte oficial específica e escopo de validação.

## Documentação

README e `docs/` são a documentação atual de uso. Preserve os relatórios históricos e diferencie fatos verificados, mudanças documentais e testes ainda não executados.

## Pacotes

Os artefatos de `packages/0.1.0/` são preservados; não os substitua silenciosamente. Mudanças no runtime exigem versão, hashes e validação adequados. Não distribua testes e gabaritos dentro dos runtimes.

## Verificações antes de enviar uma mudança

Execute os quatro comandos de validação no [README](README.md). Não publique credenciais, dados brutos de clientes, dumps ou identificadores privados. Use exemplos sintéticos ou anonimizados.

Este projeto não instala integrações, executa consultas ou aplica alterações no seu tenant como parte dos testes de publicação.
