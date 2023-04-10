#check main thread
import threading as th

print("check main thread")

# t1 = th.current_thread().getName()

t1 = th.current_thread().name
print(t1)