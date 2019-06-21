

import time
start_time = time.time()
def saysorry():
    print("亲爱的我错了！！！！")
    time.sleep(1)

if __name__ == "__main__":
    start_time = time.time()
    for i in range(5):
        saysorry()
    stop_time = time.time()

    print("耗时%f秒" % (stop_time - start_time))    #耗时5秒多


#Threading线程优势
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

    print("耗时%f秒" % (stop_time-start_time))   #耗时0.027894秒
