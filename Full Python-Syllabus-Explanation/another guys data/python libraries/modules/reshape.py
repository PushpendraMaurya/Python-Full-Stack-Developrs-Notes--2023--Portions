import numpy as np

a=np.arange(0,10)
print(a,"diamension:-",a.ndim)

b=np.reshape(a,(2,5),order="f")
print(b,"diamension:-",b.ndim)
