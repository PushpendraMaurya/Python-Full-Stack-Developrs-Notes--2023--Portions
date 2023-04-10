import pandas as pd

df = pd.read_csv("data.csv")


# d = df.head() # return top 5 row 

# print(d)


# d1 = df.tail() # return bottom 5 row 


# print(d1)

d = df[1:4]
print(d)