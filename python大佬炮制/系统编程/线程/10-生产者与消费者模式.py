#生产者和消费者问题解决

from queue import Queue
from threading import Thread,current_thread
from time import sleep

class Producer(Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() <100:
                for i in range(50):
                    queue.put("%s-生产产品-%d" %(current_thread().name,i))
                    print("%s-生产产品-%d" %(current_thread().name,i))

class Customer(Thread):
    def run(self):
        global queue
        while True:

            if queue.qsize() > 50:
                for i in range(3):
                    print("-%s-消耗了%s" %(current_thread().name,queue.get()))




if __name__ == "__main__":

    print("开始")
    queue = Queue()

    for i in range(200):
        queue.put("初始产品-%d" %i)

    for i  in range(2):
        prouducer = Producer()
        prouducer.start()

    for i  in range(5):
        customer = Customer()
        customer.start()



