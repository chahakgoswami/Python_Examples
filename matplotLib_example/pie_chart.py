from matplotlib import pyplot as plt

plt.style.use("ggplot")
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
colors =['#008fd5','#fc4f30' , '#e5ae37','#6d904f'] 
explode =[0,0,0,.1,0]
plt.pie(slices,labels=labels,explode=explode,shadow=True,startangle=45,autopct='%1.01f%%',
      wedgeprops={'edgecolor':'black'})
plt.title('Demo')
plt.show()
#print(plt.style.available)