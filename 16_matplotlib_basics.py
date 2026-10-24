
import matplotlib.pyplot as plt


# Program 1: Line Chart - Monthly Sales

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [1000, 1500, 1200, 2000]

plt.plot(months, sales, marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()


# Program 2: Bar Chart - Product Sales

products = ["Laptop", "Phone", "Tablet", "Watch"]
units_sold = [50, 80, 30, 60]

plt.bar(products, units_sold)
plt.title("Product Sales Comparison")
plt.xlabel("Products")
plt.ylabel("Units Sold")
plt.show()


# Program 3: Bar Chart with Value Labels

products = ["A", "B", "C", "D"]
sales = [25, 70, 45, 90]

bars = plt.bar(products, sales)
plt.title("Product Sales Comparison")
plt.xlabel("Products")
plt.ylabel("Units Sold")
plt.bar_label(bars)
plt.show()


# Program 4: Scatter Plot - Study Hours vs Marks

study_hours = [1, 2, 3, 4, 5]
marks = [40, 50, 65, 75, 90]

plt.scatter(study_hours, marks)
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()
