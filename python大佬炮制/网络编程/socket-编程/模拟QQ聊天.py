from socket import *
from threading import Thread


class sendFunc(Thread):
    def run(self):
        while True:
            incontext = input("<<")
            udpsocket.sendto(incontext.encode("GBK"),(dest,destPort))



class acceptFunc(Thread):
    def run(self):

        while True:
            rev = udpsocket.recvfrom(1024)
            context,destAddr = rev
            print(">> %s" % context.decode("GBK"))


if __name__ == "__main__":
    udpsocket = socket(AF_INET, SOCK_DGRAM)
    udpsocket.bind(("127.0.0.1", 8074))
    dest = input("对方IP地址：")
    destPort = int(input("端口"))
    sendstd = sendFunc()
    acceptstd = acceptFunc()
    sendstd.start()
    acceptstd.start()
