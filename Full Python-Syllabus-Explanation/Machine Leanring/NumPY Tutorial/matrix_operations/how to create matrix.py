import  numpy as np
m1 = np.matrix("1,2,3 ;4,5,6")

# print(m1)

m2 = np.matrix("1,2,3 ;4,5,6")
# print(m2)
print()
# print(type(m1))
print(m1 +m2)
print()
print(m1 - m2)
print()

m3 = m2.T
print(m3)
print(m2)

print(m1*m3)