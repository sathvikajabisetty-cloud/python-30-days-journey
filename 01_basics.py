"""Day 1–3: Variables, input, type conversion, f-strings, and operators."""

# 1. Variables and common data types
name = "Sathvika"
age = 18
branch = "CSE-DS"
percentage = 95.0
is_learning_python = True

print(name, age, branch, percentage, is_learning_python)
print(type(name), type(age), type(percentage), type(is_learning_python))

# 2. Input and type conversion
# Uncomment these lines to practise interactive input:
# username = input("Enter your name: ")
# user_age = int(input("Enter your age: "))
# print(f"Hello {username}, you are {user_age} years old.")

# 3. Basic calculations
length = 10
width = 5
print("Rectangle area:", length * width)

price = 500
quantity = 3
print("Bill total:", price * quantity)

# 4. Arithmetic operators
a, b = 20, 10
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor division:", a // b)
print("Remainder:", a % b)
print("Power:", a ** 2)

# 5. Comparison and logical operators
x, y = 15, 20
print("x > y:", x > y)
print("x == y:", x == y)
print("Both conditions:", x > 10 and y > 10)
print("At least one condition:", x > 20 or y > 10)
print("Not equal:", x != y)

# 6. Membership operators
languages = ["Python", "SQL", "Excel"]
print("Python" in languages)
print("Java" not in languages)

# 7. Profit and profit margin
revenue = 50000
cost = 32000
profit = revenue - cost
print("Profit:", profit)
print("Profit margin (%):", profit / revenue * 100 if revenue else 0)
