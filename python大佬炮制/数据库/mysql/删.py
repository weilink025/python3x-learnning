import MySQLdb

try:
    conn = MySQLdb.connect(host='localhost', port=3306, db="test", user="test", passwd="test", charset="utf8")
    cur = conn.cursor()
    cur.execute("delete from student where name='小刘'")
    conn.commit()
    cur.close()
    conn.close()
except:
    "数据库连接异常"

