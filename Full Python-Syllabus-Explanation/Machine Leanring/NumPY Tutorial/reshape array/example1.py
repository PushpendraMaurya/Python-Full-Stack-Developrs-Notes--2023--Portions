# cinverting one to another dimentional arry


import numpy as np
arr1 = np.arange(1,9)
print(arr1.ndim)
print(arr1.shape)


arr2 = arr1.reshape(4,2)

print(arr2)

arr3 = arr1.reshape(2,4)
print(arr3)

arr4 = arr1.reshape(1,8)
print(arr4)

arr4 = arr1.reshape(-1,1)
print(arr4)