import matplotlib.pyplot as plt

import random

data = [random.randint(0,80) for i in range(100)]

plt.title("Analysis")

plt.xlabel("Age")

plt.ylabel("Number of Person")

plt.hist(data, rwidth=0.9, bins= 7)

plt.show()