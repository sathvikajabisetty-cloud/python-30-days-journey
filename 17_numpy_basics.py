
import numpy as np


# Program 1: Create a NumPy Array

sales = np.array([100, 200, 300, 400])
print("Sales:", sales)


# Program 2: Arithmetic Operations

prices = np.array([100, 250, 400, 150])

print("Prices + 50:", prices + 50)
print("Prices * 2:", prices * 2)


# Program 3: NumPy Statistical Functions

marks = np.array([70, 85, 90, 65, 80])

print("Total:", np.sum(marks))
print("Average:", np.mean(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))


# Program 4: Indexing and Slicing

values = np.array([100, 200, 300, 400, 500])

print("Second value:", values[1])
print("Middle values:", values[1:4])
print("Last value:", values[-1])


# Program 5: Filtering Arrays

sales = np.array([120, 450, 200, 600, 350])

print("Sales above 300:", sales[sales > 300])
print("Sales below 300:", sales[sales < 300])
