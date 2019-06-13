#可迭代对象(iterable)   简单理解为可以用for循环的对你
#一类是集合数据类型：list,tunple,dict,set,str
#一类是生成器,包括生成器和带yield的generator function

#判断是否是迭代对象
from collections import Iterable
print(isinstance([],Iterable))

print(isinstance('abcd',Iterable))

#把可迭代对象iter()，就是转成了迭代器
a=[1,2,3,'abc']
b=iter(a)
print(b)  #<list_iterator object at 0x000002588CAE8128> 迭代器

print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))