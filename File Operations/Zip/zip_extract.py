#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import zipfile
import os

print(os.listdir('.'))


data_zip = zipfile.ZipFile('data.zip', 'r')

# Extract a single file to current directory
data_zip.extract('tmp/read.py')


print(os.listdir('.'))


# Extract all files into a different directory
data_zip.extractall(path='extract_dir/')

print(os.listdir('.'))


print(os.listdir('extract_dir'))


data_zip.close()