#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import pathlib

x = ["one", "two", "three", "four"]
y =  ["red", "green", "blue", "purple"]
i = 0
j = 0

while i < len(x):
	while j < len(y):
		p = pathlib.Path(f'Desktop/2018/{x[i]}')
		p.mkdir(parents=True)
		i += 1
		q = pathlib.Path(f'Desktop/2018/{x[0]}/{y[j]}')
		q.mkdir(parents=True)
		j += 1
