from numpy import random

print("*********************************************************")
print("print an integer number between 1 and 100")
arr1 = random.randint(100) # print an integer number between 1 and 100
print(arr1) # Generate Random Number
print("*********************************************************")

print("print 10 float numbers")
arr2 = random.rand(10) # print 10 float numbers
print(arr2) # Generate Random Number
print("*********************************************************")

print("print a float number")
arr3 = random.rand() # print a float number
print(arr3) # Generate Random Number
print("*********************************************************")

# The randint() method takes a size parameter where you can specify the shape of an array
print("print 5 integer numbers between 1-100 in array")
arr4 = random.randint(100, size=(5)) # print 5 integer numbers between 1-100 in array
print(arr4) # Generate Random Number
print("*********************************************************")

# Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100
print("Generate a 2-D array with 3 rows") # generate 5 columns and 3 rows
arr5 = random.randint(100, size=(3,5)) # print 5 integer numbers between 1-100 in array
print(arr5) # Generate Random Number
print("*********************************************************")

print("Return one of the values in an array") # Return one of the values in an array
arr6 = random.choice([1,2,3,4,5]) # Return one of the values in an array
print(arr6) # Generate Random Number
print("*********************************************************")

# Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9)
print("Return one of the values in an array") # Return one of the values in an array
arr7 = random.choice([1,2,3,4,5], size=(3,5)) # Return one of the values in an array
print(arr7) # Generate Random Number
print("*********************************************************")