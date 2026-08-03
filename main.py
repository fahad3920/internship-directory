# Day 7 - Machine Learning Basics: Supervised Learning, Train-Test Split, Linear Regression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# ============================================================
# 1. UNDERSTANDING SUPERVISED LEARNING
# ============================================================
print("=" * 60)
print("DAY 7: MACHINE LEARNING BASICS")
print("=" * 60)

print("""
📚 SUPERVISED LEARNING:
Supervised learning is a type of machine learning where the model learns
from labeled training data. Each training example has an input (features)
and a known output (target/label).

Key Concepts:
- Features (X): Input variables used to make predictions (e.g., Study Hours)
- Target (y): The output variable we want to predict (e.g., Exam Scores)
- Training: Model learns patterns from labeled data
- Prediction: Model predicts target for new, unseen data

Types of Supervised Learning:
- Regression: Predicting continuous values (e.g., scores)
- Classification: Predicting categories (e.g., pass/fail)
""")

# ============================================================
# 2. LOAD THE DATASET
# ============================================================
print("-" * 60)
print("LOADING THE DATASET")
print("-" * 60)

df = pd.read_csv("student_scores.csv")
print(f"\nDataset loaded: {df.shape[0]} samples")
print(f"Features: {list(df.columns)}")

# Features (X) and Target (y)
X = df[['Hours']]  # Feature matrix (2D)
y = df['Scores']   # Target vector (1D)

print(f"\nFeatures (X) shape: {X.shape}")
print(f"Target (y) shape: {y.shape}")
print(f"\nFeature sample (first 5):")
print(X.head())
print(f"\nTarget sample (first 5):")
print(y.head())

# ============================================================
# 3. TRAIN-TEST SPLIT
# ============================================================
print("-" * 60)
print("TRAIN-TEST SPLIT")
print("-" * 60)

print("""
Why Split?
- Train Set: Used to train the model (learn patterns)
- Test Set: Used to evaluate model performance (unseen data)
- Typical split: 80% training, 20% testing
""")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training set size: {len(X_train)} samples ({len(X_train)/len(X)*100:.0f}%)")
print(f"Testing set size: {len(X_test)} samples ({len(X_test)/len(X)*100:.0f}%)")
print(f"\nTraining features (first 5):")
print(X_train.head())
print(f"\nTesting features (first 5):")
print(X_test.head())

# ============================================================
# 4. LINEAR REGRESSION CONCEPT
# ============================================================
print("-" * 60)
print("LINEAR REGRESSION CONCEPT")
print("-" * 60)

print("""
📈 LINEAR REGRESSION:

Linear Regression finds the best-fit line through the data points.
The line is represented as:

    y = mx + b

Where:
    y = predicted score (target)
    x = study hours (feature)
    m = slope (coefficient) - how much score increases per hour
    b = intercept - base score when hours = 0

Goal: Find m and b that minimize the error between predicted and actual values.
""")

# ============================================================
# 5. VISUALIZE TRAIN-TEST SPLIT
# ============================================================
print("\n📊 Visualizing Train-Test Split...")

plt.figure(figsize=(10, 6))
plt.scatter(X_train, y_train, color='blue', s=100, alpha=0.7, 
            edgecolors='black', label='Training Data')
plt.scatter(X_test, y_test, color='red', s=100, alpha=0.7, 
            edgecolors='black', label='Testing Data')
plt.title('Train-Test Split Visualization', fontsize=16, fontweight='bold')
plt.xlabel('Study Hours', fontsize=12)
plt.ylabel('Exam Scores', fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('train_test_split.png', dpi=150)
print("✅ Saved: train_test_split.png")
plt.close()

# Save output
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Day 7 - Machine Learning Basics: Completed Successfully\n")
    f.write(f"Total samples: {len(X)}\n")
    f.write(f"Training samples: {len(X_train)}\n")
    f.write(f"Testing samples: {len(X_test)}\n")
    f.write("Concepts covered: Supervised Learning, Train-Test Split, Linear Regression\n")

print("\n" + "=" * 60)
print("DAY 7 COMPLETED SUCCESSFULLY!")
print("ML fundamentals understood!")
print("=" * 60)
