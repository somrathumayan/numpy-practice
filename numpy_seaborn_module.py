import matplotlib.pyplot as plt
import  seaborn as sns
sns.distplot([0,1,2,3,4,5]) # Plotting a Displot
plt.show() # Plotting a Displot
print("**********************************************")

sns.distplot([0,1,2,3,4,5], hist=False)
plt.show() # Plotting a Displot
print("**********************************************")