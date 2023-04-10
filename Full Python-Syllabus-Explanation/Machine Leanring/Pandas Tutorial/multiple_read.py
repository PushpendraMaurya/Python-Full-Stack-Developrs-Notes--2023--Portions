import pandas as pd

df = pd.read_csv("data.csv")

# fetch single column


coll = df[['name','gender','contact']].values # values is nothing but its a attributes

print(coll)

print(type(coll))

print(coll.ndim)

