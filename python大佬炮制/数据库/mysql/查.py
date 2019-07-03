import MySQLdb
try:
    conn = MySQLdb.connect(host='localhost',port=3306,db='test',user='test',passwd='test',charset='utf8')
    cur=conn.cursor()
    cur.execute("select * from student where name='张伟'")

    #result = cur.fetchone()    #只显示一条记录
    #result = cur.fetchall()  # 显示所有记录
    result = cur.fetchmany(2)   #显示多少条记录
    print(result)
    print(cur.rowcount)  # 多少条记录
    print(cur.rownumber)  #分组标记

    cur.close()
    conn.close()
except:
    print("数据库异常")