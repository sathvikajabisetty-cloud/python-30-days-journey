# Day 19 - Program 1: Method Overriding

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Woof!")


class Cat(Animal):
    def sound(self):
        print("Meow!")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

# Day 19 - Program 2: Polymorphism without Inheritance

class Bird:
    def move(self):
        print("Bird is flying")


class Fish:
    def move(self):
        print("Fish is swimming")


def show_movement(animal):
    animal.move()


show_movement(Bird())
show_movement(Fish())

# Day 19 - Program 3: Same Function, Different Objects

class Car:
    def move(self):
        print("Car is driving")


class Plane:
    def move(self):
        print("Plane is flying")


def start_moving(vehicle):
    vehicle.move()


start_moving(Car())
start_moving(Plane())

# Day 19 - Program 4: Payment Polymorphism

class UPI:
    def pay(self, amount):
        print("Paid", amount, "using UPI")


class Card:
    def pay(self, amount):
        print("Paid", amount, "using Card")


def make_payment(method, amount):
    method.pay(amount)


make_payment(Card(), 1000)
make_payment(UPI(), 500)

# Day 19 - Program 5: Operator Polymorphism

print(10 + 20)

print("Hello " + "Sathvika")

print([1, 2] + [3, 4])

# Day 19 - Program 6: Shape Polymorphism

class Rectangle:
    def area(self):
        print("Rectangle area:", 10 * 5)


class Square:
    def area(self):
        print("Square area:", 4 * 4)


class Circle:
    def area(self):
        print("Circle area:", 3.14 * 3 * 3)


def calculate_area(shape):
    shape.area()


calculate_area(Rectangle())
calculate_area(Square())
calculate_area(Circle())
