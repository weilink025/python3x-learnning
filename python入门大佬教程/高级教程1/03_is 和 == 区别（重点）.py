# == 判断值是否相等
# is  用来判断内存id是否相等     id(arg)可以返回变量对应的内存id

#示例1
a=1
b=1
print(a==b)   #True
print(a is b)   #True  说明a和b用是同一内存
print(id(a))
print(id(b))

#示例2
c=[11,22,33]
d=[11,22,33]
print(c==d)   #True
print(c is d)   #False
print(id(c))
print(id(d))

#示例3
e=c      #只是在c变量的内存空间中增加一个e变量的标签
print(c == e)   #True
print(c is e)   #True