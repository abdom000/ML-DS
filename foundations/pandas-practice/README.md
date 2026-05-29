# Pandas Practice — Data Wrangling and Optimization

## Summary

A six-exercise progression through core pandas operations: file I/O, datetime handling, preprocessing, filtering and aggregation, enrichment (joins and pivot tables), and performance optimization. Demonstrates end-to-end data wrangling on a car fines and ownership dataset.

## Topics Covered

- Reading and writing tabular data (CSV, JSON, log files)
- Datetime parsing and component extraction
- Categorical binning with `pd.cut`
- Missing value detection and treatment (dropna, fillna, ffill)
- Duplicate detection and removal
- Boolean filtering and selection
- Grouped aggregations (median, count, min, max, std)
- Multi-table joins (inner merge)
- Pivot tables
- Vectorized vs. iterative computation (for-loop, iterrows, apply, Series ops, .values)
- Memory optimization (downcasting, categorical dtype)

## Workflow

1. Load tab-separated log files with custom headers and row skipping
2. Parse datetimes, extract components, bin hours into daytime categories
3. Clean auto dataset: drop duplicates, handle missing values, split compound columns
4. Filter and aggregate by make, model, and car number
5. Enrich data with random owner surnames, build pivot tables
6. Benchmark 5 computation methods and optimize memory footprint

## Tools and Libraries

Python, pandas, NumPy, Jupyter Notebook

## Project Structure

```
pandas-practice/
  README.md
  src/
    ex00/load_and_save.ipynb
    ex01/basic_operations.ipynb
    ex02/preprocessing.ipynb
    ex03/selects_n_aggs.ipynb
    ex04/enrichment.ipynb
    ex05/optimizations.ipynb
```

## Key Learning Points

- Vectorized pandas operations are ~40x faster than for-loops and ~10x faster than `apply`
- Converting object columns to `category` dtype reduced memory by ~50%
- `pd.cut()` enables clean continuous-to-categorical binning
- `ffill()` and mean-imputation are complementary strategies for different missing-data patterns
- Multi-table enrichment via merge/pivot unlocks cross-domain analysis

## Dataset / Data Notes

The project uses synthetic car fine records and a US surname dataset. Data files are included as artifacts of the exercises but are not the focus of this portfolio. The original log files (`feed-views.log`, `auto.csv`, `surname.json`) are local samples and are not required to understand the notebook logic.

## Notes

The exercises increase in complexity from basic file loading to advanced performance tuning. Each notebook is self-contained and can be run independently.
