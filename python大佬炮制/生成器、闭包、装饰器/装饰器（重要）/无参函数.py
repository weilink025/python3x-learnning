def func(fun):
    print("已经装饰好了")
    def funcin():
        fun()
        print("---funcin----")

    return funcin

@func
def test():
    print("---test---")


test()