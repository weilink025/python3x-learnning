class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat(self):
        print("----%s-正在吃---" %self.name)


def run(self):
    print("----%s-正在跑----" %self.name)
p1=Person("wade",30)
p1.eat()

p1.run=run

#p1.run()   #虽然p1对你中的run属性指向run函数，但是这句代码还不正确
            #因为run属性指向的函数，最后来添加的p1.run()的时候，并没有把p1当做第1个参数传递进去

from types import MethodType   #导入库

p1.run=MethodType(run,p1)     #函数绑定到p1对象
p1.run()

