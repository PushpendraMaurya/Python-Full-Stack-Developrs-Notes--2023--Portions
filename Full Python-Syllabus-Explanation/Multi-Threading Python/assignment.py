# # use without constructor to make parameter value
# import threading as th

# class Mythread1():
#     def __init__(self):
#         pass
#     def squar(self,ls):
#         ls = [1,2,3,4,5,6,7,8,9]
#         for i in self.ls:
#             print(f"square of {i} is {i**2}\t")


# class Mythread2():
#     def __init__(self):
#         pass
#     def cube(self,ls):
#         ls = [1,2,3,4,5,6,7,8,9]
#         for i in self.ls:
#             print(f"cube of {1} is {i**3}\t")

# m1 = Mythread1(squar)
# m2 = Mythread2(cube)
# t1 = th.Thread(target=m1.squar)
# t2 = th.Thread(target=m2.cube)
# t1.start()
# t2.start()

import threading as th

class Mythread1():
    def __init__(self):
        pass
    def squar(self):
        for i in range(1,10):
            print(f"square of {i} is {i**2}\t")


class Mythread2():
    def __init__(self):
        pass
    def cube(self):
        for i in range(1,10):
            print(f"cube of {1} is {i**3}\t")

m1 = Mythread1()
m2 = Mythread2()
t1 = th.Thread(target=m1.squar)
t2 = th.Thread(target=m2.cube)
t1.start()
t2.start