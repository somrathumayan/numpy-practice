import numpy as np

arr1 = np.array([1, 2, 3, 4, 5, 4, 4])
print("Find the indexes where the value is 4")
x1 = np.where(arr1==4) # joto bar 1 ta number thakbe toto bar position print korbe
print(x1)
print("********************************************************************************************")

arr2 = np.array([1, 2, 3, 4, 5, 4, 4])
print("Find the indexes where the values are even")
x2 = np.where(arr2%2 == 1) # Find the indexes where the values are even
print(x2)
print("********************************************************************************************")

arr3 = np.array([1, 2, 3, 4, 5, 4, 4])
print("Find the indexes where the values are odd")
x3 = np.where(arr3%2 == 0) # Find the indexes where the values are odd
print(x3)
print("********************************************************************************************")

arr4 = np.array([6, 7, 8, 9])
print("Find the indexes where the value 7 should be inserted")
x4 = np.searchsorted(arr4, 7) # Find the indexes where the value 7 should be inserted
print(x4)
print("********************************************************************************************")

arr5 = np.array([6, 7, 8, 9])
print("Find the indexes where the value 7 should be inserted, starting from the right")
x5 = np.searchsorted(arr5, 7, side='right') # Find the indexes where the value 7 should be inserted, starting from the right
print(x5)
print("********************************************************************************************")















