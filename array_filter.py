import numpy as np

print("Create an array from the elements on index 0 and 2")
arr1 = np.array([41, 42, 43, 44])
x1 = arr1[[True, False, True, False]]
print(x1) # printed only true value ans: 41, 43
print("*******************************************************************")

print("Create a filter array that will return only values higher than 41")
arr2 = np.array([41, 42, 43, 44])
newfilter = []

for element in arr2:
    if element > 41:
        newfilter.append(True)
    else:
        newfilter.append(False)

result=arr2[newfilter]
print(result)
print("*******************************************************************")

print("Create a filter array that will return only even numbers")
arr3 = np.array([41, 42, 43, 44])
newfilter1 = []

for element in arr3:
    if element % 2 == 0:
        newfilter1.append(True)
    else:
        newfilter1.append(False)

result=arr3[newfilter1]
print(result)
print("*******************************************************************")


print("Create a filter array that will return only even numbers")
arr4 = np.array([41, 42, 43, 44])

filter_arr = arr4 > 42

newarr = arr4[filter_arr]

print(filter_arr)
print(newarr)
print("*******************************************************************")