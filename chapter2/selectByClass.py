#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bsObj = BeautifulSoup(html.read())
namelist = bsObj.find_all('span',{'class':'green'})

for name in namelist:
    print(name.get_text())