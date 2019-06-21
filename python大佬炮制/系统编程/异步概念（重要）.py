#同步调用就是你喊你朋友吃饭，你朋友在忙，你就一直在那等，等你朋友忙完了，你们一起去
#异步就是你喊你朋友吃饭，你朋友说知道了，等会忙完去找你，你就去做别的

from multiprocessing import Pool
import time
import os

def func1():
    print("---进程池的进程----pid=%d,ppid=%d---" %(os.getpid(),os.getppid()))
    for i in range(3):
        print("---%d---" %i)
        time.sleep(1)
    return "haha"      #return的参数返回去主进程了
"""
子进程3秒后，执行完继续

"""

def func2(arg):          #通过主进程传入arg的值
    print("----callback func --pid=%d"%os.getpid())
    print("----callback func --arg=%s" % arg)

if __name__ == '__main__':
    pool =Pool(3)
    pool.apply_async(func=func1,callback=func2)

    time.sleep(6)   #子进程，主进程还在执行sleep，callback马上让主进程离开自己的任务，去处理func2的任务。

    pool.close()
    pool.join()