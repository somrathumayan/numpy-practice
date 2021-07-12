import numpy as np

arr1 = np.array([1,2,3,4,5,6,7,8,9])
print("Array Indexing arr[2] : ", arr1[2])
print("****************************************************************")

arr2 = np.array([1,2,3])
arr3 = np.array([4,5,6])
print("Array concatenation (Add two numbers) is : ", arr2[1] + arr3[1])
print("****************************************************************")

arr4 = np.array([[1,2,3,4,5], [6,7,8,9,10]])  #Access 2-D Arrays
print("2nd element on 1st dim is : ", arr4[0,1])
print("****************************************************************")

arr5 = np.array([[1,2,3,4,5], [6,7,8,9,10]])  #Access 2-D Arrays
print("5th element on 2nd dim is : ", arr5[1,4])
print("****************************************************************")

arr6 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])  #Access 3-D Arrays
print("3rd element of the 2nd array is : ", arr6[0, 1, 2])
print("****************************************************************")

arr7 = np.array([[1,2,3,4,5], [6,7,8,9,10]])  #Negative Indexing
print("Last element from 2nd dim is : ", arr7[1, -1])
print("****************************************************************")