#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError:
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError:
        return None
    return title


if __name__ == '__main__':
    title = getTitle('http://www.pythonscraping.com/pages/page1.html')
    if title == None:
        print('Title could not be found')
    else:
        print(title)
