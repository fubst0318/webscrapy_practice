#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page2.html')
bsObj = BeautifulSoup(html, 'html.parser')
tags = bsObj.find_all(lambda tag: len(tag.attrs) == 2)
for tag in tags:
    print(tag)
