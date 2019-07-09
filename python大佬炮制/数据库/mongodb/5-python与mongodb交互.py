import pymongo

client = pymongo.MongoClient('localhost',27017)

db=client.student

stu = db.stu




#增加数据
s1={'name':'wde','age':12,'gender':1}
s2={'name':'wde','age':12,'gender':1}
stu.insert(s1,s2)

#查一个
stu.find_one()

for cur in stu.find():
   print(cur)
