#命令空间，全局变量，局部变量


from os import path   #os就是命令空间

a=2     #全局变量
print(globals())   #输出所有全局变量

def fun1():
    a=1   #局部变量
    print(locals())

fun1()

#所有内建函数

