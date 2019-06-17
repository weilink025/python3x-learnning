def test():
    print("--1--")

print(test)   #<function test at 0x00000292C227C1E0>
b=test
print(b)   #<function test at 0x00000209D0BFC1E0>

test()   #--1--
b()      #--1--


def test1(a,b):
    def test2(x):
        return a*x+b
    return test2      #返回了function类型

a=test1(2,3)   #a指向了test2
print(a(4))

b=test1(5,7)
print(b(10))