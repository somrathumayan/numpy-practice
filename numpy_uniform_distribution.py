from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


x1 = random.uniform(size=(2,3))
print(x1)

# Visualization of Uniform Distribution

sns.distplot(random.uniform(size=1000), hist=False)
plt.show()