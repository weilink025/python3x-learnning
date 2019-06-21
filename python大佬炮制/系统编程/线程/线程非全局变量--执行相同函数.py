from threading import Thread,current_thread

import time

g_num = 1

def test1(g_num):

    for i in range(3):
        if current_thread().name == "Thread-1":     #线程是thread-1：g_num加1
            g_num+=1
            print("test1= %d 当前线程 %s" %(g_num,current_thread().name))

        if current_thread().name != "Thread-1":    #线程不是thread-1：直接输出g_num
            g_num+=1
            print("test1= %d 当前线程 %s" % (g_num, current_thread().name))

p1 = Thread(target=test1,args=(g_num,))
p2 = Thread(target=test1,args=(g_num,))
p1.start()

p2.start()


#结果：
"""
test1= 2 当前线程 Thread-1
test1= 3 当前线程 Thread-1
test1= 4 当前线程 Thread-1
test1= 1 当前线程 Thread-2
test1= 1 当前线程 Thread-2
test1= 1 当前线程 Thread-2

结果证明 函数内部的非共享变量，线程调用是也是隔离的，各个线程独占用一份代码

"""
