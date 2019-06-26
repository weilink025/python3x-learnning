#udp 发送
"""
from socket import *

udpsocket = socket(AF_INET,SOCK_DGRAM)

udpsocket.sendto("在家吗".encode("gb2312"),('127.0.0.1',8080))

udpsocket.close()
"""

#udp server

"""
from socket import *

udp1 = socket(AF_INET,SOCK_DGRAM)

udp1.bind(('127.0.0.1',8088))

while True:
    ret=udp1.recvfrom(1024)

    ccontext,dest = ret

    print("%s:%s" % (dest,ccontext.decode('gb2312')))
    
    """

#tcp client
"""4
from socket import *

tcpsocket = socket(AF_INET,SOCK_STREAM)

tcpsocket.connect(('127.0.0.1',8080))

while True:
    sendData = input(":")
    tcpsocket.send(sendData.encode("gb2312"))
  """
#tcp server

from  socket import *

tcpsocket = socket(AF_INET,SOCK_STREAM)

tcpsocket.bind(('127.0.0.1',8089))

tcpsocket.listen(5)

newsocket,dest = tcpsocket.accept()

while True:
    ret = newsocket.recv(2048)

    print("%s:%s" % (dest,ret.decode('gb2312')))


