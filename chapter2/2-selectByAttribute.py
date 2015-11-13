import requests
from bs4 import BeautifulSoup

html = requests.get("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html.text, "lxml")
allText = bsObj.findAll(id="text")
print(allText[0].get_text())
