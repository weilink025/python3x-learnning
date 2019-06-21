#进程间通信  queues 队列

"""
    queue =  Queue(10)
    queue.put("aaaa")
    print(queue.qsize())
    print(queue.full())
    print(queue.empty())

    print(queue.get())

"""
"""
#Process创建的子进程，用队列通信
from multiprocessing import Queue,Process
import os
def func(queue,name):
    queue.put(name)
    print("子进程编号：%d 父进程编号：%d put一次" %(os.getpid(),os.getppid()))


if __name__ == "__main__":

    queue = Queue()
    print("父进程号%d" % os.getpid())

    for name in range(4):
        process = Process(target=func,args=(queue,name,))
        process.start()
        print("主进程%d get: %s" %( os.getpid(),queue.get()))

"""
#Pool创建的子进程，用队列通信

from multiprocessing import Manager,Pool
import os
from time import sleep

def func(queue,name):
    queue.put(name)
    print("子进程编号：%d 父进程编号：%d put:" %(os.getpid(),os.getppid()))
    sleep(5)

if __name__ == "__main__":

    pool = Pool(5)
    print("父进程号%d" % os.getpid())
    queue = Manager().Queue()    #与Pocess不同之处


    for name in range(10):
        process = pool.apply_async(func,(queue,name,))

    pool.close()

    pool.join()

    for name in range(10):
         print("主进程%d get: %s" %( os.getpid(),queue.get()))



