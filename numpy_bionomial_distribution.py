from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

print("Given 10 trials for coin toss generate 10 data points:")
x1 = random.binomial(n=10, p=0.5, size=10)
print(x1) # Given 10 trials for coin toss generate 10 data points:
print("************************************************************************")

# sns.distplot(random.binomial(n=10, p=.5, size=1000), hist=True, kde=False)
# plt.show()
# print("************************************************************************")

sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
plt.show()
print("************************************************************************")



