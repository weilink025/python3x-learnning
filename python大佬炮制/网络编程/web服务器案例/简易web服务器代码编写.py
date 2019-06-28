from socket import *
from multiprocessing import Process


def revcfun(newSocket,destAddr):

    while True:

        recvData = newSocket.recv(1024)
        if recvData:

            print(recvData.decode("gb2312"))

        else:
            break
    newSocket.close()


if __name__ == '__main__':

    serSocket = socket(AF_INET,SOCK_STREAM)

    serSocket.bind(("",8080))

    serSocket.listen(1024)
    while True:
        newSocket,destAddr = serSocket.accept()
        p = Process(target=revcfun,args=(newSocket,destAddr))
        p.start()
    serSocket.close()




