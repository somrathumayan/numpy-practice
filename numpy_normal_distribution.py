from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

print("randomly 2 rows and 3 columns")
x1 = random.normal(size=(2, 3))
print(x1)
print("************************************************************")


# Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2:
print("randomly 2 rows and 3 columns")
x2 = random.normal(loc=1, scale=2, size=(2,3))
print(x2)
print("************************************************************")


print("randomly 2 rows and 3 columns")
sns.distplot(random.normal(size=1000), hist=False)
plt.show()
print("************************************************************")







