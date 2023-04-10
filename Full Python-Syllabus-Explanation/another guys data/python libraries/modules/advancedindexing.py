import numpy as np

a=np.arange(1,10)

# index=np.array([1,6,4])
# print(a[index])

a=np.array([[1,-2,3],[4,-2,-3]])
print(a.ndim)
print(a[a<0])
