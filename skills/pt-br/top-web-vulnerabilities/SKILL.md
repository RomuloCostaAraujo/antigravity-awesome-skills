---
name: top-web-vulnerabilities-ptbr
description: Use para identificar vulnerabilidades web, explicar falhas comuns, entender o OWASP Top 10 e aprender sobre ataques de injeção, controle de acesso e segurança de APIs.
---

# Referência das Principais Vulnerabilidades Web (OWASP)

## Objetivo

Fornecer uma referência estruturada para as vulnerabilidades web mais críticas, alinhada com os padrões do OWASP Top 10. Ajuda na identificação, avaliação de impacto e estratégias de mitigação.

---

## Categorias de Vulnerabilidades (OWASP 2021)

### A01: Quebra de Controle de Acesso
- **Definição**: Usuários podem acessar recursos fora de suas permissões pretendidas.
- **Exemplo**: IDOR (Referência Direta Insegura a Objetos) - acessar `perfil/123` em vez de `meu-perfil`.
- **Mitigação**: Aplicar o princípio do privilégio mínimo; negar por padrão.

### A02: Falhas Criptográficas
- **Definição**: Exposição de dados sensíveis devido à falta ou fraqueza na criptografia.
- **Exemplo**: Senhas armazenadas em texto simples ou uso de algoritmos antigos como MD5.
- **Mitigação**: Usar protocolos modernos (TLS 1.2+), hashes fortes (Argon2, bcrypt) e desabilitar protocolos inseguros.

### A03: Injeção
- **Definição**: Dados fornecidos pelo usuário são interpretados como parte de um comando ou consulta.
- **Tipos**: SQL Injection, Command Injection, XSS (Cross-Site Scripting).
- **Mitigação**: Usar consultas parametrizadas (Prepared Statements); codificar a saída; validar entradas.

### A04: Design Inseguro
- **Definição**: Falhas na arquitetura e design do sistema que não podem ser corrigidas apenas com implementação perfeita.
- **Exemplo**: Recuperação de senha baseada em perguntas de segurança previsíveis.
- **Mitigação**: Implementar modelagem de ameaças no início do desenvolvimento.

### A05: Configurações Inseguras
- **Definição**: Servidores ou aplicações mal configurados (senhas padrão, cabeçalhos faltando).
- **Exemplo**: Página de admin com credenciais `admin/admin` ou erros detalhados expostos em produção.
- **Mitigação**: Autenticação reforçada em todas as interfaces; remover funcionalidades não utilizadas.

### A06: Componentes Vulneráveis e Desatualizados
- **Definição**: Uso de bibliotecas, frameworks ou SO com vulnerabilidades conhecidas.
- **Mitigação**: Manter um inventário de dependências e atualizar patches de segurança constantemente.

### A07: Falhas de Identificação e Autenticação
- **Definição**: Problemas no login, sessões ou proteção contra força bruta.
- **Mitigação**: Implementar MFA (Autenticação de Múltiplos Fatores); políticas de senha forte.

### A08: Falhas na Integridade de Dados e Software
- **Definição**: Código ou dados modificados durante o envio ou armazenamento sem validação.
- **Exemplo**: Deserialização insegura de objetos (Remote Code Execution).
- **Mitigação**: Assinaturas digitais; validar integridade de atualizações.

### A09: Falhas nos Logs e Monitoramento
- **Definição**: Falta de visibilidade sobre incidentes de segurança, impedindo a detecção de ataques em curso.
- **Mitigação**: Registrar logins, falhas de acesso e atividades de alto risco com alertas automáticos.

### A10: SSRF (Server-Side Request Forgery)
- **Definição**: Aplicação web faz requisições a URLs fornecidas pelo usuário sem validação.
- **Impacto**: Acesso a redes internas ou metadados de serviços na nuvem (AWS/Azure).
- **Mitigação**: Whitelist de domínios; desabilitar redirecionamentos automáticos no servidor.

---

## Cabeçalhos de Segurança Críticos

```http
Content-Security-Policy: default-src 'self'
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
Strict-Transport-Security: max-age=31536000
```

> **Habilidade Relacionada**: Use `@depuracao-sistematica` para investigar causas raiz de falhas de segurança.
