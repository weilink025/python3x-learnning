import os

a=100
print("全局变量a=100")

ret=os.fork()

if ret==0:
    a+=1
    print(a)

else:
    print(a)

print(a)


#进程间所有数量是隔离的