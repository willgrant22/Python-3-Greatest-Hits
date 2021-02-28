#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Safari()

browser.get('http://www.google.com')
assert 'Google' in browser.title

elem = browser.find_element_by_name('q')  # Find the search box
elem.send_keys('this is selenium typing' + Keys.RETURN)

browser.quit()
