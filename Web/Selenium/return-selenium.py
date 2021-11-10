#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Safari()
browser.get('https://google.com')

browser.find_element_by_name("q").send_keys("selenium python"+Keys.RETURN)
