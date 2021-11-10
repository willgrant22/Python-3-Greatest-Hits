#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import os

# List all subdirectories using scandir()
basepath = '/Users/will/'
array = []
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_dir():
        	array.append(entry.name)
            
print(array)