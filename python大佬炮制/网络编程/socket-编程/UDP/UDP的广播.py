from socket import *

dest = ('<broadcast>',8080)

udpsocket = socket(AF_INET,SOCK_DGRAM)

udpsocket.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

udpsocket.sendto("hi world".encode("UTF-8"),dest)

print("等待对方回复！！")

while True:
    buf,address = udpsocket.recvfrom(1024)
    print("Received from %s:%s" %(address,buf))