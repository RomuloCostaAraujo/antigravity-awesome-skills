# DAX Best Practices and Patterns

Use these patterns to implement high-performance, maintainable DAX measures.

## Core Principles

- **CALCULATE is King**: Understand context transition.
- **Variables are Essential**: Use VAR for readability and performance (prevents multiple evaluations).
- **Measure Branching**: Build complex measures on top of simple base measures.
- **Star Schema First**: Optimize the model before complicating the DAX.

## Common Patterns

### Time Intelligence

```dax
-- Total Sales YTD
Sales YTD = 
CALCULATE(
    [Total Sales],
    DATESYTD( 'Date'[Date] )
)

-- Previous Year Sales
Sales PY = 
CALCULATE(
    [Total Sales],
    SAMEPERIODLASTYEAR( 'Date'[Date] )
)

-- % Growth YoY
Growth YoY % = 
VAR SalesBase = [Total Sales]
VAR SalesPrev = [Sales PY]
RETURN
DIVIDE( SalesBase - SalesPrev, SalesPrev, 0 )
```

### Formatting Best Practices

- Use `DIVIDE(num, den, alt)` instead of `/` to handle division by zero.
- Keep measures in logic-based folders.
- Avoid using calculated columns for aggregations; use Measures instead.

## Performance Tuning

- **Use KEEPFILTERS**: Preserves original filter context when applying additional filters.
- **Avoid Filter(All(...))**: Use `REMOVEFILTERS` or `ALL` inside `CALCULATE` directly.
- **Minimize Iterator Functions**: Be careful with `SUMX`, `AVERAGEX` over large tables.
