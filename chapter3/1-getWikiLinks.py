import requests
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    html = requests.get("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html.text, 'lxml')
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
links = getLinks("/wiki/Kevin_Bacon")
print([link.attrs["href"] for link in links])
while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)
