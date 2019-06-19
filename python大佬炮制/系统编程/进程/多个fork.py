import os
"""
ret=os.fork()
if ret==0:
    print('1')
else:
    print('2')
ret1=os.fork()
if ret1==0:
    print('3')
else:
    print('4')



"""

os.fork()
os.fork()
os.fork()
print('a %d' %os.getpid())


#fork炸弹
while True:
    os.fork()