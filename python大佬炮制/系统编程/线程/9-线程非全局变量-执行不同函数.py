from threading import Thread,current_thread

import time

g_num = 0

def test1(g_num):

    for i in range(1000):
        g_num+=1
    print("test1= %d 当前线程 %s" %(g_num,current_thread().name))
def test2(g_num):
    for i in range(10000000):
        g_num+=1
    print("test2= %d 当前线程 %s" % (g_num, current_thread().name))


p1 = Thread(target=test1,args=(g_num,))


p2 = Thread(target=test2,args=(g_num,))

p1.start()
##time.sleep(1)
p2.start()

time.sleep(5)
print(g_num)


#结果：
"""
test1= 10000000 当前线程 Thread-1
test2= 10000000 当前线程 Thread-2

"""
