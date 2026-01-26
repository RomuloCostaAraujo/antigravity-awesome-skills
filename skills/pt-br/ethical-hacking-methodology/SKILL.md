---
name: ethical-hacking-methodology-ptbr
description: Use quando o usuário pedir para "aprender hacking ético", "entender o ciclo de vida do pentest", "realizar reconhecimento", "conduzir varredura de segurança", "explorar vulnerabilidades" ou "escrever relatórios de pentest". Fornece metodologia e técnicas abrangentes.
---

# Metodologia de Hacking Ético

## Objetivo

Dominar o ciclo de vida completo do teste de invasão (pentest), do reconhecimento ao relatório. Esta habilidade cobre as cinco etapas da metodologia, ferramentas essenciais, técnicas de ataque e relatórios profissionais para avaliações de segurança autorizadas.

## Pré-requisitos

### Ambiente Necessário
- Kali Linux instalado (persistente ou live)
- Acesso à rede para os alvos autorizados
- Autorização por escrito do proprietário do sistema

### Conhecimento Necessário
- Conceitos básicos de redes
- Proficiência na linha de comando Linux
- Entendimento de tecnologias web
- Familiaridade com conceitos de segurança

## Entregáveis

1. **Relatório de Reconhecimento** - Informações coletadas sobre o alvo
2. **Avaliação de Vulnerabilidades** - Fraquezas identificadas
3. **Evidência de Exploração** - Provas de conceito de ataques
4. **Relatório Final** - Descobertas executivas e técnicas

## Fluxo de Trabalho Principal

### Fase 1: Entendendo os Tipos de Hackers

Classificação dos profissionais de segurança:

**White Hat (Hacker Ético)**
- Profissionais de segurança autorizados.
- Realizam testes com permissão.
- Objetivo: Identificar e corrigir vulnerabilidades.

**Black Hat (Cibercriminoso)**
- Intrusões não autorizadas.
- Motivados por lucro, vingança ou notoriedade.
- Objetivo: Roubar dados, causar danos.

**Grey Hat (Hacker Híbrido)**
- Pode cruzar fronteiras éticas.
- Не é necessariamente malicioso, mas pode quebrar regras.
- Frequentemente divulga vulnerabilidades publicamente.

### Fase 2: Reconhecimento

Coleta de informações sem interação direta com o sistema:

**Reconhecimento Passivo**
```bash
# WHOIS lookup
whois alvo.com

# Enumeração DNS
nslookup alvo.com
dig alvo.com ANY
dig alvo.com MX

# Descoberta de subdomínios
dnsrecon -d alvo.com

# Coleta de e-mails
theHarvester -d alvo.com -b all
```

**Google Hacking (OSINT)**
- `site:alvo.com filetype:pdf` (Encontrar arquivos expostos)
- `site:alvo.com intitle:"index of"` (Encontrar listagem de diretórios)
- `site:alvo.com inurl:login` (Encontrar páginas de login)

### Fase 3: Varredura (Scanning)

Enumeração ativa dos sistemas alvo:

**Descoberta de Hosts**
```bash
# Varredura de ping
nmap -sn 192.168.1.0/24

# ARP scan (rede local)
arp-scan -l
```

**Varredura de Portas**
```bash
# Varredura SYN (stealth)
nmap -sS alvo.com

# Versão de serviços e SO
nmap -sV -O alvo.com

# Varredura agressiva
nmap -A alvo.com
```

### Fase 4: Análise de Vulnerabilidades

Identificar fraquezas exploráveis:

- **Automação**: `nikto -h http://alvo.com`
- **Manual**: `gobuster dir -u http://alvo.com -w /usr/share/wordlists/dirb/common.txt`

### Fase 5: Exploração

Explorar ativamente as vulnerabilidades descobertas:

**Metasploit Framework**
```bash
msfconsole
msf> search type:exploit name:smb
msf> use exploit/windows/smb/ms17_010_eternalblue
msf> set RHOSTS alvo.com
msf> exploit
```

### Fase 6: Pós-Exploração e Manutenção de Acesso

Garantir acesso persistente e escalonamento de privilégios:
- **Persistência**: Criar backdoors ou usuários ocultos.
- **Escalonamento**: `sudo -l`, busca por binários SUID.

### Fase 7: Relatórios

Documentação profissional das descobertas:
1. **Sumário Executivo**: Visão de alto nível para gestores.
2. **Descobertas Técnicas**: Evidências, prints e detalhes.
3. **Recomendações**: Como corrigir cada falha.

---

## Guia Rápido de Referência

| Estágio | Propósito | Ferramentas |
|-------|---------|-----------|
| Reconhecimento | Coleta de dados | theHarvester, WHOIS |
| Varredura | Enumerar alvos | Nmap, Nikto, Gobuster |
| Exploração | Obter acesso | Metasploit, SQLMap |
| Relatório | Documentar | Templates de Relatório |

> 🔴 **AVISO LEGAL:** Testes de invasão sem autorização prévia por escrito são ilegais. Use este conhecimento apenas para fins éticos e profissionais.
