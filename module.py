
# Day 14: Modules in Python

# Program 1: Math module
import math

print("Square root:", math.sqrt(25))
print("Factorial:", math.factorial(5))
print("Value of pi:", math.pi)


# Program 2: Random module
import random

print("Random number:", random.randint(1, 100))

names = ["Riya", "Anu", "Priya", "Sana"]
print("Random name:", random.choice(names))


# Program 3: Date and time module
from datetime import datetime

today = datetime.now()

print("Current date and time:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)
print("Formatted date:", today.strftime("%d-%m-%Y"))


# Program 4: Student performance calculator
def calculate_average(marks):
    return sum(marks) / len(marks)


marks = [85, 90, 75, 95, 80]

average = calculate_average(marks)

print("Marks:", marks)
print("Total:", sum(marks))
print("Average:", round(average, 2))
print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Square root of total:", round(math.sqrt(sum(marks)), 2))


# Program 5: Function and random number challenge
number = random.randint(1, 100)
print("Random number:", number)


def square(number):
    return number ** 2


print("Square of 5:", square(5))
