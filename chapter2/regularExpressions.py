#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pattern = re.compile(r'../img/gifts/img.*.jpg')
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html)
images = bsObj.find_all('img', {'src': pattern})
for image in images:
    print(image['src'])
