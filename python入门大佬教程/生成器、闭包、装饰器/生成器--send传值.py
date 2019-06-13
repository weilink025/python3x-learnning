def test():
    i=0
    while i < 15:
        temp = yield i   #第一次暂停后，send值传给temp
        print(temp)
        i+=1

a=test()
print(a.send(None))   #第一次不传值，或者用a.__next__()
print(a.send("哈哈1"))
print(a.send("哈哈2"))
print(a.send("哈哈3"))


