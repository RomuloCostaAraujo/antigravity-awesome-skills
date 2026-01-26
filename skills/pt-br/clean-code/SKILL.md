---
name: clean-code-ptbr
description: Padrões de codificação pragmática - conciso, direto, sem excesso de engenharia, sem comentários desnecessários.
allowed-tools: Read, Write, Edit
version: 2.0
priority: CRITICAL
---

# Código Limpo - Padrões de Codificação Pragmática para IA

> **HABILIDADE CRÍTICA** - Seja **conciso, direto e focado na solução**.

---

## Princípios Fundamentais

| Princípio | Regra |
|-----------|------|
| **SRP** | Responsabilidade Única - cada função/classe faz APENAS UMA coisa |
| **DRY** | Não se repita - extraia duplicatas, reutilize |
| **KISS** | Mantenha o simples - a solução mais simples que funciona |
| **YAGNI** | Você não vai precisar disso - não construa funcionalidades não utilizadas |
| **Escoteiro** | Deixe o código mais limpo do que você o encontrou |

---

## Regras de Nomenclatura

| Elemento | Convenção |
|----------|------------|
| **Variáveis** | Revele a intenção: `userCount` em vez de `n` |
| **Funções** | Verbo + substantivo: `getUserById()` em vez de `user()` |
| **Booleanos** | Forma de pergunta: `isActive`, `hasPermission`, `canEdit` |
| **Constantes** | SCREAMING_SNAKE: `MAX_RETRY_COUNT` |

> **Regra:** Se você precisa de um comentário para explicar um nome, renomeie-o.

---

## Regras para Funções

| Regra | Descrição |
|------|-------------|
| **Pequenas** | Máximo 20 linhas, idealmente 5-10 |
| **Uma Coisa** | Faz uma coisa e faz bem |
| **Um Nível** | Um nível de abstração por função |
| **Poucos Argumentos** | Máximo 3 argumentos, prefira 0-2 |
| **Sem Efeitos Colaterais** | Não altere as entradas de forma inesperada |

---

## Estrutura de Código

| Padrão | Aplicação |
|---------|-------|
| **Cláusulas de Guarda** | Retornos antecipados para casos de borda |
| **Plano > Aninhado** | Evite aninhamento profundo (máx. 2 níveis) |
| **Composição** | Funções pequenas compostas juntas |
| **Colocação** | Mantenha o código relacionado próximo |

---

## Estilo de Codificação para IA

| Situação | Ação |
|-----------|--------|
| Usuário pede funcionalidade | Escreva o código diretamente |
| Usuário relata bug | Corrija, não explique |
| Requisito não está claro | Pergunte, não assuma |

---

## Anti-padrões (NÃO FAÇA)

| ❌ Padrão | ✅ Correção |
|-----------|-------|
| Comentar cada linha | Delete comentários óbvios |
| Helper para uma linha | Coloque o código diretamente no local |
| Fábrica para 2 objetos | Instanciação direta |
| utils.ts com 1 função | Coloque o código onde ele é usado |
| "Primeiro vamos importar..." | Apenas escreva o código |
| Aninhamento profundo | Cláusulas de guarda |
| Números mágicos | Constantes nomeadas |
| Funções "Deus" | Divida por responsabilidade |

---

## 🔴 Antes de Editar QUALQUER Arquivo (PENSE PRIMEIRO!)

**Antes de alterar um arquivo, pergunte-se:**

| Pergunta | Por que |
|----------|-----|
| **O que importa este arquivo?** | Eles podem quebrar |
| **O que este arquivo importa?** | Mudanças de interface |
| **Quais testes cobrem isso?** | Testes podem falhar |
| **É um componente compartilhado?** | Múltiplos locais afetados |

**Verificação Rápida:**
```
Arquivo para editar: UserService.ts
└── Quem importa isso? → UserController.ts, AuthController.ts
└── Eles precisam de mudanças também? → Verifique as assinaturas das funções
```

> 🔴 **Regra:** Edite o arquivo + todos os arquivos dependentes na MESMA tarefa.
> 🔴 **Nunca deixe imports quebrados ou atualizações ausentes.**

---

## Resumo

| Faça | Não Faça |
|----|-------|
| Escreva código diretamente | Escreva tutoriais |
| Deixe o código se auto-documentar | Adicione comentários óbvios |
| Corrija bugs imediatamente | Explique a correção primeiro |
| Use inline para coisas pequenas | Crie arquivos desnecessários |
| Nomeie as coisas claramente | Use abreviações |
| Mantenha funções pequenas | Escreva funções de 100+ linhas |

> **Lembre-se: O usuário quer código funcional, não uma lição de programação.**

---

## 🔴 Autoverificação Antes de Concluir (OBRIGATÓRIO)

**Antes de dizer "tarefa concluída", verifique:**

| Check | Pergunta |
|-------|----------|
| ✅ **Objetivo atingido?** | Fiz exatamente o que o usuário pediu? |
| ✅ **Arquivos editados?** | Modifiquei todos os arquivos necessários? |
| ✅ **Código funciona?** | Testei/verifiquei a alteração? |
| ✅ **Sem erros?** | Lint e TypeScript passam? |
| ✅ **Nada esquecido?** | Algum caso de borda perdido? |

> 🔴 **Regra:** Se QUALQUER verificação falhar, corrija antes de concluir.

---

## Scripts de Verificação (OBRIGATÓRIO)

> 🔴 **CRÍTICO:** Cada agente executa APENAS os scripts de sua própria habilidade após concluir o trabalho.

### Mapeamento Agente → Script

| Agente | Script | Comando |
|-------|--------|---------|
| **frontend-specialist** | Auditoria UX | `python scripts/ux_audit.py .` |
| **backend-specialist** | Validador de API | `python scripts/api_validator.py .` |
| **security-auditor** | Scan de Segurança | `python scripts/security_scan.py .` |
| **Any agent** | Check de Lint | `python scripts/lint_runner.py .` |
| **Any agent** | Cobertura de Tipos | `python scripts/type_coverage.py .` |

> 🔴 **Regra:** Sempre LEIA o output → RESUMA → PERGUNTE ao usuário → depois corrija.
