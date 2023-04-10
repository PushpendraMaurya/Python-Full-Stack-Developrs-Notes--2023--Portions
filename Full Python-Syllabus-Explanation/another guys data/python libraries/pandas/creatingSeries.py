import pandas as pd
import numpy as np

# s=pd.Series()
# print(s)

# #using Arrey
# l=np.array([10,20,30,40])
# s=pd.Series(l)
# print(s)

# using List
# l=[10,20,30,40]
# s=pd.Series(l)
# print(s)

#using Dictonary
D={"a":10,"b":20,"c":30}
s=pd.Series(D)
print(s)

# dt=[("a",10),("b",20)]
# print(dt)

# s=pd.Series(dt)
# print(s)

#Series of Attributes

#index
print(s.index)

#arrey
# print(s.array)

#values
print(s.values)

#name
# print(s.name)

# #shape
# print(s.shape)

# #ndim
# print(s.ndim)

# #size
# print(s.size)

# #nbyte
# print(s.nbytes)

#memory Uses
print(s.memory_usage())

#empty
# dg=[]
# s=pd.Series(dg)
# print(s.empty)


