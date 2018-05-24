#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen('https://en.wikipedia.org/' + str(pageUrl))
    bsObj = BeautifulSoup(html)

    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id='mw-content-text').find_all('p')[0])
        print(bsObj.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('页面缺少数据！不过不用担心!')

    for link in bsObj.find_all('a', href=re.compile(r'^(/wiki/)')):
        if 'href' in link.attrs:
            if link['href'] not in pages:
                # 我们遇到了新的页面
                newpage = link.attrs['href']
                print('-----------\n' + newpage)
                pages.add(newpage)
                getLinks(newpage)


if __name__ == '__main__':
    getLinks('')
