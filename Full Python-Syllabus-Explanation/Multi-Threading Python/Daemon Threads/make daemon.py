import threading as th

import time 

class MyThread(th.Thread):
    def __init__(self):
        super().__init__()


    def run(self):
        count = 0
        while True:
            time.sleep(1)
            if count == 60:
                break

            else:
                count +=1
                print(f"Second Thread{count}")

t1 = MyThread()
t1.setDaemon(True)
t1.start()

name  = input("ENter Your Name :")
print(f"Name is {name}")