#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import unittest
from bs4 import BeautifulSoup
from urllib.request import urlopen


class WikiTest(unittest.TestCase):
    bsObj = None
    url = None

    def test_PageProperties(self):
        global bsObj
        global url

        url = "http://en.wikipedia.org/wiki/Monty_Python"
        # 测试遇到的前100个页面
        for i in range(1, 100):
            bsObj = BeautifulSoup(urlopen(url))
            titles = self.titleMatchesURL()
            self.assertEquals(titles[0], titles[1])
            self.assertTrue(self.contentExists())
            url = self.getNextLink()
        print('Done!')

    def titleMatchesURL(self):
        global bsObj
        global url
        pageTitle = bsObj.find('h1').get_text()
        urlTitle = url[(url.index('/wiki/') + 6):]
        

    def contentExists(self):
        pass

    def getNextLink(self):
        pass


if __name__ == '__main__':
    unittest.main()
