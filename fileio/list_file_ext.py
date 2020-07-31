#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import glob, os

cwd = os.getcwd()

file_list = []

for subdir, dirs, files in os.walk(cwd):
    for file in files:
        if file.endswith(".png"):
            w = os.path.splitext(file)[0]
            file_list.append(w)
            


for i in range(len(file_list)):
    print(file_list[i])