import numpy as np
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
print("Array Addition of arr1 and arr2")  # Join two arrays
arr3 = np.concatenate((arr1,arr2))  # array add kora
print(arr3)
print("****************************************************************")

arr4 = np.array([[1, 2], [3, 4]])   # Join two 2-D arrays along rows (axis=1)
arr5 = np.array([[5, 6], [7, 8]])
print("Array Addition of arr4 and arr5")  # Join two arrays
arr6 = np.concatenate((arr4,arr5), axis=1)  # array add kora
print(arr6)
print("****************************************************************")

