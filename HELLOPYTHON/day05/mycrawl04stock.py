import os
import sys
from bs4 import BeautifulSoup
import urllib.request
from future.backports.urllib.request import urlopen
from sqlalchemy.sql.expression import false
import pymysql
from datetime import datetime


html = urlopen("https://vip.mk.co.kr/newSt/rate/item_all.php")
bsObject = BeautifulSoup(html,"html.parser")

titles_by_find_all = bsObject.tr.find_all("a")
price_find_all = bsObject.tr.find_all("td",{"class",'st2'})
now  = datetime.now()
formattedDate = now.strftime("%Y%m%d.%H%M")
clock_find_all = bsObject.tr.find("span",{"class",'t_11_black'})
#print(clock_find_all.get_text())

a = []
b = []
c = []
d = []

for title in price_find_all:
    a.append(title.next_sibling.next_sibling.get_text().replace(",",""))
    
for title in titles_by_find_all:
    if title.get('title') is not None:
        b.append(title.get('title'))
        c.append(title.get_text())
        
for i,info in enumerate(c):
    d.append(formattedDate)

conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')
curs = conn.cursor()        

for i,info in enumerate(c):
    sql = "INSERT INTO stock (s_code,s_name,s_price,crawl_date) VALUES(%s,%s,%s,%s)"
    val = (b[i],c[i],a[i],d[i])
    curs.execute(sql,val)
    print(curs.rowcount, "record inserted")

conn.commit()
conn.close()    