#接收发送的信息，然后把消息返回给发送方
from socket import *

udpsocket = socket(AF_INET,SOCK_DGRAM)
bindAddr = ("",8087)
udpsocket.bind(bindAddr)
while True:
    revc = udpsocket.recvfrom(1024)
    content,dest = revc
    print(content.decode('GBK'))
    udpsocket.sendto(content,dest)

