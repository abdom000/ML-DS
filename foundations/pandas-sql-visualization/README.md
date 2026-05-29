# Data Visualization — pandas, Matplotlib, Seaborn, Plotly

## Summary

A ten-exercise tutorial on data visualization techniques using matplotlib, seaborn, and plotly. Sources data from a SQLite database of user activity logs to create line charts, bar charts, histograms, boxplots, scatter matrices, heatmaps, and animated plots.

## Topics Covered

- Line charts with matplotlib (single and multi-series)
- Bar charts (stacked, grouped, average comparisons)
- Histograms and distribution overlays
- Boxplots for group comparison (A/B test analysis)
- Scatter matrix for multi-dimensional relationships
- Heatmaps (weekday × hour commit patterns)
- Seaborn line plots with hue-based grouping
- Plotly animated frames and interactive controls

## Workflow

1. Connect to SQLite and load pageview/commit data
2. Plot daily view counts as line charts
3. Compare views and commits on styled multi-series charts
4. Analyze commit timing by time of day (stacked bars)
5. Compare weekday vs. weekend commit patterns (bar charts and histograms)
6. Visualize A/B test results with boxplots
7. Explore correlations across avg_diff, pageviews, and commits (scatter matrix)
8. Build a weekday × hour heatmap of commit activity
9. Track project1 leaderboard dynamics with seaborn
10. Create an animated plotly visualization of cumulative progress

## Tools and Libraries

Python, pandas, NumPy, matplotlib, seaborn, plotly, SQLite3, Jupyter Notebook

## Project Structure

```
pandas-sql-visualization/
  README.md
  src/
    ex00/00_line_chart.ipynb
    ex01/01_line_chart_styles.ipynb
    ex02/02_bar_chart.ipynb
    ex03/03_bar_charts.ipynb
    ex04/04_histogram.ipynb
    ex05/05_boxplot.ipynb
    ex06/06_scatter_matrix.ipynb
    ex07/07_heatmap.ipynb
    ex08/08_seaborn.ipynb
    ex09/09_plotly.ipynb
```

## Key Learning Points

- Most user commits occur in the evening and afternoon — peak at Thursday 9 PM (~28.8 avg commits)
- Weekend commits exceed weekday commits most during hours 11–13 and 22–23
- No strong linear relationship exists between pageviews, commits, and commit timing
- `user_4` led the project1 commit leaderboard almost the entire period
- Plotly animations effectively communicate temporal dynamics that static charts miss

## Dataset / Data Notes

Uses the `checking-logs.sqlite` database (pageviews, checker, deadlines tables) and an `ab-test.csv` file. The SQLite database captures user activity from an educational platform. These data files are not included in this repository.

## Notes

Notebooks were adapted from an educational SQL → visualization workflow. The exercise numbering reflects the original progression. No statistical hypothesis testing was applied to the A/B analysis — the boxplots in ex05 are purely descriptive.
