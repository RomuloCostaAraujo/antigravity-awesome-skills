# Diretrizes de Performance & UX para Power BI

Este documento serve como referência técnica para o **Power BI Analyst** ao realizar auditorias e edições em projetos PBIP.

## 1. Checklist de Performance (Motor VertiPaq)

### Modelagem de Dados
- **Star Schema**: Use sempre Fatos (longas e estreitas) e Dimensões (curtas e largas).
- **Cardinalidade**: Identifique colunas com alta cardinalidade (IDs, carimbos de data/hora com segundos) e avalie se são realmente necessárias.
- **Tipos de Dados**: Prefira números inteiros para chaves de relacionamento.
- **Auto Date/Time**: Desabilite a opção "Data/hora automática" globalmente para reduzir o tamanho do modelo.

### DAX
- **Variáveis (VAR)**: Use variáveis para evitar cálculos repetidos e melhorar a legibilidade.
- **Iterator Functions**: Use `SUMX`, `AVERAGEX` apenas quando necessário realizar cálculos linha a linha.
- **KEEPFILTERS**: Use `KEEPFILTERS` em vez de sobrescrever contextos de filtro desnecessariamente.
- **Medidas vs Colunadas Calculadas**: Sempre prefira Medidas. Use Colunas Calculadas apenas para categorizações fixas que serão usadas como filtros/eixos.

### Power Query (M)
- **Query Folding**: Garanta que o maior número possível de etapas seja "dobrado" para a fonte de dados (SQL).
- **Remover Colunas**: Remova todas as colunas desnecessárias logo no início do processo de ETL.
- **Granularidade**: Agregue os dados na fonte ou no Power Query se o nível de detalhe não for necessário para a análise.

---

## 2. Checklist de User Experience (UX)

### Design Visual & Storytelling
- **Gestalt**: Agrupe elementos relacionados (filtros de um lado, KPIs do outro).
- **Hierarquia Visual**: O KPI principal deve ser o elemento mais proeminente da página.
- **Grids**: Use layouts baseados em grade (ex: 8px ou 12px) para manter o alinhamento perfeito.
- **Cores**: Use uma paleta de cores limitada e consistente. Evite o "efeito arco-íris". Use cores para destacar (ex: vermelho para metas não atingidas).

### Interatividade & Acessibilidade
- **Tooltips Personaizados**: Use tooltips para fornecer detalhes sem poluir o visual principal.
- **Navegação**: Use botões e bookmarks para criar fluxos de navegação claros entre as páginas.
- **Títulos & Labels**: Títulos devem ser descritivos e responder à pergunta: "O que este gráfico está me dizendo?".
- **Padrão Z de Leitura**: Posicione as informações mais importantes no canto superior esquerdo (onde a leitura começa).

---

## 3. Guia de Edição PBIP

Ao editar arquivos do projeto diretamente (`.pbip`), siga estas precauções:

- **model.bim**: O coração do modelo. Edite descrições, sinônimos e medidas aqui para aplicação em lote.
- **report.json**: Contém a definição visual. Útil para substituir fontes, cores ou ajustar coordenadas de visuais programaticamente.
- **diagramLayout.json**: Útil para limpar a visão de diagrama do modelo caso esteja bagunçada.

> [!IMPORTANT]
> Sempre faça um backup ou commit em Git antes de editar arquivos PBIP manualmente.
