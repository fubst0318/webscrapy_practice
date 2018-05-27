#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup


if __name__ == '__main__':
    html = urlopen('http://pythonscraping.com')
    bsObj = BeautifulSoup(html, 'html.parser')
    imageLocation = bsObj.find('a', {'id': 'logo'}).find('img')['src']
    urlretrieve(imageLocation, 'logo.jpg')
