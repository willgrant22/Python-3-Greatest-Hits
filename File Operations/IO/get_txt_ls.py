#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import os

def getTXT(cwd):
	file_list = []
	for files in os.listdir(cwd):
	    if files.endswith(".txt"):
	        w = os.path.splitext(files)[0]
	        file_list.append(w)

	rfile=range(len(file_list))
	j = len(file_list)
	for i in rfile:
		print(file_list[i])
		i = i + 1
		if 2 <= i >= 1:
			i = i + 1
			
	return file_list
	
cwd = os.getcwd()
getTXT(cwd)