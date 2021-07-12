from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=2, size=(2, 3))

print(x)
print("*************************************")

x1 = random.zipf(a=2, size=1000)
sns.distplot(x1[x1<10], kde=False)
plt.show()