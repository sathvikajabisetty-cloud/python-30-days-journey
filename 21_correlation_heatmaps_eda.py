
 DAY 27 - Correlation, Heatmaps and EDA

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating a sales dataset
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone",
                "Tablet", "Watch", "Laptop", "Phone", "Watch"],
    "Category": ["Electronics", "Electronics", "Electronics",
                 "Electronics", "Electronics", "Electronics",
                 "Accessories", "Electronics", "Electronics",
                 "Accessories"],
    "Price": [50000, 20000, 15000, 50000, 20000,
              15000, 5000, 50000, 20000, 5000],
    "Quantity": [2, 5, 3, 1, 4, 2, 6, 3, 2, 8],
    "Rating": [4.5, 4.2, 3.8, 4.8, 4.1,
               3.9, 4.6, 4.7, 4.0, 4.8]
}

df = pd.DataFrame(data)

# Creating Revenue column
df["Revenue"] = df["Price"] * df["Quantity"]

# Exploratory Data Analysis
print("First 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

# Product-wise Revenue
product_revenue = df.groupby("Product")["Revenue"].sum()
print("\nProduct Revenue:")
print(product_revenue)

# Category-wise Revenue
category_revenue = df.groupby("Category")["Revenue"].sum()
print("\nCategory Revenue:")
print(category_revenue)

# Correlation
print("\nCorrelation:")
print(df.corr(numeric_only=True))

# Correlation Heatmap
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Sales Data Correlation Heatmap")
plt.show()

# Revenue by Product
sns.barplot(data=df, x="Product", y="Revenue", estimator=sum)
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.show()

# Pair Plot
sns.pairplot(df.select_dtypes(include="number"))
plt.show()
