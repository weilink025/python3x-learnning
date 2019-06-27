from socket import *
import threading

def sendtoData(clientSocket):
    for j in range(10000):
        clientSocket.send(('data-'+str(j)).encode())


if __name__ == '__main__':

    clientSocket = socket(AF_INET,SOCK_STREAM)

    destAddr = input("输入IP:")
    destPort = int(input("输入PORT:"))

    testNum = int(input("输入请求次数："))

    for i in range(testNum):
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((destAddr,destPort))
        p1 = threading.Thread(target=sendtoData,args=(clientSocket,))
        p1.start()




