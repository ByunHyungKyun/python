import pymysql

conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')
 
curs = conn.cursor()
 
sql = """update hello
         set col02 = '5'
         ,col03='5'
         where col01=3"""
curs.execute(sql)
conn.commit()

print(curs.rowcount, "record inserted")
conn.close()

