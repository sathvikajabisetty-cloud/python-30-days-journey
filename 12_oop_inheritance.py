# Program 1: Inheritance

class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


dog1 = Dog()
dog1.eat()
dog1.bark()

# Program 2: Using super()

class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


s1 = Student("Sathvika", 95)
s1.display()

# Program 3: Method Overriding

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Woof!")


dog1 = Dog()
dog1.sound()

# Program 4: Method Overriding with super()

class Animal:
    def sound(self):
        print("Animal sound")


class Dog(Animal):
    def sound(self):
        super().sound()
        print("Woof!")


dog1 = Dog()
dog1.sound()

# Program 5: Employee and Manager

class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        print("Employee is working")


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name)

    def work(self):
        print("Manager is managing the team")


m1 = Manager("Sathvika")
print("Name:", m1.name)
m1.work()

# Program 6: Student Result

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_result(self):
        print(self.name, "has marks:", self.marks)


class Topper(Student):
    def display_result(self):
        print(self.name, "is a topper with", self.marks, "marks!")


s1 = Student("Rahul", 75)
s2 = Topper("Sathvika", 95)

s1.display_result()
s2.display_result()
