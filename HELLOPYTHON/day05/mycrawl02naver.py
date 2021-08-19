import os
import sys
from bs4 import BeautifulSoup
import urllib.request
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
if(rescode==200):
    response_body = response.read()
    
    html = response_body.decode("utf-8")
    soup = BeautifulSoup(html,'html.parser')
    
    items = soup.select("item")
    for i,item in enumerate(items):
        print(item.title.get_text())
        print()
        print()
        print(item.description.get_text())
        print()
        print()
        
else:
    print("Error Code:" + rescode)