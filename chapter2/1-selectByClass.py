import requests
from bs4 import BeautifulSoup

html = requests.get("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html.text, 'lxml')
diagList = bsObj.findAll("span", {"class": "red"})
for diag in diagList:
    print(diag.get_text())
