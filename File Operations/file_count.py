#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import os

# Path IN which we have to count files and directories
PATH = os.getcwd()   # Give your path here

fileCount = 0
dirCount = 0

for root, dirs, files in os.walk(PATH):
    print('Looking in:',root)
    for directories in dirs:
        dirCount += 1
    for Files in files:
        fileCount += 1

print('Number of files',fileCount)
print('Number of Directories',dirCount)
print('Total:',(dirCount + fileCount))
