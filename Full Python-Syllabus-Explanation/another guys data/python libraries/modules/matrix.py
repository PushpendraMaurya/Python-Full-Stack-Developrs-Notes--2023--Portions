import numpy as np

a=np.matrix("1,2;3,4")
print(a)

b=np.matrix([[10,20],[10,54]])
print(b)

print("addition:-",a+b)
print("subtraction:-",a-b)
print("multiplication:-",a*b)

print(a.T)
print(b.T)