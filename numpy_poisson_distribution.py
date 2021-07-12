from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

print("*******************************************************")
print("Generate a random 1x10 distribution for occurence 2")
x1 = random.poisson(lam=2, size=10)
print(x1) # Generate a random 1x10 distribution for occurence 2
print("*******************************************************")


print("*******************************************************")
print("Generate a random 1x10 distribution for occurence 2")
sns.distplot(random.poisson(lam=2, size=1000), kde=False)

plt.show() # Visualization of Poisson Distribution
print("*******************************************************")


sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')

plt.show() # Difference Between Normal and Poisson Distribution
print("*******************************************************")












