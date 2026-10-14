# Day 15: Object-Oriented Programming (OOP)

# Program 1: Create a class and object
class Car:
    def __init__(self, brand, colour):
        self.brand = brand
        self.colour = colour

    def display(self):
        print("Brand:", self.brand)
        print("Colour:", self.colour)


car1 = Car("Porsche", "White")
car1.display()


# Program 2: Create two student objects
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


student1 = Student("Sathvika", 90)
student2 = Student("Rahul", 85)

student1.display()
student2.display()


# Program 3: Check pass or fail
class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    def check_result(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"


student3 = StudentResult("Sathvika", 75)
student4 = StudentResult("Rahul", 32)

student3.display()
print("Result:", student3.check_result())

student4.display()
print("Result:", student4.check_result())


# Program 4: Calculate total and average marks
class StudentMarks:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)


student5 = StudentMarks("Sathvika", [85, 90, 95])

print("Name:", student5.name)
print("Total:", student5.calculate_total())
print("Average:", student5.calculate_average())


# Program 5: Update object attributes
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


employee1 = Employee("Priya", 25000)
employee1.display()

employee1.salary = 30000

print("After salary update:")
employee1.display()
