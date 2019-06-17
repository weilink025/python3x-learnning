#不建议这样写，因为类是一等公民
def choose_class(name):
    if name=='foo':
        class Foo(object):
            def __init__(self,a,b):
                self.a=a
                self.b=b
            def func(self):
                return self.a+self.b

        return Foo    #返回的是类，不是类实例

    else:
        class Bar(object):
            print('--2--')
        return Bar

Myclass=choose_class('foo')   #Myclass接收返回的类的对象

a=Myclass(1,2)   #实例化类
print(a.func())


