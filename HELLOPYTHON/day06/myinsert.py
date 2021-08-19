import pymysql

conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')
 
curs = conn.cursor()
 
 
 
val = (
        (6,"6","6")
        ,(7,"7","7")
        ,(8,"8","8")
     )
sql = "INSERT INTO hello (col01,col02,col03) VALUES(%s,%s,%s)"
#val = (3,"3","3")
curs.executemany(sql,val)

conn.commit()

print(curs.rowcount, "record inserted")
conn.close()

