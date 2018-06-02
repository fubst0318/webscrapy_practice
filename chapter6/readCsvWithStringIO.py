#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from urllib.request import urlopen
from io import StringIO
import csv

if __name__ == '__main__':
    data = urlopen(
        'http://pythonscraping.com/files/MontyPythonAlbums.csv').read().decode('ascii', 'ignore')
    dataFile = StringIO(data)
    csvReader = csv.reader(dataFile)

    for row in csvReader:
        print(row)
