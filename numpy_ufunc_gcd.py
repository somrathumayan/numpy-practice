import numpy as np

num1 = 6
num2 = 9

x = np.gcd(num1, num2)

print(x) # Returns: 3 because that is the highest number both numbers can be divided by (6/3=2 and 9/3=3).



arr2 = np.array([20, 8, 32, 36, 16])
x2 = np.gcd.reduce(arr2)
print(x2) # Returns: 4 because that is the highest number all values can be divided by.
