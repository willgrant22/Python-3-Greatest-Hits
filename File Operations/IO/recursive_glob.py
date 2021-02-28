#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import glob
for file in glob.iglob('**/*.py', recursive=True):
    print(file)
#.py files in the current directory and subdirectories.