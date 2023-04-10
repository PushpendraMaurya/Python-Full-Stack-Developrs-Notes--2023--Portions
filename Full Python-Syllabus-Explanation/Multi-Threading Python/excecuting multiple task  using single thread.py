import threading as th

class Mythread1(th.Thread):
    def __init__(self):
        super().__init__()
        self.squar()
        self.cube()
    def squar(self):
        for i in range(1,10):
            print(f"square of {i} is {i**2}\t")

    
    def cube(self):
        for i in range(1,10):
            print(f"cube of {1} is {i**3}\t")

m1 = Mythread1()
m1.start()
