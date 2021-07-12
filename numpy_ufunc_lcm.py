import numpy as np

num1 = 4
num2 = 6
x = np.lcm(num1, num2)
print(x) # 12 because that is the lowest common multiple of both numbers (4*3=12 and 6*2=12).

arr2 = np.array([3, 6, 9])
x2 = np.lcm.reduce(arr2)
print(x2) # 18 because that is the lowest common multiple of all three numbers (3*6=18, 6*3=18 and 9*2=18).

arr4 = np.arange(1, 11)
x4 = np.lcm.reduce(arr4)
print(x4)






