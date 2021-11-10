#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from prettytable import from_csv
    
with open("data.csv", "r") as fp: 
    x = from_csv(fp)
    
print(x)