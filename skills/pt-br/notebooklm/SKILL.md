---
name: notebooklm-ptbr
description: Use esta habilidade para consultar seus cadernos do Google NotebookLM diretamente do Claude Code para obter respostas baseadas em fontes e citações do Gemini. Automação de navegador, gerenciamento de biblioteca, autenticação persistente. Reduz drasticamente alucinações através de respostas baseadas exclusivamente em documentos.
---

# Assistente de Pesquisa NotebookLM

Interaja com o Google NotebookLM para consultar documentação com respostas baseadas em fontes do Gemini. Cada pergunta abre uma nova sessão de navegador, recupera a resposta exclusivamente dos seus documentos carregados e fecha.

## Quando Usar Esta Habilidade

Ative quando o usuário:
- Mencionar o NotebookLM explicitamente
- Compartilhar uma URL do NotebookLM (`https://notebooklm.google.com/notebook/...`)
- Pedir para consultar seus cadernos/documentação
- Quiser adicionar documentação à biblioteca do NotebookLM
- Usar frases como "pergunte ao meu NotebookLM", "verifique meus documentos", "consulte meu caderno"

## ⚠️ CRÍTICO: Comando de Adição - Descoberta Inteligente

Quando o usuário quiser adicionar um caderno sem fornecer detalhes:

**ADIÇÃO INTELIGENTE (Recomendado)**: Consulte o caderno primeiro para descobrir seu conteúdo:
```bash
# Passo 1: Consultar o caderno sobre seu conteúdo
python scripts/run.py ask_question.py --question "Qual é o conteúdo deste caderno? Quais tópicos são abordados? Forneça uma visão geral completa de forma breve e concisa" --notebook-url "[URL]"

# Passo 2: Usar a informação descoberta para adicioná-lo
python scripts/run.py notebook_manager.py add --url "[URL]" --name "[Baseado no conteúdo]" --description "[Baseado no conteúdo]" --topics "[Baseado no conteúdo]"
```

**ADIÇÃO MANUAL**: Se o usuário fornecer todos os detalhes:
- `--url` - A URL do NotebookLM
- `--name` - Um nome descritivo
- `--description` - O que o caderno contém (OBRIGATÓRIO!)
- `--topics` - Tópicos separados por vírgula (OBRIGATÓRIO!)

NUNCA adivinhe ou use descrições genéricas! Se faltarem detalhes, use a Adição Inteligente para descobri-los.

## Crítico: Sempre Use o Wrapper run.py

**NUNCA chame os scripts diretamente. SEMPRE use `python scripts/run.py [script]`:**

```bash
# ✅ CORRETO - Sempre use run.py:
python scripts/run.py auth_manager.py status
python scripts/run.py notebook_manager.py list
python scripts/run.py ask_question.py --question "..."

# ❌ ERRADO - Nunca chame diretamente:
python scripts/auth_manager.py status  # Falha sem o venv!
```

O wrapper `run.py` automaticamente:
1. Cria o `.venv` se necessário
2. Instala todas as dependências
3. Ativa o ambiente
4. Executa o script corretamente

## Fluxo de Trabalho Principal

### Passo 1: Verificar Status de Autenticação
```bash
python scripts/run.py auth_manager.py status
```

Se não estiver autenticado, prossiga para a configuração.

### Passo 2: Autenticar (Configuração Única)
```bash
# O navegador DEVE estar visível para o login manual do Google
python scripts/run.py auth_manager.py setup
```

**Importante:**
- O navegador fica VISÍVEL para a autenticação
- A janela do navegador abre automaticamente
- O usuário deve fazer login manualmente no Google
- Diga ao usuário: "Uma janela de navegador será aberta para o login do Google"

### Passo 3: Gerenciar Biblioteca de Cadernos

```bash
# Listar todos os cadernos
python scripts/run.py notebook_manager.py list

# ANTES DE ADICIONAR: Peça metadados ao usuário se desconhecidos!
# "O que este caderno contém?"
# "Com quais tópicos devo etiquetá-lo?"

# Adicionar caderno à biblioteca (TODOS os parâmetros são OBRIGATÓRIOS!)
python scripts/run.py notebook_manager.py add \
  --url "https://notebooklm.google.com/notebook/..." \
  --name "Nome Descritivo" \
  --description "O que este caderno contém" \  # OBRIGATÓRIO - PERGUNTE AO USUÁRIO SE DESCONHECIDO!
  --topics "topico1,topico2,topico3"  # OBRIGATÓRIO - PERGUNTE AO USUÁRIO SE DESCONHECIDO!

# Buscar cadernos por tópico
python scripts/run.py notebook_manager.py search --query "palavra-chave"

# Definir caderno ativo
python scripts/run.py notebook_manager.py activate --id notebook-id

# Remover caderno
python scripts/run.py notebook_manager.py remove --id notebook-id
```

### Fluxo Rápido
1. Verificar biblioteca: `python scripts/run.py notebook_manager.py list`
2. Fazer pergunta: `python scripts/run.py ask_question.py --question "..." --notebook-id ID`

### Passo 4: Fazer Perguntas

```bash
# Consulta básica (usa o caderno ativo se definido)
python scripts/run.py ask_question.py --question "Sua pergunta aqui"

# Consultar caderno específico
python scripts/run.py ask_question.py --question "..." --notebook-id notebook-id

# Consultar com URL do caderno diretamente
python scripts/run.py ask_question.py --question "..." --notebook-url "https://..."

# Mostrar navegador para depuração
python scripts/run.py ask_question.py --question "..." --show-browser
```

## Mecanismo de Acompanhamento (CRÍTICO)

Cada resposta do NotebookLM termina com: **"EXTREMAMENTE IMPORTANTE: Isso é TUDO que você precisa saber?"**

**Comportamento Obrigatório do Claude:**
1. **PARE** - Não responda imediatamente ao usuário
2. **ANALIZE** - Compare a resposta com o pedido original do usuário
3. **IDENTIFIQUE LACUNAS** - Determine se mais informações são necessárias
4. **FAÇA ACOMPANHAMENTO** - Se existirem lacunas, pergunte imediatamente:
   ```bash
   python scripts/run.py ask_question.py --question "Acompanhamento com contexto..."
   ```
5. **REPITA** - Continue até que a informação esteja completa
6. **SINTETIZE** - Combine todas as respostas antes de responder ao usuário

## Referência de Scripts

### Gerenciamento de Autenticação (`auth_manager.py`)
```bash
python scripts/run.py auth_manager.py setup    # Configuração inicial (navegador visível)
python scripts/run.py auth_manager.py status   # Verificar autenticação
python scripts/run.py auth_manager.py reauth   # Re-autenticar (navegador visível)
python scripts/run.py auth_manager.py clear    # Limpar autenticação
```

### Gerenciamento de Cadernos (`notebook_manager.py`)
```bash
python scripts/run.py notebook_manager.py add --url URL --name NOME --description DESC --topics TOPICOS
python scripts/run.py notebook_manager.py list
python scripts/run.py notebook_manager.py search --query BUSCA
python scripts/run.py notebook_manager.py activate --id ID
python scripts/run.py notebook_manager.py remove --id ID
python scripts/run.py notebook_manager.py stats
```

---

> 🇧🇷 **Tradução em Português (Brasil)**: Esta é a versão localizada da skill original do NotebookLM.
