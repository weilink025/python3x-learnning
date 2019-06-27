#遇到耗时操作会自动切换
import gevent

def f(n):
    for i in range(n):
        print(str(i),gevent.getcurrent())
        gevent.sleep(1)  #一个协程遇到耗时操作，会先让另一个协程执行

g1=gevent.spawn(f,5)
g2=gevent.spawn(f,5)
g3=gevent.spawn(f,5)

g1.join()
g2.join()
g3.join()

