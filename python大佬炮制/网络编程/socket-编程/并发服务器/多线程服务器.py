from socket import *

tcpSocket = socket(AF_INET,SOCK_STREAM)

tcpSocket.bind(("",8800))

tcpSocket.listen(10)

tcpSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)  #服务器先挥手时需要加这一句

recvData = ""
def cli_ser(*args,**kwargs):
    while True:
        recvData = newSocket.recv(1024)
        if recvData:
            print(recvData)
        else:
            break



while True:
    newSocket, clientAddr = tcpSocket.accept()
    cli_ser(newSocket,clientAddr)



