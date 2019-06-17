#多任务方式之一 协程

def test1():       #任务1
    while True:
        print("--任务1--")
        yield None

def test2():       #任务2
    while True:
        print("--任务2--")
        yield None

a=test1()
b=test2()

while True:
    a.__next__()
    b.__next__()
"""结果：
--任务1--
--任务2--
--任务1--
--任务2--
--任务1--
--任务2--
"""

