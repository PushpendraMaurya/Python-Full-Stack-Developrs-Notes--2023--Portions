import threading as th

class MyThread1(th.Thread):
    def __init__(self,ls):
        super().__init__()
        self.ls = ls

    def run(self):
        for i in  self.ls:
            print(f"squar of {i} is {i**2}")

class MyThread2(th.Thread):
    def __init__(self,ls):
        super().__init__()
        self.ls = ls

    def run(self):
        for i in  self.ls:
            print(f"cube of {i} is {i**3}")

ls = [1,2,3,4,5,6,7,8,9,10]
t1 = MyThread1(ls)
t2 = MyThread2(ls)
t1.start()
t2.start()