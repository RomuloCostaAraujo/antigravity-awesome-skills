---
name: concise-planning-ptbr
description: Use quando um usuário pedir um plano para uma tarefa de codificação, para gerar um checklist claro, acionável e atômico.
---

# Planejamento Conciso

## Objetivo

Transformar um pedido do usuário em um **plano único e acionável** com passos atômicos.

## Fluxo de Trabalho

### 1. Analisar Contexto

- Leia `README.md`, documentos e arquivos de código relevantes.
- Identifique restrições (linguagem, frameworks, testes).

### 2. Interação Mínima

- Faça **no máximo 1–2 perguntas** e apenas se forem realmente impeditivas.
- Assuma premissas razoáveis para incógnitas que não bloqueiam o progresso.

### 3. Gerar Plano

Use a seguinte estrutura:

- **Abordagem**: 1-3 frases sobre o quê e por quê.
- **Escopo**: Tópicos para "Dentro" (In) e "Fora" (Out).
- **Itens de Ação**: Uma lista de 6-10 tarefas atômicas e ordenadas (começando com Verbo).
- **Validação**: Pelo menos um item para testes.

## Modelo de Plano (Template)

```markdown
# Plano

<Abordagem de alto nível>

## Escopo

- Dentro:
- Fora:

## Itens de Ação

[ ] <Passo 1: Descoberta/Análise>
[ ] <Passo 2: Implementação>
[ ] <Passo 3: Implementação>
[ ] <Passo 4: Validação/Testes>
[ ] <Passo 5: Entrega/Commit>

## Perguntas em Aberto

- <Pergunta 1 (máx 3)>
```

## Diretrizes do Checklist

- **Atômico**: Cada passo deve ser uma única unidade lógica de trabalho.
- **Verbo primeiro**: "Adicionar...", "Refatorar...", "Verificar...".
- **Concreto**: Nomeie arquivos ou módulos específicos sempre que possível.
