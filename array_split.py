import numpy as np

print("Array Split into 4 parts")     # Split the array in 4 parts
arr1 = np.array([1, 2, 3, 4, 5, 6])
newarray1 = np.array_split(arr1, 4)

print(newarray1)
print("********************************************************")

print("Array Split into 3 parts")   # Split the array in 3 parts
arr2 = np.array([1, 2, 3, 4, 5, 6])
newarray2 = np.array_split(arr2, 3)

print(newarray2[0])
print(newarray2[1])
print(newarray2[2])
print("********************************************************")


print("Array Split into 3 parts")   # Split the array in 3 parts
arr3 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarray3 = np.array_split(arr3, 3)
print(newarray3)
print("********************************************************")

print("Array Split into 3 parts")   # Split the array in 3 parts
arr4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarray4 = np.array_split(arr4, 3)
print(newarray4) # Split the 2-D array into three 2-D arrays.
print("********************************************************")
