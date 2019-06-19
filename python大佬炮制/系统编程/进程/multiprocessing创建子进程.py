# multiprocessing创建子进程  使用此模块支持跨平台

#Process主进程会等子进程结束后再结束，而fork主进程时随时可以结束
from multiprocessing import Process
import os
import time


def test():
    while True:
        print("子进程中，pid=%d..%d." % (os.getpid(), os.getppid()))
        time.sleep(1)


p = Process(target=test)
p.start()

p.join()  #等创建的子进程执行完成后，主进程才会往下执行  #即  堵塞

#p.join(1)  #等待5秒

#p.terminate()   直接钉死进程


while True:
        print("---main---")
        time.sleep(1)


######################## 现实中常用
from multiprocessing import Process
import os

def run_proc(name):
    print('子进程运行中，name= %s,pid= %d...' %(name,os.getpid()))

if __name__ == '__main__':
    print('父进程 %d' % os.getpid())
    P=Process(target=run_proc,args=('test',))
    P.start()
    p.join()
    print("子进程已经结束")