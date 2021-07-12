import numpy as np

print("Truncation") # using trunc()
arr1 = np.trunc([-3.1666, 3.6667])
# Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.
print(arr1)
print("*********************************************88888888")


print("Truncation") # using fix()
arr2 = np.fix([-3.1666, 3.6667])
# Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.
print(arr2)
print("*********************************************88888888")


print("Rounding") # using around()
arr3 = np.around(3.1666, 2)
# round off to 1 decimal point, 3.16666 is 3.2
print(arr3) # The around() function increments preceding digit or decimal by 1 if >=5 else do nothing
print("*********************************************88888888")



print("Floor") # using floor()
arr4 = np.floor([-3.1666, 3.6667])
# Floor the elements of following array
print(arr4)
print("*********************************************88888888")





print("Ceil") # using ceil()
arr5 = np.ceil([-3.1666, 3.6667])
# Ceil the elements of following array
print(arr5)
print("*********************************************88888888")
