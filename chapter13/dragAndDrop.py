#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains


if __name__ == '__main__':
    driver = webdriver.PhantomJS(
        executable_path=r'D:\Program Files\PhantomJS\phantomjs-2.1.1-windows\bin\phantomjs')
    driver.get('http://pythonscraping.com/pages/javascript/draggableDemo.html')

    print(driver.find_element_by_id('message').text)

    element = driver.find_element_by_id('draggable')
    target = driver.find_element_by_id('div2')
    acitons = ActionChains(driver)
    acitons.drag_and_drop(element, target).perform()

    print(driver.find_element_by_id('message').text)
    driver.close()
