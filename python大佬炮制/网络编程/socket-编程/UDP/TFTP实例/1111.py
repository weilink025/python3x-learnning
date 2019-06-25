import struct
from socket import *

clientSocket = socket(AF_INET,SOCK_DGRAM)

firstSend = struct.pack("!H7sb5sb".encode("UTF-8"),1,"TFTP客户端client.py".encode("UTF-8"),0,'octet'.encode("UTF-8"),0)

serverAddr = ('192.168.22.190',69)

clientSocket.sendto(firstSend,serverAddr)
