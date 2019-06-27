from socket import *
import os
from multiprocessing import Pool,Process



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

    tcpSocket.bind(("",8881))

    tcpSocket.listen(10)

    tcpSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)  #服务器先挥手时需要加这一句


    #processPool = Pool(1)
    try:
        while True:


            newSocket, clientAddr = tcpSocket.accept()
            print("一个新客户端到来 %d" % os.getpid())
            Prs = Process(target=cli_ser,args=(newSocket,clientAddr))
            Prs.start()
            #processPool.apply_async(cli_ser,(newSocket,clientAddr,))
            newSocket.close()
    except:
            pass
    finally:
        tcpSocket.close()





