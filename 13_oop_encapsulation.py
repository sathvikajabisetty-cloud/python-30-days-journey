# Day 18 - Program 1: Access Modifiers

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self._age = age
        self.__marks = marks

    def show_marks(self):
        print("Marks:", self.__marks)


s1 = Student("Sathvika", 18, 95)

print("Name:", s1.name)
print("Age:", s1._age)
s1.show_marks()

# Day 18 - Program 2: Encapsulation

class Product:
    def __init__(self, price):
        self.__price = price

    def show_price(self):
        print("Price:", self.__price)


p1 = Product(1000)
p1.show_price()

# Day 18 - Program 3: Bank Deposit

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful")
        else:
            print("Invalid amount")

    def show_balance(self):
        print("Balance:", self.__balance)


account = BankAccount(1000)
account.deposit(500)
account.show_balance()

# Day 18 - Program 4: Bank Account with Deposit and Withdrawal

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance:", self.__balance)


account = BankAccount(1000)

account.deposit(500)
account.withdraw(300)
account.show_balance()

# Day 18 - Program 5: Private Attribute Access

class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def show_salary(self):
        print("Salary:", self.__salary)


e1 = Employee(30000)

e1.show_salary()

# Direct access normally raises AttributeError
# print(e1.__salary)
