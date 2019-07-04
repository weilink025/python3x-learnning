import MySQLdb

class mysqlHelper():
    #init方法
    def __init__(self,host,port,db,user,passwd,charset):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset

    #连接数据库，创建cusor
    def conn(self):
        try:
            self.connData = MySQLdb.connect(host=self.host,port=self.port,db=self.db,user=self.user,passwd=self.passwd,charset=self.charset)
            self.cur = self.connData.cursor()
        except:
            print("连接数据库错误")
            self.cur.close()
            self.connData.close()

    def closeData(self):
        self.cur.close()
        self.connData.close()
    #查一条
    def selectOne(self,sql):
        self.cur.execute(sql)
        resultData = self.cur.fetchone()
        return resultData

    #查多条
    def selectAll(self,sql):
        self.cur.execute(sql)
        resultData = self.cur.fetchall()
        return resultData
    def selectNum(self,sql,num):
        self.cur.execute(sql)
        resultData = self.cur.fetchmany(num)
        return resultData

    #增
    def addData(self,sql,param=()):
        self.cur.execute(sql,param)
        self.connData.commit()
        return self.cur.rowcount   #影响行数
    #删
    def delData(self,sql):
        self.cur.execute(sql)
        self.connData.commit()
        return self.cur.rowcount

    #改
    def updateData(self,sql):
        self.cur.execute(sql)
        self.connData.commit()
        return self.cur.rowcount




testData = mysqlHelper('localhost',3306,'test','test','test','utf8')  #实例化类
testData.conn()   #调用连接数据的方法
""" 
data=testData.selectOne("select * from student")
#print(data)
dataAll= testData.selectAll("select * from student")
#print(dataq)
dataNum= testData.selectNum("select * from student",3)
#print(dataNum)
params = (('王小',12,'小二'),('小朱',22,'朱重八'),('巴小刘',12,'小巴'),('李小三',12,'小三'),('店长刘',12,'刘3'))
for param in params:
    sql="insert into student(name,age,beizhu) values (%s,%s,%s)"
    dataAdd = testData.addData(sql,param)

rel = testData.delData("delete from student where name='巴小刘'")
print(rel)
"""
res = testData.updateData("update student set age = 25 where name='小朱'")
print(res)