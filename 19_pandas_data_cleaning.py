
import pandas as pd

# Day 25: Pandas Data Cleaning

# 1. Create a dataset with missing values and duplicates
data = {
    "Product": ["Laptop", "Phone", "Laptop", "Tablet", "Watch"],
    "Price": [50000, None, 50000, 15000, None],
    "Sales": [10, 25, 10, 15, 30]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# 2. Count missing values in each column
print("\nMissing Values by Column:")
print(df.isnull().sum())

# 3. Count all missing cells
print("\nTotal Missing Cells:")
print(df.isnull().sum().sum())

# 4. Detect duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated())

print("\nTotal Duplicate Rows:")
print(df.duplicated().sum())

# 5. Remove duplicate rows
df = df.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(df)

# 6. Fill missing prices with 0
df["Price"] = df["Price"].fillna(0)

print("\nAfter Filling Missing Prices:")
print(df)

# 7. Check missing values again
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# 8. Basic analysis
print("\nTotal Sales:", df["Sales"].sum())
print("Highest Price:", df["Price"].max())
