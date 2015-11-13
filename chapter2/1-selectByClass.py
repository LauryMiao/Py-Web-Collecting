import requests
from bs4 import BeautifulSoup

html = requests.get("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html.text, 'lxml')

nameList = bsObj.findAll("span", {"class": "green"})
print(nameList)
print(len(nameList))
diagList = bsObj.findAll("span", {"class": "red"})
for diag in diagList:
    pass
    # print(diag.get_text())
