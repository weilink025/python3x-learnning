def func(funcname):
    def funcin(*args,**kwargs):  #随意传递多少个任意类型
        print("我是装饰器！！！")
        funcname(*args,**kwargs)
    return funcin

@func
def fun1(a,b,c):
    print(a,b,c)

fun1(1,2,3)

fun1([1,3],2,3)




