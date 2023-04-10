# rasie condition

import threading as th
balance = 0
def deposite(lock):
    global balance
    for i in range(100000):
        lock.acquire() # it is used to waiting for another threads.
        balance +=1
        lock.release() # it is used to passsed the  thread and insert wating Thread.
lock = th.Lock()

print(balance)
t1 = th.Thread(target=deposite,args=(lock,))
t2 = th.Thread(target=deposite,args=(lock,))


t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
