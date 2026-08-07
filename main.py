# Day 10 - Model Evaluation: MAE, MSE, R2 Score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ============================================================
# 1. LOAD DATA AND TRAIN MODEL
# ============================================================
print("=" * 60)
print("DAY 10: MODEL EVALUATION")
print("=" * 60)

df = pd.read_csv("student_scores.csv")
X = df[['Hours']]
y = df['Scores']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

print(f"Model: Score = {model.coef_[0]:.4f} × Hours + {model.intercept_:.4f}")

# ============================================================
# 2. MAKE PREDICTIONS
# ============================================================
print("\n" + "-" * 60)
print("MAKING PREDICTIONS")
print("-" * 60)

y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

print("✓ Predictions generated for both training and test sets.")

# ============================================================
# 3. CALCULATE EVALUATION METRICS
# ============================================================
print("\n" + "-" * 60)
print("MODEL EVALUATION METRICS")
print("-" * 60)

# Training set metrics
train_mae = mean_absolute_error(y_train, y_train_pred)
train_mse = mean_squared_error(y_train, y_train_pred)
train_rmse = np.sqrt(train_mse)
train_r2 = r2_score(y_train, y_train_pred)

# Test set metrics
test_mae = mean_absolute_error(y_test, y_test_pred)
test_mse = mean_squared_error(y_test, y_test_pred)
test_rmse = np.sqrt(test_mse)
test_r2 = r2_score(y_test, y_test_pred)

print(f"""
{'─'*50}
{'METRIC':<20} {'TRAINING SET':<15} {'TEST SET':<15}
{'─'*50}
{'MAE (Mean Absolute Error)':<20} {train_mae:<15.4f} {test_mae:<15.4f}
{'MSE (Mean Squared Error)':<20} {train_mse:<15.4f} {test_mse:<15.4f}
{'RMSE (Root Mean Sq Error)':<20} {train_rmse:<15.4f} {test_rmse:<15.4f}
{'R² Score':<20} {train_r2:<15.4f} {test_r2:<15.4f}
{'─'*50}
""")

# ============================================================
# 4. INTERPRET THE METRICS
# ============================================================
print("-" * 60)
print("INTERPRETATION OF METRICS")
print("-" * 60)

print(f"""
📊 METRIC INTERPRETATION:

1️⃣ MAE (Mean Absolute Error): {test_mae:.4f}
   - Average absolute difference between predicted and actual scores
   - On average, predictions are off by {test_mae:.2f} points

2️⃣ MSE (Mean Squared Error): {test_mse:.4f}
   - Average squared difference (penalizes larger errors more)
   - Lower is better

3️⃣ RMSE (Root Mean Squared Error): {test_rmse:.4f}
   - Square root of MSE (same unit as target variable)
   - On average, prediction error is about {test_rmse:.2f} points

4️⃣ R² Score (Coefficient of Determination): {test_r2:.4f}
   - Proportion of variance in target explained by the model
   - {test_r2*100:.2f}% of the variation in scores is explained by study hours
   - Ranges from 0 to 1 (higher is better)
   - A value of {test_r2:.4f} indicates {'excellent' if test_r2 > 0.9 else 'good' if test_r2 > 0.8 else 'moderate'} model fit
""")

# ============================================================
# 5. VISUALIZE MODEL PERFORMANCE
# ============================================================
print("\n📊 Creating Model Evaluation Visualizations...")

plt.figure(figsize=(14, 5))

# Plot 1: Actual vs Predicted (with perfect prediction line)
plt.subplot(1, 2, 1)
plt.scatter(y_test, y_test_pred, color='purple', s=100, alpha=0.7, 
            edgecolors='black')
# Perfect prediction line
min_val = min(y_test.min(), y_test_pred.min())
max_val = max(y_test.max(), y_test_pred.max())
plt.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, 
         label='Perfect Prediction')
plt.title(f'Actual vs Predicted (Test Set)\nR² = {test_r2:.4f}', 
          fontsize=14, fontweight='bold')
plt.xlabel('Actual Scores', fontsize=11)
plt.ylabel('Predicted Scores', fontsize=11)
plt.legend()
plt.grid(True, alpha=0.3)

# Plot 2: Residuals
plt.subplot(1, 2, 2)
residuals = y_test - y_test_pred
plt.scatter(y_test_pred, residuals, color='orange', s=100, alpha=0.7,
            edgecolors='black')
plt.axhline(y=0, color='red', linestyle='--', linewidth=2)
plt.title(f'Residual Plot (Test Set)', fontsize=14, fontweight='bold')
plt.xlabel('Predicted Scores', fontsize=11)
plt.ylabel('Residuals (Actual - Predicted)', fontsize=11)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('model_evaluation.png', dpi=150)
print("✅ Saved: model_evaluation.png")
plt.close()

# ============================================================
# 6. METRICS SUMMARY TABLE
# ============================================================
print("-" * 60)
print("FINAL EVALUATION SUMMARY")
print("-" * 60)

print(f"""
{'='*50}
{'METRIC EVALUATION SUMMARY':^50}
{'='*50}

MAE  : {test_mae:.4f}  → Average prediction error: {test_mae:.2f} points
MSE  : {test_mse:.4f}  → Squared error (lower is better)
RMSE : {test_rmse:.4f}  → Typical error magnitude: {test_rmse:.2f} points
R²   : {test_r2:.4f}  → Model explains {test_r2*100:.2f}% of variance

CONCLUSION: The model performs {'very well' if test_r2 > 0.9 else 'well' if test_r2 > 0.8 else 'adequately'}.
{'='*50}
""")

# Save output
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Day 10 - Model Evaluation: Completed Successfully\n")
    f.write(f"MAE (Test): {test_mae:.4f}\n")
    f.write(f"MSE (Test): {test_mse:.4f}\n")
    f.write(f"RMSE (Test): {test_rmse:.4f}\n")
    f.write(f"R² Score (Test): {test_r2:.4f}\n")
    f.write(f"Interpretation: Model explains {test_r2*100:.2f}% of variance in scores\n")

print("\n" + "=" * 60)
print("DAY 10 COMPLETED SUCCESSFULLY!")
print("Model performance measured and evaluated!")
print("=" * 60)
