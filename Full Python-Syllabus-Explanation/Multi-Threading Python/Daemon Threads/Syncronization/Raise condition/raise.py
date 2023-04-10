#  

import threading as th
balance = 0
def deposite():
    global balance
    for i in range(100000):
        balance +=1



print(balance)
t1 = th.Thread(target=deposite)
t2 = th.Thread(target=deposite)

t1.start()
t2.start()
print(balance)
