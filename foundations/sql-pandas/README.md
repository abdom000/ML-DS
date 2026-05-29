# SQL + Pandas — Querying and Analysis with SQLite

## Summary

A five-exercise series bridging SQL and pandas for data analysis. Uses SQLite to query user activity logs (pageviews, commit checkers, deadlines), progressively building from basic SELECT statements to multi-table joins, CTEs, aggregations, and an A/B test framework.

## Topics Covered

- SQLite connection and schema inspection (`PRAGMA table_info`)
- `SELECT`, `WHERE`, `LIKE`, `ORDER BY`
- `LEFT JOIN` and multi-table relationships
- `GROUP BY` with aggregation functions
- CTEs (`WITH` clause)
- Date/time arithmetic with `julianday`
- Loading SQL query results into pandas DataFrames
- Correlation analysis in pandas
- A/B test group classification (test vs. control)
- Conditional aggregation (`HAVING SUM(...)`)

## Workflow

1. Query pageviews and checker tables with basic filtering
2. Inspect table schemas and preview data
3. Build a datamart via LEFT JOIN and GROUP BY, creating test/control splits
4. Analyze commit timing relative to deadlines using aggregations and CTEs
5. Compute correlations between pageviews and commit behavior
6. Classify commits as before/after first pageview and compare groups

## Tools and Libraries

Python, pandas, SQLite3, Jupyter Notebook

## Project Structure

```
sql-pandas/
  README.md
  src/
    ex00/ex00_first_select.ipynb
    ex01/ex01_subquery.ipynb
    ex02/ex02_joins.ipynb
    ex03/ex03_aggs.ipynb
    ex04/ex04_ab-test.ipynb
```

## Key Learning Points

- SQL and pandas integrate seamlessly via `pd.io.sql.read_sql()` — the best of both worlds
- A weak negative correlation (r = -0.28) was found between pageviews and commit earliness
- Users who viewed pages before committing had different timing patterns than those who did not
- CTEs make complex analytical queries readable and maintainable
- Building test/control groups in SQL enables clean A/B analysis preparation

## Dataset / Data Notes

Uses the `checking-logs.sqlite` database containing `pageviews`, `checker`, and `deadlines` tables. This database logs user pageview events, lab checking activity, and assignment deadlines. The database file is not included in this repository.

## Notes

Exercises build sequentially — later notebooks depend on tables created in earlier ones (e.g., `datamart`, `test`, `control` tables from ex02 are used in ex03 and ex04).
