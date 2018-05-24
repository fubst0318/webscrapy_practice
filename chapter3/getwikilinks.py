#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    html = urlopen('https://en.wikipedia.org' + str(articleUrl))
    bsObj = BeautifulSoup(html)
    return bsObj.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile(r"^(/wiki/)((?!:).)*$"))


links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0,len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)