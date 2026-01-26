---
name: kaizen-ptbr
description: Guia para melhoria contínua, prevenção de erros e padronização. Use quando quiser melhorar a qualidade do código, refatorar ou discutir melhorias de processo.
---

# Kaizen: Melhoria Contínua

## Visão Geral

Pequenas melhorias, continuamente. À prova de erros por design. Siga o que funciona. Construa apenas o necessário.

**Princípio fundamental:** Muitas pequenas melhorias superam uma única grande mudança. Previna erros no momento do design, não com remendos.

## Os Quatro Pilares

### 1. Melhoria Contínua (Kaizen)

Pequenas e frequentes melhorias se acumulam em ganhos exponenciais.

- **Incremental em vez de revolucionário:** Faça a menor mudança viável que melhore a qualidade. Verifique cada mudança antes da próxima.
- **Sempre deixe o código melhor:** Corrija pequenos problemas ao encontrá-los. Refatore enquanto trabalha. Remova código morto.
- **Refinamento iterativo:** 1º faz funcionar; 2º faz ser claro; 3º faz ser eficiente. Não tente os três ao mesmo tempo.

### 2. Poka-Yoke (À Prova de Erros)

Projete sistemas que previnem erros no tempo de compilação/design, não em tempo de execução.

- **Torne os erros impossíveis:** O sistema de tipos deve capturar erros. Estados inválidos devem ser irrepresentáveis.
- **Design para segurança:** Falhe rápido e de forma ruidosa. Forneça mensagens de erro úteis.
- **Defesa em camadas:** Sistema de tipos → Validação → Guardas → Limites de erro.

### 3. Trabalho Padronizado

Siga padrões estabelecidos. Documente o que funciona. Facilite as boas práticas.

- **Consistência sobre "esperteza":** Siga os padrões do projeto existente. Não reinvente problemas já resolvidos.
- **Automatize padrões:** Linters, verificações de tipo e testes devem garantir a qualidade automaticamente.

### 4. Just-In-Time (JIT)

Construa o que é necessário agora. Sem mais, sem menos. Evite otimização prematura e excesso de engenharia.

- **YAGNI (Você não vai precisar disso):** Implemente apenas os requisitos atuais.
- **A coisa mais simples que funciona:** Adicione complexidade apenas quando necessário. Refatore quando os requisitos mudarem.
- **Otimize quando houver medição:** Sem otimização prematura. Meça o impacto antes de mudar.

## Mentalidade Kaizen
Bom o suficiente hoje, melhor amanhã. Repita.
