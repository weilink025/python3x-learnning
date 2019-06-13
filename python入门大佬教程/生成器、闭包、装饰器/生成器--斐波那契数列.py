#斐波那契数列 1 1 2 3 5 8 13 21 34 55
def fob(m):
    a, b = 0, 1
    for i in range(m):
        print(b,end=' ')
        a,b=b,a+b    #先取到=号后面的变量的值，然后赋值给，=号前面的变量

fob(10)

#将上述变成生成器
def fob1(m):
    a, b = 0, 1
    for i in range(m):
        yield b    #遇到yield函数暂停，然后返回后面的值，下次调用函数时，从暂停处继续执行
        a, b = b, a + b  # 先取到=号后面的变量的值，然后赋值给，=号前面的变量
a=fob1(10)
print(a)   # <generator object fob1 at 0x000001779A52EB10>
print(next(a))
print(next(a))
print(next(a))
