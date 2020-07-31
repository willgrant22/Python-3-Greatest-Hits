#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import string

txt = "Hello, And Welcome To My World!"
myTuple = ("John", "Peter", "Vicky")
nl = '\n'

a = txt.casefold()

b = txt.capitalize()

c = txt.isidentifier()

d = "#".join(myTuple)

e = txt.ljust(20)

f = txt.lower()

g = txt.zfill(10)

h = txt.upper()

i = txt.title() #Make the first letter in each word upper case:

j = txt.count("apple")


print(a, nl, b, nl, c, nl, d, nl, e, nl, f, nl, g, nl, h, nl, i, nl, j)
