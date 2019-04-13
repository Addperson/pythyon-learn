import os
import time
ret=os.fork()
print(ret)
if ret>0:
    print("---父进程---%s"%os.getpid())
    time.sleep(3)
else:
    print("---子进程---%s---%s"%(os.getpid(),os.getppid()))
    time.sleep(6)

print("---over---")
