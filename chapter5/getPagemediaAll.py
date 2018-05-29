#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import os
import re

downloadDirectory = 'downloaded'
baseUrl = 'http://pythonscraping.com'


def getAbsoulteURL(baseUrl, source):
    if source.startswith('http://www.'):
        url = 'http://' + source[11:]
    elif source.startswith('http://'):
        url = source
    elif source.startswith('www.'):
        url = 'http://' + source[4:]
    else:
        url = baseUrl + '/' + source
    if baseUrl not in url:
        return None
    return url


def getDownloadPath(baseUrl, absoulteUrl, downloadDirectory):
    path = absoulteUrl.replace('www.', '')
    path = path.replace(baseUrl, '')
    path = downloadDirectory + path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)

    return path


if __name__ == '__main__':
    html = urlopen('http://www.pythonscraping.com')
    bsObj = BeautifulSoup(html)
    downloadList = bsObj.find_all(src=True)

    for download in downloadList:
        fileUrl = getAbsoulteURL(baseUrl, download['src'])
        if fileUrl is not None:
            print(fileUrl)
            if re.match(re.compile(r'[\s\S]*jpg$'), fileUrl):
                urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))
