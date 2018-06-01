#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql

conn = pymysql.connect('localhost', port=3306, user='root',
                       password='root', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute('USE wikipedia')
pages = set()


def pagesScraped(link):
    print('pagesScraped,link={0}'.format(link))
    cur.execute('select * from pages where url = %s', (link))
    if cur.rowcount == 0:
        return False

    page = cur.fetchone()

    cur.execute('select * from links where fromPageId=%s', (int(page[0])))
    if cur.rowcount == 0:
        return False

    return True


def insertPageIfNotExists(Url):
    print('insertPageIfNotExists,Url={0}'.format(Url))
    cur.execute("select * from `pages` where `url` = %s", (Url))
    if cur.rowcount == 0:
        cur.execute('insert into pages (url) values (%s)', Url)
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]


def insertLink(fromPageId, ToPageId):
    print('insertLink,fromPageId={0},ToPageId={1}'.format(
        fromPageId, ToPageId))
    cur.execute('select * from links where fromPageId = %s and toPageId = %s',
                (fromPageId, ToPageId))
    if cur.rowcount == 0:
        cur.execute(
            'insert into links (fromPageId,toPageId) values (%s,%s) ', (fromPageId, ToPageId))
        conn.commit()


def getLinks(Url, recrusive_level):
    if recrusive_level > 4:
        return
    pageId = insertPageIfNotExists(Url)
    html = urlopen('https://en.wikipedia.org' + Url)
    bsObj = BeautifulSoup(html, 'html.parser')
    for link in bsObj.find_all('a', href=re.compile(r'^(/wiki/)((?!:).)*$')):
        insertLink(pageId, insertPageIfNotExists(link.attrs['href']))
        if not pagesScraped(link.attrs['href']):
            newPage = link.attrs['href']
            print(newPage)
            getLinks(newPage, recrusive_level + 1)
        else:
            print('Skipping: ' + str(link.attrs['href']) + " found on " + Url)


if __name__ == '__main__':
    try:
        getLinks('/wiki/Kevin_Bacon', 0)
    finally:
        cur.close()
        conn.close()
