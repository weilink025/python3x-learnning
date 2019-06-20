import os
from multiprocessing import Pool,Queue,Manager
from time import sleep

def copyfunc(name,old_file,new_file,queues):
    fr = open(old_file+"/"+name,"r")
    fw = open(new_file+"/"+name,'w')
    context=fr.read()
    fw.write(context)
    fr.close()
    fw.close()
    queues.put(name)




if __name__ == "__main__":


    old_file = input("输入你要copy的文件夹：")
    print(" ")
    new_file = old_file + "-bak"

    os.mkdir(new_file)
    listfile = os.listdir(old_file)

    pool= Pool(5)
    queues = Manager().Queue()
    for name in listfile:

        pool.apply_async(copyfunc,(name,old_file,new_file,queues,))

    pool.close()

    for i in range(1920):
         print(queues.get())
    pool.join()




