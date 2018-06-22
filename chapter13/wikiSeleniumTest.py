#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.PhantomJS(
        executable_path=r'D:\Program Files\PhantomJS\phantomjs-2.1.1-windows\bin\phantomjs')
    driver.get('http://en.wikipedia.org/wiki/Monty_Python')
    assert 'Monty Python' in driver.title
    print('Monty Python was in the title')
    driver.close()
