import requests
from bs4 import BeautifulSoup
import sys


def getTitle(url):
    try:
        html = requests.get(url)
    except Exception as e:
        print(e)
        return None
        # return null, break, or do some other "plan B"
#   else:
#   program continues. Note:If you return or break in the
#   exception catch, you do not need to use the "else" statement
    try:
        bsObj = BeautifulSoup(html.text, 'lxml')
        title = bsObj.head.title.text
    except AttributeError as e:
        print(e)
        return None
    return title

url_test = "http://www.pythonscraping.com/exercises/exercise1.html"
url_test2 = "http://www.baidu.com"
title = getTitle(url_test2)
if title == None:
    print("Title could not be found")
else:
    print(title)
