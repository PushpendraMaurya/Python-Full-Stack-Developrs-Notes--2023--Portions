import numpy as np

# a=np.array([[[1,2,3],[3,4,5]],[[6,7,8],[8,9,10]]])
# print(a,a.ndim)
# print(a.flatten(order="c"))

a=np.array([[[1,2,3],[3,4,5]],[[6,7,8],[8,9,10]]])

af=a.flatten()
print(af)
af[2]=45
print(a)