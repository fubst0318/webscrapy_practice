#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

html = urlopen('https://en.wikipedia.org/wiki/Comparison_of_text_editors')
bsObj = BeautifulSoup(html, 'html.parser')

# 主比对表格是当前页面上的第一个表格
table = bsObj.find_all('table', {'class': 'wikitable'})[0]
rows = table.find_all('tr')

with open('editor.csv', 'wt', newline='', encoding='utf-8') as csvFile:
    writer = csv.writer(csvFile)
    for row in rows:
        csvRow = []
        for cell in row.find_all(['th', 'td']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)