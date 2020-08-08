#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import os, sys
from pathlib import Path
home = str(Path.home())
print(home)
path=home+'/new/txt/test.txt'
days_file = open(path,'r')
for line in days_file: 
	print(line)
 
days_file.close() 