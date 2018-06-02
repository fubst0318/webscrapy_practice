#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup


def ngrams(input, n):
    input = input.split(' ')
    output = []
    for i in range(len(input) - n + 1):
        output.append(input[i:i + n])
    return output


if __name__ == '__main__':
    html = urlopen(
        'https://en.wikipedia.org/wiki/Python_(programming_language)')
    bsObj = BeautifulSoup(html, 'html.parser')
    content = bsObj.find('div', {'id': 'mw-content-text'}).get_text()
    ngrams = ngrams(content, 2)
    print(ngrams)
    print('2-grams count is: '+str(len(ngrams)))