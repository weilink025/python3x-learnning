#Garbage collection(GC 垃圾回收)
#[-5,257] 小整数池

a=5
b=5
c=1000
d=1000

print(id(a),id(b),id(c),id(d))

print(c is d)

e='hello# world'
f='hello# world'

print(e is f)