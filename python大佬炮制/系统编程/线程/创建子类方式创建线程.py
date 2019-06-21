"""
#普通创建
import threading,time
import time

def saysorry():
    print("亲爱的我错了！！！！")
    time.sleep(1)

if __name__ == "__main__":
    start_time = time.time()
    for i in range(200):
        t = threading.Thread(target=saysorry)
        t.start()
    stop_time = time.time()

    print("耗时%f秒" % (stop_time-start_time))

"""

import threading ,time,os

class myThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm "+self.name + "@"+str(i)
            print(msg)


if __name__ == "__main__":
    t = myThread()
    t.start()


