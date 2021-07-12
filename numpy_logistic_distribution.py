from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x1 = random.logistic(loc=1, scale=2, size=(2, 3))

print(x1)  # Draw 2x3 samples from a logistic distribution with mean at 1 and stddev 2.0:
print("************************************************")


sns.distplot(random.logistic(size=1000), hist=False)

plt.show()  # Visualization of Logistic Distribution
print("************************************************")


sns.distplot(random.normal(scale=2, size=1000), hist=False, label='normal')
sns.distplot(random.logistic(size=1000), hist=False, label='logistic')

plt.show()






