from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')
curs = conn.cursor()
 
sql = "select s_code,s_name,s_price,crawl_date from stock where s_name='삼성전자'"
curs.execute(sql)
 
sam =[] 
rows = curs.fetchall()
for i,row in enumerate(rows):
    sam.append(row[2])
conn.close()


conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')
curs = conn.cursor()
 
sql = "select s_code,s_name,s_price,crawl_date from stock where s_name='LG전자'"
curs.execute(sql)
 
lg =[] 
rows = curs.fetchall()
for i,row in enumerate(rows):
    lg.append(row[2])
conn.close()

conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')
curs = conn.cursor()
 
sql = "select s_code,s_name,s_price,crawl_date from stock where s_name='흥아해운'"
curs.execute(sql)
 
h =[] 
rows = curs.fetchall()
for i,row in enumerate(rows):
    h.append(row[2])
conn.close()

fig = plt.figure()
ax = plt.axes(projection='3d')
z = np.array(sam)
x = np.array([1,1,1,1,1,1,1,1,1,1])
y =np.array([0,1,2,3,4,5,6,7,8,9])

z2 = np.array(lg)
x2 = np.array([2,2,2,2,2,2,2,2,2,2])
y2 =np.array([0,1,2,3,4,5,6,7,8,9])

z3 = np.array(h)
x3 = np.array([3,3,3,3,3,3,3,3,3,3])
y3 =np.array([0,1,2,3,4,5,6,7,8,9])

ax.plot3D(x, y, z, 'blue')
ax.plot3D(x2, y2, z2, 'red')
ax.plot3D(x3, y3, z3, 'maroon')
ax.set_title('3D line jusic')
plt.show()

















