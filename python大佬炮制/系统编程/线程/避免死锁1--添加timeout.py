#方法1

from threading import Thread,Lock
import time

class myTread1(Thread):
    def run(self):
        mutexA.acquire()
        time.sleep(2)   #暂停个2秒

        if mutexB.acquire(timeout=3):

            mutexB.release()

        mutexA.release()


class myTread2(Thread):
    def run(self):
        mutexB.acquire()
        if mutexA.acquire(timeout=3):
             mutexA.release()
        mutexB.release()

mutexA  = Lock()
mutexB  = Lock()

if __name__ == "__main__":
    t1 =  myTread1()
    t2 = myTread2()
    t1.start()
    t2.start()




