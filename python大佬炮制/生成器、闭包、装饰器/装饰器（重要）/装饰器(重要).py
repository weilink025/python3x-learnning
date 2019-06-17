def w1(func):   #把函数当成变量传入到闭包内执行
    print('正在装饰w1')
    def inner():
        print("---正在验证权限1---")
        func()
    return inner

def w2(func):   #把函数当成变量传入到闭包内执行
    print('正在装饰w2')
    def inner():
        print("---正在验证权限2---")
        func()
    return inner

@w1     #两修饰器   解析器执行这到里时，就已经进行了装饰了。 调用时，函数已经装修完了。
@w2
def f1():
    print("f1")

@w1
def f2():
    print("f2")


f2()

f1()
