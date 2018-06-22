#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


if __name__ == '__main__':
    driver = webdriver.PhantomJS(
        executable_path=r'D:\Program Files\PhantomJS\phantomjs-2.1.1-windows\bin\phantomjs')
    driver.get('http://pythonscraping.com/pages/files/form.html')

    firstnameField = driver.find_element_by_name('firstname')
    lastnameField = driver.find_element_by_name('lastname')
    submitButton = driver.find_element_by_id('submit')

    '''
    方法一
    '''
    firstnameField.send_keys('Ryan')
    lastnameField.send_keys('Mitchell')
    submitButton.click()

    '''
    方法二
    '''
    actions = ActionChains(driver).click(firstnameField).send_keys(
        'Ryan').click(lastnameField).send_keys('Mitchell').send_keys(Keys.RETURN)
    actions.perform()

    print(driver.find_element_by_tag_name('body').text)

    driver.close()
