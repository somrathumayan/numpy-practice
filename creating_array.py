import numpy as np

arrOd = np.array(42)
print("0-D array is ", arrOd)
print("Array Dimension : ", arrOd.ndim)
print("****************************")

arr1d = np.array([1, 2, 3, 4, 5])
print("1-D array is ", arr1d)
print("Array Dimension : ", arr1d.ndim)
print("****************************")

arr2d = np.array([[1,2,3], [4,5,6]])
print("2-D array is ", arr2d)
print("Array Dimension : ", arr2d.ndim)
print("****************************")

arr3d = np.array([[[1,2,3],[4,5,6]], [[7,8,9], [10,11,12]]])
print("3-D array is ", arr3d)
print("Array Dimension : ", arr3d.ndim)
print("****************************")


arr5d = np.array([1,2,3,4,5], ndmin = 5)
print("5-D array is ", arr5d)
print("Array Dimension : ", arr5d.ndim)
print("****************************")
