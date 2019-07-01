from socket import *
from multiprocessing import Process



#接收数据，并给客户端发送数据
def revcfun(newSocket,destAddr):

    recvData = newSocket.recv(1024)
    if recvData:

        recvGetLocal = recvData.decode().split("\r\n")
        pathLocal = recvGetLocal[0].split(" ")
        getfile = pathLocal[1]
        htmlRootDir = 'html'

        try:
            sendfile = open(htmlRootDir+getfile,"rb")
            print(getfile)
        except IOError:

            responseFirst = "HTTP/1.1 404 Not Found\r\n"
            responseHeards = "server: myserver \r\n"
            responseBody = "对访问出错！！"

        else:
            filedata = sendfile.read()
            responseFirst = "HTTP/1.1 200 OK \r\n"
            responseHeards = "server: myserver \r\n"
            responseBody = filedata.decode("utf-8")

        response = responseFirst+responseHeards+ "\r\n" +responseBody
        print(response)
        newSocket.send(bytes(response,"utf-8"))
        newSocket.close()

    else:
        newSocket.close()








#开启监听端口，多进程等客户端连接
if __name__ == '__main__':

    serSocket = socket(AF_INET,SOCK_STREAM)

    serSocket.bind(("",8088))

    serSocket.listen(1024)
    while True:
        newSocket,destAddr = serSocket.accept()
        p = Process(target=revcfun,args=(newSocket,destAddr))
        p.start()
        newSocket.close()




