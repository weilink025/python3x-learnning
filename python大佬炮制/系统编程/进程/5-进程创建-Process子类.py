######################## 现实中常用

"""
from multiprocessing import Process
import os

def run_proc(name):
        #功能写了函数中

        print('子进程运行中，name= %s,pid= %d...' %(name,os.getpid()))

if __name__ == '__main__':
    print('父进程 %d' % os.getpid())
    P=Process(target=run_proc,args=('test',))
    P.start()   #启动子进程
    P.join()    #等子进程结束，主进程才往下执行
    print("子进程已经结束")

"""

######################## 把函数放类中实现

from multiprocessing import Process
import os
class Process_class(Process):
    def __init__(self,interval):     #重写 init方法
        Process.__init__(self)    #把Process的  init的方法传递进来
        self.interval = interval

    #重写Process类的run()方法

    def run(self):
            ##功能写在了类中
            print('子进程运行中，name= %s,pid= %d...' % (self.interval, os.getpid()))


if __name__ == '__main__':
    print('父进程 %d' % os.getpid())
    P = Process_class(2)
    P.start()  # 启动子进程  会调用重写后的run()方法
    P.join()  # 等子进程结束，主进程才往下执行
    print("子进程已经结束")
