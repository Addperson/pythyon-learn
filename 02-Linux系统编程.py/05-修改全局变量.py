import os
import time
ret=os.fork()
g_num=100
if ret>0:
    print("---父进程---")
    time.sleep(3)
    print(g_num)
else:
    print("---子进程---")
    g_num+=100
    print(g_num)
print("---over---")
