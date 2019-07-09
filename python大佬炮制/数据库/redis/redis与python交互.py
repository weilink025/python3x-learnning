from redis import *

try:
    r=StrictRedis(host='localhost', port=6379 ,db=0 ,password='myredis')
except:
    print("连接错误")
pipe = r.pipeline()
pipe.mset({'name1':11,'we':313})
pipe.execute()

#＃＃＃直接读
print(r.get('we'))