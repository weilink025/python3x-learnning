#encoding=utf-8
import MySQLdb
try:
    conn=MySQLdb.connect(host='localhost',port=3306,db='test',user='test',passwd='test',charset='utf8')
    cs1=conn.cursor()

    params=[('dog0',12,'sam'),('dog1',12,'sam'),('dog2',12,'sam')]

    for param in params:
        cs1.execute('insert into student(name,age,beizhu) values(%s,%s,%s)',param)

    conn.commit()
    cs1.close()
    conn.close()
except:
    print("数据库异常")