######################## 现实中常用
from multiprocessing import Process
import os

def run_proc(name):
#    while True:
        print('子进程运行中，name= %s,pid= %d...' %(name,os.getpid()))

if __name__ == '__main__':
    print('父进程 %d' % os.getpid())
    P=Process(target=run_proc,args=('test',))
    P.start()   #启动子进程
    P.join()    #等子进程结束，主进程才往下执行
    print("子进程已经结束")