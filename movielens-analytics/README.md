# MovieLens Analytics — OOP Data Analysis

## Summary

An object-oriented analysis of the MovieLens dataset using custom Python classes. The project demonstrates clean software design in a data science context — each data domain (movies, ratings, tags, links) is encapsulated in its own class with focused analytical methods.

## Problem

Analyze a sample of the MovieLens dataset to answer questions about movie release trends, genre distributions, rating patterns, user behavior, tag characteristics, and external metadata (budget, director, profitability). The goal is to build a reusable, modular analysis library rather than a one-off script.

## Approach

- Design four independent classes: `Movies`, `Ratings`, `Tags`, `Links`
- Each class loads its data from CSV and provides query methods (distributions, top-N rankings, aggregations)
- The `Links` class connects to external IMDB-style data (director, budget, runtime, gross)
- A notebook demonstrates every method with execution time measurements
- A `Tests` class validates the module

## Workflow

1. Load 1000-record MovieLens sample (movies, ratings, tags, links)
2. Analyze movies by release year and genre distribution
3. Analyze ratings from both movie and user perspectives
4. Analyze tags by length, frequency, and word count
5. Query external links data (top directors, most expensive, most profitable)
6. Measure execution time for each method group

## Tools and Libraries

- Python (OOP, csv, collections, requests)
- BeautifulSoup (web scraping for IMDB data)
- Jupyter Notebook

## Project Structure

```
movielens-analytics/
├── README.md
├── requirements.txt
└── src/
    ├── movielens_analysis.py
    ├── movielens_report.ipynb
    ├── movies.py
    ├── ratings.py
    ├── tags.py
    ├── links.py
    ├── movies_1000.csv
    ├── ratings_1000.csv
    ├── tags_1000.csv
    └── links_1000.csv
```

## Results

- Movies dataset spans 1939–1996; Drama (522) and Comedy (355) are the dominant genres.
- Ratings are concentrated in the 3.5–4.0 range; the most controversial movie (highest rating variance) is movieId 33166.
- The top 10 most popular tags include "In Netflix queue", "seen", and "DVD".
- Links class successfully retrieves external metadata: budgets, directors, and profitability.

## Dataset

MovieLens 1000-record sample (subset of the full MovieLens dataset). Sample CSV files are included in `src/`.

## Notes

- Notebook: `src/movielens_report.ipynb`
- This project emphasizes object-oriented design for data analysis workflows.
- The `Tests` class in `movielens_analysis.py` provides unit test coverage for core methods.
- IMDB-style data retrieval uses a synthetic fallback when web fetching is disabled.
