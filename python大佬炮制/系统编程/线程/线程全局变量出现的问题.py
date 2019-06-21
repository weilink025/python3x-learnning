from threading import Thread

import time

g_num = 0

def test1():
    global g_num
    for i in range(10000000):
        g_num+=1
    print("test1= %d" %g_num)
def test2():
    global g_num
    for i in range(10000000):
        g_num+=1
    print("test2= %d" % g_num)


p1 = Thread(target=test1)


p2 = Thread(target=test2)

p1.start()
##time.sleep(1)
p2.start()


#一个写没有执行完，另一个线程也在执行，所有变量取值可能会取到g_num=0的值
"""
结果：
test2= 10969133
test1= 11012215
"""