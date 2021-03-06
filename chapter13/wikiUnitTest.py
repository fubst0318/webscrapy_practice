#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import unittest
from urllib.request import urlopen
from bs4 import BeautifulSoup


class TestWikipedia(unittest.TestCase):
    bsObj = None

    def setUpClass():
        global bsObj
        url = "http://en.wikipedia.org/wiki/Monty_Python"
        bsObj = BeautifulSoup(urlopen(url))

    def test_titleText(self):
        global bsObj
        pageTitle = bsObj.find('h1').get_text()
        self.assertEqual(pageTitle, 'Monty Python')

    def test_contentExists(self):
        global bsObj
        content = bsObj.find('div', {'id': 'mw-content-text'})
        self.assertIsNotNone(content)


if __name__ == '__main__':
    unittest.main()
