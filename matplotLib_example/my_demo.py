from matplotlib import pyplot as plt
import numpy as np

dev_x =[25,26,27,28,29,30,31,32,33,34,35]
dev_y =[35000,36000,40000,45000,50000,52000,55000,57000,59000,60000,61000]
#plt.xkcd()
age_index = np.arange(len(dev_x))
width =0.25
plt.bar(age_index-width,dev_y,width=width,color='#0f0f0f', label='All Dev')

py_dev_y =[35500,37000,40200,45070,51000,52010,55080,57200,59100,60300,61010]
plt.bar(age_index,py_dev_y,width=width,color='b',  label='Python Dev')

plt.title('Median Salary W.R.T Age')
plt.xlabel('Age')
plt.ylabel('Median Salary')
plt.legend()
plt.xticks(ticks=age_index,labels=dev_x)

plt.tight_layout()
plt.show()
#print(plt.style.available)
