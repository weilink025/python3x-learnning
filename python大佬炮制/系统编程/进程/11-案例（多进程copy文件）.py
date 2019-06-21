import os
from multiprocessing import Pool,Manager
from time import sleep

def copyfunc(name,old_file,new_file,queues):

    print(queues.get())
    fr = open(old_file+"/"+name,"r")
    fw = open(new_file+"/"+name,'w')
    context=fr.read()
    fw.write(context)
    fr.close()
    fw.close()





if __name__ == "__main__":

    old_file = input("输入你要copy的文件夹：")
    print(" ")
    new_file = old_file + "-bak"

    os.mkdir(new_file)
    listfile = os.listdir(old_file)
    print(len(os.listdir(old_file)))

    pool= Pool(2)
    queues = Manager().Queue()



    for name in listfile:

        pool.apply_async(copyfunc,(name,old_file,new_file,queues,))




    num=0
    allnum = len(listfile)


    while num <= allnum:
        print("%s —————————— 已经copy完成" % queues.get())
        num+=1

    print("所有文件已经复制完成！！")







