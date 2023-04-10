import matplotlib.pyplot as plt

import random

x = list(range(1,50))

y = [random.randint(1,100) for  i in range(1,50)]

plt.title("Scatter Plot ")

plt.scatter(x,y,color="red")

plt.show()