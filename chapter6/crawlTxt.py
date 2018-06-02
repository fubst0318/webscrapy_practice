#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from urllib.request import urlopen

if __name__ == '__main__':
    txtFile = urlopen(
        'http://www.pythonscraping.com/pages/warandpeace/chapter1.txt')
    print(txtFile.read())
