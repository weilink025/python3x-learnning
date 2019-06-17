#使用装饰器对有返回值的函数进行装饰
def func(funname):
    def funcin(*args,**kwargs):
        print("11111")
        test1=funname(*args,**kwargs)        #用一个变量接收函数返回值
        return test1
    return funcin



@func
def fun1(a,b):
    print("--我是主函数--")
    return a+b


print(fun1(11,33))