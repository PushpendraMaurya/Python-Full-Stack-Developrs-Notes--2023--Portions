import pandas as pd

df = pd.read_csv("data.csv")

d = df['Age'].max()

print(d)


d = df['Age'].min()

print(d)


d = df['Age'].mean()

print(d)

