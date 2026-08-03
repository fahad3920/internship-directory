# Day 6 - Data Visualization: Scatter Plots, Bar Charts, Line Charts using Matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ============================================================
# 1. LOAD THE CLEAN DATASET
# ============================================================
print("=" * 60)
print("DAY 6: DATA VISUALIZATION WITH MATPLOTLIB")
print("=" * 60)

df = pd.read_csv("student_scores.csv")
print(f"\nDataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# ============================================================
# 2. SCATTER PLOT: Hours vs Scores
# ============================================================
print("\n📊 Creating Scatter Plot: Hours vs Scores...")

plt.figure(figsize=(10, 6))
plt.scatter(df['Hours'], df['Scores'], color='blue', alpha=0.7, s=100, edgecolors='black')
plt.title('Study Hours vs Exam Scores', fontsize=16, fontweight='bold')
plt.xlabel('Study Hours', fontsize=12)
plt.ylabel('Exam Scores', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('scatter_hours_vs_scores.png', dpi=150)
print("✅ Saved: scatter_hours_vs_scores.png")
plt.close()

# ============================================================
# 3. BAR CHART: Average Score per Hour Range
# ============================================================
print("\n📊 Creating Bar Chart: Average Score by Hour Range...")

# Create hour bins
df['Hour_Range'] = pd.cut(df['Hours'], bins=[0, 2, 4, 6, 8, 10], 
                           labels=['0-2 hrs', '2-4 hrs', '4-6 hrs', '6-8 hrs', '8-10 hrs'])

avg_scores = df.groupby('Hour_Range', observed=True)['Scores'].mean()

plt.figure(figsize=(10, 6))
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
bars = plt.bar(avg_scores.index, avg_scores.values, color=colors, edgecolors='black', linewidth=1.2)

# Add value labels on bars
for bar, val in zip(bars, avg_scores.values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
             f'{val:.1f}', ha='center', va='bottom', fontweight='bold')

plt.title('Average Exam Score by Study Hours Range', fontsize=16, fontweight='bold')
plt.xlabel('Study Hours Range', fontsize=12)
plt.ylabel('Average Score', fontsize=12)
plt.ylim(0, 100)
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('bar_avg_score_by_hours.png', dpi=150)
print("✅ Saved: bar_avg_score_by_hours.png")
plt.close()

# ============================================================
# 4. LINE CHART: Study Hours Trend (Sorted)
# ============================================================
print("\n📊 Creating Line Chart: Score Trend by Study Hours...")

# Sort by hours for a proper line chart
df_sorted = df.sort_values('Hours')

plt.figure(figsize=(12, 6))
plt.plot(df_sorted['Hours'], df_sorted['Scores'], 
         marker='o', color='#2E86AB', linewidth=2, markersize=8, 
         markerfacecolor='#A23B72', markeredgecolor='black')
plt.title('Score Trend by Study Hours', fontsize=16, fontweight='bold')
plt.xlabel('Study Hours (sorted)', fontsize=12)
plt.ylabel('Exam Scores', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('line_score_trend.png', dpi=150)
print("✅ Saved: line_score_trend.png")
plt.close()

# ============================================================
# 5. COMBINED VISUALIZATION (Subplots)
# ============================================================
print("\n📊 Creating Combined Visualization...")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Top-left: Scatter
axes[0, 0].scatter(df['Hours'], df['Scores'], color='blue', alpha=0.7, s=80, edgecolors='black')
axes[0, 0].set_title('Study Hours vs Scores', fontweight='bold')
axes[0, 0].set_xlabel('Hours')
axes[0, 0].set_ylabel('Scores')
axes[0, 0].grid(True, alpha=0.3)

# Top-right: Bar
axes[0, 1].bar(avg_scores.index, avg_scores.values, color=colors, edgecolors='black')
axes[0, 1].set_title('Avg Score by Hour Range', fontweight='bold')
axes[0, 1].set_xlabel('Hours Range')
axes[0, 1].set_ylabel('Avg Score')
axes[0, 1].tick_params(axis='x', rotation=15)
axes[0, 1].grid(True, alpha=0.3, axis='y')

# Bottom-left: Line
axes[1, 0].plot(df_sorted['Hours'], df_sorted['Scores'], 
                marker='o', color='#2E86AB', linewidth=2, markersize=6)
axes[1, 0].set_title('Score Trend', fontweight='bold')
axes[1, 0].set_xlabel('Hours')
axes[1, 0].set_ylabel('Scores')
axes[1, 0].grid(True, alpha=0.3)

# Bottom-right: Histogram of scores
axes[1, 1].hist(df['Scores'], bins=8, color='#96CEB4', edgecolors='black', alpha=0.8)
axes[1, 1].axvline(df['Scores'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {df["Scores"].mean():.1f}')
axes[1, 1].set_title('Score Distribution', fontweight='bold')
axes[1, 1].set_xlabel('Scores')
axes[1, 1].set_ylabel('Frequency')
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3)

plt.suptitle('Student Performance Analysis - Data Visualization', fontsize=18, fontweight='bold')
plt.tight_layout()
plt.savefig('combined_visualization.png', dpi=150)
print("✅ Saved: combined_visualization.png")
plt.close()

# Clean up temporary column
df.drop('Hour_Range', axis=1, inplace=True)

# Save output info
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Day 6 - Data Visualization: Completed Successfully\n")
    f.write("Charts created:\n")
    f.write("1. scatter_hours_vs_scores.png\n")
    f.write("2. bar_avg_score_by_hours.png\n")
    f.write("3. line_score_trend.png\n")
    f.write("4. combined_visualization.png\n")

print("\n" + "=" * 60)
print("DAY 6 COMPLETED SUCCESSFULLY!")
print("All 4 charts saved as PNG files!")
print("=" * 60)
