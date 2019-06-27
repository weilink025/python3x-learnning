from socket import *
from threading import Thread


def cli_ser(newSocket,clientAddr):
    while True:
        recvData = newSocket.recv(1024)
        if len(recvData) > 0:
            print("一个新客户端到来 ")
            print(recvData)
        else:
            print("没有数据关闭连接")
            break
    newSocket.close()


def main():
    tcpSocket = socket(AF_INET, SOCK_STREAM)

    tcpSocket.bind(("", 8822))

    tcpSocket.listen(10)

    tcpSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 服务器先挥手时需要加这一句

    try:
        while True:

            newSocket, clientAddr = tcpSocket.accept()

            myTread = Thread(target=cli_ser,args=(newSocket,clientAddr))

            myTread.start()

            #newSocket.close()   #不能关闭，因为线程都共享这个变量

    except:
        pass
    finally:
        tcpSocket.close()

if __name__ == "__main__":
    main()