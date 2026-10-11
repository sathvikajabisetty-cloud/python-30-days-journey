"""Day 8: Tuples, sets, dictionaries, and dictionary loops."""

# 1. Tuple
employee = ("Sathvika", 18, "Data Analyst")
print(employee[0])
print(employee[-1])

# 2. Set removes duplicate values
cities = {"Hyderabad", "Mumbai", "Delhi", "Hyderabad", "Mumbai"}
print(cities)
cities.add("Chennai")
cities.discard("Delhi")
print("Mumbai" in cities)

# 3. Dictionary: read, update, add, remove
student = {
    "name": "Sathvika",
    "age": 18,
    "branch": "CSE-DS",
    "marks": 85
}
print(student["name"])
student["marks"] = 90
student["city"] = "Hyderabad"
student.pop("age")
print(student)

# 4. Loop through a dictionary
sales = {
    "Monday": 12000,
    "Tuesday": 15000,
    "Wednesday": 8000,
    "Thursday": 18000,
    "Friday": 22000
}
for day, amount in sales.items():
    print(day, amount)

# 5. Total, count, and average
total = 0
for amount in sales.values():
    total += amount
count = len(sales)
average = total / count if count else 0
print("Total:", total)
print("Count:", count)
print("Average:", average)

# 6. Highest and lowest daily sales
amounts = list(sales.values())
print("Highest:", max(amounts))
print("Lowest:", min(amounts))
