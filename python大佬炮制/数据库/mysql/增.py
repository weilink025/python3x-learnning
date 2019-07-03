import MySQLdb

try:
    conn = MySQLdb.connect(host="localhost",port=3306,db='test',user='test',passwd='test',charset='utf8')
    cur = conn.cursor()

    cur.execute("insert into student (name,age,beizhu) values ('张伟',27,'崩')")

    conn.commit()
    cur.close()
    conn.close()
except:
    print("数据库异常")

