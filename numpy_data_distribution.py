from numpy import random
print("**********************************************************************************************")
# Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9
print("Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9")
x1 = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x1)
print("**********************************************************************************************")


# Same example as above, but return a 2-D array with 3 rows, each containing 5 values
print("Generate a 2-D array containing 100 values, where each value has to be 3, 5, 7 or 9")
x2 = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x2)
print("**********************************************************************************************")