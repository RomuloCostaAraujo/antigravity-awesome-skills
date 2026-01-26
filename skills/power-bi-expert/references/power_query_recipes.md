# Power Query (M) Recipes

Use these snippets for robust ETL transformations.

## General Formatting

- **Indentation**: Standard M indentation for steps.
- **Step Naming**: Avoid spaces in step names (`Source` vs `#"Filtered Rows"`).

## Common Snippets

### Date Table Generator

```m
let
    StartDate = #date(2020, 1, 1),
    EndDate = Date.From(DateTime.LocalNow()),
    DayCount = Duration.Days(Duration.From(EndDate - StartDate)) + 1,
    Source = List.Dates(StartDate, DayCount, #duration(1, 0, 0, 0)),
    #"Converted to Table" = Table.FromList(Source, Splitter.SplitByNothing(), null, null, ExtraValues.Error),
    #"Renamed Columns" = Table.RenameColumns(#"Converted to Table",{{"Column1", "Date"}}),
    #"Changed Type" = Table.TransformColumnTypes(#"Renamed Columns",{{"Date", type date}}),
    #"Inserted Year" = Table.AddColumn(#"Changed Type", "Year", each Date.Year([Date]), Int64.Type),
    #"Inserted Month" = Table.AddColumn(#"Inserted Year", "Month", each Date.Month([Date]), Int64.Type),
    #"Inserted Month Name" = Table.AddColumn(#"Inserted Month", "Month Name", each Date.MonthName([Date]), type text)
in
    #"Inserted Month Name"
```

### Optimization

- **Buffer for Performance**: Use `Table.Buffer` or `List.Buffer` when referencing the same sub-set multiple times.
- **Query Folding**: Ensure steps "fold" to the source database whenever possible (Filter, SelectColumns).
- **Avoid Hardcoding**: Use Parameters (Power Query Parameters) for server names and file paths.
