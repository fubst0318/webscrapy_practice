#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root',
                       password='root', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute('USE wikipedia')


class SolutionFound(BaseException):
    def __init__(self, message):
        self.message = message


def getLinks(fromPageId):
    cur.execute('SELECT toPageId FROM links WHERE fromPageId = %s', (fromPageId))
    if cur.rowcount == 0:
        return None
    else:
        return [x[0] for x in cur.fetchall()]


def constructDict(currentPageId):
    links = getLinks(currentPageId)
    if links:
        return dict(zip(links, [{}] * len(links)))
    return {}


def searchDepth(targetPageId, currentPageId, linkTree, depth):
    # 链接树要么为空，要么包含多个链接
    if depth == 0:
        # 停止递归，返回结果
        return linkTree
    if not linkTree:
        linkTree = constructDict(currentPageId)
        if not linkTree:
            # 若此节点页面无链接，则跳过此节点
            return {}
    if targetPageId in linkTree.keys():
        print('TARGET ' + str(targetPageId) + " FOUND!")
        raise SolutionFound("PAGE: " + str(currentPageId))

    for branchKey, branchValue in linkTree.items():
        try:
            # 递归建立链接树
            linkTree[branchKey] = searchDepth(
                targetPageId, branchKey, branchValue, depth - 1)
        except SolutionFound as e:
            print(e.message)
            raise SolutionFound("PAGE: " + str(currentPageId))
    return linkTree


if __name__ == '__main__':
    try:
        searchDepth(134951, 1, {}, 4)
        print('No solution found')
    except SolutionFound as e:
        print(e.message)
