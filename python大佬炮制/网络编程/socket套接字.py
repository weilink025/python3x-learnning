"""

import socket

#建立TCP套接字
tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("tcp socket建立成功")

#建立UDP套接字
tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("udp socket建立成功")

"""

#简单实例

from socket import *
#创建套接字
udpsocket=socket(AF_INET,SOCK_DGRAM)

#准备接收方的地址
sendAddr=('192.168.100.73',8080)

#从键盘获取数据
while True:
    sendData = bytes(input("请输入你要发送的数据："),encoding="UTF-8")

#发送数据到指定的电脑上

    udpsocket.sendto(sendData,sendAddr)

#关闭套接字

udpsocket.close()