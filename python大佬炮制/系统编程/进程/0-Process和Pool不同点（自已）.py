from multiprocessing import Process,Pool
import time
def printtest(i):
    time.sleep(3)
    print(i)

def main():
    MyProcess = Process(target=printtest,args=(1,))

    MyProcess.start()




if __name__ == "__main__":
    main()

#结果只打印了“1”

"""
MyProcess没有start()之前，就是已经把要传递的参数传递给了，子进程。

而pool不需要start 主进程已经结束了，子进程也没有收到参数。主进程先于子进程结束，于是子进程也不执行了

"""