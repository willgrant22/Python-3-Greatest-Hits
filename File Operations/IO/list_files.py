#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Will Grant
# Description : Get files with specific ext
# =============================================================================
# Imports
# =============================================================================
import os

# Get all .py files in current directory
def getTXT(cwd):
	file_list = []
	for files in os.listdir(cwd):
	    if files.endswith(".py"):
	        w = os.path.splitext(files)[0]
	        file_list.append(w)

	rfile=range(len(file_list))
	j = len(file_list)
	for i in rfile:
		print(file_list[i])
		i = i + 1
		if 2 <= i >= 1:
			i = i + 1
			
	print(file_list)
			
	return file_list

cwd = os.getcwd()
getTXT(cwd)