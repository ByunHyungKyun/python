import requests
from bs4 import BeautifulSoup

url = 'http://localhost:9090/CRAWL/crawl.html'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select("td")
    
    for i,info in enumerate(title):
        if i > 1:
            print(info.get_text())
else : 
    print(response.status_code)
    
    
    