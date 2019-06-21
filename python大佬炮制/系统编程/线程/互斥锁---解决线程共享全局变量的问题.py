#使用互斥锁---解决变量共享问题

from threading import Thread,Lock      #Lock锁模块


g_num = 0

def test1():
    global g_num
    locktest.acquire()    # 上锁
    for i in range(10000000):
        g_num+=1
    print("test1= %d" %g_num)
    locktest.release()     #解锁
def test2():
    global g_num
    locktest.acquire()   # 上锁
    for i in range(10000000):
        g_num+=1
    print("test2= %d" % g_num)
    locktest.release()       #解锁
locktest = Lock()  #创建一把互斥锁


p1 = Thread(target=test1)


p2 = Thread(target=test2)

p1.start()
##time.sleep(1)
p2.start()

#test1和test2 无论那方先执行，只要上锁后，另一方只能卡着，等待开锁后，才能执行另一个
