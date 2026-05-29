# Model Validation Strategies

## Summary

An exploration of model validation methodology. This project focuses on designing a trustworthy evaluation pipeline — implementing custom train/test splits, cross-validation methods, feature selection techniques, and hyperparameter optimization from scratch, then comparing each against scikit-learn equivalents.

## Problem

A model's reported quality is only as reliable as the validation strategy behind it. Optimistic results can come from incorrect data splits, future information leaking into training, grouped data appearing in both train and test sets, or feature selection done unfairly. This project treats evaluation pipeline design as the primary problem, not just model training.

## Approach

- Use the Kaggle Two Sigma rent-hop dataset (apartment listings with price as target)
- Implement custom split methods: random, date-based, and deterministic
- Implement custom cross-validation: K-Fold, Group K-Fold, Stratified K-Fold, Time Series split
- Validate each implementation against scikit-learn's equivalents
- Apply feature selection: Lasso coefficients, nan-ratio + correlation filter, permutation importance, SHAP
- Optimize hyperparameters on ElasticNet using Grid Search, Random Search, and Optuna (Bayesian)

## Workflow

1. Load and clean the dataset (parse features, create binary amenity columns, handle timestamps)
2. Implement and test custom random and date-based train/val/test splits
3. Implement custom K-Fold, Group K-Fold, Stratified K-Fold, and TimeSeriesSplit
4. Compare all custom CV methods against sklearn equivalents (fold sizes, feature distributions, group separation)
5. Select the most appropriate validation scheme for the dataset
6. Run feature selection with 4 different methods (Lasso, filter, permutation, SHAP)
7. Tune ElasticNet hyperparameters via Grid Search, Random Search, and Optuna
8. Compare all tuning approaches on validation and test sets

## Tools and Libraries

- Python, pandas, NumPy
- scikit-learn (pipelines, metrics, model comparison)
- SHAP (feature importance)
- Optuna (hyperparameter optimization)
- Jupyter Notebook

## Project Structure

```
validation/
├── README.md
├── requirements.txt
└── src/
    └── Validation.ipynb
```

## Results

- The custom K-Fold, Group K-Fold, Stratified K-Fold, and TimeSeriesSplit implementations matched sklearn's behavior closely, with minor differences in fold balance for Group K-Fold due to group-level splitting.
- Time-based validation was identified as the most appropriate scheme for this dataset (chronological listing data).
- Lasso-based feature selection (top 10 features) preserved comparable validation MAE to the full 22-feature set.
- Optuna achieved the best test MAE among tuning methods, demonstrating the value of Bayesian optimization over exhaustive or random search.

## Dataset

Kaggle: Two Sigma Connect — Rental Listing Inquiries. The dataset contains apartment rental listings with price, location, amenity features, and interest level. Data is not included in this repository.

## Notes

- Notebook: `src/Validation.ipynb`
- The dataset (`train.json`) must be placed in a `data/` directory at the project root before running the notebook.
- This project prioritizes evaluation methodology over model performance — the goal is fair and reproducible results, not the lowest possible error.
