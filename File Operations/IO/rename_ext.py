#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Will Grant
# Description : Search txt file for file names, and change ext
# =============================================================================
import os

with open ("rename.txt", "r") as fileHandler:
	i = 0
	for line in fileHandler:
		i = i + 1
		str = line.strip()
		new = str.replace('.txt', '.sh')
		print(str)
		print(new)
		src =(str) 
		dst =(new) 
		os.rename(src, dst)