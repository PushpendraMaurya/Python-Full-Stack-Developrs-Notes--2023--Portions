import numpy as np
import sys
import time
start = time.time()
ls = list(range(10000))

arr = np.arange(10000)

add = arr + ls

end = time.time()

result = (end - start)

a = result*1000

print(a)