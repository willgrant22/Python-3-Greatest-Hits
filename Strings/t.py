#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

mylines = []                             
with open ('myfile.txt', 'rt') as myfile:
    for myline in myfile:
        mylines.append(myline)
print(mylines)
