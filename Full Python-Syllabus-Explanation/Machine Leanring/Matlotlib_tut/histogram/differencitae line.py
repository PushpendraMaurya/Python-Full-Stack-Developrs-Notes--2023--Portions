import matplotlib.pyplot as plt
import numpy as np

# collecting data 
company = ["TCS","ACCENTURE","INFOSYS","CAPEGEMINI"]
revenue = [1000,2000,3000,4000]

profit = [100,200,300,499]

company_name = np.arange(len(company))

# plot graph 

plt.title("Stock Data")

plt.xlabel("Company Name")
plt.ylabel("Revenue and Profit")

plt.bar((company_name-0.2), revenue,width=0.4,label="Revenue")
plt.bar((company_name+0.2),profit,width=0.4,label="Profit")

plt.xticks(company_name,company)

plt.legend()
plt.show()