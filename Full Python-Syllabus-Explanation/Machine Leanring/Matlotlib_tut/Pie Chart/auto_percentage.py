import matplotlib.pyplot as plt

ex_label = ["rent","mess","laundary","bills","travel","fees","saving","others"]

exp = [5000,3000,500,1500,20000,20000,2000,4000]


plt.pie(exp,labels= ex_label, shadow=True , autopct= '%1.0f%%', )
plt.savefig("pic.png")
plt.show()