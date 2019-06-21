from threading import Thread,Lock
import time

class myTread1(Thread):
    def run(self):
        mutexA.acquire()        #第一步：   mutexA 上锁了
        time.sleep(2)   #暂停个2秒
        if mutexB.acquire():      #第三步     本函数要到mutexB解锁后才能上锁
            mutexB.release()

        mutexA.release()


class myTread2(Thread):
    def run(self):
        mutexB.acquire()      #第二步：    mutexB 上锁了
        if mutexA.acquire():      #第四步     本函数要到mutexA解锁后才能上锁
            mutexA.release()
        mutexB.release()
mutexA  = Lock()
mutexB  = Lock()

if __name__ == "__main__":
    t1 =  myTread1()
    t2 = myTread2()
    t1.start()
    t2.start()


    #此时就造成互相锁死   函数1  锁A要解锁必须先给B上锁（函数2必须要解锁B锁）
                        # 函数2  锁B要解锁必须先给A上锁（函数1必须要解锁B锁）

