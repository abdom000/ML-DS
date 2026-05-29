# Decision Trees and Ensemble Models for Bad Buy Prediction

## Summary

A tree-based classification project that implements a Decision Tree, Random Forest, and GBDT from scratch, then compares them against scikit-learn baselines and modern boosting libraries (XGBoost, LightGBM, CatBoost) on the Kaggle Don't Get Kicked dataset. Uses time-aware validation to prevent data leakage.

## Problem

Predict whether a vehicle purchased at auction is a bad buy (`IsBadBuy`). The dataset includes vehicle attributes, auction metadata, pricing, and warranty information. Because the data spans multiple years, a chronological split is used instead of random sampling to simulate real-world deployment conditions.

## Approach

- Split chronologically by `PurchDate`: oldest 33% for training, middle 33% for validation, newest 33% for testing
- Build preprocessing pipelines for numeric (median imputation) and categorical (most-frequent imputation + one-hot encoding) features
- Train a scikit-learn Decision Tree as a baseline
- Implement a custom Decision Tree from scratch using Gini impurity
- Extend into a custom Random Forest and a custom GBDT
- Compare against XGBoost, LightGBM, and CatBoost
- Evaluate using ROC AUC and Gini coefficient

## Workflow

1. Load and sort data by purchase date
2. Split into train, validation, and test chronologically
3. Preprocess numeric and categorical features
4. Train sklearn Decision Tree baseline
5. Implement and train custom Decision Tree, Random Forest, and GBDT
6. Train XGBoost, LightGBM, and CatBoost
7. Compare all models on validation set
8. Evaluate the best model on the test set

## Tools and Libraries

- Python, pandas, NumPy
- scikit-learn (pipelines, metrics, baselines)
- XGBoost, LightGBM, CatBoost
- Jupyter Notebook

## Project Structure

```
decision-trees/
├── README.md
├── requirements.txt
└── src/
    └── decision_trees.ipynb
```

## Results

| Model | Validation Gini |
|---|---|
| XGBoost | 0.3790 |
| LightGBM | 0.3678 |
| CatBoost | 0.3422 |
| Sklearn Random Forest | 0.3172 |
| Custom GBDT | 0.2991 |
| Sklearn Decision Tree | 0.2950 |
| Custom Random Forest | 0.2875 |
| Custom Decision Tree | 0.2721 |

- XGBoost achieved the best validation Gini (0.3790) and generalized well to the test set (Gini 0.3876).
- Ensemble methods consistently outperformed single trees.
- Custom implementations helped build intuition for how tree-based models work internally.
- Modern boosting libraries significantly outperformed the custom implementations, as expected from optimized, production-grade systems.

## Dataset

Kaggle competition: Don't Get Kicked. Data is not included in this repository.

## Notes

- Notebook: `src/decision_trees.ipynb`
- Download the Kaggle dataset and place `training.csv` in a `data/` directory before running.
- Custom implementations are educational — they demonstrate core concepts but are not optimized for production performance.
