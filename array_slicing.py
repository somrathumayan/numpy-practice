import numpy as np

arr1 = np.array([1,2,3,4,5,6,7,8,9])
print("Slice elements from index 1 to index 5 : ", arr1[1:5])
print("**************************************************************************************")

arr2 = np.array([1,2,3,4,5,6,7,8,9])
print("Slice elements from index 4 to the end : ", arr2[4:])
print("**************************************************************************************")

arr3 = np.array([1,2,3,4,5,6,7,8,9])
print("Slice elements from the beginning to index 4 : ", arr3[:4])
print("**************************************************************************************")

arr4 = np.array([1,2,3,4,5,6,7,8,9])  # negative slicing
print("Slice from the index 4 from the end to index 1 from the end : ", arr4[-4:-1])
print("**************************************************************************************")

arr5 = np.array([1,2,3,4,5,6,7,8,9])
print("Return every other element from index 1 to index 6 : ", arr5[1:6:2])
print("**************************************************************************************")

arr6 = np.array([1,2,3,4,5,6,7,8,9])
print("Return every other element from the entire array : ", arr6[::2])
print("**************************************************************************************")

arr7 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("From the second element, slice elements from index 1 to index 4 : ", arr7[1, 1:4])
print("**************************************************************************************")

arr8 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("From both elements, return index 2 : ", arr8[0:2, 2])
print("**************************************************************************************")

arr9 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("From both elements, slice index 1 to index 4 - return 2D array : ", arr9[0:2, 1:4])
print("**************************************************************************************")

