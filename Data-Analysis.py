# 📊 Data Analysis and Visualization Assignment
# Author: Alembesh Getaneh

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load Iris dataset
iris_data = load_iris()
df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
df['species'] = pd.Categorical.from_codes(iris_data.target, iris_data.target_names)

# Display first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Task 2: Basic Data Analysis
print("\nBasic statistics of numerical columns:")
print(df.describe())

# Group by species and compute mean of numerical columns
print("\nMean values by species:")
grouped = df.groupby('species').mean()
print(grouped)

# Observations
print("\nObservations:")
print("1. Setosa has the smallest sepal and petal dimensions on average.")
print("2. Virginica has the largest sepal and petal dimensions.")
print("3. Versicolor is in between, showing a gradual increase in size.")

# Task 3: Data Visualization

# 1️⃣ Line Chart: Mean sepal length of each species
plt.figure(figsize=(6,4))
grouped['sepal length (cm)'].plot(kind='line', marker='o')
plt.title('Average Sepal Length by Species')
plt.xlabel('Species')
plt.ylabel('Sepal Length (cm)')
plt.xticks(ticks=range(len(grouped)), labels=grouped.index)
plt.grid(True)
plt.show()

# 2️⃣ Bar Chart: Mean petal length by species
plt.figure(figsize=(6,4))
sns.barplot(x=grouped.index, y=grouped['petal length (cm)'], palette='viridis')
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.show()

# 3️⃣ Histogram: Distribution of sepal width
plt.figure(figsize=(6,4))
plt.hist(df['sepal width (cm)'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.show()

# 4️⃣ Scatter Plot: Sepal length vs Petal length colored by species
plt.figure(figsize=(6,4))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df, s=100, palette='Set2')
plt.title('Sepal Length vs Petal Length by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()

# Optional: Error handling demonstration
try:
    df2 = pd.read_csv('non_existing_file.csv')
except FileNotFoundError:
    print("\nError: File not found. Please check the file path.")