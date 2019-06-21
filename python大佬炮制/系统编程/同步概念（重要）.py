#同步就是协同步调，按预定的先后次序进行运行。

#异步不确定执行次序

#同步的应用

from threading import Lock,Thread,current_thread
import time

class task1(Thread):
    def run(self):

        while True:
            if lock1.acquire():
                print("1--线程-%s" %current_thread().name)
                time.sleep(0.5)
                lock2.release()

class task2(Thread):

    def run(self):
        while True:
            if lock2.acquire():
                print("2--线程-%s" %current_thread().name)
                time.sleep(0.5)
                lock3.release()

class task3(Thread):
    def run(self):
        while True:
            if lock3.acquire():
                time.sleep(0.5)
                print("3--线程-%s" %current_thread().name)
                lock1.release()


if __name__ == "__main__":

    lock1 = Lock()
    lock2 = Lock()
    lock2.acquire()   #先锁上2
    lock3 = Lock()

    lock3.acquire()   #先锁上3

    task_1 = task1()
    task_2 = task2()
    task_3 = task3()

    task_1.start()
    task_2.start()
    task_3.start()


"""

先锁除1步后面全部要执行函数
执行完 第一步，马上给第二步解锁
执行完 第二步，马上给第三步解锁
.
.
.
.
执行完 最后一步，马上给第一步解锁

"""