import numpy as np

arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr)
print(newarr) # for [1, 2, 3, 4], the discrete difference would be [2-1, 3-2, 4-3] = [1, 1, 1]
print("**************************************************8")

arr2 = np.array([10, 15, 25, 5])
newarr2 = np.diff(arr2, n=2)
print(newarr2) # [5 -30] because: 15-10=5, 25-15=10, and 5-25=-20 AND 10-5=5 and -20-10=-30