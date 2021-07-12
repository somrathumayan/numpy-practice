import numpy as np
arr1 = np.array([1,2,3,4,5,6])
print("arr1 = np.array([1,2,3,4,5,6]) is ", arr1.dtype) #integer
print("*****************************************************************")

arr2 = np.array(['apple', 'banana', 'cherry'])  #string
print("arr2 = np.array(['apple', 'banana', 'cherry']) is ", arr2.dtype)
print("*****************************************************************")

arr3 = np.array([1, 2, 3, 4], dtype='S')  #string
print("arr3 = np.array([1, 2, 3, 4], dtype='S') is ", arr3.dtype)
print("*****************************************************************")

arr4 = np.array([1, 2, 3, 4], dtype='i4')  # 4 bytes integer
print("arr4 = np.array([1, 2, 3, 4], dtype='i4') is ", arr4.dtype)
print("*****************************************************************")

arr5 = np.array([1.1, 2.1, 3.1])  # Change data type from float to integer
arrayastype = arr5.astype('i') # we can write "int" instead of "i"
print("new value of arr5 is : ", arrayastype)
print("arr5 = np.array([1.1, 2.1, 3.1]) now is ", arrayastype.dtype)
print("*****************************************************************")


arr6 = np.array([1,0,3])  # Change data type from integer to boolean
arrayastype6 = arr5.astype('bool') # we can write "int" instead of "i"
print("new value of arr5 is : ", arrayastype6)
print("arr5 = np.array([1,0,3]) now is ", arrayastype6.dtype)
print("*****************************************************************")