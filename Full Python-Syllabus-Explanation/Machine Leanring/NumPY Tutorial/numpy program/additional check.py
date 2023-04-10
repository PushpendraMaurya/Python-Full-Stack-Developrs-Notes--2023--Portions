import numpy as np
import sys
import time
start = time.time()
ls1 = list(range(10000))
ls2 = list(range(10000))

add = [i+j for i,j in zip(ls1,ls2)]

end = time.time()
result = (end - start) *1000
print(result)