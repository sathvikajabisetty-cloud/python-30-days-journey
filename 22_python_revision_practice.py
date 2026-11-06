
# DAY 28 - Python Revision and Practice
# Revising Python Fundamentals, OOP and Data Analysis

# 1. Lists
fruits = ["Apple", "Banana", "Mango"]
fruits.append("Orange")
fruits.remove("Banana")
print("Fruits:", fruits)

# 2. Dictionary
student = {
    "Name": "Sathvika",
    "Marks": 95
}
student["Marks"] = 98
print("Student:", student)

# 3. Functions
def calculate_total(a, b):
    return a + b

print("Total:", calculate_total(10, 20))

# 4. List Comprehension
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even Numbers:", even_numbers)

# 5. NumPy
import numpy as np

sales = np.array([100, 200, 300, 400, 500])
print("Average Sales:", np.mean(sales))
print("Total Sales:", np.sum(sales))
print("Sales above 250:", sales[sales > 250])

# 6. Pandas
import pandas as pd

data = {
    "Product": ["Laptop", "Phone", "Tablet", "Watch"],
    "Price": [50000, 20000, 15000, 5000],
    "Sales": [10, 25, 15, 30]
}

df = pd.DataFrame(data)
df["Revenue"] = df["Price"] * df["Sales"]

print("\nDataset:")
print(df)

print("\nProduct with Price above 15000:")
print(df[df["Price"] > 15000])

print("\nTotal Revenue by Product:")
print(df.groupby("Product")["Revenue"].sum())

# 7. Data Cleaning
print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# 8. Visualization
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(data=df, x="Product", y="Revenue")
plt.title("Revenue by Product")
plt.show()

sns.heatmap(df.corr(numeric_only=True), annot=True,
            cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
