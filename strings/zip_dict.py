#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

x = ['a', 'b', 'c']

a = [ i for i in x ]
b = [j for j in range(0, 3)]
c = [ k for k in zip(a, b)]
#y = lambda a, b : a + b
#z = y(a, b)
print(c)

