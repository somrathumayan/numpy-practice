import numpy as np

print("Add")
arr1 = np.array([10,11,12,13,14,15])
arr2 = np.array([20,21,22,23,24,25])

newarr1 = np.add(arr1,arr2)
print(newarr1)
print("*******************************************")

print("Subtract")
arr3 = np.array([10,20,30,40,50,60])
arr4 = np.array([20,21,22,23,24,25])

newarr2 = np.subtract(arr3,arr4)
print(newarr2)
print("*******************************************")

print("Multiplication")
arr5 = np.array([10,20,30,40,50,60])
arr6 = np.array([20,21,22,23,24,25])

newarr3 = np.multiply(arr5,arr6)
print(newarr3)
print("*******************************************")


print("Divide")
arr7 = np.array([10,20,30,40,50,60])
arr8 = np.array([20,21,22,23,24,25])

newarr4 = np.divide(arr7,arr8)
print(newarr4)
print("*******************************************")



print("Power")
arr9 = np.array([1,2,3,4,5,6])
arr10 = np.array([0,1,2,3,4,5])

newarr5 = np.power(arr9,arr10)
print(newarr5)
print("*******************************************")



print("Remainder")
arr11 = np.array([10, 20, 30, 40, 50, 60])
arr12 = np.array([3, 7, 9, 8, 2, 33])
newarr6 = np.mod(arr11, arr12)
print(newarr6)
print("*******************************************")



print("Absolute Values")
arr13 = np.array([-1, -2, -1, 2, -3, -4])
newarr7 = np.absolute(arr13)
print(newarr7)
print("*******************************************")