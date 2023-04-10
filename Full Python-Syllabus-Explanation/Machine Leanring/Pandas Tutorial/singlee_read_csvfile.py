import pandas as pd

df = pd.read_csv("data.csv")

# fetch single column

col = df['name']
print(col)

print(type(col)) # return into the series with the single data col



coll = df['gender'].values # values is nothing but its a attributes

print(coll)

print(type(coll))

print(coll.ndim)

