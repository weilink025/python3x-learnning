class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat(self):
        print("----%s-正在吃---" %self.name)

@staticmethod
def test():
    print("---static method----")

Person.test=test                #静态类绑定到类上去

p1=Person('wade',20)
p1.test()