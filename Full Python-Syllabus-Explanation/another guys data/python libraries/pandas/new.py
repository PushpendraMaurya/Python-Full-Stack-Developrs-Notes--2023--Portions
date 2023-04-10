import pandas as pd

l=[10,20,30,40]
# print(pd.Series(l))

print(pd.Series(l,index=["i","ii","iii","iv"]))

d={"name":["sundeep","surav","rajesh"],"percentage":[90,85,95]}
print(pd.DataFrame(d))

