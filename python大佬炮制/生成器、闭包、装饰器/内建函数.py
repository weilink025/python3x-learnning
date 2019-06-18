#range   3.x生成器       xrang/range  python2.x是一个列表
"""

#map
a=map(lambda x:x*x,[1,2,3])

for i in a:
    print(i)

map(lambda x,y:x+y,[1,2,3],[2,3,4])


def f1(x,y):
    return (x,y)

l1=[0,1,2,3,4,5,6]
l2=['sun','m','t','w','t','f','s']

map(f1,l1,l2)


#filter函数   过滤

filter(lambda x:x%2,[1,2,3,4])      #[1,3]       #0表示false   非0表示True


#reduce  累加

reduce(lambda x,y : x+y ,[1,2,3,4])   #10

reduce(lambda x,y : x+y ,[1,2,3,4],5)   #15  5先赋值给x

reduce(lambda x,y : x+y , ['a','c','d','e'],'f')      # f先赋值给x    结果facde
"""
#sorted函数
a=[1,23,4,5,5654,563,4,5,8,7321,4,7,2,443,543245,7122,114,7,472]
#升序：
a.sort()
print(a)   #[1, 2, 4, 4, 4, 5, 5, 7, 7, 8, 23, 114, 443, 472, 563, 5654, 7122, 7321, 543245]

#降序

a.sort(reverse=True)
print(a)    #[543245, 7321, 7122, 5654, 563, 472, 443, 114, 23, 8, 7, 7, 5, 5, 4, 4, 4, 2, 1]


print(sorted(a))    #[1, 2, 4, 4, 4, 5, 5, 7, 7, 8, 23, 114, 443, 472, 563, 5654, 7122, 7321, 543245]
print(sorted(a,reverse=True))  #[543245, 7321, 7122, 5654, 563, 472, 443, 114, 23, 8, 7, 7, 5, 5, 4, 4, 4, 2, 1]