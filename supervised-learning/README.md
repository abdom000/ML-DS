# Linear Regression and Regularization

## Summary

A supervised learning project focused on linear regression models, custom implementations of core preprocessing techniques, and the effects of regularization and polynomial feature expansion. Built on a Kaggle rental listings dataset.

## Problem

Given apartment rental listings with numeric and categorical features, predict the rental price. The project compares multiple linear models, scaling strategies, and feature expansions to understand how each affects prediction quality and model stability.

## Approach

- Build a 22-feature dataset from the top 20 amenities plus bathrooms and bedrooms
- Implement custom MinMaxScaler and StandardScaler from scratch, compare to sklearn
- Implement custom SGD-based Linear Regression from scratch, compare to sklearn
- Train Linear Regression, Ridge, Lasso, and ElasticNet with both scalers
- Expand features with polynomial degree=10 to demonstrate overfitting and the effect of regularization
- Report MAE, RMSE, and R² for all configurations

## Workflow

1. Load rental listings data and parse the amenities column
2. Engineer binary features from the top 20 most common amenities
3. Implement custom MinMaxScaler and StandardScaler
4. Implement custom Linear Regression using SGD
5. Train sklearn linear models (Linear, Ridge, Lasso, ElasticNet) on scaled features
6. Compare custom scalers and custom SGD against sklearn equivalents
7. Apply polynomial features (degree=10) and retrain all models
8. Summarize all results in comparison tables

## Tools and Libraries

- Python, pandas, NumPy
- scikit-learn (Linear, Ridge, Lasso, ElasticNet, PolynomialFeatures, metrics)
- Jupyter Notebook

## Project Structure

```
supervised-learning/
├── README.md
├── requirements.txt
└── src/
    └── Linear_Regression.ipynb
```

## Results

- Ridge with polynomial features (degree=10) achieved the lowest test MAE (~1,327).
- ElasticNet with MinMax scaling showed the most stable train/test behavior and the best test R² among scaled linear models.
- Custom scalers matched sklearn's output within floating-point precision.
- Custom SGD Linear Regression converged to results comparable to sklearn's closed-form solution.
- RMSE remained high across all models due to extreme price outliers in the dataset.

## Key Learning Points

- How L1 (Lasso) and L2 (Ridge) regularization affect coefficient magnitudes and feature selection
- How polynomial expansion increases model flexibility but risks overfitting
- How regularization controls overfitting in high-degree polynomial models
- How custom scaling and gradient descent implementations compare to production library code

## Dataset

Kaggle: Two Sigma Connect — Rental Listing Inquiries. Data is not included in this repository.

## Notes

- Notebook: `src/Linear_Regression.ipynb`
- Place `train.json` in a `data/` directory before running the notebook.
- This project focuses on understanding linear models end-to-end, not on achieving the lowest possible error.
