from socket import *
from multiprocessing import Process


#接收数据，并给客户端发送数据
def revcfun(newSocket,destAddr):
    """处理客户端请求"""

    recvData = newSocket.recv(1024)
    if recvData:

        recvGetLocal = recvData.decode().split("\r\n")
        pathLocal = recvGetLocal[0].split(" ")
        getfile = pathLocal[1]
        htmlRootDir = 'html'

        try:
            file = open(htmlRootDir + getfile, "rb")
        except IOError:
            response_start_line = "HTTP/1.1 404 Not Found\r\n"
            response_headers = "Server: My server\r\n"
            response_body = "The file is not found!"
        else:
            file_data = file.read()
            file.close()

            # 构造响应数据
            response_start_line = "HTTP/1.1 200 OK\r\n"
            response_headers = "Server: My server\r\n"
            response_body = file_data.decode("utf-8")

        response = response_start_line+response_headers+response_body
        newSocket.send(bytes(response,"utf-8"))
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
        serSocket.close()




