import numpy as np

arr1 = np.array([1,2,3,4,5,6,7,8,9])
x = arr1.copy()
arr1[0] = 42

print("Latest Value of arr1 is : ", arr1)  # change accepted & showed the last value
print("After copy value of x is : ", x)  # after copy value
print("*****************************************************")

arr2 = np.array([1,2,3,4,5,6])
y = arr2.view()
arr2[0] = 33

print("Latest Value of arr2 is : ", arr2)  # change accepted & showed the last value     (both value same)
print("After view value of y is : ", y)  # after copy value     (both value same)
print("*****************************************************")

arr3 = np.array([1,2,3,4,5,6,7,8,9])  # Check if Array Owns it's Data
m = arr3.copy()
n = arr3.view()
print("Copy Value is ", m.base)
print("View Value is ", n.base)
print("*****************************************************")
