# Day 4 - Pandas: Import, Load Dataset, Explore Rows, Columns & Info
import pandas as pd

# ============================================================
# 1. IMPORTING PANDAS AND LOADING THE DATASET
# ============================================================
print("=" * 60)
print("DAY 4: PANDAS - DATASET EXPLORATION")
print("=" * 60)

# Load the student score dataset
df = pd.read_csv("student_scores.csv")
print(f"\nDataset loaded successfully!")

# ============================================================
# 2. BASIC DATASET INFORMATION
# ============================================================
print("\n" + "-" * 60)
print("BASIC DATASET INFORMATION")
print("-" * 60)

print(f"\nShape (rows, columns): {df.shape}")
print(f"Number of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")
print(f"\nColumn names: {list(df.columns)}")
print(f"Data types:\n{df.dtypes}")

# ============================================================
# 3. EXPLORING FIRST AND LAST ROWS
# ============================================================
print("\n" + "-" * 60)
print("EXPLORING FIRST AND LAST ROWS")
print("-" * 60)

print(f"\nFirst 5 rows (head):")
print(df.head())

print(f"\nFirst 10 rows:")
print(df.head(10))

print(f"\nLast 5 rows (tail):")
print(df.tail())

print(f"\nLast 3 rows:")
print(df.tail(3))

# ============================================================
# 4. DATASET SUMMARY INFORMATION
# ============================================================
print("\n" + "-" * 60)
print("DATASET SUMMARY INFORMATION")
print("-" * 60)

print(f"\nDataset Info:")
# Capture info output
import io
buffer = io.StringIO()
df.info(buf=buffer)
info_str = buffer.getvalue()
print(info_str)

print(f"\nStatistical Summary (describe):")
print(df.describe())

# ============================================================
# 5. EXPLORING SPECIFIC COLUMNS
# ============================================================
print("\n" + "-" * 60)
print("EXPLORING SPECIFIC COLUMNS")
print("-" * 60)

print(f"\nHours column:")
print(df['Hours'])

print(f"\nScores column:")
print(df['Scores'])

# Check unique values
print(f"\nUnique study hours: {df['Hours'].nunique()}")
print(f"Unique scores: {df['Scores'].nunique()}")

# ============================================================
# 6. CHECKING FOR MISSING VALUES & DUPLICATES
# ============================================================
print("\n" + "-" * 60)
print("DATA QUALITY CHECK")
print("-" * 60)

print(f"\nMissing values per column:")
print(df.isnull().sum())

print(f"\nDuplicate rows: {df.duplicated().sum()}")

# ============================================================
# 7. BASIC ROW & COLUMN OPERATIONS
# ============================================================
print("\n" + "-" * 60)
print("ROW & COLUMN OPERATIONS")
print("-" * 60)

# Selecting specific rows
print(f"\nRow at index 5:\n{df.loc[5]}")

# Slicing rows
print(f"\nRows 3 to 7:")
print(df.iloc[3:8])

# Selecting specific columns
print(f"\nSelecting 'Hours' and 'Scores' columns:")
print(df[['Hours', 'Scores']].head())

# Adding a derived column
df['Hours_Squared'] = df['Hours'] ** 2
print(f"\nDataset with new column 'Hours_Squared':")
print(df.head())
df.drop('Hours_Squared', axis=1, inplace=True)  # Clean up

# Save output info to file
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Day 4 - Pandas: Dataset Loaded and Explored Successfully\n")
    f.write(f"Dataset shape: {df.shape}\n")
    f.write(f"Columns: {list(df.columns)}\n")
    f.write(f"Total students: {len(df)}\n")

print("\n" + "=" * 60)
print("DAY 4 COMPLETED SUCCESSFULLY!")
print(f"Dataset loaded with {df.shape[0]} rows and {df.shape[1]} columns")
print("=" * 60)
