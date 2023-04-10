import numpy as np
import sys
ls = list(range(10000))

arr = np.arange(10000)

memory_list = sys.getsizeof(ls[1])*len(ls)
print(memory_list)


memory_arr = arr.itemsize * arr.size

print(memory_arr)


