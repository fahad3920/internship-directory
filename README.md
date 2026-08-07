# Day 10 - Model Evaluation

## Concepts Covered

| Concept | Description |
|---|---|
| **MAE** | Mean Absolute Error - average absolute prediction error |
| **MSE** | Mean Squared Error - penalizes larger errors more |
| **RMSE** | Root Mean Squared Error - error in original units |
| **R² Score** | Coefficient of Determination - variance explained by model |
| **Residuals** | Difference between actual and predicted values |

## Output Files

- `model_evaluation.png` - Evaluation visualizations

## How to Run

```bash
cd "day 10"
python main.py
```

## What I Learned (Daily Submission Form)

> Today I evaluated the Linear Regression model using standard metrics. I calculated MAE, MSE, RMSE, and R² Score to measure model performance. The MAE tells me the average prediction error in points, the R² score tells me how much variance is explained by the model. I also created residual plots to check if the model's errors are randomly distributed. This evaluation is crucial for understanding how well the model will perform on new data.
