#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import datetime
import re
import pymysql

random.seed(datetime.datetime.now())

conn = pymysql.connect('localhost', port=3306,
                       user='root', password='root', db='mysql', charset='utf8')
cursor = conn.cursor()
cursor.execute('USE scraping')


def store(title, content):
    cursor.execute(
        'insert into pages (title,content) values(%s,%s)', (title, content))
    cursor.connection.commit()


def getLinks(startUrl):
    currentLink = 'https://en.wikipedia.org' + startUrl
    html = urlopen(currentLink)
    bsObj = BeautifulSoup(html, 'html.parser')
    title = bsObj.find('h1').get_text()
    content = bsObj.find('div', {'id': 'bodyContent'}).find(
        'div', {'id': 'mw-content-text'}).find('p').get_text()
    print('links:' + currentLink)
    print('title:' + title)
    print('content:' + content)
    store(title, content)

    links = bsObj.find('div', {'id': 'bodyContent'}).find_all(
        'a', href=re.compile(r'^(/wiki/)((?!:).)*$'))
    while (len(links) > 0):
        newUrl = links[random.randint(0, len(links) - 1)].attrs['href']
        print('links:' + currentLink)
        print('newUrl:' + newUrl)
        getLinks(newUrl)


if __name__ == '__main__':
    start_url = '/wiki/Kevin_Bacon'

    try:
        getLinks(start_url)
    finally:
        cursor.close()
        conn.close()
