import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2])

print(newarr)

newarr1 = np.sum([arr1, arr2], axis=1) # Summation Over an Axis
print(newarr1)

print("***********************************************")
# The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].
print("Perform cummulative summation in the following array")
arr3 = np.array([1, 2, 3])
newarr3 = np.cumsum(arr3)
print(newarr3)
print("***********************************************")
