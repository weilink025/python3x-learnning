class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat(self):
        print("----%s-正在吃---" %self.name)


@classmethod
def printt(cls):
    print("添加类方法")

Person.printt=printt
Person.printt()