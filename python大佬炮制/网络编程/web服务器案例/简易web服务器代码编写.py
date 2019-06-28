from socket import *
from multiprocessing import Process


#接收数据，并给客户端发送数据
def revcfun(newSocket,destAddr):
    """处理客户端请求"""
    while True:


        recvData = newSocket.recv(1024)
        if recvData:

            recvGetLocal = recvData.decode().split("\r\n")
            pathLocal = recvGetLocal[0].split(" ")
            getfile = pathLocal[1]
            htmlRootDir = 'html'

            try:
                sendfile1 = open(htmlRootDir+getfile,"r")
                readLines = sendfile1.read()
                newSocket.send(("HTTP1.1 200 OK \r\n "+ readLines).encode())
            except:

                newSocket.send(("HTTP1.1 404 NOT FOUND \r\n ").encode())


        else:
            break
    newSocket.close()


#开启监听端口，多进程等客户端连接
if __name__ == '__main__':

    serSocket = socket(AF_INET,SOCK_STREAM)

    serSocket.bind(("",8081))

    serSocket.listen(1024)
    while True:
        newSocket,destAddr = serSocket.accept()

        p = Process(target=revcfun,args=(newSocket,destAddr))
        p.start()
    serSocket.close()




