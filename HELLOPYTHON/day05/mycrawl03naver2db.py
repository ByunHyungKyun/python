import os
import sys
from bs4 import BeautifulSoup
import urllib.request
import pymysql
client_id = "dCsLhp_jPApCLAvFYLl7"
client_secret = "zJPRUp7AVe"
encText = urllib.parse.quote("치킨")
url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')
 
curs = conn.cursor()



if(rescode==200):
    response_body = response.read()
    
    html = response_body.decode("utf-8")
    soup = BeautifulSoup(html,'xml')
    
    items = soup.select("item")
    for i,item in enumerate(items):
        sql = "INSERT INTO chicken (title,link,description,bloggername,bloggerlink,postdate) VALUES(%s,%s,%s,%s,%s,%s)"
        val = (item.title.get_text(),item.link.get_text(),item.description.get_text(),item.bloggername.get_text(),item.bloggerlink.get_text(),item.postdate.get_text())
        
        print(item.link)
        curs.execute(sql,val)
        conn.commit()
        print(curs.rowcount, "record inserted")
       
     
        
else:
    print("Error Code:" + rescode)
    
conn.close()    
    