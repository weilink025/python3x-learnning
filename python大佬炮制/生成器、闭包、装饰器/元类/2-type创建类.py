#工作中具体不会用type来创建类，了解这个知识点
# 1,type查看通过哪个类创建的
type(1)  # int  说明1是通过int类创建出来的
type('abc')  # abc是通过str类创建出来的


class test():
    pass


a = test()

print(a)  # <__main__.test object at 0x000002226D3D65F8>
# a是通过test类创建出来的对象

##########################
# 2,type创建类

test1 = type('test1', (), {})  # （）是继承对象，{}属性

print(test1)  # <class '__main__.test1'>  他是一个类

##########################
#增加属性

test2 = type('test1', (), {'num': 10})  # 变量 num=10

print(test2)  # <class '__main__.test1'>  他是一个类

p2 = test2()
print(p2.num)  # 10

##########################
#定义方法

def printnum(self):
    print("---%d---" %self.num)

test3=type('test3',(),{"printnum":printnum})

p3=test3()
p3.num=20
p3.printnum()

##########################
#继承
class animals:
    def eat(self):
        print("---eatting---")

dog1=type('dog',(animals,),{})

wongcai=dog1()
wongcai.eat()    #wongcai.eat()

print(wongcai.__class__)
print(dog1.__class__)
print(type.__class__)
