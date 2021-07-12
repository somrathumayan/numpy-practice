import numpy as np

print("Products/Multiplication")
arr1 = np.array([1, 2, 3, 4])
x1 = np.prod(arr1) # 24 because 1*2*3*4 = 24
print(x1) # all numbers multiplication
print("****************************************")

print("Products/Multiplication")
arr2 = np.array([1, 2, 3, 4])
arr3 = np.array([5, 6, 7, 8])
x2 = np.prod([arr2, arr3]) # all numbers multiplication
print(x2) # 40320 because 1*2*3*4*5*6*7*8 = 40320
print("****************************************")



print("Products/Multiplication") # Perform summation in the following array over 1st axis:
arr4 = np.array([1, 2, 3, 4])
arr5 = np.array([5, 6, 7, 8])
x2 = np.prod([arr4, arr5], axis=1) # all numbers multiplication
print(x2) # [24 1680]
print("****************************************")



print("Cummulative product") # Take cummulative product of all elements for following array:
arr6 = np.array([5, 6, 7, 8])
newarr6 = np.cumprod(arr6)
print(newarr6) # The partial product of [1, 2, 3, 4] is [1, 1*2, 1*2*3, 1*2*3*4] = [1, 2, 6, 24]
print("****************************************")



