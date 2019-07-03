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
        self.connData = MySQLdb.connect(host=self.host,port=self.port,db=self.db,user=self.user,passwd=self.passwd,charset=self.charset)
        self.cur = self.connData.cursor()

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
        return self.cur.rowcount
    #删

    #改


testData = mysqlHelper('localhost',3306,'test','test','test','utf8')
testData.conn()
data=testData.selectOne("select * from student")
#print(data)
dataAll= testData.selectAll("select * from student")
#print(dataq)
dataNum= testData.selectNum("select * from student",3)
#print(dataNum)
listdata = (('1',2,'3'))
sql="insert into student(name,age,beizhu) values ('%s','%s','%s')"
dataAdd = testData.addData(sql,listdata)
print(dataAdd)