from socket import *

tcpSocket = socket(AF_INET,SOCK_STREAM)

tcpSocket.bind(("192.168.100.73",8081))

tcpSocket.listen(5)

newSocket,destAddr=tcpSocket.accept()   #newsocket新客户端的套接字，destAddr 新客户端的IP和port
while True:
    recvData = newSocket.recv(1024)

    print(destAddr,recvData.decode("gb2312"))


newSocket.close()
tcpSocket.close()