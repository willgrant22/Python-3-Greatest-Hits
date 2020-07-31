#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

with open('partial.txt') as f:
	graph = [tuple(map(str, i.split(','))) for i in f]

print (graph)