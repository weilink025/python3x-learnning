#简单聊天室功能
from socket import *
import datetime

udpsocket=socket(AF_INET,SOCK_DGRAM)

bindAddr=('',7782)  #绑定本机端口
udpsocket.bind(bindAddr)


while True:
    recvData=udpsocket.recvfrom(1024)
    context,destAddr=recvData
    #print(recvData)
    print(datetime.datetime.today(),destAddr,context.decode("GBK"))   #接收后，decode解码


