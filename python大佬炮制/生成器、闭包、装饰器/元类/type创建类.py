000# 1,type查看通过哪个类创建的
type(1)  #int  说明1是通过int类创建出来的
type('abc')  #abc是通过str类创建出来的

class test():
    pass

a=test()

print(a)  #<__main__.test object at 0x000002226D3D65F8>
# a是通过test类创建出来的对象








































