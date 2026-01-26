---
name: git-pushing-ptbr
description: Adiciona, commita e envia (push) alterações do git com mensagens de commit convencionais. Use quando o usuário quiser commitar e enviar mudanças, mencionar envio para o remoto, ou pedir para salvar o trabalho. Também ativado por frases como "push changes", "commit and push", "enviar para o github".
---

# Fluxo de Git Push

Adicione todas as alterações, crie um commit convencional e envie para o branch remoto.

## Quando Usar

Ativa automaticamente quando o usuário:

- Pede explicitamente para enviar alterações ("push", "commit e push", "enviar isso")
- Menciona salvar o trabalho no remoto ("salvar no github", "enviar para o remoto")
- Finaliza uma funcionalidade e quer compartilhá-la
- Diz frases como "vamos subir isso" ou "commita essas mudanças"

## Fluxo de Trabalho

**SEMPRE use o script** - NÃO use comandos manuais de git:

```bash
bash skills/git-pushing/scripts/smart_commit.sh
```

Com mensagem personalizada:

```bash
bash skills/git-pushing/scripts/smart_commit.sh "feat: adicionar nova funcionalidade"
```

O script gerencia: staging (git add), mensagem de commit convencional, rodapé do Claude, e o push com a flag `-u`.
