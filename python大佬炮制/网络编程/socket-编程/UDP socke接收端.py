#接收端绑定端口
from socket import *
udpsocket=socket(AF_INET,SOCK_DGRAM)

bindAddr=('',7781)  #绑定本机端口
udpsocket.bind(bindAddr)

while True:
    recvData=udpsocket.recvfrom(1024)
    context,destAddr=recvData
    #print(recvData)
    print(context.decode(encoding="GBK"))   #接收后，decode解码

udpsocket.close()