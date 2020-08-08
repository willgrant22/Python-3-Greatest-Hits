#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Will Grant
# Created Date: 01/18/2019
# Description : Open/Create file and write lines
# =============================================================================
# Imports
# =============================================================================

# Initialize list
mylines = []

# Open file to write
with open ('myfile.txt', 'rt') as myfile:
    for myline in myfile:
        mylines.append(myline)
print(mylines)
