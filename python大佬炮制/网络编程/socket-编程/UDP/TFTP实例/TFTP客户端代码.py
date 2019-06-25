#coding=utf-8

from socket import *
import struct
import sys


"""
#python xxx.py 192.168.100.37 在命令执行参数是获取参数的值

if len(sys.argv) != 2:
    print('-'*30)
    print("tips:")
    print("python xxxx.py 192.168.1.1")
    print('-'*30)
    exit()
else:
    ip = sys.argv[1]
    
    

"""
# 创建udp套接字
udpSocket = socket(AF_INET,SOCK_DGRAM)

cmd_buf = struct.pack("!H8sb5sb".encode("UTF-8"),1,"test.jpg".encode("UTF-8"),0,"octet".encode("UTF-8"),0)

udpSocket.sendto(cmd_buf,('192.168.100.73',69))

p_num = 0

recvFile = ''

while True:
    recvData,recvAddr = udpSocket.recvfrom(1024)

    recvDataLen = len(recvData)

    #print (recvAddr) # for test

    #print (len(recvData)) # for test

    cmdTuple = struct.unpack("!HH".encode("UTF-8"),recvData[:4])

    # print cmdTuple # for test


    cmd = cmdTuple[0]
    currentPackNum = cmdTuple[1]

    if cmd == 3: #是否为数据包

        # 如果是第一次接收到数据，那么就创建文件
        if currentPackNum == 1:
            recvFile = open("test.jpg", "ab")   #以二进行接收数据

        # 包编号是否和上次相等
        if p_num+1 == currentPackNum:
            recvFile.write(recvData[4:]);
            p_num +=1
            print ('(%d)次接收到的数据' %(p_num))

            ackBuf = struct.pack("!HH",4,p_num)

            udpSocket.sendto(ackBuf, recvAddr)
        # 如果收到的数据小于516则认为出错
        if recvDataLen<516:
            recvFile.close()
            print( '已经成功下载！！！')
            break

    elif cmd == 5: #是否为错误应答
        print ("error num:%d"%currentPackNum)
        break

udpSocket.close()