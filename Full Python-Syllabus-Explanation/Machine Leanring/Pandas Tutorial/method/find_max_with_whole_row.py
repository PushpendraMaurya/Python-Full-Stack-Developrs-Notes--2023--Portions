import pandas as pd

df = pd.read_csv("data.csv")

df1 = df[df['Age'] == df['Age'.max()]]

print(df1)