
# Day 26: Seaborn Basics

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Create a product sales dataset
data = {
    "Product": ["A", "B", "C", "D"],
    "Sales": [20, 50, 30, 70]
}

df = pd.DataFrame(data)

# 2. Bar Plot
sns.barplot(data=df, x="Product", y="Sales")

plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()

# 3. Scatter Plot
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6],
    "Marks": [40, 45, 55, 65, 75, 90]
}

df = pd.DataFrame(data)

sns.scatterplot(data=df, x="Study_Hours", y="Marks")

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

# 4. Count Plot
data = {
    "Department": ["HR", "IT", "HR", "Sales", "IT", "IT"]
}

df = pd.DataFrame(data)

sns.countplot(data=df, x="Department")

plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.show()

# 5. Change chart colour using palette
sns.barplot(
    data={"Product": ["A", "B", "C", "D"],
          "Sales": [20, 50, 30, 70]},
    x="Product",
    y="Sales",
    palette="pastel"
)

plt.title("Product Sales - Pastel Palette")
plt.show()
