
# Day 12: Error Handling and Debugging

# Program 1: Handle invalid number input
try:
    number = int(input("Enter a number: "))
    print("Number:", number)
except ValueError:
    print("Please enter a valid number!")


# Program 2: Handle division by zero
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)
except ValueError:
    print("Enter numbers only!")
except ZeroDivisionError:
    print("Cannot divide by zero!")


# Program 3: Using try, except, else and finally
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid age!")
else:
    print("Your age is:", age)
finally:
    print("Program finished.")


# Program 4: Find the square of a number
try:
    number = float(input("Enter a number: "))
    print("Square:", number ** 2)
except ValueError:
    print("Invalid number!")


# Program 5: Safe calculator
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        result = a / b
    else:
        result = None
        print("Invalid operation!")

    if result is not None:
        print("Answer:", result)

except ValueError:
    print("Please enter valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
