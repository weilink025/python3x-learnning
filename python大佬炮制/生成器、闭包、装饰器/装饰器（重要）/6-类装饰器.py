class Test(object):
    def __call__(self, *args, **kwargs):      #重写了call方法
        print("-—test---")

t=Test()
t()

#利用类来装饰函数

class tes(object):
    def __init__(self,func):
        print("---初始化---")
        print("func name is %s" %func.__name__)
        self.__func=func

    def __call__(self, *args, **kwargs):
        print("装饰器中的功能")
        self.__func()

@tes
def test():
    print("test")

test()