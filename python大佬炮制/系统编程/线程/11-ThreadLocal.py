#ThreadLocal 让全局变量不被多个线程共享
import threading

local_school = threading.local()

def func1():
    std = local_school.name
    print("%s--%s" %(std,threading.current_thread().name))

def func2(name):

    local_school.name = name
    func1()

t2 = threading.Thread(target=func2,args=("老王",))
t1 = threading.Thread(target=func2,args=("donge",))


t1.start()
t2.start()


#普通变量的无法传递
import threading

local_school = "111"


def func1():
    std = local_school
    print("最终打印：%s--%s" %(std,threading.current_thread().name))

def func2(name):

    local_school = name
    print("主函数打印值：%s" % local_school)
    func1()


t2 = threading.Thread(target=func2,args=("老王",))
t1 = threading.Thread(target=func2,args=("donge",))


t1.start()
t2.start()
