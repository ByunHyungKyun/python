import pymysql

conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')
 
curs = conn.cursor()
 
sql = "delete from hello where col01=%s"
curs.execute(sql, 1)
conn.commit()

print(curs.rowcount, "record inserted")
conn.close()

