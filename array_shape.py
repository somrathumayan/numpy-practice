import numpy as np
arr1 = np.array([[1,2,3], [4,5,6]])
print("1st one is dimension and 2nd one is elements", arr1.shape)
# This example returns (2, 3), it means that the array has 2 dimensions, # and each dimension has 3 elements.
print("**************************************")

arr2 = np.array([1, 2, 3, 4], ndmin=5)
print("5D Array is : ", arr2)
print('shape of array :', arr2.shape)
print("**************************************")
