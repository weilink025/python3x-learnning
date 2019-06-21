# 静态编译后无法修改运行内容，动态反之

# python动态体现

#1、变量动态修改
a = 100


def test():
    print("---a--")


a = test  # 变更了a的类型
a()

#2、类与变量动态添加属性
class Person():
    def __init__(self,newName,newAge):
        self.name=newName
        self.age=newAge

p1=Person("zhangwei",30)

print(p1.name)
print(p1.age)

p1.addr="CN"      #给对象添加属性,只对该对象生效。
print(p1.addr)     #结果CN

Person.myEmail='1272253421@qq.com'    #给类添加属性,对类生效，即对之后所有实例化对象生效

p2=Person("wade",30)
print(p2.myEmail)




