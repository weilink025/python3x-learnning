#fork不能直接在win系统上执行
import os
import time
re=os.fork()
print(re)   # re返回的是子进程的pid

while True:
    print('---1--- %d--父进程--%d' % (os.getpid(),os.getppid()))
    time.sleep(1)
    print("---2----%d--父进程--%d" % (os.getpid(), os.getppid()))
    time.sleep(1)

"""  执行结果：
---1--- 9535--父进程--8113
---1--- 9536--父进程--9535
---2----9536--父进程--9535
---2----9535--父进程--8113
---1--- 9535--父进程--8113
---1--- 9536--父进程--9535
---2----9536--父进程--9535
---2----9535--父进程--8113
"""