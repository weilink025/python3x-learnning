#原始单任务程序
from time import sleep
def sing():
    for i in range(3):
        print("正在唱歌————%d" %i)
        sleep(1)

def dance():
    for i in range(3):
        print("正在跳舞————%d" %i)
        sleep(1)

if __name__ == '__main__':   #下面代码只有本程序作为脚本才会直接运行，如果被其它函数调用不会执行
    sing()
    dance()

"""结果：
正在唱歌————0
正在唱歌————1
正在唱歌————2
正在跳舞————0
正在跳舞————1
正在跳舞————2
"""