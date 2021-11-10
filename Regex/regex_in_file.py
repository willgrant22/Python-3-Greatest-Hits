#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import re

a_string = "\nabc xxx abc yyy"

with open('t.txt','r') as file:
    Str = file.read()

print(Str)

new_string = re.sub(r"xxx|yyy", "fuck", Str)
new_string = re.sub(r"([a-zA-Z0-9\.\-+_]+@[a-zA-Z0-9\.\-+_]+\.[a-zA-Z]+)", "replaced email", Str)

with open('t.txt','w') as file2:
    w_file = file2.write(new_string)

print(new_string)

with open('t.txt', 'r') as f:
	data = f.readlines()
print(data)
'''
with open('t.txt', 'a') as f2:
	d = f2.writelines(a_string)
	f2.writelines(f'\n{data}')
	f2.write("")

with open('t.txt','w') as file3:
    w_file = file3.write("new_string")
'''
