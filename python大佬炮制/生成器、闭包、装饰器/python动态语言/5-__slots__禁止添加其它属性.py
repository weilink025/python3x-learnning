class Person(object):
    __slots__ = ("age","name")    #只允许age和name属性

p1=Person()

p1.name = "老王"
p1.age  =  28

print(p1.name)
print(p1.age)

p1.addr='China'   #不能赋值
print(p1.addr)