#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import random
import datetime
import re


random.seed(datetime.datetime.now())
# 收集网站上发现的所有外链列表
allExtLinks = set()
allIntLinks = set()


def getInternalLinks(bsObj, includeUrl):
    includeUrl = urlparse(includeUrl).scheme + '://' + \
        urlparse(includeUrl).netloc
    internalLinks = []
    # 找到所有以'/'开头的链接
    for link in bsObj.find_all('a', href=re.compile(r'^(/|.*' + includeUrl + ')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if(link.attrs['href'].startswith('/')):
                    internalLinks.append(includeUrl + link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks


def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # 找到所有以'http'或'www'开头的且不包含当前链接的所有链接
    for link in bsObj.find_all('a', href=re.compile(r'^(http|www)((?!' + excludeUrl + ').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    domain = urlparse(siteUrl).scheme + '://' + urlparse(siteUrl).netloc
    bsObj = BeautifulSoup(html, 'html.parser')
    internalLinks = getInternalLinks(bsObj, domain)
    externalLinks = getExternalLinks(bsObj, domain)
    for link in internalLinks:
        if link not in allIntLinks:
            allIntLinks.add(link)
            print('内链：' + link)
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print('外链: ' + link)


if __name__ == '__main__':
    allIntLinks.add('http://oreilly.com')
    getAllExternalLinks('http://oreilly.com')
