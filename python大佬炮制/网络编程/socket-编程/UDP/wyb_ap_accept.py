# coding=utf-8

from socket import *
import datetime
from multiprocessing import Pool
import os

def acceptData(udpSocket,recvData):
    # 创建udp套接字
        apData = recvData.hex()
        a = apData.split("cc83")
        a = a[2:]
        aLen = len(a)
        print(os.getpid())
        for i in range(aLen):
            print("AP_MAC:   %s,  client_MAC:   %s,  RSSI:   %d,  噪声:   %d,  时间:   %s" % (
                a[i][12:24], a[i][28:40], int(a[i][60:62], 16) - 256, int(a[i][62:64], 16) - 256,
                datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

        udpSocket.close()


if __name__ == "__main__":
    processPool = Pool(10)
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    udpSocket.bind(("", 7728))
    while True:
        recvData, recvAddr = udpSocket.recvfrom(2048)
        if recvData:
            processPool.apply_async(acceptData,(udpSocket,recvData))
    udpSocket.close()
