"""Day 4: if, elif, else, nested conditions, and classifications."""

# 1. Even or odd
number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# 2. Positive, negative, or zero
number = -3
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# 3. Grade classification
marks = 85
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Needs improvement"
print("Grade:", grade)

# 4. Validate age range
age = 18
if age < 0 or age > 120:
    print("Invalid age")
else:
    print("Age is in a valid range")

# 5. Sales classification
amount = 15000
if amount >= 20000:
    print("High sales")
elif amount >= 10000:
    print("Medium sales")
else:
    print("Low sales")

# 6. Nested condition example
username = "student"
password = "python123"
if username == "student":
    if password == "python123":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("User not found")
