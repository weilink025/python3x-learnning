from socket import *
from threading import Thread

tcpSocket = socket(AF_INET,SOCK_STREAM)


tcpSocket.connect(("127.0.0.1",8080))


def sendData():
    while True:
        try:
            sendata = input("")
            tcpSocket.send(sendata.encode("gb2312"))
        except OSError:
            print("通信结束！！")

while True:
    myThread = Thread(target=sendData)
    myThread.start()
    try:
        recvData = tcpSocket.recv(1024)
    except OSError:
        print("通信结束！！")
        break



    while len(recvData) == 0:

        tcpSocket.close()
        break
    else:

        print("%s" % recvData.decode('gb2312'))
