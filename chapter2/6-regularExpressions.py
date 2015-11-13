import requests
from bs4 import BeautifulSoup
import re

html = requests.get("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.text, 'lxml')
images = bsObj.findAll("img", {"src": re.compile(r"../img/gifts/img.*.jpg")})
for image in images:
    print(image["src"])
