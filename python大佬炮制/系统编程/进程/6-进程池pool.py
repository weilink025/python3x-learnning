from multiprocessing import Pool
import os,time,random

def work(msg):
    t_start = time.time()
    print("%s开始执行，进程号为%d" %(msg,os.getpid()))
    time.sleep((random.random()*2))
    t_stop=time.time()
    print(msg,"执行完毕,耗时%0.2f" %(t_stop - t_start))


if __name__ == "__main__":     #注意一定要加上这个判断，否则win平台无法执行

    po=Pool(5) #表示进程池最多有5个进程同时执行

    for i in range(0,10):

        po.apply_async(work,(i,))     #非堵塞
        #po.apply(work,(i,))    #堵塞，进程一个执行完。不会并发执行，几乎不用。

    print("---start----")
    po.close()  #关闭进程池，不能够再向进程池添加新任务了
    po.join()    #堵塞，保证主进程不结束。让进程池子进程完成任务。
    print("---end----")