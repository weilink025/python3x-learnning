def test1(arg):
    def test0(funmae):

        def test2(*args,**kwargs):
            if arg==1:
                print('---test---',arg)     #调用装饰器传进来的参数

                ret=funmae(*args,**kwargs)
                return ret
            else:
                print('---test2---', arg)  # 调用装饰器传进来的参数

                ret = funmae(*args, **kwargs)
                return ret
        return test2

    return test0

"""

@test1("我是一个带参数的装饰器")   #先处理test1("我是一个带参数的装饰器")这个函数再装饰。
def printone(a,b):
    print("---2--")
    return a+b

printone(11,22)

"""

#带装饰器，可以通过判断参数，来决定装修效果

@test1(1)   #先处理test1("我是一个带参数的装饰器")这个函数再装饰。
def printone1(a,b):
    print("---2--")
    return a+b

printone1(11,22)

@test1(2)   #先处理test1("我是一个带参数的装饰器")这个函数再装饰。
def printone2(a,b):
    print("---2--")
    return a+b

printone2(11,22)