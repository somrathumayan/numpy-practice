import numpy as np

x = np.sin(np.pi/2)

print(x) # Find sine value of PI/2:
print("*****************************************************")


arr2 = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x2 = np.sin(arr2)

print(x2)  # Find sine values for all of the values in arr
print("*****************************************************")


arr3 = np.array([90, 180, 270, 360])

x3 = np.deg2rad(arr3)

print(x3) # Convert all of the values in following array arr to radians:
print("*****************************************************")



arr4 = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x4 = np.rad2deg(arr4)
print(x4)
print("*****************************************************")


arr5 = np.array([1, -1, 0.1])
x5 = np.arcsin(arr5)
print(x5) # Find the angle for all of the sine values in the array



print("*****************************************************")

base = 3
perp = 4

x6 = np.hypot(base, perp)

print(x6) # Find the hypotenues for 4 base and 3 perpendicular: