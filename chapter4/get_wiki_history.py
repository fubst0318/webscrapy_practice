#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import re
import datetime

random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    html = urlopen('https://en.wikipedia.org/' + articleUrl)
    bsObj = BeautifulSoup(html)
    return bsObj.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile(r'^(/wiki/)((?!:).)*$'))


def getHistoryIPs(pageUrl):
    # 编辑历史页面URL链接格式是:
    # https://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    pageUrl = pageUrl.replace('/wiki/', '')
    historyUrl = 'https://en.wikipedia.org/w/index.php?title=' + \
        pageUrl + '&action=history'
    print('history url is: ' + historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html)
    # 找出class属性是'mw-anonuserlink'的链接
    # 它们用 IP地址代替用户名
    ipAddresses = bsObj.find_all('a', {'class': 'mw-anonuserlink'})
    addresslist = set()
    for ipAddress in ipAddresses:
        addresslist.add(ipAddress.get_text())
    return addresslist


if __name__ == '__main__':
    links = getLinks('wiki/Python_(programming_language)')

    while(len(links) > 0):
        for link in links:
            print('----------------------')
            historyIPs = getHistoryIPs(link.attrs['href'])
            for historyIP in historyIPs:
                print(historyIP)

    newLink = links[random.randint(0, len(links) - 1)].attrs['href']
    links = getLinks(newLink)