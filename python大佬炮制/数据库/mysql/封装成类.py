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




testData = mysqlHelper('localhost', 3306, 'wyb_ap_data', 'root', 'root', 'utf8')  #实例化类
testData.conn()   #调用连接数据的方法
""" 
data=testData.selectOne("select * from student")
#print(data)
dataAll= testData.selectAll("select * from student")
#print(dataq)
dataNum= testData.selectNum("select * from student",3)
#print(dataNum)
params = [('703a7300d001', 'ec3586523344', -56, '2019-07-10 09:37:11'), ('703a7300d001', '009d6b41467e', -79, '2019-07-10 09:37:11'), ('703a7300d001', '90b0edb65a58', -77, '2019-07-10 09:37:11'), ('703a7300d001', '80c5f247ee5c', -82, '2019-07-10 09:37:11'), ('703a7300d001', '48a19549a401', -92, '2019-07-10 09:37:11'), ('703a7300d001', '3c6aa7d092a1', -83, '2019-07-10 09:37:11'), ('703a7300d001', '7440bb65fb8b', -70, '2019-07-10 09:37:11'), ('703a7300d001', '144f8a564cf8', -76, '2019-07-10 09:37:11'), ('703a7300d001', 'a81b6a886793', -86, '2019-07-10 09:37:11'), ('703a7300d001', '3052cbe1055e', -73, '2019-07-10 09:37:11'), ('703a7300d001', 'f099bf131b6b', -85, '2019-07-10 09:37:11'), ('703a7300d001', '48a19506b922', -82, '2019-07-10 09:37:11'), ('703a7300d001', '483c0cc14009', -77, '2019-07-10 09:37:11'), ('703a7300d001', 'a4933f1793d7', -73, '2019-07-10 09:37:11'), ('703a7300d001', 'b0d59dda6848', -79, '2019-07-10 09:37:11'), ('703a7300d001', '90324b14b880', -80, '2019-07-10 09:37:11'), ('703a7300d001', 'dcf090a717df', -83, '2019-07-10 09:37:11'), ('703a7300d001', '7047e924b661', -83, '2019-07-10 09:37:11'), ('703a7300d001', '5c03399b4b31', -75, '2019-07-10 09:37:11'), ('703a7300d001', '9809cf80c858', -79, '2019-07-10 09:37:11')]
for param in params:
    sql = "insert into student(ap_mac,client_mac,rssi,time_stamp ) values (%s,%s,%s,%s)"
    dataAdd = testData.addData(sql,param)

rel = testData.delData("delete from student where name='巴小刘'")
print(rel)

res = testData.updateData("update student set age = 25 where name='小朱'")
print(res)
"""
params = [('703a7300d001', 'ec3586523344', -56, '2019-07-10 09:37:11'), ('703a7300d001', '009d6b41467e', -79, '2019-07-10 09:37:11'), ('703a7300d001', '90b0edb65a58', -77, '2019-07-10 09:37:11'), ('703a7300d001', '80c5f247ee5c', -82, '2019-07-10 09:37:11'), ('703a7300d001', '48a19549a401', -92, '2019-07-10 09:37:11'), ('703a7300d001', '3c6aa7d092a1', -83, '2019-07-10 09:37:11'), ('703a7300d001', '7440bb65fb8b', -70, '2019-07-10 09:37:11'), ('703a7300d001', '144f8a564cf8', -76, '2019-07-10 09:37:11'), ('703a7300d001', 'a81b6a886793', -86, '2019-07-10 09:37:11'), ('703a7300d001', '3052cbe1055e', -73, '2019-07-10 09:37:11'), ('703a7300d001', 'f099bf131b6b', -85, '2019-07-10 09:37:11'), ('703a7300d001', '48a19506b922', -82, '2019-07-10 09:37:11'), ('703a7300d001', '483c0cc14009', -77, '2019-07-10 09:37:11'), ('703a7300d001', 'a4933f1793d7', -73, '2019-07-10 09:37:11'), ('703a7300d001', 'b0d59dda6848', -79, '2019-07-10 09:37:11'), ('703a7300d001', '90324b14b880', -80, '2019-07-10 09:37:11'), ('703a7300d001', 'dcf090a717df', -83, '2019-07-10 09:37:11'), ('703a7300d001', '7047e924b661', -83, '2019-07-10 09:37:11'), ('703a7300d001', '5c03399b4b31', -75, '2019-07-10 09:37:11'), ('703a7300d001', '9809cf80c858', -79, '2019-07-10 09:37:11')]
for param in params:
    sql = "insert into ap_data_source(ap_mac,client_mac,rssi,time_stamp ) values (%s,%s,%s,%s)"
    dataAdd = testData.addData(sql,param)
