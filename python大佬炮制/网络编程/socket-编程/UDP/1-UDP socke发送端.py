"""

import socket

#建立TCP套接字
tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("tcp socket建立成功")

#建立UDP套接字
tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("udp socket建立成功")

"""

#UDP socket简单实例

"""
from socket import *
#创建套接字 
udpsocket=socket(AF_INET,SOCK_DGRAM)

#准备接收方的地址
sendAddr=('127.0.0.1',8080)

#从键盘获取数据
while True:
    sendData = bytes(input("请输入你要发送的数据："),encoding="GBK")

#发送数据到指定的电脑上

    udpsocket.sendto(sendData,sendAddr)

#关闭套接字

udpsocket.close()


"""

from socket import *
udpsocket=socket(AF_INET,SOCK_DGRAM)
#str=bytes("我是张伟",encoding='UTF-8')  #转换编码
while True:
    str = input(":")

    udpsocket.sendto(str.encode("GBK"),('192.168.22.190',8081))    #

udpsocket.close()