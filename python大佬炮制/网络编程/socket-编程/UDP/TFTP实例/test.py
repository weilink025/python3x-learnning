from socket import *
import struct
udpSocket = socket(AF_INET, SOCK_DGRAM)


#构造下载请求数据
cmd_buf = struct.pack("!H8sb5sb".encode("UTF-8"),1,"test.jpg".encode("UTF-8"),0,"octet".encode("UTF-8"),0)

#发送下载文件请求数据到指定服务器

udpSocket.sendto(cmd_buf,('192.168.100.73',69))