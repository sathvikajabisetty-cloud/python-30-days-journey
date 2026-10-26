
import pandas as pd

# Day 24: Pandas Basics

# 1. Create a DataFrame
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Watch", "Camera"],
    "Price": [50000, 20000, 15000, 5000, 30000],
    "Sales": [10, 25, 15, 30, 12]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# 2. Select columns
print("\nProduct Names:")
print(df["Product"])

print("\nProduct and Sales Columns:")
print(df[["Product", "Sales"]])

# 3. Inspect the DataFrame
print("\nFirst Five Rows:")
print(df.head())

print("\nDataFrame Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

# 4. Filter rows
print("\nProducts with Price above 15000:")
print(df[df["Price"] > 15000])

print("\nProducts with Sales at least 15:")
print(df[df["Sales"] >= 15])

# 5. Sort data
print("\nProducts Sorted by Sales:")
print(df.sort_values("Sales"))

print("\nProducts Sorted by Price (Highest First):")
print(df.sort_values("Price", ascending=False))

# 6. Create a calculated column
df["Revenue"] = df["Price"] * df["Sales"]

print("\nDataFrame with Revenue:")
print(df)

# 7. Basic statistics
print("\nTotal Sales:", df["Sales"].sum())
print("Average Sales:", df["Sales"].mean())
print("Highest Price:", df["Price"].max())
