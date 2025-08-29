# Week 5 Assignment – Data Analysis and Visualization

## Student Info
- Name: Alembesh Getaneh  
- Department: Computer Science  
- Program: PLP, July 2025 Cohort  

---

## Description
This assignment focuses on data analysis and visualization using Python.  
The Iris dataset is used to demonstrate:

1. Loading and inspecting a dataset.
2. Basic statistical analysis.
3. Grouping data by categories.
4. Visualizing data using line charts, bar charts, histograms, and scatter plots.
5. Optional: Handling errors when reading files.

---

## Steps Performed

1. Load Dataset  
   - Imported pandas, matplotlib.pyplot, seaborn, and sklearn.datasets.
   - Loaded the Iris dataset into a pandas DataFrame.
   - Added a species column for categorical labels.

2. Basic Data Analysis  
   - Displayed the first 5 rows.
   - Computed descriptive statistics using .describe().
   - Grouped data by species and computed the mean of numerical columns.
   - Noted observations about differences between species.

3. Data Visualization  
   - Line Chart: Average sepal length by species.
   - Bar Chart: Average petal length by species.
   - Histogram: Distribution of sepal width.
   - Scatter Plot: Sepal length vs petal length, colored by species.

4. Error Handling  
   - Demonstrated handling FileNotFoundError when trying to read a non-existing CSV file.

---

## Code Summary

```python
# Key Steps:
# 1. Load dataset and create DataFrame
# 2. Display head and descriptive statistics
# 3. Group by species and compute means
# 4. Visualize with line, bar, histogram, and scatter plots
# 5. Handle file reading errors gracefully

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

iris_data = load_iris()
df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
df['species'] = pd.Categorical.from_codes(iris_data.target, iris_data.target_names)

# Display first rows and statistics
print(df.head())
print(df.describe())
print(df.groupby('species').mean())

# Visualizations: line, bar, histogram, scatter
# (plots generated using matplotlib and seaborn)

# Optional error handling
try:
    pd.read_csv('non_existing_file.csv')
except FileNotFoundError:
    print("Error: File not found.")
Observations
Setosa has the smallest sepal and petal dimensions on average.

Virginica has the largest sepal and petal dimensions.

Versicolor is in between, showing gradual growth in size.

Outcomes 🎉
Learned to load and inspect datasets using pandas.

Performed basic statistical analysis on numerical columns.

Applied grouping operations to extract insights by category.

Created visualizations (line chart, bar chart, histogram, scatter plot) to understand data patterns.

Practiced error handling to make code robust and prevent crashes.