from numpy import random
import numpy as np

arr1 = np.array([1,2,3,4,5]) # Shuffling Arrays
random.shuffle(arr1)
print(arr1)
print("******************************************")

arr2 = np.array([1, 2, 3, 4, 5]) # Generate a random permutation of elements of following array
print(random.permutation(arr2))
print("******************************************")