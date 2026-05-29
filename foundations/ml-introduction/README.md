# Introduction to Machine Learning — Regression

## Summary

An introductory regression project that predicts apartment rental prices from property features (bathrooms, bedrooms, interest level). Trains and compares polynomial linear regression, decision tree regressor, and naive baselines on the RentHop dataset.

## Topics Covered

- Supervised vs. unsupervised learning concepts
- Regression problem formulation
- Exploratory data analysis (outlier detection, correlation analysis)
- Polynomial feature engineering
- Linear regression with polynomial features
- Decision tree regressor
- Model evaluation: R-squared, MAE, RMSE
- Naive baseline comparison

## Workflow

1. Load and inspect rental listing data (49k+ records)
2. Clean outliers using percentile-based filtering
3. Explore correlations between price, bathrooms, bedrooms, and interest level
4. Encode categorical target and engineer polynomial features (degree 10)
5. Train and evaluate polynomial linear regression
6. Train and evaluate decision tree regressor
7. Compare both models against mean/median baselines

## Tools and Libraries

Python, pandas, NumPy, matplotlib, seaborn, scikit-learn, Jupyter Notebook

## Project Structure

```
ml-introduction/
  README.md
  src/
    ml_intro.ipynb
```

## Key Learning Points

- Both ML models significantly outperform naive mean/median baselines
- Decision tree achieved lower test error (RMSE ~$1,089) than polynomial linear regression (RMSE ~$1,100)
- Number of bathrooms showed strongest correlation with price (r = 0.67)
- Using only 2 features limits predictive power — adding location, amenities, or text features would improve performance

## Dataset / Data Notes

Uses the RentHop apartment listings dataset (Kaggle Two Sigma Connect). The dataset contains 49,352 listings with 15 columns including price, room counts, building info, geographic coordinates, and text descriptions. The data file is not included in this repository.

## Notes

This is a minimal-feature baseline. Future work would incorporate additional predictors and explore more advanced models.
