#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import re

newline_pattern = r'\n{3,}'

with open('t.txt','r') as file:
    Str = file.read()

find_pattern = re.findall(newline_pattern, Str)
print(find_pattern)

new_string = re.sub(f'{newline_pattern}', '\n\n', Str)

with open('t.txt', 'w') as file:
	fixed = file.write(new_string)




