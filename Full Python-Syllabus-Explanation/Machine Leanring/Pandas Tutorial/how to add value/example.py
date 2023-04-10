import pandas as pd

df = pd.read_csv("data.csv")

age = [21,12,45,78,45]

df['AGE'] = age

print(df)
