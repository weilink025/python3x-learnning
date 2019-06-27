from builtins import print
from socket import *
from socket import socket


def main():
    tcpsocket = socket(AF_INET,SOCK_STREAM)

    tcpsocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    tcpsocket.setblocking(False)  #被动socket设置为非阻塞

    tcpsocket.bind(('',8812))

    tcpsocket.listen(10)

    socketList = []
    while True:

        try:


            newSocket,destAddr = tcpsocket.accept()

        except:
            pass
        else:
            print("新客户到来")

            newSocket.setblocking(False)   #客户端socket设置为非阻塞
            socketList.append(newSocket)

        for newSocket in socketList:
            try:
                revcData = newSocket.recv(1024)
                if revcData:
                    print(revcData)
                else:
                    newSocket.close()
                    socketList.remove(newSocket)



            except:
                pass

if __name__ == "__main__":
    main()