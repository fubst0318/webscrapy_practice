#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from selenium import webdriver
import time

if __name__ == '__main__':
    driver = webdriver.PhantomJS(
        executable_path=r'D:\Program Files\PhantomJS\phantomjs-2.1.1-windows\bin\phantomjs')
    driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
    time.sleep(3)
    print(driver.find_element_by_id('content').text)
    driver.close()
