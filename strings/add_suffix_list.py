#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import string

upper = list(string.ascii_uppercase)
new = []

addedUpper=2
string = f'{addedUpper}'

for i in range(0,7):
	new.append(upper[i])

print(f'Before add: {new}')

formatList = [upper + string for upper in new]

print(f'After add: {formatList}')
