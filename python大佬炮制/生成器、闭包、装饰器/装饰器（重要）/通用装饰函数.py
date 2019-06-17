def func(funcname):  # 我是通用装饰器
    def funcin(*args, **kwargs):  # 随意传递多少个任意类型
        print("我是装饰器！！！")
        ret = funcname(*args, **kwargs)
        return ret
    return funcin


@func
def fun1(a, b, c):
    print('我是有参数函数装饰')
    print(a, b, c)


@func
def fun2(a, b, c):
    print('我是有返回值函数装饰')
    print(a, b, c)
    return a + b + c


@func
def fun3():
    print('我是无参数函数装饰')


fun1(1, 2, 3)
print(fun2(1, 2, 3))
fun3()
