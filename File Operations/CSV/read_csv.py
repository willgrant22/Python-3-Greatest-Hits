#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import csv

f = open("orders.csv", "rt")
orders = csv.reader(f)
for order in orders:
    print(order)
f.close()