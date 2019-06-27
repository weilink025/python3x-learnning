#利用生成器实现
import time

def A():
    a=0
    while True:
        print("----A---")
        yield a
        time.sleep(0.5)

def B():
    b=0
    while True:
        print("----B---")
        yield b
        time.sleep(0.5)

if __name__=='__main__':

    a1=A()
    b1=B()
    while True:
        next(a1)
        next(b1)