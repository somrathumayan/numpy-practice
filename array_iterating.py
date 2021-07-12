import numpy as np
arr1 = np.array([1,2,3]) # 1D array
print("Print x one by one")
for x in arr1:
    print(x)
print("*************************************************************************")

arr2 = np.array([[1,2,3],[4,5,6]]) # 2D array
print("Print y one by one")
for y in arr2:
    print(y)
print("************************************************************************")

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) # 3D array
print("Print z one by one")
for z in arr3:
  print(z)
print("*************************************************************************")

arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) # 3D array
print("Print m one by one")
for m in arr4:
    for n in m:
        for p in n:
            print(p)
print("*************************************************************************")

arr5 = np.array([[1,2,3],[4,5,6]]) # 2D array
print("Print q one by one")
for q in np.nditer(arr5):
    print(q)
print("*************************************************************************")

arr6 = np.array([1, 2, 3])
print("Print r one by one")
for r in np.nditer(arr6, flags=['buffered'], op_dtypes=['S']):
  print(r)
print("*************************************************************************")

arr7 = np.array([[1,2,3,4], [5,6,7,8]])
print("Iterate through every scalar element of array skipping 1 element")
for s in np.nditer(arr7[:, ::2]): # ekhane 2 mane holo 1 number por por print korbe....
    print(s)
print("*************************************************************************")


arr8 = np.array([1,2,3,4])   # Enumerate on following 1D arrays elements
print("Enumerate on following 1D arrays elements")
for idx, t in np.ndenumerate(arr8): # ans er sathe value r positio bole dibe
    print(idx, t)
print("*************************************************************************")

arr9 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])   # Enumerate on following 1D arrays elements
print("Enumerate on following 2D array's elements")
for idy, u in np.ndenumerate(arr9): # ans er sathe value r positio bole dibe
    print(idy, u)
print("*************************************************************************")

