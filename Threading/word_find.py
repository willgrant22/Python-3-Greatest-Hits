#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import os

words = ["PurchaseOrder:", "1Z"]

def word_find(line,words):
    return list(set(line.strip().split()) & set(words))

def main(file,words):
	for j in range(1, 4):
	    with open(f'label_{j}-output.txt') as f:
	        for i,x in enumerate(f, start=1):
	            common = word_find(x,words)
	            if common:
	            	print(x)
	                

main('file', words)