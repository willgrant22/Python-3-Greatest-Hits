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
days_file = open(path,'w')
days_file.write('Hello World\n') 
days_file.write('This is our new text days_file ') 
days_file.write('and this is another line.\n') 
days_file.write('Why? Because we can.\n') 
 
days_file.close() 