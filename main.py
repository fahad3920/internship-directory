# Day 5 - Data Cleaning: Handle Missing Values, Remove Duplicates, Dataset Statistics
import pandas as pd
import numpy as np

# ============================================================
# 1. LOAD THE DATASET AND INTRODUCE SOME IMPERFECTIONS
# ============================================================
print("=" * 60)
print("DAY 5: DATA CLEANING")
print("=" * 60)

# Load original dataset
df = pd.read_csv("student_scores.csv")
print(f"\nOriginal dataset shape: {df.shape}")
print(f"\nOriginal data:")
print(df.head(10))

# Create a copy with imperfections for cleaning practice
df_clean = df.copy()

# Introduce some missing values and duplicates for demonstration
df_dirty = df.copy()
df_dirty.loc[2, 'Scores'] = np.nan
df_dirty.loc[7, 'Hours'] = np.nan
df_dirty.loc[15, 'Scores'] = np.nan
# Add a duplicate row
df_dirty = pd.concat([df_dirty, df_dirty.iloc[[0]]], ignore_index=True)
# Add another duplicate
df_dirty = pd.concat([df_dirty, df_dirty.iloc[[5]]], ignore_index=True)

print("\n" + "=" * 60)
print("DIRTY DATASET (with missing values & duplicates)")
print("=" * 60)
print(f"\nDirty dataset shape: {df_dirty.shape}")
print(df_dirty.head(15))

# ============================================================
# 2. CHECKING FOR MISSING VALUES
# ============================================================
print("\n" + "-" * 60)
print("STEP 1: CHECKING FOR MISSING VALUES")
print("-" * 60)

print(f"\nMissing values per column:")
print(df_dirty.isnull().sum())
print(f"\nTotal missing values: {df_dirty.isnull().sum().sum()}")

# Visual check for missing data
print(f"\nRows with missing values:")
print(df_dirty[df_dirty.isnull().any(axis=1)])

# ============================================================
# 3. HANDLING MISSING VALUES
# ============================================================
print("\n" + "-" * 60)
print("STEP 2: HANDLING MISSING VALUES")
print("-" * 60)

# Option A: Fill missing values with mean
df_filled = df_dirty.copy()
df_filled['Hours'].fillna(df_filled['Hours'].mean(), inplace=True)
df_filled['Scores'].fillna(df_filled['Scores'].mean(), inplace=True)
print(f"\nFilled missing values with column means:")
print(f"Missing values after filling: {df_filled.isnull().sum().sum()}")

# Option B: Drop rows with missing values
df_dropped = df_dirty.copy()
df_dropped.dropna(inplace=True)
print(f"\nDropped rows with missing values:")
print(f"Shape before: {df_dirty.shape}, Shape after: {df_dropped.shape}")

# ============================================================
# 4. FINDING AND REMOVING DUPLICATES
# ============================================================
print("\n" + "-" * 60)
print("STEP 3: FINDING AND REMOVING DUPLICATES")
print("-" * 60)

print(f"\nDuplicate rows before removal: {df_filled.duplicated().sum()}")
print(f"\nDuplicate rows:")
print(df_filled[df_filled.duplicated(keep=False)])

# Remove duplicates
df_filled.drop_duplicates(inplace=True)
print(f"\nShape after removing duplicates: {df_filled.shape}")
print(f"Duplicate rows after removal: {df_filled.duplicated().sum()}")

# ============================================================
# 5. UNDERSTANDING DATASET STATISTICS
# ============================================================
print("\n" + "-" * 60)
print("STEP 4: UNDERSTANDING DATASET STATISTICS")
print("-" * 60)

print(f"\nStatistical Summary:")
print(df_filled.describe())

# Additional statistics
print(f"\nMedian values:")
print(df_filled.median())

print(f"\nMode values:")
print(df_filled.mode().iloc[0])

print(f"\nVariance:")
print(f"Hours variance: {df_filled['Hours'].var():.2f}")
print(f"Scores variance: {df_filled['Scores'].var():.2f}")

print(f"\nCorrelation between Hours and Scores:")
print(f"Correlation coefficient: {df_filled['Hours'].corr(df_filled['Scores']):.4f}")

# ============================================================
# 6. FINAL CLEAN DATASET
# ============================================================
print("\n" + "-" * 60)
print("FINAL CLEAN DATASET")
print("-" * 60)

print(f"\nClean dataset shape: {df_filled.shape}")
print(f"\nClean dataset preview:")
print(df_filled.head(10))

# Save the clean dataset
df_filled.to_csv("student_scores_clean.csv", index=False)
print(f"\n✅ Clean dataset saved to 'student_scores_clean.csv'")

# Save output to file
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Day 5 - Data Cleaning: Completed Successfully\n")
    f.write(f"Original shape: {df_dirty.shape}\n")
    f.write(f"Missing values handled: {df_dirty.isnull().sum().sum()}\n")
    f.write(f"Duplicates removed: {df_dirty.duplicated().sum()}\n")
    f.write(f"Final clean shape: {df_filled.shape}\n")
    f.write(f"Correlation (Hours vs Scores): {df_filled['Hours'].corr(df_filled['Scores']):.4f}\n")

print("\n" + "=" * 60)
print("DAY 5 COMPLETED SUCCESSFULLY!")
print("Clean dataset ready for analysis and ML!")
print("=" * 60)
