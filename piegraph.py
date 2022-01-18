import matplotlib.pyplot as plt
labels = ('A','B','C','D')
sizes = [10,15,25,45]

plt.pie(sizes, labels=labels,autopct='%1.1f%%')
plt.show()