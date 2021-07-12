import numpy as np

# One way of doing it is to iterate over both of the lists and then sum each elements.
x = [1,2,3,4]
y = [4,5,6,7]
z=[]

for i, j in zip(x,y):
    z.append(i+j)
print(z)

print("*********************************")

x1 = [1, 2, 3, 4]
y1 = [4, 5, 6, 7]
z = np.add(x1,y1)
print(z)
print("*********************************")