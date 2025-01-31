# Importing Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Dataset (Replace 'student_scores.csv' with your actual file)
df = pd.read_csv("C:\\Users\\iamsa\\min_pr\\student_scores.csv")

# Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# --------------------------------
# 🛠 DATA CLEANING & PREPROCESSING
# --------------------------------

# Check for missing values
print("\nMissing Values:\n", df.isnull().sum())

# Fill missing values (if any) with the mean of the column
df.fillna(df.mean(), inplace=True)

# Remove duplicate rows (if any)
df.drop_duplicates(inplace=True)

# Detect and Remove Outliers using IQR (Interquartile Range)
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

df_cleaned = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]

# Display dataset info after cleaning
print("\nDataset info after cleaning:")
print(df_cleaned.info())

# --------------------------------
# 📊 DATA VISUALIZATION & ANALYSIS
# --------------------------------

# Correlation Heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(df_cleaned.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.show()

# Box Plot to detect outliers in scores
plt.figure(figsize=(6, 4))
sns.boxplot(x=df_cleaned["Student_Score"])
plt.title("Distribution of Student Scores")
plt.show()

# Scatter Plot: Study Hours vs. Performance
plt.figure(figsize=(6, 4))
sns.scatterplot(x=df_cleaned["Study_Hours"], y=df_cleaned["Student_Score"])
plt.title("Study Hours vs. Performance")
plt.xlabel("Study Hours")
plt.ylabel("Student Score")
plt.show()

# --------------------------------
# 🔢 STATISTICAL ANALYSIS
# --------------------------------

# Display key statistics
print("\nStatistical Summary:")
print(df_cleaned.describe())

# Find the correlation between study hours and scores
correlation = df_cleaned["Study_Hours"].corr(df_cleaned["Student_Score"])
print(f"\nCorrelation between Study Hours and Performance: {correlation:.2f}")

# Conclusion based on correlation value
if correlation > 0.7:
    print("✅ Strong positive correlation: More study hours generally lead to higher scores.")
elif correlation > 0.4:
    print("🔄 Moderate correlation: Study hours impact scores, but other factors may contribute.")
else:
    print("❌ Weak correlation: Other factors influence performance more than study hours.")
