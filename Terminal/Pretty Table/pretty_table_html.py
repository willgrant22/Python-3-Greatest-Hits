#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from prettytable import from_html_one
    
with open("data.html", "r") as fp: 
    html = fp.read()

x = from_html_one(html)
print(x)