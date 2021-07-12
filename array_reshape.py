import numpy as np
arr1 = np.array([1,2,3,4,5,6]) # 1D to 2D conversion
newarray1 = arr1.reshape(3, 2) # 3 means 3rows and 2 means 2 columns
print("elements", newarray1)
print("**************************************")

arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) # 1D to 2D conversion
newarr2 = arr2.reshape(4, 3) # 4 means 4 rows and 3 means 3 columns
print("elements", newarr2)
print("**************************************")

arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) # 1D to 3D conversion
newarray3 = arr3.reshape(2, 3, 2) # 3 means 3rows and 2 means 2 columns
print("elements", newarray3) # 1st 2 means 2 ta alada matrics & 3 means 3 rows and 2 means 2 columns
print("**************************************")

arr4 = np.array([1, 2, 3, 4, 5, 6, 7, 8]) # Convert 1D array with 8 elements to 3D array with 2x2 elements
newarray4 = arr4.reshape(2, 2, -1) # 2 means 2rows and 2 means 2 columns
print("elements", newarray4) # Pass -1 as the value, and NumPy will calculate this number for you
print("**************************************")

arr5 = np.array([[1, 2, 3], [4, 5, 6]]) # Convert 3D to 1D array with 8 elements with 2x2 elements
newarray5 = arr5.reshape(-1)
print("elements", newarray5) # Convert 3D to 1D array with 8 elements with 2x2 elements
print("**************************************")