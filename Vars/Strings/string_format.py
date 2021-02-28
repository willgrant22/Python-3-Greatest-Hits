#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Will Grant
# Description : String formatting
# =============================================================================
import string

txt = "Hello, And Welcome To My World!"
myTuple = ("John", "Peter", "Vicky")

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


print(a)