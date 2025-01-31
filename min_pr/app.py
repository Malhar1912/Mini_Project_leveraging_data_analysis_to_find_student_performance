import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
file_path = "C:\\Users\\iamsa\\min_pr\\student_scores.csv"  
df = pd.read_csv(file_path)

# Rename columns to remove spaces & lowercase them
df.columns = df.columns.str.strip().str.lower()

# Display dataset info
print("Dataset Info:")
print(df.info())

# Display first few rows
print("\nFirst 5 Rows:")
print(df.head())

# Box Plot: Distribution of Student Scores
plt.figure(figsize=(6, 4))
sns.boxplot(x=df["scores"], color="skyblue")
plt.title("Distribution of Student Scores")
plt.xlabel("Scores")
plt.show()

# Scatter Plot: Study Hours vs. Scores
plt.figure(figsize=(6, 4))
sns.scatterplot(x=df["hours"], y=df["scores"], color="red", marker="o")
plt.title("Study Hours vs. Student Scores")
plt.xlabel("Study Hours")
plt.ylabel("Scores")
plt.show()
