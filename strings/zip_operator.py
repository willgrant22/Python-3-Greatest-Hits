#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import operator

mylist = list(zip(range(40, 240), range(-100, 100)))

x = sorted(mylist, key=operator.itemgetter(1))

print(x)