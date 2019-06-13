#生成器的好处：只保存列表的生成方法，需要用到时再调用。不保存内容，节约内存空间

a=[ i for i in range(10)]     #这是列表
print(a)

b=( i for i in range(10))   #把列表中括号换成括号就行，这是生成器
for temp in b:
    print(temp)

next(b)  #生成器逐个输出,生成器一次生成一个值，一次全部存入内存，节约很多