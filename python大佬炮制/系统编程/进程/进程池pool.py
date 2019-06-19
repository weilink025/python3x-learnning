from multiprocessing import Pool
import os,time,random

def work(msg):
    t_start = time.time()
    print("%s开始执行，进程号为%d" %(msg,os.getpid()))
    time.sleep((random.random()*2))
    t_stop=time.time()
    print(msg,"执行完毕,耗时%0.2f" %(t_stop - t_start))


if __name__ == "__main__":     #注意一定要加上这个判断，否则win平台无法执行
    po=Pool(5)

    for i in range(0,10):
        po.apply_async(work,(i,))


    print("---start----")
    po.close()
    po.join()
    print("---end----")