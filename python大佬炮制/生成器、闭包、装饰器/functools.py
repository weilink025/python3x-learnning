"""import functools
dir( functools)

#偏函数

def showarg(*args,**kwargs):
    print(args)
    print(kwargs)

p1=functools.partial(showarg(1,2,3))
p1()   #1,2,3
p1(4,5,6)  #1,2,3,4,5,6

"""
#wraps函数
import functools

def note(func):
    "note function"
    @functools.wraps(func)
    def wrapper():
        "wrapper function"
        print("note something")
        return func()
    return wrapper

@note
def test():
    "test function"
    print("I am test")

test()
print(test.__doc__)  #帮忙文档显示形式，完函数帮忙文档

