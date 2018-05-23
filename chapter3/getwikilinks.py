#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen('https://en.wikipedia.org'+ str(articleUrl))
    bsObj = BeautifulSoup(html)
    
    
html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
bsObj = BeautifulSoup(html)
for alink in bsObj.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile(r"^(/wiki/)((?!:).)*$")):
    if 'href' in alink.attrs:
        print(alink.attrs['href'])
