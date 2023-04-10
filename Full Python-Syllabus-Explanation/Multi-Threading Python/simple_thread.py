#check main thread
import threading as th

# simple Example,,,,,,,,,,,,,
def squar(ls):
    for i in ls:
        print(f"squar of {i} is {1**2}\t")


def cube(ls):
    for i in ls:
        print(f"cube of {i} is {i**3}\t")

ls = [1,2,3,4,5,6,7,8]
squar(ls)
cube(ls)
