#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import datetime

pages = set()
random.seed(datetime.datetime.now())


def getInternalLinks(bsObj, includeUrl):
    # 获取页面所有内链的列表
    internalLinks = []
    # 找出所有以'/'开头的链接
    for link in bsObj.find_all('a', href=re.compile(r"^(/|.*" + includeUrl + ")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks


def getExternalLinks(bsObj, excludeUrl):
    # 获取页面所有外链的列表
    externalLinks = []
    # 找出所有以'http' 或 'wwww'开头且不包含当前URL的链接
    for link in bsObj.find_all('a', href=re.compile(r"^(http|www)((?!" + excludeUrl + ").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def splitAddress(address):
    addressParts = address.replace('http://', '').split('/')
    return addressParts


def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html)
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(startingPage, '')
        return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks) - 1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]


def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink('http://oreilly.com')
    print('随机外链是:' + externalLink)
    followExternalOnly(externalLink)


if __name__ == '__main__':
    followExternalOnly('http://oreilly.com')
