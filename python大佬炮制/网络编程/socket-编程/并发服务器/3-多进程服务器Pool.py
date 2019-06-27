from socket import *
import os
from multiprocessing import Pool
import time


def cli_ser(newSocket,dest):
    while True:
            print("一个新客户端到来 %d" % os.getpid())
            newrcv = newSocket.recv(1024)

            if newrcv:
                print(newrcv,dest)
            else:

                break

    newSocket.close()



if __name__ == "__main__":
    tcpSocket = socket(AF_INET,SOCK_STREAM)

    tcpSocket.bind(("",8887))

    tcpSocket.listen(10)

    tcpSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)  #服务器先挥手时需要加这一句


    processPool = Pool(10)   #只有十个进程
    try:
        while True:


            newSocket, clientAddr = tcpSocket.accept()
            print("一个新客户端到来 %d" % os.getpid())
            processPool.apply_async(cli_ser,(newSocket,clientAddr,))
            time.sleep(2)  #这里先休眠两秒
            #processPool.close()
            newSocket.close() #这里不能关闭  因为不确定子进程和主进程那个先执行，可能变量还没有传进去就已经关了




    except:
            pass
    finally:
        tcpSocket.close()





