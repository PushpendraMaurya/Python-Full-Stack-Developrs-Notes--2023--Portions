import pandas as pd


df = pd.read_excel("new_file.xlsx")

#with value get their datas,,,
x = df.iloc[1:4,1:4] 
print(df)

# without value get their datas 
x1 = df.iloc[1:3,2:4].values

print(x1)