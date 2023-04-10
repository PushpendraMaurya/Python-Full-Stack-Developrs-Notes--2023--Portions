import matplotlib.pyplot as plt

# collect their data ..

x = ["sun","mon","Tue","Wed","thu","Fri","Sat"]
y = [11,12,13,14,15,17,19]

# create graph....

plt.title("Weather data")

plt.xlabel("Days")

plt.ylabel("Temp")

plt.plot(x,y,marker="+",color="yellow",markersize =10, markerfacecolor="blue",linestyle="dashed",linewidth=3)
plt.grid()

plt.show()