#类也是对象

class test():
    print("____test_____")
    def __init__(self,name):
        self.name=name
#建立test类后，就会创建对象来print

print(test)   #<class '__main__.test'>