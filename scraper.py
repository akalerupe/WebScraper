import requests
from bs4 import BeautifulSoup

URL='https://www.jumia.co.ke/hisense-13kg-top-load-washing-machine-wtja1302t-70510165.html'

headers={
 "user-Agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    } 

page=requests.get(URL,headers=headers)

soup=BeautifulSoup(page.content,"html.parser")
print(soup.prettify)

title=soup.find(id="price")
