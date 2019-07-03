import MySQLdb

try:

    conn = MySQLdb.connect(host='localhost',port=3306,db='test',user='test',passwd='test',charset='utf8')
    cu1 = conn.cursor()
    cu1.execute("update student set age=12, beizhu = '123' where name='张伟'")
    conn.commit()
    cu1.close()
    conn.close()

except:
    print("数据库异常")

