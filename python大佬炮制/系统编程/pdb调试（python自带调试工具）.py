
"""
#第一种方式
python3 -m pdb test.py

命令：
l------>  显示当前的代码
n------>  向下执行代码
c------>  continue  继续执行全部代码
b 7    -------> 第七行加断点   直接按 b  查看所有断点
clear num      ------>  num是断点编号，可以按 b  查看具体编号
p  ------>   print  打印一个变量的值
s-------->   step进入到一个函数
a-------->  args 打印所有的形参数据
r--------> return快速执行到函数最后一行

"""

#有些情况直接按  c  不行，先按 n 再执行其它操作



######################## #第二种方式
#用pdb模块交互式调试
import pdb

def test():
    print("")

pdb.run(test())


######################第三程序中埋点
import pdb
def printest(a,b):

    print(a,b)
    return a+b

a=100
b=200

pdb.set_trace()    #当程序执行到这个步会自动进入调试模式

ret=printest(a,b)
print(ret)



#日志调试（生产环境）

