import os
import sys
from bs4 import BeautifulSoup
import urllib.request
import pymysql
from datetime import datetime
import time

for i in range(0,10):
    url = "https://vip.mk.co.kr/newSt/rate/item_all.php"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    
    if(rescode==200):
        response_body = response.read()
        
        html = response_body.decode("euc-kr")
        soup = BeautifulSoup(html,'html.parser')
        
        now  = datetime.now()
        formattedDate = now.strftime("%Y%m%d.%H%M")
        
        conn = pymysql.connect(host='localhost', user='root', password='java',
                           db='python', charset='utf8')
        
        curs = conn.cursor()  
        items = soup.select(".st2")
        for i,item in enumerate(items):
            s_code = item.a["title"]
            s_name = item.text
            s_price =item.parent.select("td")[1].text.replace(",","")
            crawl_date = formattedDate
            sql = "INSERT INTO stock (s_code,s_name,s_price,crawl_date) VALUES(%s,%s,%s,%s)"
            val = (s_code,s_name,s_price,crawl_date)
            curs.execute(sql,val)
            
    else:
        print("Error Code:" + rescode)
    print(curs.rowcount, "record inserted")      
    conn.commit()
    conn.close()  
    time.sleep(60)    