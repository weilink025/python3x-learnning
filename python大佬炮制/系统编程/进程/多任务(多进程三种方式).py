#第一个种方式 fork()，只支持类unix操作系统
"""
import os

ret=os.fork()    #主进程一旦执行完会直接退出
if ret==0:
    print('1')
else:
    print('2')

"""
#第二个种方式 Process
"""
from multiprocessing import Process
import os

def proc():
    print("我是子程序：%d，我的父进程:%d." %(os.getpid(),os.getppid()))

if __name__ == "__main__":
    print("我是的父进程：%d" %os.getpid())
    processtest = Process(target=proc)
    processtest.start()

    processtest.join()

    print("进程执行结")
"""
#第三种方式 pool进程池

from multiprocessing import Pool
import os

def proc():
    print("我是子程序：%d，我的父进程:%d." %(os.getpid(),os.getppid()))

if __name__ == "__main__":
    print("我是的父进程：%d" % os.getpid())
    pooltest = Pool(3)

    for i in range(10):
        pooltest.apply_async(proc)

    pooltest.close()
    pooltest.join()
