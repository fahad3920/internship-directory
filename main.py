# Day 9 - Prediction: Use the trained model to predict student scores
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# ============================================================
# 1. LOAD DATA AND TRAIN MODEL (SAME AS DAY 8)
# ============================================================
print("=" * 60)
print("DAY 9: PREDICT STUDENT SCORES FROM STUDY HOURS")
print("=" * 60)

df = pd.read_csv("student_scores.csv")
X = df[['Hours']]
y = df['Scores']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

print(f"Model trained: Score = {model.coef_[0]:.4f} × Hours + {model.intercept_:.4f}")

# ============================================================
# 2. MAKE PREDICTIONS ON TEST DATA
# ============================================================
print("\n" + "-" * 60)
print("PREDICTIONS ON TEST DATA (Unseen Data)")
print("-" * 60)

y_pred = model.predict(X_test)

# Create a comparison table
results = pd.DataFrame({
    'Study Hours': X_test['Hours'].values,
    'Actual Score': y_test.values,
    'Predicted Score': np.round(y_pred, 2),
    'Difference': np.round(y_test.values - y_pred, 2)
})
results['Absolute Diff'] = np.abs(results['Difference'])

print("\nTest Set Predictions:")
print(results.to_string(index=False))

# ============================================================
# 3. PREDICT FOR SPECIFIC STUDY HOURS
# ============================================================
print("\n" + "-" * 60)
print("PREDICTIONS FOR SPECIFIC STUDY HOURS")
print("-" * 60)

test_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for hours in test_hours:
    pred = model.predict([[hours]])
    print(f"  If you study {hours:2d} hour(s), predicted score: {pred[0]:.2f}")

# ============================================================
# 4. VISUALIZE: ACTUAL vs PREDICTED
# ============================================================
print("\n" + "-" * 60)
print("VISUALIZING ACTUAL vs PREDICTED SCORES")
print("-" * 60)

plt.figure(figsize=(14, 5))

# Plot 1: Actual vs Predicted (Test Set)
plt.subplot(1, 2, 1)
plt.scatter(range(len(y_test)), y_test, color='blue', s=100, 
            alpha=0.7, label='Actual Scores', marker='o')
plt.scatter(range(len(y_pred)), y_pred, color='red', s=100, 
            alpha=0.7, label='Predicted Scores', marker='s')
plt.plot(range(len(y_test)), y_test, color='blue', alpha=0.3, linestyle='--')
plt.plot(range(len(y_pred)), y_pred, color='red', alpha=0.3, linestyle='--')
plt.title('Actual vs Predicted Scores (Test Set)', fontsize=14, fontweight='bold')
plt.xlabel('Sample Index', fontsize=11)
plt.ylabel('Score', fontsize=11)
plt.legend()
plt.grid(True, alpha=0.3)

# Plot 2: Regression line with test points highlighted
plt.subplot(1, 2, 2)
plt.scatter(X_train, y_train, color='blue', s=80, alpha=0.5, 
            label='Training Data', edgecolors='black')
plt.scatter(X_test, y_test, color='green', s=120, alpha=0.8, 
            label='Actual Test Data', edgecolors='black', marker='o')
plt.scatter(X_test, y_pred, color='red', s=120, alpha=0.8, 
            label='Predicted Test Data', edgecolors='black', marker='s')
# Regression line
x_line = np.linspace(X.min(), X.max(), 100)
y_line = model.predict(x_line.reshape(-1, 1))
plt.plot(x_line, y_line, color='red', linewidth=2, label='Regression Line')
plt.title('Predictions Visualization', fontsize=14, fontweight='bold')
plt.xlabel('Study Hours', fontsize=11)
plt.ylabel('Exam Scores', fontsize=11)
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('predictions_visualization.png', dpi=150)
print("✅ Saved: predictions_visualization.png")
plt.close()

# ============================================================
# 5. PREDICTION FUNCTION
# ============================================================
print("\n" + "-" * 60)
print("PREDICTION FUNCTION")
print("-" * 60)

def predict_score(hours):
    """Predict exam score based on study hours."""
    prediction = model.predict([[hours]])
    return prediction[0]

# Example usage
print("\nUsing the predict_score() function:")
example_hours = [2.5, 4.0, 7.5, 9.0]
for hours in example_hours:
    score = predict_score(hours)
    print(f"  Study Hours: {hours} → Predicted Score: {score:.2f}")

# Save output
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Day 9 - Predictions: Completed Successfully\n")
    f.write("Test Set Predictions:\n")
    for i in range(len(y_test)):
        f.write(f"  Hours={X_test.iloc[i,0]:.1f}, Actual={y_test.values[i]:.0f}, "
                f"Predicted={y_pred[i]:.2f}, Diff={y_test.values[i]-y_pred[i]:.2f}\n")

print("\n" + "=" * 60)
print("DAY 9 COMPLETED SUCCESSFULLY!")
print("Model predictions generated for test data and custom hours!")
print("=" * 60)
