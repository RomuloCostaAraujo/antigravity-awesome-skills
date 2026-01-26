# Modeling and UX Best Practices

## Data Modeling (Star Schema)

- **One-to-Many Relationships**: The standard for Power BI. Avoid Many-to-Many if possible.
- **Avoid Bi-directional Filters**: Use them only when absolutely necessary (e.g., specific security scenarios) as they kill performance and cause ambiguity.
- **Integer Keys**: Use integers for relationship keys between Factor and Dimension tables for faster joins.
- **Hide Keys**: Hide ID/Key columns from the report view to reduce clutter for users.

## UX & Visualization (The "WOW" Factor)

### Layout & Composition

- **F-Pattern**: Users scan from top-left. Place the most important KPIs there.
- **White Space**: Don't cram visuals. Leave "breathing room" between charts.
- **Grid Alignment**: Always use the "Snap to Grid" feature for a premium look.

### Color Theory

- **Color Inclusivity**: Use color-blind friendly palettes.
- **Semantic Colors**: Blue for Positive, Red for Negative, Gray for Background/Neutral.
- **Minimalism**: Use a maximum of 3 key colors + shades of gray.

### Accessibility

- **Alt Text**: Add descriptions to all visuals.
- **Tab Order**: Ensure the tab order follows the logical flow of the report.
- **Contrast**: High contrast (Ratio 4.5:1) for text elements.
- **Tooltips**: Use Report Page Tooltips for "Deep Dive" info without cluttering the main view.
