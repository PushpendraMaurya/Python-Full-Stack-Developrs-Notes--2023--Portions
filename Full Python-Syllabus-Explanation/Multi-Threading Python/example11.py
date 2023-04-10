import threading as th
class MyThread1(th.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        print(f"1- Thread Name is :{th.current_thread().name}")
        th.current_thread().name = "Squar Thread"
        print(f"1- Thread Name is :{th.current_thread().name}")

class MyThread2(th.Thread):
    
    def __init__(self):
        super().__init__()

    def run(self):    
        print(f"2- Thread Name is :{th.current_thread().name}")
        th.current_thread().name = "Cube Thread"
        print(f"2- Thread Name is :{th.current_thread().name}")

t1 = MyThread1()
t2 = MyThread2()

t1.start()
t2.start()
print(f"3- Thread Name is :{th.current_thread().name}")