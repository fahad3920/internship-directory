# Day 8 - Build the Model: Linear Regression using Scikit-learn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# ============================================================
# 1. LOAD THE DATASET
# ============================================================
print("=" * 60)
print("DAY 8: BUILD THE LINEAR REGRESSION MODEL")
print("=" * 60)

df = pd.read_csv("student_scores.csv")
print(f"\nDataset loaded: {df.shape[0]} samples")

X = df[['Hours']]
y = df['Scores']

print(f"Features (X): Study Hours")
print(f"Target (y): Exam Scores")

# ============================================================
# 2. SPLIT THE DATA
# ============================================================
print("\n" + "-" * 60)
print("STEP 1: TRAIN-TEST SPLIT")
print("-" * 60)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

# ============================================================
# 3. CREATE AND TRAIN THE MODEL
# ============================================================
print("\n" + "-" * 60)
print("STEP 2: CREATE AND TRAIN LINEAR REGRESSION MODEL")
print("-" * 60)

# Create the model
model = LinearRegression()

# Train the model (fit to training data)
model.fit(X_train, y_train)

print("Model training completed!")
print(f"\nModel Coefficients:")
print(f"  Slope (m): {model.coef_[0]:.4f}")
print(f"  Intercept (b): {model.intercept_:.4f}")
print(f"\nModel Equation: Score = {model.coef_[0]:.4f} × Hours + {model.intercept_:.4f}")
print(f"\nInterpretation: For every additional hour studied,")
print(f"the exam score increases by approximately {model.coef_[0]:.2f} points.")

# ============================================================
# 4. MAKE PREDICTIONS ON TRAINING DATA
# ============================================================
print("\n" + "-" * 60)
print("STEP 3: PREDICTIONS ON TRAINING DATA")
print("-" * 60)

y_train_pred = model.predict(X_train)

print(f"\nTraining Data - First 5 predictions vs actual:")
comparison = pd.DataFrame({
    'Actual': y_train.values[:5], 
    'Predicted': y_train_pred[:5].round(2),
    'Difference': (y_train.values[:5] - y_train_pred[:5]).round(2)
})
print(comparison.to_string(index=False))

# ============================================================
# 5. VISUALIZE THE REGRESSION LINE
# ============================================================
print("\n" + "-" * 60)
print("STEP 4: VISUALIZE THE REGRESSION LINE")
print("-" * 60)

plt.figure(figsize=(12, 5))

# Plot 1: Training data with regression line
plt.subplot(1, 2, 1)
plt.scatter(X_train, y_train, color='blue', s=80, alpha=0.7, 
            edgecolors='black', label='Training Data')
plt.plot(X_train, y_train_pred, color='red', linewidth=2, 
         label='Regression Line')
plt.title('Training Data with Regression Line', fontsize=14, fontweight='bold')
plt.xlabel('Study Hours', fontsize=11)
plt.ylabel('Exam Scores', fontsize=11)
plt.legend()
plt.grid(True, alpha=0.3)

# Plot 2: Full data with regression line
plt.subplot(1, 2, 2)
plt.scatter(X, y, color='green', s=80, alpha=0.7, 
            edgecolors='black', label='All Data')
# Generate points for the regression line
x_line = np.linspace(X.min(), X.max(), 100)
y_line = model.predict(x_line.reshape(-1, 1))
plt.plot(x_line, y_line, color='red', linewidth=2, label='Regression Line')
plt.title('Linear Regression Model - All Data', fontsize=14, fontweight='bold')
plt.xlabel('Study Hours', fontsize=11)
plt.ylabel('Exam Scores', fontsize=11)
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('linear_regression_model.png', dpi=150)
print("✅ Saved: linear_regression_model.png")
plt.close()

# ============================================================
# 6. SAVE THE MODEL PARAMETERS
# ============================================================
print("\n" + "-" * 60)
print("MODEL SUMMARY")
print("-" * 60)

print(f"""
📊 Model Summary:
─────────────────────────────────
Algorithm    : Linear Regression
Training set : {len(X_train)} samples
Testing set  : {len(X_test)} samples
Slope (m)    : {model.coef_[0]:.4f}
Intercept (b): {model.intercept_:.4f}
Equation     : Score = ({model.coef_[0]:.2f}) × Hours + ({model.intercept_:.2f})
─────────────────────────────────
""")

# Save model details
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Day 8 - Build the Model: Completed Successfully\n")
    f.write(f"Model: Linear Regression\n")
    f.write(f"Slope: {model.coef_[0]:.4f}\n")
    f.write(f"Intercept: {model.intercept_:.4f}\n")
    f.write(f"Equation: Score = {model.coef_[0]:.4f} * Hours + {model.intercept_:.4f}\n")
    f.write(f"Training samples: {len(X_train)}\n")
    f.write(f"Testing samples: {len(X_test)}\n")

print("\n" + "=" * 60)
print("DAY 8 COMPLETED SUCCESSFULLY!")
print("Linear Regression model trained and saved!")
print("=" * 60)
