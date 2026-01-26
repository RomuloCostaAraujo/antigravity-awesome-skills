---
name: power-bi-expert
description: Power BI specialist for DAX, Power Query (M), Data Modeling (Star Schema), and premium UX design. Use when: building dashboards, writing DAX measures, fixing M-code errors, designing data models, or optimizing report performance. Triggers onKeywords: [power bi, dax, power query, m-code, star schema, dashboard ux].
---

# Power BI Expert

Expert in end-to-end Business Intelligence solutions using Microsoft Power BI. This skill guides the transformation of raw data into high-performance, visually stunning insights.

## Core Capabilities

- **DAX Mastery**: Complex CALCULATE logic, Time Intelligence, and performance-tuned measures.
- **Power Query (M)**: Advanced ETL, Query Folding optimization, and dynamic data ingestion.
- **Data Modeling**: Star Schema design, RLS (Row Level Security), and relationship management.
- **UX & Visual Design**: Premium dashboard layouts, accessibility, and high-impact data storytelling.

## Workflow

### 1. Data Prep (Power Query)
- Use [references/power_query_recipes.md](references/power_query_recipes.md) for cleaning and transforming data.
- Ensure Query Folding is active for SQL sources.

### 2. Modeling
- Follow [references/modeling_ux.md](references/modeling_ux.md) for Star Schema principles.
- Use integers for keys and hide them from users.

### 3. DAX Implementation
- Reference [references/dax_patterns.md](references/dax_patterns.md) for standard measures.
- Always use VARIABLES (`VAR`) for clarity and performance.

### 4. Design & UX
- Apply Gestalt principles and grid-based layouts from [references/modeling_ux.md](references/modeling_ux.md).
- Ensure 100% accessibility compliance.

## Performance Checklist
- ✅ No bi-directional filters (unless critical).
- ✅ Minimal calculated columns (prefer Measures).
- ✅ Star schema (Dimensions and Facts clearly separated).
- ✅ Indented DAX and M code for readability.
