#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests
from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.PhantomJS(
        executable_path=r'D:\Program Files\PhantomJS\phantomjs-2.1.1-windows\bin\phantomjs')
    driver.get('http://pythonscraping.com/')
    driver.implicitly_wait(1)
    print(driver.get_cookies())

    savedCookies = driver.get_cookies()

    driver2 = webdriver.PhantomJS(
        executable_path=r'D:\Program Files\PhantomJS\phantomjs-2.1.1-windows\bin\phantomjs')
    driver2.get('http://pythonscraping.com/')
    driver2.delete_all_cookies()
    for cookie in savedCookies:
        driver2.add_cookie(cookie)

    driver2.get('http://pythonscraping.com/')
    driver2.implicitly_wait(1)
    print('------------------')
    print(driver2.get_cookies())
