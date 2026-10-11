"""Day 9–11: Functions, parameters, return values, scope, and lambda."""

# 1. Basic function
def greet(name):
    return f"Hello, {name}!"

print(greet("Sathvika"))

# 2. Function to calculate average
def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers) if numbers else 0

print(calculate_average([10, 20, 30, 40, 50]))

# 3. Return multiple values
def analyse_sales(sales):
    total = sum(sales)
    average = total / len(sales) if sales else 0
    return total, average

print(analyse_sales([10000, 15000, 20000, 5000]))

# 4. Find highest and lowest using a loop
def find_high_low(numbers):
    if not numbers:
        return None, None
    highest = lowest = numbers[0]
    for number in numbers:
        if number > highest:
            highest = number
        if number < lowest:
            lowest = number
    return highest, lowest

print(find_high_low([45, 12, 89, 34, 7, 66]))

# 5. Default parameter
def calculate_bill(price, quantity=1):
    return price * quantity

print(calculate_bill(500))
print(calculate_bill(500, 3))

# 6. Classify sales
def classify_sales(amount):
    if amount >= 20000:
        return "high"
    elif amount >= 10000:
        return "medium"
    return "low"

print(classify_sales(25000))
print(classify_sales(15000))
print(classify_sales(5000))

# 7. Count high sales
def count_high_sales(sales):
    count = 0
    for sale in sales:
        if sale >= 10000:
            count += 1
    return count

print(count_high_sales([5000, 12000, 8000, 25000, 15000, 3000]))

# 8. Combined sales report
def sales_report(sales):
    if not sales:
        return 0, 0, 0
    total = 0
    count_high = 0
    for sale in sales:
        total += sale
        if sale >= 10000:
            count_high += 1
    average = total / len(sales)
    return total, average, count_high

print(sales_report([12000, 5000, 18000, 7000, 25000, 3000, 15000]))

# 9. Local vs global scope
value = 50
def show_local_value():
    value = 20
    print("Local value:", value)

show_local_value()
print("Global value:", value)

# 10. print vs return
def multiply_and_return(a, b):
    return a * b

result = multiply_and_return(4, 5)
print(result)
print(result * 2)

# 11. Lambda functions
square = lambda number: number ** 2
add = lambda a, b: a + b
discounted_price = lambda price: price * 0.85

print(square(6))
print(add(10, 20))
print(discounted_price(2000))
