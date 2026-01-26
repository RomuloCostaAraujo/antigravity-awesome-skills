---
name: systematic-debugging-ptbr
description: Use ao encontrar qualquer bug, falha em teste ou comportamento inesperado, antes de propor correções.
---

# Depuração Sistemática

## Visão Geral

Correções aleatórias desperdiçam tempo e criam novos bugs. "Remendos" rápidos apenas escondem problemas subjacentes.

**Princípio Fundamental:** SEMPRE encontre a causa raiz antes de tentar qualquer correção. Corrigir apenas o sintoma é um erro.

**Violar a letra deste processo é violar o espírito da depuração.**

## A Lei de Ferro

```
SEM CORREÇÕES ANTES DA INVESTIGAÇÃO DA CAUSA RAIZ
```

Se você não completou a Fase 1, não pode propor correções.

## Quando Usar

Use para QUALQUER problema técnico:
- Falhas em testes
- Bugs em produção
- Comportamento inesperado
- Problemas de performance
- Falhas de build
- Problemas de integração

**Use ESPECIALMENTE quando:**
- Estiver sob pressão de tempo (emergências tornam o "chute" tentador)
- "Apenas uma correção rápida" parecer óbvio
- Você já tentou várias correções sem sucesso
- A correção anterior não funcionou
- Você não entende completamente o problema

## As Quatro Fases

Você DEVE completar cada fase antes de prosseguir para a próxima.

### Fase 1: Investigação da Causa Raiz

**ANTES de tentar QUALQUER correção:**

1. **Leia Mensagens de Erro com Atenção**
   - Não ignore erros ou avisos. Eles costumam conter a solução exata.
   - Leia as stack traces completamente. Anote linhas, arquivos e códigos de erro.

2. **Reproduza Consistentemente**
   - Você consegue disparar o erro de forma confiável? Quais os passos exatos?
   - Se não for reproduzível -> reúna mais dados, não adivinhe.

3. **Verifique Mudanças Recentes**
   - O que mudou que pode ter causado isso? Veja git diff, commits recentes, dependências.

4. **Colete Evidências em Sistemas Complexos**
   - Adicione logs em cada fronteira de componente: o que entra, o que sai, estado de cada camada.
   - Identifique ONDE quebra antes de investigar COMO quebra.

### Fase 2: Análise de Padrão

**Encontre o padrão antes de corrigir:**
- Localize código similar que funciona. O que ele faz de diferente?
- Leia a implementação de referência COMPLETAMENTE. Não apenas passe o olho.
- Entenda as dependências, configurações e premissas do sistema.

### Fase 3: Hipótese e Teste

**Método Científico:**
1. **Formule uma Única Hipótese:** "Eu acho que X é a causa raiz devido a Y". Seja específico.
2. **Teste Minimamente:** Faça a MENOR alteração possível para testar a hipótese. Uma variável por vez.
3. **Verifique:** Funcionou? Passe para a Fase 4. Não funcionou? Formule uma NOVA hipótese.

### Fase 4: Implementação

**Corrija a causa raiz, não o sintoma:**
1. **Crie um Caso de Teste que Falha:** Você DEVE ter um teste que comprove o erro antes de corrigi-lo.
2. **Implemente uma Única Correção:** Resolva a causa raiz identificada. Sem melhorias "já que estou aqui".
3. **Verifique a Correção:** O teste passa? Nada mais quebrou?
4. **Se a correção não funcionar (3+ tentativas): PARE.** Questione a arquitetura. Não tente a 4ª correção sem discutir a abordagem fundamental.

## Sinais de Alerta - PARE e Siga o Processo

Se você se pegar pensando:
- "Correção rápida agora, investigo depois"
- "Vou só mudar X e ver se funciona"
- "Vou pular o teste, verifico manualmente"
- "Provavelmente é X, deixa eu corrigir"

**Tudo isso significa: PARE. Volte para a Fase 1.**
