# Day 16: Object-Oriented Programming (OOP)
# Topics: Updating Attributes, Methods, and Objects


# Program 1: Update Employee Salary

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, amount):
        self.salary += amount

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


emp1 = Employee("Sathvika", 25000)

emp1.display()

emp1.increase_salary(5000)

print("After Salary Increase:")
emp1.display()


# Program 2: Apply Discount to a Product

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self):
        self.price = self.price * 0.90

    def display(self):
        print("Product:", self.name)
        print("Price:", self.price)


product1 = Product("Shoes", 1000)

product1.display()

product1.apply_discount()

print("After 10% Discount:")
product1.display()


# Program 3: Modify Student Marks

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def update_marks(self, new_marks):
        self.marks = new_marks

    def check_result(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Result:", self.check_result())


student1 = Student("Sathvika", 35)

student1.display()

student1.update_marks(75)

print("After Updating Marks:")
student1.display()


# Program 4: Bank Account Operations

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
        else:
            print("Enter a valid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid withdrawal amount")
        elif amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


account1 = BankAccount("Sathvika", 1000)

account1.check_balance()
account1.deposit(500)
account1.withdraw(200)
account1.check_balance()


# Program 5: Each Object Has Its Own Data

class Box:
    def __init__(self, value):
        self.value = value

    def update(self):
        self.value += 5

    def display(self):
        print("Value:", self.value)


box1 = Box(10)
box2 = Box(20)

box1.update()

print("Box 1:")
box1.display()

print("Box 2:")
box2.display()
