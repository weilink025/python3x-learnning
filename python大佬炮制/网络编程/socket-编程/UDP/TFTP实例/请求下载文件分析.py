#1、怎么完成下载
"""
1、创建一个空文件
2、向里面写数据
3、关闭




###大概思维####

from socket import *

udpsoket =socket(AF_INET,SOCK_DGRAM)

f = open("test.jpg","bw")

while True:
    recvData = udpsoket.recvfrom(1024)
    context,dest = recvData
    if lcontext大小 <516:
        #没有数据
        break
    else:
    #收到数据
        f.write(recvData)

"""

#2、怎么规定下载完成
#收到数据小于516个字节  (2个操作码，2个序列号，数据点512)，意味发送完毕


#3、如何保证操作码占两个字节

from socket import *
import struct
"""
udpsoket =socket(AF_INET,SOCK_DGRAM)

cmd_buf= struct.pack("!H8sb5sb".encode("UTF-8"),1,"test.jpg".encode("UTF-8"),0,"octet".encode("UTF-8"),0)

#“!”按网络数据  H 占两字节  “1替换H”,"test.jpg替换 8s","octet 替换 5s , "0替换b""

udpsoket.sendto(cmd_buf,('192.168.100.73',69))
##ret = struct.unpack("!H".encode("UTF-8"),cmd_buf[:2])  把操作码解析出来

"""

udpSocket = socket(AF_INET, SOCK_DGRAM)


#构造下载请求数据
cmd_buf = struct.pack("!H8sb5sb".encode("UTF-8"),1,"test.jpg".encode("UTF-8"),0,"octet".encode("UTF-8"),0)

#发送下载文件请求数据到指定服务器

udpSocket.sendto(cmd_buf,('192.168.100.73',69))
