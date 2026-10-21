
from abc import ABC, abstractmethod


# Program 1: Basic Abstract Class

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Woof!")


dog1 = Dog()
dog1.sound()


# Program 2: Abstract Class with Rectangle

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area:", self.length * self.width)


r1 = Rectangle(10, 5)
r1.area()


# Program 3: Payment System Using Abstraction

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI")


class Card(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Card")


upi = UPI()
card = Card()

upi.pay(500)
card.pay(1000)


# Program 4: Cash Payment

class Cash(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Cash")


cash = Cash()
cash.pay(200)
