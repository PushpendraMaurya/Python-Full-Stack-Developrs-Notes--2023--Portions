import threading as th

class MyThread1(th.Thread):
    def __int__(self):
        super().__init__()

    def run(self):
        for i in  range(1,10):
            print(f"squar of {i} is {i **2}\t")
 
class MyThrea2(th.Thread):
    
    def __int__(self):
        super().__init__()

    def run(self):
        for i in  range(1,10):
            print(f"cube of {i} is {i **3}\t")

t1 = MyThread1()
t2 = MyThrea2()
t1.start()
t2.start()
