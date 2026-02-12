# 📘 Assignment: Data Analysis

## 🎯 Objective

Students will learn the basics of data analysis using Python. They will load, explore, and analyze a dataset to extract meaningful insights.

## 📝 Tasks

### 🛠️ Data Loading and Exploration

#### Description
Load a provided CSV dataset and perform basic exploration to understand its structure and contents.

#### Requirements
Completed program should:

- Load a CSV file using Python (e.g., with pandas)
- Display the first 5 rows of the dataset
- Show summary statistics (mean, median, etc.) for numeric columns

#### Example Input
```python
import pandas as pd

# Load the dataset
df = pd.read_csv('data.csv')
print(df.head())
print(df.describe())
```

#### Example Output
```
   id  age  score
0   1   23   85.5
1   2   34   92.0
2   3   28   78.5
3   4   45   88.0
4   5   31   95.5

              id        age      score
count   5.000000   5.000000   5.000000
mean    3.000000  32.200000  87.900000
std     1.581139   8.408330   6.723095
min     1.000000  23.000000  78.500000
...
```


### 🛠️ Data Visualization and Insights

#### Description
Create visualizations to help understand the data and summarize key findings.

#### Requirements
Completed program should:

- Generate at least two different types of plots (e.g., histogram, scatter plot)
- Identify and describe at least two insights or trends from the data
- Save the plots as image files

#### Example Input
```python
import matplotlib.pyplot as plt

# Create histogram
plt.hist(df['age'], bins=10)
plt.title('Age Distribution')
plt.savefig('age_histogram.png')

# Create scatter plot
plt.scatter(df['age'], df['score'])
plt.xlabel('Age')
plt.ylabel('Score')
plt.savefig('age_score_scatter.png')
```

#### Example Output
```
Insights:
1. Most participants are between 25-35 years old
2. There is a positive correlation between age and score

Files created:
- age_histogram.png
- age_score_scatter.png
```
