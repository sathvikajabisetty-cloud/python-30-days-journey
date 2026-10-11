"""Day 5–6: for/while loops, range, counters, break/continue, and patterns."""

# 1. Print numbers from 1 to 5
for number in range(1, 6):
    print(number)

# 2. Sum numbers from 1 to n
n = 5
total = 0
for number in range(1, n + 1):
    total += number
print("Sum:", total)

# 3. Multiplication table
number = 5
for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# 4. While loop
count = 1
while count <= 5:
    print(count)
    count += 1

# 5. break and continue
for number in range(1, 8):
    if number == 5:
        break
    print(number)

for number in range(1, 6):
    if number == 3:
        continue
    print(number)

# 6. Total and count from a list
sales = [12000, 5000, 18000, 7000, 25000]
total = 0
count = 0
for sale in sales:
    total += sale
    count += 1
print("Total sales:", total)
print("Number of sales:", count)
print("Average sales:", total / count if count else 0)

# 7. Highest and lowest values
highest = sales[0]
lowest = sales[0]
for sale in sales:
    if sale > highest:
        highest = sale
    if sale < lowest:
        lowest = sale
print("Highest:", highest)
print("Lowest:", lowest)

# 8. Count positive, negative, and zero values
values = [4, -2, 0, 7, -5, 0]
positive = negative = zero = 0
for value in values:
    if value > 0:
        positive += 1
    elif value < 0:
        negative += 1
    else:
        zero += 1
print("Positive:", positive, "Negative:", negative, "Zero:", zero)

# 9. Star pattern
for row in range(1, 5):
    print("* " * row)

# 10. Nested loop example
for row in range(1, 4):
    for column in range(1, 4):
        print("*", end=" ")
    print()
