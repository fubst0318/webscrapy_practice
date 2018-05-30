#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import csv

if __name__ == '__main__':
    with open('test.csv', 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(['number', 'number plus 2', 'number times 2'])
        for i in range(10):
            writer.writerow([i, i + 2, i * 2])
