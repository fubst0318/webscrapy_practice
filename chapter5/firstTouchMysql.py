#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import pymysql

if __name__ == '__main__':
    conn = pymysql.connect('localhost', port=3306,
                           user='root', password='root', db='mysql')
    cur = conn.cursor()
    cur.execute('USE scraping')
    cur.execute("select * from pages where id =1 ")
    print(cur.fetchone())
    cur.close()
    conn.close()
