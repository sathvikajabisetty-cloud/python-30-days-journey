"""Day 7: Lists, indexing, slicing, methods, sorting, and filtering."""

sales = [12000, 5000, 18000, 7000, 25000]

# 1. Indexing
print(sales[0])
print(sales[2])
print(sales[-1])
print(sales[-2])

# 2. Updating elements
sales[1] = 6000
print(sales)

# 3. Add items
sales.append(15000)
sales.insert(1, 9000)
print(sales)

# 4. Remove items
sales.remove(7000)  # removes the matching value
sales.pop()         # removes the last item
print(sales)

# 5. Slicing
numbers = [1000, 2000, 3000, 4000, 5000, 6000]
print(numbers[:3])
print(numbers[3:])
print(numbers[1:5])
print(numbers[::2])
print(numbers[::-1])

# 6. Membership and list length
print(2000 in numbers)
print("Number of values:", len(numbers))

# 7. Sorting and top three values
numbers.sort()
print("Ascending:", numbers)
print("Top three:", numbers[-3:])

# 8. Build a list from user input (uncomment to practise)
# entered_numbers = []
# for _ in range(3):
#     entered_numbers.append(int(input("Enter a number: ")))
# print(entered_numbers)

# 9. Filtering
sales = [12000, 5000, 18000, 7000, 25000]
high_sales = []
for sale in sales:
    if sale >= 10000:
        high_sales.append(sale)
print("Sales of at least 10000:", high_sales)
