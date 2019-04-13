import os

ret=os.fork()
print(ret)
if ret>0:
    print("---父进程---%s"%os.getpid())

else:
    print("---子进程---%s---%s"%(os.getpid(),os.getppid()))
