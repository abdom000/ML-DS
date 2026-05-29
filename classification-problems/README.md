# Binary Classification — Car Auction Bad Buy Prediction

## Summary

A binary classification project that predicts whether a purchased vehicle is a bad buy using the Kaggle Don't Get Kicked dataset. The project implements three classifiers from scratch (KNN, Gaussian Naive Bayes, Logistic Regression) and compares them against scikit-learn baselines, with time-aware validation to prevent data leakage.

## Problem

Vehicle auctions involve risk — some purchased cars turn out to be bad buys (defective, overpriced, or unsellable). The goal is to predict the binary `IsBadBuy` flag using vehicle attributes, auction metadata, pricing, and warranty information. The dataset spans multiple years, so a chronological split is used to avoid training on future data.

## Approach

- Split the dataset chronologically by `PurchDate` (train on older purchases, validate and test on newer ones)
- Preprocess numeric features (scaling) and categorical features (one-hot encoding)
- Train sklearn baselines: Logistic Regression, GaussianNB, KNeighborsClassifier
- Implement custom versions of all three classifiers from scratch
- Tune classification threshold for the imbalanced target (~12% bad buys)
- Compare models using ROC AUC, Gini, Precision, Recall, and F1

## Workflow

1. Load and inspect the dataset (72,983 records, 34 columns)
2. Split by purchase date into train / validation / test (33% each)
3. Build preprocessing pipeline for numeric and categorical features
4. Train sklearn Logistic Regression, GaussianNB, and KNN
5. Implement and train custom KNN, Gaussian Naive Bayes, and Logistic Regression
6. Tune the classification threshold on the best model
7. Compare all models on validation and test sets

## Tools and Libraries

- Python, pandas, NumPy
- scikit-learn (preprocessing, metrics, baselines)
- Jupyter Notebook

## Project Structure

```
classification-problems/
├── README.md
├── requirements.txt
└── src/
    └── Classification.ipynb
```

## Results

| Model | ROC AUC | Gini | Precision | Recall | F1 |
|---|---|---|---|---|---|
| Logistic Regression (best) | 0.6991 | 0.3982 | 0.2123 | 0.6302 | 0.3176 |
| Manual Logistic Regression | 0.6567 | 0.3135 | 0.1877 | 0.5552 | 0.2805 |
| Manual Gaussian Naive Bayes | 0.6494 | 0.2987 | 0.2291 | 0.2521 | 0.2400 |
| Manual KNN | 0.6155 | 0.2310 | 0.2857 | 0.0380 | 0.0670 |

- Logistic Regression with `C = 0.05` and threshold `0.15` was the best model.
- Custom implementations confirmed the core mechanics of each algorithm.
- Threshold tuning was critical for the imbalanced target — the default 0.5 threshold produced zero recall.

## Dataset

Kaggle competition: Don't Get Kicked. The dataset includes vehicle, auction, and pricing features. Data is not included in this repository.

## Notes

- Notebook: `src/Classification.ipynb`
- Download the Kaggle dataset and place `training.csv` in a `data/` directory before running.
- Custom implementations use only numeric features to keep training stable and interpretable.
