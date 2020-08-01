#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.headless = True

driver = Chrome(options=opts, executable_path='chromedriver.exe')

try:
    driver.get('http://webcode.me')

    assert 'My html page!' == driver.title

finally:

    driver.quit()